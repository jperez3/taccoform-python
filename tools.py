import os
from typing import List
from pathlib import Path

def find_terraform_directories(root_directory: str) -> List[str]:
    """
    
    Args:
        root_directory: The root directory to start searching from
        
    Returns:
        List of directory paths that contain provider.tf files
    """
    root_path = Path(root_directory)
    
    if not root_path.exists():
        raise ValueError(f"Directory does not exist: {root_directory}")
    
    if not root_path.is_dir():
        raise ValueError(f"Path is not a directory: {root_directory}")
    
    provider_directories = []
    
    try:
        # Use pathlib's rglob to find all provider.tf files recursively
        for provider_file in root_path.rglob("provider.tf"):
            # Get the parent directory of the provider.tf file
            provider_directories.append(str(provider_file.parent.absolute()))
        
        return sorted(provider_directories)
        
    except PermissionError as e:
        print(f"Permission denied accessing directory: {e}")
        return provider_directories
    except Exception as e:
        print(f"Error occurred while searching: {e}")
        return provider_directories
