# This sets specific roles for access to AWS services
# used by compute environments and batch queues


### Batch Role
resource "aws_iam_role" "batch_service_role" {
  name = "data-refinery-batch-service-role-${var.user}-${var.stage}"
  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
        "Service": "batch.amazonaws.com"
        }
    }
    ]
}
EOF
  tags = var.default_tags
}

resource "aws_iam_role_policy_attachment" "batch_service_role" {
  role = aws_iam_role.batch_service_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole"
}

### ECS Instance Role
resource "aws_iam_role" "ecs_instance_role" {
  name = "data-refinery-ecs-instance-role-${var.user}-${var.stage}"
  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
        "Service": "ec2.amazonaws.com"
        }
    }
    ]
}
EOF
  tags = var.default_tags
}

resource "aws_iam_policy" "ecs_instance_role" {
  name = "data-refinery-ecs-instance-role-policy-${var.user}-${var.stage}"
  description = "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html"

  # Policy text based off of:
  # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeTags",
                "ecs:CreateCluster",
                "ecs:DeregisterContainerInstance",
                "ecs:DiscoverPollEndpoint",
                "ecs:Poll",
                "ecs:RegisterContainerInstance",
                "ecs:StartTelemetrySession",
                "ecs:UpdateContainerInstancesState",
                "ecs:Submit*",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
EOF

}

resource "aws_iam_role_policy_attachment" "ecs_instance_role" {
  role = aws_iam_role.ecs_instance_role.name
  policy_arn = aws_iam_policy.ecs_instance_role.arn
}

resource "aws_iam_instance_profile" "ecs_instance_profile" {
  name = "data-refinery-ecs-instance-profile-${var.user}-${var.stage}"
  role = aws_iam_role.ecs_instance_role.name
}
