resource "aws_ecs_task_definition" "cooing_chat_task" {
  family                   = "cooing-chat-app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = "arn:aws:iam::740944045569:role/ecsTaskExecutionRole"
  container_definitions    = <<DEFINITION
[
  {
    "image": "740944045569.dkr.ecr.us-east-1.amazonaws.com/cooing-chat-image",
    "cpu": 256,
    "memory": 512,
    "name": "cooing-chat-container",
    "networkMode": "awsvpc",
    "portMappings": [
      {
        "containerPort": 5000,
        "hostPort": 5000,
        "protocol": "tcp"
      }
    ],
        "entryPoint": [
      "flask",
      "run",
      "--host=0.0.0.0"
    ],
    "secrets": [
      {
        "name": "AWS_ACCESS_KEY_ID",
        "valueFrom": "arn:aws:ssm:us-east-1:740944045569:parameter/cooing-chat-admin-access-key-id"
      },
      {
        "name": "AWS_SECRET_ACCESS_KEY",
        "valueFrom": "arn:aws:ssm:us-east-1:740944045569:parameter/cooing-chat-admin-secret-key"
      }
    ],
    "environment": [
      {
        "name": "FLASK_APP",
        "value": "cooing_chat"
      },
      {
        "name": "AWS_DEFAULT_REGION",
        "value": "us-east-1"
      }
    ]
  }
]
DEFINITION
}


resource "aws_security_group" "cooing_chat_task" {
  name   = "cooing_chat_task-security-group"
  vpc_id = aws_vpc.default.id

  ingress {
    protocol        = "tcp"
    from_port       = 5000
    to_port         = 5000
    security_groups = [aws_security_group.cooing_chat_lb.id]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}