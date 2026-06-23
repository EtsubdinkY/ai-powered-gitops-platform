variable "network_name" {
  type        = string
  description = "Name of the VPC network."
}

variable "subnet_name" {
  type        = string
  description = "Name of the subnet."
}

variable "region" {
  type        = string
  description = "GCP region where the subnet will be created."
}

variable "subnet_cidr" {
  type        = string
  description = "Primary CIDR range for the subnet."
}

variable "pods_range_name" {
  type        = string
  description = "Secondary range name used by GKE pods."
}

variable "pods_cidr" {
  type        = string
  description = "Secondary CIDR range used by GKE pods."
}

variable "services_range_name" {
  type        = string
  description = "Secondary range name used by GKE services."
}

variable "services_cidr" {
  type        = string
  description = "Secondary CIDR range used by GKE services."
}