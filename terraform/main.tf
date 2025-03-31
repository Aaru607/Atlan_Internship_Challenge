provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "cost_data" {
  bucket = "your-cost-data-bucket"
  acl    = "private"
}

resource "aws_budget" "monthly_budget" {
  name              = "monthly-cost-budget"
  time_unit         = "MONTHLY"
  budget_type       = "COST"
  limit_amount      = 1000
  limit_unit        = "USD"
  cost_filters      = {}
}
