#!/usr/bin/env python3

import os
import subprocess
import sys

repo_url = "https://github.com/etbcf/automate-post-install.git"
repo_name = "automate-post-install"

try:
    # Check if the repo directory already exists
    if not os.path.isdir(repo_name):
        print(f"Cloning repository '{repo_name}'...")
        subprocess.run(["git", "clone", repo_url])
    else:
        print(f"Repository '{repo_name}' already exists. Skipping clone.")

    os.chdir(repo_name)

    # Run the main.py script
    subprocess.run([sys.executable, "main.py"], check=True)

    print("Success!")

except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")
except Exception as e:
    print(f"Error: {e}")
