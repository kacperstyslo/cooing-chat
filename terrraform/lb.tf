resource "aws_lb" "default" {
  name            = "cooing-chat-lb"
  subnets         = aws_subnet.public.*.id
  security_groups = [aws_security_group.cooing_chat_lb.id]
}

resource "aws_lb_target_group" "cooing_chat_lb" {
  name        = "cooing-chat-lb-group"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.default.id
  target_type = "ip"
}

resource "aws_lb_listener" "cooing_chat_lb" {
  load_balancer_arn = aws_lb.default.id
  port              = "80"
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.cooing_chat_lb.id
    type             = "forward"
  }
}

resource "aws_security_group" "cooing_chat_lb" {
  name   = "cooing-chat-lb-security-group"
  vpc_id = aws_vpc.default.id

  ingress {
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}