locals {
  application_name = "cooing-chat"
}

resource "aws_ecs_cluster" "main" {
  name = local.application_name
}

output "load_balancer_ip" {
  value = aws_lb.default.dns_name
}

