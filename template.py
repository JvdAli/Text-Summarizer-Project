import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:)')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfiles",
    "requirements.txt",
    "setup.py",
    "reseach/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)                #this is to handle forward slash(/) as in Windows only backward slash(/) are used

    filedir,filename = os.path.split(filepath)  # to split the file and folder

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # to create the folder if not present
        logging.info(f"Creating folder {filedir} for the file {filename}")


    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath, "w") as f:
            pass                     # i am only creating file , not doing anything inside the file
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")