import os
from tf_commands import destroy
from tools import find_terraform_directories


workspace_root = os.path.abspath("terraform")

def main():
    directories = find_terraform_directories(workspace_root)

    for directory in directories:
        try:
            destroy(directory)
        except Exception as e:
            print(f"Error processing {directory}: {e}")
            
if __name__ == "__main__":
    main()