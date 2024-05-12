import subprocess
import sys
import os

def AdvancedLogging(message, PRINT = True):
    from logging import info
    try: 
        assert type(PRINT) == bool
    except:
        raise ValueError(f'PRINT value not passed as bool, passed as type {type(PRINT)} with value: {PRINT}')
    info(f"Logging information: {message}\n")
    if PRINT == True:
        print(f"Print Information: {message}\n")
    else:
        return

def MakeVenv() -> None:
    try:
        subprocess.run([sys.executable, '-m', 'venv', '.venv'])
        AdvancedLogging("Virtual environment '.venv' created successfully!")
        subprocess.run([sys.executable, '-m', 'venv', '.venv'])
    except Exception as e:
        AdvancedLogging(f"Error creating virtual environment: {e}")
        raise Exception(e)
    

def MakeEnvFile():
    try:
        ENV_FILE_PATH = os.path.join('.venv', '.env')
        with open(ENV_FILE_PATH, 'w') as FILE:
            FILE.write(f'"EXAMPLE_ENV_VAR":"EXAMPLE_VAR_VAR_VALUE"')
            pass
        AdvancedLogging(f"Made .env file")
        return
    except Exception as e:
        AdvancedLogging(f"Error making .env file: {e}")
        raise Exception(e)
     

def InstallRequirements():
    try:
        ACTIVATE = '".venv/Scripts/activate"' ## WIP testing on other OS if sys.platform == 'win32' else '".venv/bin/activate"'
        
        subprocess.run(ACTIVATE, shell=True, check=True)
        AdvancedLogging(f"Activated venv")

        PIP_PATH = os.path.join('.venv', 'Scripts', 'pip.exe') ## WIP on other os  if os.name == 'nt' else 'bin', 'pip'
        subprocess.run([PIP_PATH, 'install', '-r', 'requirements.txt'], check=True)
        AdvancedLogging(f"Installed all requirements.")
        return
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    




def CreateDirectories():
    try:
        for DIR in ['Assets', 'Classifiers']:
            os.makedirs(DIR, exist_ok=True)
            AdvancedLogging(f"Empty directory '{DIR}' created successfully!")
    except Exception as e:
        AdvancedLogging(f"Error creating directory '{DIR}': {e}")






def main() -> None:
    MakeVenv()
    MakeEnvFile()
    InstallRequirements()
    CreateDirectories()
    return


main()






