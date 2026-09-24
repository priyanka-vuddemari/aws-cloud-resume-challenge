output "s3_website_url" {
  description = "S3 static website URL"
  value       = aws_s3_bucket_website_configuration.resume.website_endpoint
}

output "api_gateway_url" {
  description = "API Gateway invoke URL"
  value       = "${trimsuffix(aws_apigatewayv2_stage.default.invoke_url, "/")}/count"
}

output "cloudfront_url" {
  description = "CloudFront distribution URL"
  value       = "Add CloudFront manually for now"
}