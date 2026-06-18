from cost.terraform_parser import parse_terraform_resources
from cost.cost_mapper import RESOURCE_COST_MAP


def estimate_costs():
    resources = parse_terraform_resources()
    estimates = []

    for resource in resources:
        resource_type = resource["type"]
        cost_info = RESOURCE_COST_MAP.get(resource_type)

        if cost_info:
            estimates.append({
                "resource": f"{resource['type']}.{resource['name']}",
                "file": resource["file"],
                **cost_info
            })
        else:
            estimates.append({
                "resource": f"{resource['type']}.{resource['name']}",
                "file": resource["file"],
                "service": "Unknown",
                "daily": None,
                "weekly": None,
                "monthly": None,
                "note": "No cost mapping exists yet for this resource type."
            })

    return estimates


if __name__ == "__main__":
    results = estimate_costs()

    print("===================================")
    print(" Cloud Cost Estimate")
    print("===================================")

    if not results:
        print("No Terraform resources found.")

    for item in results:
        print(f"\nResource: {item['resource']}")
        print(f"Service: {item['service']}")
        print(f"File: {item['file']}")

        if item["daily"] is not None:
            print(f"Daily: ${item['daily']:.2f}")
            print(f"Weekly: ${item['weekly']:.2f}")
            print(f"Monthly: ${item['monthly']:.2f}")
        else:
            print("Daily: needs pricing lookup")
            print("Weekly: needs pricing lookup")
            print("Monthly: needs pricing lookup")

        print(f"Note: {item['note']}")