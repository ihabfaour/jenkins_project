import os
import shutil

# Example deployment logic
print("Starting deployment...")

# Define deployment directory
deploy_dir = os.path.join(os.getcwd(), 'deploy')
if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

# Define source files to be deployed
src_files = ['app1.py', 'requirements.txt']

# Copy application files to deployment directory
for file_name in src_files:
    full_file_name = os.path.join(os.getcwd(), file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, deploy_dir)

print("Deployment complete.")
