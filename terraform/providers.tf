terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    
  }
  required_version = ">= 1.0"
  backend "s3" {
    bucket = "priyanka-terraform-state-bk"
    key    = "cloud-resume/terraform.tfstate"
    region = "ap-south-2"
}
}

provider "aws" {
  region = var.aws_region
}