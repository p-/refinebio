from django.test import TestCase, tag


class ImportTestCase(TestCase):
    @tag("downloaders")
    def test_downloader_imports(self):
        # Make sure we can import the downloader tests
        import tests.downloaders.test_array_express
        import tests.downloaders.test_geo
        import tests.downloaders.test_sra
        import tests.downloaders.test_transcriptome_index
