variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-2"
}

variable "bucket_name" {
  description = "S3 bucket name"
  type        = string
  default     = "priyanka-cloud-resume-challenge"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "cloud-resume-counter"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  type        = string
  default     = "cloud-resume-counter"
}