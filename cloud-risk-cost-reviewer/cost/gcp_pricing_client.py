import subprocess
import requests

COMPUTE_SERVICE_ID = "services/6F81-5844-456A"

def get_access_token():
    return subprocess.check_output(
        ["gcloud", "auth", "print-access-token"],
        text=True
    ).strip()

def get_skus(service_id):
    url = f"https://cloudbilling.googleapis.com/v1/{service_id}/skus"
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json().get("skus", [])

skus = get_skus(COMPUTE_SERVICE_ID)

for sku in skus:
    description = sku.get("description", "")

    if "E2" in description and "Iowa" in description:
        print(description)

    if (
        "E2" in description
        and "Core" in description
        and "Iowa" in description
        and "Spot" not in description
        and "Preemptible" not in description
    ):
        print(description)
        print(
            sku.get("pricingInfo", [{}])[0].get(
                "pricingExpression", {}
            )
        )
        print()