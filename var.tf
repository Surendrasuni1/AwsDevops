variable "region" {
}

variable "vpc_cidr" {
default = "10.1.0.0/16"
}

variable "sub1_cidr" {
default = "10.1.0.0/24"
}

variable "sub2_cidr" {
default = "10.1.1.0/24"
}

variable "route_cidr" {
default ="0.0.0.0/0"
}
