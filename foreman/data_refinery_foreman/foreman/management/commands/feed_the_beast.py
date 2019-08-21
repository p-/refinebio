"""This command will slowly retry Salmon jobs that timed out.
This is now necessary because samples with unmated reads will no longer cause
us to time out. It will only queue 300 an hour so as to not overload ENA.
"""

import time
from typing import List

from django.core.management.base import BaseCommand
from nomad import Nomad

from data_refinery_common.utils import  get_env_variable
from data_refinery_foreman.foreman.performant_pagination.pagination import PerformantPaginator as Paginator
from data_refinery_foreman.surveyor.management.commands.surveyor_dispatcher import queue_surveyor_for_accession
from data_refinery_common.logging import get_and_configure_logger
from data_refinery_common.models import Experiment, ProcessorJob


logger = get_and_configure_logger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        nomad_host = get_env_variable("NOMAD_HOST")
        nomad_port = get_env_variable("NOMAD_PORT", "4646")
        nomad_client = Nomad(nomad_host, port=int(nomad_port), timeout=30)

        with open("config/all_rna_seq_accessions.txt") as accession_list_file:
            all_accessions = [line.strip() for line in accession_list_file]

        # We've surveyed up to ERP113019 so far!
        all_accessions = all_accessions[all_accessions.index('ERP113019'):]

        BATCH_SIZE = 1000
        batch_index = 0
        batch_accessions = all_accessions[0:BATCH_SIZE]

        while batch_accessions:
            logger.info(
                "Looping through another batch of 1000 experiments, starting with accession code: %s",
                batch_accessions[0]
            )

            existing_experiments = Experiment.objects.filter(
                accession_code__in=batch_accessions
            ).values(
                'accession_code'
            )

            existing_accessions = [experiment['accession_code'] for experiment in existing_experiments]

            missing_accessions = set(batch_accessions) - set(existing_accessions)
            while len(missing_accessions) > 0:
                try:
                    all_surveyor_jobs = nomad_client.jobs.get_jobs(prefix="SURVEYOR")

                    num_surveyor_jobs = 0
                    for job in all_surveyor_jobs:
                        if job['ParameterizedJob'] and job['JobSummary'].get('Children', None):
                            num_surveyor_jobs = num_surveyor_jobs + job['JobSummary']['Children']['Pending']
                            num_surveyor_jobs = num_surveyor_jobs + job['JobSummary']['Children']['Running']
                except:
                    logger.exception("Exception caught counting surveyor jobs!")
                    # Probably having trouble communicating with Nomad, let's try again next loop.
                    continue

                if num_surveyor_jobs < 15:
                    accession_code = missing_accessions.pop()
                    try:
                        queue_surveyor_for_accession(accession_code)
                        time.sleep(30)
                    except:
                        # We don't want to stop, gotta keep feeding the beast!!!!
                        logger.exception("Exception caught while looping through all accessions!",
                                         accession_code=accession_code)
                else:
                    # Do it here so we don't sleep when there's an exception.
                    time.sleep(30)

            batch_index += 1
            if batch_index * BATCH_SIZE >= len(all_accessions):
                break

            batch_start = batch_index * BATCH_SIZE
            batch_end = batch_start + BATCH_SIZE
            batch_accessions = all_accessions[batch_start:batch_end]