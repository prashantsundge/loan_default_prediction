import os 

#define folder structure 
folders = [
    "data/raw",
    "notebooks",
    "models",
    "src"

]


#define files to create

files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "src/__init__.py",
    "src/data_loader.py",
    "src/data_preprocessor.py",
    "src/model_trainer.py",
    "src/model_evaluator.py",
    "src/main.py",
    "src/logger.py",
    "src/exception.py",
    "notebooks/loan_data_exploration.ipynb"

]

#create folders 
for folder in folders:
    os.makedirs(folder, exist_ok=True)


#create files
for file in files:
    if not os.path.exists(file):
        with open(file , 'w') as f:
            pass 

print("Project folder and file Structure has been created successfully! ")  