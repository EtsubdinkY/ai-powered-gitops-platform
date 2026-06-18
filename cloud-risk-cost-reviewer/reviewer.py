import os

print("===================================")
print(" AI Risk Reviewer")
print("===================================")

issues = []

for root, dirs, files in os.walk("kubernetes"):
    for file in files:
        if file.endswith((".yaml", ".yml")):
            path = os.path.join(root, file)

            with open(path, "r") as f:
                content = f.read()

            if "latest" in content:
                issues.append(f"[MEDIUM] latest image tag detected in {path}")

            if "LoadBalancer" in content:
                issues.append(f"[HIGH] LoadBalancer service detected in {path}")

if issues:
    print("\nIssues Found:\n")
    for issue in issues:
        print(issue)
else:
    print("No risks detected.")