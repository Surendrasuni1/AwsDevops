#provider info
provider "aws"{
region="us-west-2"
}

#vpc Creation
resource "aws_vpc" "sunivpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "sunivpc"
  }
}
}
