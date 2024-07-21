resource "aws_cognito_user_pool" "healthmed_user_pool" {
  name = "healthmed-user-pool"

  username_attributes        = ["email"]
  auto_verified_attributes   = ["email"]

  lambda_config {
    pre_sign_up         = aws_lambda_function.lambda_pre_sign_up.arn
    post_confirmation   = aws_lambda_function.lambda_post_confirmation.arn
    pre_authentication  = aws_lambda_function.lambda_pre_authentication.arn
    post_authentication = aws_lambda_function.lambda_post_authentication.arn
  }

  schema {
    name                = "email"
    attribute_data_type = "String"
    required            = true
  }

  schema {
    name                = "phone_number"
    attribute_data_type = "String"
    required            = false
  }

  schema {
    name                = "USER_TYPE"
    attribute_data_type = "String"
    required            = false
  }

  schema {
    name                = "CPF"
    attribute_data_type = "String"
    required            = false
  }

  schema {
    name                = "CRM"
    attribute_data_type = "String"
    required            = false
  }

  password_policy {
    minimum_length    = 8
    require_uppercase = true
    require_numbers   = true
    require_symbols   = true

  }
}

resource "aws_cognito_user_pool_client" "my_user_pool_client" {
  name         = "healthmed-app-client"
  user_pool_id = aws_cognito_user_pool.healthmed_user_pool.id

  explicit_auth_flows = [
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_SRP_AUTH",
    "ALLOW_CUSTOM_AUTH"
  ]
}

resource "aws_cognito_user_group" "patients" {
  user_pool_id = aws_cognito_user_pool.healthmed_user_pool.id
  name         = "patients"
  description  = "Grupo para pacientes"
}

resource "aws_cognito_user_group" "doctors" {
  user_pool_id = aws_cognito_user_pool.healthmed_user_pool.id
  name         = "doctors"
  description  = "Grupo para médicos"
}
