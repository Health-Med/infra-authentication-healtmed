resource "aws_lambda_function" "lambda_pre_sign_up" {
  function_name = var.lambda_name_pre_signup
  handler       = var.function_handler
  runtime       = var.function_runtime
  role          = aws_iam_role.lambda_role.arn
  filename      = "${path.root}/../deploy/presignup.zip"
}

resource "aws_lambda_function" "lambda_post_confirmation" {
  function_name = var.lambda_name_post_confirmation
  handler       = var.function_handler
  runtime       = var.function_runtime
  role          = aws_iam_role.lambda_role.arn
  filename      = "${path.root}/../deploy/postconfirmation.zip"
}

resource "aws_lambda_function" "lambda_pre_authentication" {
  function_name = var.lambda_name_pre_authentication
  handler       = var.function_handler
  runtime       = var.function_runtime
  role          = aws_iam_role.lambda_role.arn
  filename      = "${path.root}/../deploy/preauthentication.zip"
}

resource "aws_lambda_function" "lambda_post_authentication" {
  function_name = var.lambda_name_post_authentication
  handler       = var.function_handler
  runtime       = var.function_runtime
  role          = aws_iam_role.lambda_role.arn
  filename      = "${path.root}/../deploy/postauthentication.zip"
}

resource "aws_lambda_permission" "allow_cognito_invoke" {
  for_each     = {
    pre_sign_up_function         = aws_lambda_function.lambda_pre_sign_up.arn
    post_confirmation_function   = aws_lambda_function.lambda_post_confirmation.arn
    pre_authentication_function  = aws_lambda_function.lambda_pre_authentication.arn
    post_authentication_function = aws_lambda_function.lambda_post_authentication.arn
  }
  statement_id  = "AllowCognitoToInvoke${each.key}"
  action        = "lambda:InvokeFunction"
  function_name = each.value
  principal     = "cognito-idp.amazonaws.com"
  source_arn    = aws_cognito_user_pool.healthmed_user_pool.arn
}
