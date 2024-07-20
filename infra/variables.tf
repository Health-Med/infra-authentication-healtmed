variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "regiao da conta aws"
}

variable "lambda_name_pre_signup" {
  type        = string
  default     = "faas-lambda-pre-sign-up"
  description = "nome da lambda pre signup"
}

variable "lambda_name_post_confirmation" {
  type        = string
  default     = "faas-lambda-post-confirmation"
  description = "nome da lambda post confirmation"
}

variable "lambda_name_pre_authentication" {
  type        = string
  default     = "faas-lambda-pre-authentication"
  description = "nome da lambda pre authentication"
}

variable "lambda_name_post_authentication" {
  type        = string
  default     = "faas-lambda-post-authentication"
  description = "nome da lambda post authentication"
}

variable "function_handler" {
  type = string
  description = "Handler da lambda"
  default = "lambda_function.lambda_handler"
}

variable "function_runtime" {
  type = string
  description = "Runtime da lambda"
  default = "python3.11"
}