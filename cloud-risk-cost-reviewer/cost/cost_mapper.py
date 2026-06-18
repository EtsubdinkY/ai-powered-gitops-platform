RESOURCE_COST_MAP = {
    "google_compute_network": {
        "service": "VPC Network",
        "daily": 0.00,
        "weekly": 0.00,
        "monthly": 0.00,
        "note": "VPC network itself has no direct cost."
    },
    "google_storage_bucket": {
        "service": "Cloud Storage Bucket",
        "daily": 0.00,
        "weekly": 0.00,
        "monthly": 0.00,
        "note": "Bucket cost depends on stored data, operations, and retrieval."
    },
    "google_container_cluster": {
        "service": "GKE Cluster",
        "daily": None,
        "weekly": None,
        "monthly": None,
        "note": "Needs GKE pricing and node pool details."
    },
    "google_compute_instance": {
        "service": "Compute Engine VM",
        "daily": None,
        "weekly": None,
        "monthly": None,
        "note": "Needs machine type, region, disk, and runtime hours."
    },
}