variable "cluster_name" {
  type        = string
  description = "Name of the GKE cluster."
}

variable "region" {
  type        = string
  description = "GCP region for the GKE cluster."
}

variable "network_id" {
  type        = string
  description = "VPC network ID."
}

variable "subnet_id" {
  type        = string
  description = "Subnet ID."
}

variable "pods_range_name" {
  type        = string
  description = "Secondary range name for GKE pods."
}

variable "services_range_name" {
  type        = string
  description = "Secondary range name for GKE services."
}

variable "node_count" {
  type        = number
  description = "Number of nodes in the default node pool."
  default     = 1
}

variable "machine_type" {
  type        = string
  description = "Machine type for GKE nodes."
  default     = "e2-small"
}