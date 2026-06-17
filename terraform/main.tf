resource "google_storage_bucket" "terraform_test" {
  name                        = "terraform-test-bucket-75857734333"
  location                    = "US"
  force_destroy               = true
  uniform_bucket_level_access = true
}