import os

# List of files to create
list_of_files = [
    # Components
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_preprocessing.py",

    # Pipelines
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",

    # Utils
    "src/utils/__init__.py",
    "src/utils/common.py",

    # Config
    "src/config.py",

    # Root level
    "config.yml",
    "requirements.txt",
    "README.md",

    "setup.py"

]

for file_path in list_of_files:
    file_path = os.path.normpath(file_path)
    dir_name = os.path.dirname(file_path)

    # Create directory if not exists
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)

    # Create file if not exists or empty
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass

        print(f"Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")