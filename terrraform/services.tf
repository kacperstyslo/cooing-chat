resource "aws_ecs_service" "service" {
  name            = "cooing-chat-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.cooing_chat_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    security_groups = [aws_security_group.cooing_chat_task.id]
    subnets         = aws_subnet.private.*.id
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.cooing_chat_lb.id
    container_name   = "cooing-chat-container"
    container_port   = 5000
  }

  depends_on = [aws_lb_listener.cooing_chat_lb]
}