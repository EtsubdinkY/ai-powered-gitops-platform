output "cluster_name" {
  value = google_container_cluster.this.name
}

output "cluster_id" {
  value = google_container_cluster.this.id
}

output "cluster_endpoint" {
  value     = google_container_cluster.this.endpoint
  sensitive = true
}

output "cluster_location" {
  value = google_container_cluster.this.location
}

output "node_pool_name" {
  value = google_container_node_pool.primary.name
}