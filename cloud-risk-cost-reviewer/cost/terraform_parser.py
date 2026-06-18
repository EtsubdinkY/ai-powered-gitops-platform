import os
import re


def find_terraform_files(base_path="terraform"):
    terraform_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".tf"):
                terraform_files.append(os.path.join(root, file))

    return terraform_files


def parse_terraform_resources(base_path="terraform"):
    resources = []

    resource_pattern = re.compile(
        r'resource\s+"([^"]+)"\s+"([^"]+)"\s*\{',
        re.MULTILINE
    )

    for file_path in find_terraform_files(base_path):
        with open(file_path, "r") as file:
            content = file.read()

        matches = resource_pattern.findall(content)

        for resource_type, resource_name in matches:
            resources.append({
                "file": file_path,
                "type": resource_type,
                "name": resource_name
            })

    return resources


if __name__ == "__main__":
    detected_resources = parse_terraform_resources()

    print("Terraform Resources Detected:")

    if not detected_resources:
        print("No Terraform resources found.")

    for resource in detected_resources:
        print(
            f"- {resource['type']}.{resource['name']} "
            f"found in {resource['file']}"
        )