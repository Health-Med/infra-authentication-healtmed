resource "aws_cloudwatch_log_group" "lambda_pre_sign_up_logs" {
  name              = "/aws/lambda/${var.lambda_name_pre_signup}"
  retention_in_days = 1
}

resource "aws_cloudwatch_log_group" "lambda_post_confirmation_logs" {
  name              = "/aws/lambda/${var.lambda_name_post_confirmation}"
  retention_in_days = 1
}

resource "aws_cloudwatch_log_group" "lambda_pre_authentication_logs" {
  name              = "/aws/lambda/${var.lambda_name_pre_authentication}"
  retention_in_days = 1
}

resource "aws_cloudwatch_log_group" "lambda_post_authentication_logs" {
  name              = "/aws/lambda/${var.lambda_name_post_authentication}"
  retention_in_days = 1
}
