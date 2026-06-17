resource "google_compute_network" "test_vpc" {
  name                    = "terraform-test-vpc"
  auto_create_subnetworks = false
}