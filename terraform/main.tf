resource "google_compute_network" "terraform_test" {
  name                    = "terraform-test-vpc"
  auto_create_subnetworks = false
}