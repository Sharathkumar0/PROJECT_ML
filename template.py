import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name = "MLProject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)                  # Create specified path format according your system
    file_dr,file_name = os.path.split(file_path) # Returns folder and file
    
    if file_dr != "":                            # Checking whether directory present or not if not creating it
        os.makedirs(file_dr,exist_ok=True)        # Creating directory
        logging.info(f"creating directory: {file_dr} for the file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):    # Checking whether file is in particular dir
        with open(file_path,"w") as f:                                          # If not present creating a file
            pass
            logging.info(f"creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is already exists")