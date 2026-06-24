module "network" {
  source = "../../modules/network"

  network_name = "gitops-dev-vpc"
  subnet_name  = "gitops-dev-subnet"

  region      = "us-central1"
  subnet_cidr = "10.10.0.0/20"

  pods_range_name = "gke-pods"
  pods_cidr       = "10.20.0.0/16"

  services_range_name = "gke-services"
  services_cidr       = "10.30.0.0/20"
}
module "gke" {
  source = "../../modules/gke"

  cluster_name = "gitops-dev-gke"
  region       = var.region

  network_id          = module.network.network_id
  subnet_id           = module.network.subnet_id
  pods_range_name     = module.network.pods_range_name
  services_range_name = module.network.services_range_name

  node_count   = 1
  machine_type = "e2-small"
}