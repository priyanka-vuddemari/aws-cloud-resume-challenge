# AWS Cloud Resume Challenge

A static resume site hosted on AWS with a serverless visitor counter. The site is served through CloudFront, and each page load calls an API Gateway endpoint backed by Lambda and DynamoDB.

**Live site:** [https://d14zfhp4g206cx.cloudfront.net/](https://d14zfhp4g206cx.cloudfront.net/)

> The HTML currently contains sample resume details. Replace the name, contact information, experience, education, and project content in `index.html` before presenting it as a personal resume.

## Architecture

- **Frontend:** HTML and CSS in `index.html` and `styles.css`, hosted in S3 and delivered through CloudFront.
- **Visitor counter:** Browser JavaScript calls an API Gateway HTTP API. The endpoint invokes a Python 3.12 Lambda function, which reads and increments the `views` value in DynamoDB.
- **Infrastructure:** Terraform provisions the S3 website bucket, DynamoDB table, Lambda function, IAM permissions, and API Gateway resources.
- **Deployment:** GitHub Actions deploys on pushes to `main` and can also be started manually. It syncs the site files to S3, invalidates CloudFront, applies Terraform, and runs API smoke tests.

## Repository Layout

```text
.
|-- index.html
|-- styles.css
|-- lambda/
|   `-- lambda_function.py
|-- terraform/
|   |-- main.tf
|   |-- outputs.tf
|   |-- providers.tf
|   `-- variables.tf
|-- tests/
|   `-- test_resume.py
`-- .github/workflows/deploy.yml
```

## Deployment Configuration

The deployment workflow currently expects these GitHub Actions repository secrets. Add them under **Settings > Secrets and variables > Actions > Secrets**:

| Name | Purpose |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | AWS access key used by the workflow |
| `AWS_SECRET_ACCESS_KEY` | Matching AWS secret access key |
| `AWS_REGION` | AWS region (`ap-south-2`); the workflow currently reads this from Secrets |
| `CLOUDFRONT_DISTRIBUTION_ID` | Distribution to invalidate after publishing |

Use an IAM identity with only the permissions needed by the deployment. For a long-lived public project, prefer GitHub Actions OIDC with an AWS IAM role over stored access keys, and rotate/revoke any credentials that may have been exposed.

**Do not treat public URLs as secrets.** The resume URL and API Gateway URL are visible to every site visitor, and any value embedded in `index.html` is public after deployment. Keep public endpoints and resource identifiers in source or GitHub Actions **Variables**; reserve **Secrets** for credentials, tokens, and other values whose disclosure grants access. The current workflow has the S3 bucket name and API smoke-test URL in its source, while the page itself contains the API URL.

Terraform uses an S3 backend configured in `terraform/providers.tf`. The state bucket (`priyanka-terraform-state-bk` in `ap-south-2`) must exist before running `terraform init`. Keep Terraform state and `terraform.tfvars` files out of version control; state can contain sensitive infrastructure data. The Terraform `.gitignore` excludes these files.

## Run Locally

Requirements: Terraform 1.x, AWS CLI credentials with permissions to manage the resources, and Python 3.12 for the Lambda runtime.

Initialize and review the infrastructure from the Terraform directory:

```sh
cd terraform
terraform init
terraform plan
terraform apply
```

Run the API smoke tests from the repository root:

```sh
python -m pip install pytest requests playwright
python -m pytest tests/ -v
```

These tests call the deployed API, and requests increment the live visitor counter. They require network access and a reachable API endpoint.

Architecture Diagram 

<img width="1200" height="1059" alt="CRC" src="https://github.com/user-attachments/assets/893a49e4-6740-4567-bb1a-59f211f7762f" />


## References

- [Cloud Resume Challenge (AWS edition)](https://www.youtube.com/watch?v=zAhXukIDWkM&list=PLRBkbp6t5gM1GLxpZ382Egi7IKGIq6jVF)
- [Host a static website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html)
- [Cloudflare: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
