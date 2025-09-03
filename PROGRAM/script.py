# Let's create the complete MalSim Pro project structure
import os
import json
from datetime import datetime

# Create project directory structure
project_structure = {
    'MalSimPro': {
        'simulators': [
            'ransomware_sim.py',
            'trojan_sim.py', 
            'worm_sim.py',
            'spyware_sim.py',
            '__init__.py'
        ],
        'monitoring': [
            'process_monitor.py',
            'file_monitor.py',
            'network_monitor.py',
            'system_monitor.py',
            '__init__.py'
        ],
        'dashboard': [
            'web_interface.py',
            'analytics.py', 
            'reporting.py',
            '__init__.py'
        ],
        'database': [
            'analysis_db.py',
            '__init__.py'
        ],
        'config': [
            'settings.json'
        ],
        'templates': [
            'dashboard.html',
            'report.html'
        ],
        'static': {
            'css': ['style.css'],
            'js': ['dashboard.js']
        },
        'logs': [],
        'reports': [],
        'test_files': []
    }
}

def create_project_structure(structure, base_path=''):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(content, path)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file)
                with open(file_path, 'w') as f:
                    f.write(f"# {file} - Created {datetime.now()}\n")
        else:
            with open(path, 'w') as f:
                f.write(f"# {name} - Created {datetime.now()}\n")

# Create the project structure
create_project_structure(project_structure)
print("✅ Project structure created successfully!")

# List the created structure
def list_structure(path, level=0):
    items = []
    if os.path.exists(path):
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            indent = "  " * level
            if os.path.isdir(item_path):
                items.append(f"{indent}{item}/")
                items.extend(list_structure(item_path, level + 1))
            else:
                items.append(f"{indent}{item}")
    return items

structure_list = list_structure('MalSimPro')
print("\n📁 Project Structure:")
for item in structure_list:
    print(item)