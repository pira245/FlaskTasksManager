# Import system library
import sys
sys.path.append('.')
# load environment variables
import os
import json
from dotenv import load_dotenv, set_key
# Set working directory and filename
current_filename = os.path.basename(__file__) # The name of the current file
project_dir = os.path.dirname(__file__) # The project directory
project_name = os.path.basename(project_dir).strip() # The name of the project
project_env_file = os.path.join(project_dir, 'project.env')
project_csv_file = os.path.join(project_dir, 'project.csv')

# load project.env file
load_dotenv(project_env_file)

# Project directories 
print('Project Name :\n', project_name)
print('File :\n', current_filename)
print('Project Directory :\n', project_dir)
print('Environment Variables :\n', project_env_file)

# Create environment variables
os.environ['ProjectName'] = project_name
os.environ['ProjectDir'] = project_dir
os.environ['ProjectEnv'] = project_env_file
os.environ['ProjectCsv'] = project_csv_file

# Write to project.env file
set_key(project_env_file, "ProjectName", os.environ["ProjectName"])
set_key(project_env_file, "ProjectDir", os.environ["ProjectDir"])
set_key(project_env_file, "ProjectEnv", os.environ["ProjectEnv"])
set_key(project_env_file, "ProjectCsv", os.environ["ProjectCsv"])

# List all subfolders
subfolders = [ f.path for f in os.scandir(project_dir) if f.is_dir() ]
# Create PYTHONPATH to include locals modules:
os.environ['PYTHONPATH'] = project_dir
# Create a python configuration setup for vscode: 
python_vscode_debug_config =  {"name": "{}: {}: {}".format("Python","Module", project_name),"type": "{}".format("debugpy"),"request": "{}".format("launch"),"module": "{}".format(project_name),"env":{"PYTHONPATH": project_dir},"console": "{}".format("integratedTerminal")}
python_vscode_debug_config = json.dumps(python_vscode_debug_config) # , indent=4
# Create vscode_config to include locals modules when working with vscode:
os.environ['python_vscode_debug_config'] = python_vscode_debug_config
# Write PYTHONPATH to .env file.
set_key(project_env_file, "PYTHONPATH", os.environ["PYTHONPATH"])
# Write configuration setup for vscode to .env file.
set_key(project_env_file, "python_vscode_debug_config", os.environ["python_vscode_debug_config"])

# Set vscode workspace 
def vscode_workspace(project_name, subfolders, project_env_file):
    try:
        # load project_template.code-workspace
        for folder in subfolders:
            if os.path.basename(folder) == ".vscode":
                workspace_template = os.path.join(folder, 'workspace_template.json')
                
                project_workspace = os.path.join(folder, '{}.code-workspace'.format(project_name))
                
                # Open template json file and write data
                with open(workspace_template, 'r', encoding='utf-8') as workspace:
                    # loda json data
                    data = json.load(workspace)
                    
                    # Update workspace data
                    # Folders
                    for folder in subfolders:
                        name = os.path.basename(folder)
                        data["folders"].append({"path": name})
                    # Settings
                    data["settings"]["terminal.integrated.cwd"] = project_dir # Update
                    data["settings"]["python.envFile"] = project_env_file # Update
                    data["settings"]["projectManager.any.baseFolders"].append(project_dir) # Update
                    data["settings"]["projectManager.git.baseFolders"].append(project_dir) # Update
                    data["settings"]["projectManager.vscode.baseFolders"].append(project_dir) # Update
                    # Launch for debuging
                    python_launch_debug_configuration = os.getenv("python_vscode_debug_config")
                    #python_launch_debug_configuration = python_launch_debug_configuration.replace('\"', '')
                    data["launch"]["configurations"].append(python_launch_debug_configuration ) # Python
                    # Tasks
                    
                    # write data to workspace
                    data = json.dumps(data, indent=4)
                with open(project_workspace, 'w', encoding='utf-8') as workspace:
                    workspace.write(data)
            
            else:
                pass
        
        # Create environment variables
        os.environ['vscode_workspace'] = project_workspace
        # Write configuration setup for vscode to .env file.
        set_key(project_env_file, "vscode_workspace", os.environ["vscode_workspace"])

    except (OSError, NameError, ImportError, SyntaxError, UnicodeError) as error:
        print(error.args)
    
# Add comment to workspace file

def AddComment(workspace_file):
    comment = {
        "settings":"// Controls the settings that apply to all profiles :",
        "launch":"// Add debuging configurations to project :",
        "tasks":"// Automate project tasks"
    }
    try:
        with open(workspace_file, 'r', encoding='utf-8') as workspace:
            data = workspace.read()
            # Update data with comments location
            update_data = data[:]
            # serach pattern settings
            m_settings = update_data.find("settings")
            update_data = f"{update_data[:m_settings-2]}\n// Controls the settings that apply to all profiles :\n{update_data[m_settings-2:]}"

            # serach pattern launch
            m_launch = update_data.find("launch")
            update_data = f"{update_data[:m_launch-2]}\n// Add debuging configurations to project :\n{update_data[m_launch-2:]}"

            # serach pattern tasks
            m_tasks = update_data.find("tasks")
            update_data = f"{update_data[:m_tasks-2]}\n// Automate project tasks :\n{update_data[m_tasks-2:]}"
            
        with open(workspace_file, 'w', encoding='utf-8') as workspace:
            # Write  updates to file
            workspace.write(update_data)

    except (OSError, NameError, ImportError, SyntaxError, UnicodeError) as error:
        print(error.args)
    
# Create a project csv file 
import pandas as pd

def ProjectCsv(project_csv_file):

    projectInfo = {
        "ProjectName":["TemplateProject"],
        "LinkProjectRepo":["https://github.com/pira245/FlaskTasksManager"],
        "ImageName":["FlaskTasksManager.png"],
        "LinkImageRepo":["https://github.com/pira245/FlaskTasksManager/media/FlaskTasksManager.png"],
        "Category":["Web"],
        "ProjectAbout":["This is a basic web aplication created with Python and Flask to manage tasks."]
    }
    try:
        # Convert Python dic to csv
        df = pd.DataFrame.from_dict(projectInfo, orient='columns')
        # Write CSV to file and add to OS env file
        df.to_csv(project_csv_file, index=False)
    except (OSError, NameError, ImportError, SyntaxError, UnicodeError) as error:
        print(error.args)
    

if __name__ == "__main__":

   # Set vscode workspace 
   vscode_workspace(project_name, subfolders, project_env_file)

   # Add comment to workspace 
   workspace_file = os.getenv("vscode_workspace")
   AddComment(workspace_file)
   
   # Create a project csv
   csv_file = os.getenv("ProjectCsv")
   ProjectCsv(csv_file)


