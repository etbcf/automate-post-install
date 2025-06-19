#!/usr/bin/env python3

import subprocess
import sys

repo_name = "automate-post-install"

try:
    # Run the main.py script
    subprocess.run([sys.executable, "main.py"], check=True)

    print("Success!")

except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")

except Exception as e:
    print(f"Error: {e}")
