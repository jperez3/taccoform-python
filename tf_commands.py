import json
import os
import subprocess


def init(workspace: str):
    os.chdir(workspace)
    result = subprocess.run(["terraform", "init"], stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        raise Exception(f"Terraform initialization failed for {workspace}: {result.stderr}")

def plan(workspace: str):
    os.chdir(workspace)
    result = subprocess.run(["terraform", "plan", "-json"], capture_output=True, text=True)
    plan = [json.loads(line) for line in result.stdout.splitlines() if line]
    change_summary = plan[-1]['changes']
    change_count = change_summary['add'] + change_summary['change'] + change_summary['import'] + change_summary['remove']
    print(f"Workspace: {os.getcwd().split("taccoform-python/")[-1]}")
    print(f"Change Summary: {change_summary}")
    print(f"Change Count: {change_count}")


def apply(workspace: str):
    os.chdir(workspace)
    result = subprocess.run(["terraform", "apply", "-auto-approve", "-json"], capture_output=True, text=True)
    apply = [json.loads(line) for line in result.stdout.splitlines() if line]
    apply_summary = apply[-2]['@message']
    print(apply_summary)
    print("")

def destroy(workspace: str):
    os.chdir(workspace)
    result = subprocess.run(["terraform", "destroy", "-auto-approve", "-json"], capture_output=True, text=True)
    destroy = [json.loads(line) for line in result.stdout.splitlines() if line]
    destroy_summary = destroy[-2]['@message']
    print(f"Workspace: {os.getcwd().split("taccoform-python/")[-1]}")
    print(destroy_summary)
    print("")    