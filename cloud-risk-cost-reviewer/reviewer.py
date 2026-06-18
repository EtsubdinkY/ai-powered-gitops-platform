import os
import sys

sys.path.append(os.path.dirname(__file__))

print("\n===================================")
print(" Cloud Cost Estimate")
print("===================================")

from cost.cost_estimator import estimate_costs

cost_results = estimate_costs()

if not cost_results:
    print("No Terraform resources found.")
else:
    for item in cost_results:
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