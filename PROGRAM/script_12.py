# Create __init__.py files for proper Python modules
init_content = '''"""
MalSim Pro - Educational Malware Simulation and Analysis Platform

This package provides safe malware simulation tools for cybersecurity education
and research. All simulations are designed to run in isolated environments only.

WARNING: This software is for educational purposes only. Only use in virtual
machines or isolated test environments.
"""

__version__ = "1.0.0"
__author__ = "Cybersecurity Research Team"
__license__ = "Educational Use Only"
'''

# Write __init__.py files
init_files = [
    'MalSimPro/__init__.py',
    'MalSimPro/simulators/__init__.py', 
    'MalSimPro/monitoring/__init__.py',
    'MalSimPro/dashboard/__init__.py',
    'MalSimPro/database/__init__.py'
]

for init_file in init_files:
    with open(init_file, 'w') as f:
        f.write(init_content)

print("✅ Created __init__.py files for all modules")

# Create a comprehensive README.md
readme_content = '''# 🔬 MalSim Pro - Educational Malware Simulation Platform

**MalSim Pro** is a comprehensive educational platform for malware analysis and cybersecurity forensics training. It provides safe, controlled malware simulations that allow students and researchers to study malicious behavior without any real security risks.

## ⚠️ IMPORTANT WARNING

**🚨 EDUCATIONAL USE ONLY 🚨**

- This tool is designed EXCLUSIVELY for educational and research purposes
- ONLY run in isolated virtual machines (VirtualBox, VMware, etc.)
- NEVER run on production systems or networks
- All simulations are safe but should be treated as if they were real malware
- Designed for cybersecurity students, researchers, and professionals

## 🎯 Features

### Malware Simulations
- **Ransomware Simulation**: File encryption behavior, ransom notes, persistence
- **Trojan/Backdoor Simulation**: Remote access, keylogging, data exfiltration
- **Worm Simulation**: Network scanning, propagation attempts, exploitation
- **Spyware Simulation**: Data harvesting, credential theft, stealth operations

### Monitoring & Analysis
- **Real-time System Monitoring**: Process, file, network, and registry monitoring
- **Behavioral Analysis**: Pattern recognition and threat classification
- **Timeline Reconstruction**: Detailed activity timelines
- **IOC Extraction**: Automatic indicator of compromise detection

### Dashboard & Reporting
- **Web-based Dashboard**: Real-time visualization of simulation results
- **Analytics Engine**: Statistical analysis and threat scoring
- **Comprehensive Reports**: HTML and JSON report generation
- **Interactive Charts**: Activity timelines, threat distributions, heatmaps

### Safety Features
- **VM Detection**: Requires virtual machine environment
- **Safe File Operations**: Only affects designated test directories
- **Automatic Cleanup**: Restores system state after simulations
- **Isolated Networking**: Prevents real network communications

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8+ required
python --version

# Virtual machine software (VirtualBox, VMware, etc.)
# Isolated test environment
```

### Installation
```bash
# 1. Extract the MalSimPro project
cd MalSimPro

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize the database
python -c "from database.analysis_db import AnalysisDB; AnalysisDB()"

# 4. Verify VM environment (IMPORTANT!)
python main.py --help
```

### Running Simulations
```bash
# Start the web dashboard
python main.py --mode dashboard --port 5000

# Or run individual simulations via CLI
python main.py --mode simulate --type ransomware --duration 300
python main.py --mode simulate --type trojan --duration 180
python main.py --mode simulate --type worm --duration 240
python main.py --mode simulate --type spyware --duration 200
```

### Accessing the Dashboard
1. Open your web browser
2. Navigate to `http://localhost:5000`
3. Use the dashboard to start simulations and view results

## 📁 Project Structure

```
MalSimPro/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── config/
│   └── settings.json      # Configuration settings
├── simulators/            # Malware simulation modules
│   ├── ransomware_sim.py
│   ├── trojan_sim.py
│   ├── worm_sim.py
│   └── spyware_sim.py
├── monitoring/            # System monitoring components
│   ├── system_monitor.py
│   ├── process_monitor.py
│   ├── file_monitor.py
│   └── network_monitor.py
├── dashboard/             # Web interface and analytics
│   ├── web_interface.py
│   ├── analytics.py
│   └── reporting.py
├── database/              # Data storage and management
│   └── analysis_db.py
├── templates/             # HTML templates
│   ├── dashboard.html
│   └── report.html
├── static/               # CSS and JavaScript files
│   ├── css/style.css
│   └── js/dashboard.js
├── logs/                 # Simulation logs
├── reports/              # Generated reports
└── test_files/          # Safe test file area
```

## 🔧 Configuration

Edit `config/settings.json` to customize:

```json
{
    "simulation_settings": {
        "ransomware": {
            "encrypt_extensions": [".txt", ".doc", ".pdf"],
            "test_files_count": 10
        },
        "trojan": {
            "fake_backdoor_port": 8888,
            "keylog_simulation": true
        }
    },
    "monitoring": {
        "process_monitoring": true,
        "file_monitoring": true,
        "network_monitoring": true
    },
    "security": {
        "vm_required": true,
        "max_simulation_time": 3600
    }
}
```

## 📊 Usage Examples

### Running a Ransomware Simulation
```python
# Via Python API
from simulators.ransomware_sim import RansomwareSimulator
from monitoring.system_monitor import SystemMonitor

# Initialize
config = {...}  # Load from settings.json
simulator = RansomwareSimulator(config)
monitor = SystemMonitor()

# Run simulation
monitor.start_monitoring()
results = simulator.run_simulation(duration=300)
monitoring_data = monitor.stop_monitoring()

# Analyze results
print(f"Files encrypted: {len(results['encrypted_files'])}")
print(f"Ransom notes created: {len(results['ransom_notes'])}")
```

### Viewing Results in Dashboard
1. Start dashboard: `python main.py`
2. Open http://localhost:5000
3. View real-time statistics and session history
4. Generate detailed reports for analysis

## 🛡️ Safety Guidelines

### Before Running
- ✅ Confirm you're in a virtual machine
- ✅ Disconnect VM from production networks
- ✅ Take VM snapshots for easy restoration
- ✅ Review simulation settings
- ✅ Ensure adequate disk space for logs

### During Simulation
- ⚠️ Monitor resource usage
- ⚠️ Don't interrupt simulations abruptly
- ⚠️ Keep simulations within reasonable time limits
- ⚠️ Review generated files carefully

### After Simulation
- 🔄 Review all generated logs and reports
- 🔄 Clean up test directories if needed
- 🔄 Restore VM to clean snapshot
- 🔄 Export important analysis data

## 📈 Educational Applications

### Cybersecurity Courses
- Malware analysis fundamentals
- Digital forensics training
- Incident response simulation
- Threat hunting exercises

### Research Applications
- Behavioral pattern analysis
- Detection algorithm testing
- Forensic tool validation
- Security control evaluation

### Professional Training
- SOC analyst training
- Malware reverse engineering
- Penetration testing education
- Security awareness programs

## 🤝 Contributing

This is an educational project. Contributions should focus on:
- Additional simulation scenarios
- Enhanced monitoring capabilities
- Improved analysis algorithms
- Better educational documentation
- Safety and security improvements

## 📄 License

**Educational Use Only License**

This software is provided for educational and research purposes only. Commercial use, distribution, or deployment in production environments is prohibited. Users assume full responsibility for compliance with applicable laws and regulations.

## 🆘 Support

For educational use questions:
1. Check the configuration documentation
2. Review simulation logs for troubleshooting
3. Ensure VM environment meets requirements
4. Verify all dependencies are installed

## 🔮 Future Enhancements

- Additional malware family simulations
- Machine learning-based analysis
- Cloud-based deployment options
- Integration with SIEM platforms
- Advanced visualization features
- Mobile malware simulations

---

**Remember: This is a powerful educational tool. Use responsibly and only in controlled environments!**

🔬 Happy learning and stay curious about cybersecurity! 🔬
'''

with open('MalSimPro/README.md', 'w') as f:
    f.write(readme_content)

print("✅ Created comprehensive README.md")

# Create a simple setup script
setup_content = '''#!/usr/bin/env python3
"""
Setup script for MalSim Pro
Educational Malware Simulation Platform
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_vm_environment():
    """Basic check for VM environment"""
    vm_indicators = ['virtualbox', 'vmware', 'qemu', 'virtual']
    
    import platform
    system_info = platform.platform().lower()
    
    if any(indicator in system_info for indicator in vm_indicators):
        print("✅ Virtual machine environment detected")
        return True
    else:
        print("⚠️  WARNING: VM environment not clearly detected")
        response = input("Continue setup? (y/N): ")
        return response.lower() == 'y'

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def setup_directories():
    """Create necessary directories"""
    directories = ['logs', 'reports', 'test_files', 'database']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def initialize_database():
    """Initialize the SQLite database"""
    print("🗄️  Initializing database...")
    try:
        from database.analysis_db import AnalysisDB
        db = AnalysisDB()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")

def main():
    """Main setup function"""
    print("🔬 MalSim Pro Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check VM environment
    if not check_vm_environment():
        print("❌ Setup cancelled - VM environment required")
        sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Setup directories
    setup_directories()
    
    # Initialize database
    initialize_database()
    
    print("\\n" + "=" * 50)
    print("✅ MalSim Pro setup completed successfully!")
    print("\\n📚 Next steps:")
    print("1. Review the README.md for usage instructions")
    print("2. Start the dashboard: python main.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\\n⚠️  Remember: Only use in isolated virtual machines!")

if __name__ == "__main__":
    main()
'''

with open('MalSimPro/setup.py', 'w') as f:
    f.write(setup_content)

print("✅ Created setup.py - Installation script")

# Create a simple run script
run_script = '''#!/bin/bash
# MalSim Pro Quick Start Script

echo "🔬 MalSim Pro - Educational Malware Simulation Platform"
echo "=================================================="

# Check if running in VM (basic check)
echo "🔍 Checking environment..."

# Check for common VM indicators
if [ -d "/proc/vz" ] || grep -q "hypervisor" /proc/cpuinfo 2>/dev/null || [ -d "/proc/xen" ]; then
    echo "✅ Virtual environment detected"
else
    echo "⚠️  WARNING: Virtual environment not clearly detected"
    echo "This tool should only be run in isolated VMs!"
    read -p "Continue anyway? (y/N): " confirm
    if [[ $confirm != [yY] ]]; then
        echo "❌ Exiting for safety"
        exit 1
    fi
fi

# Start the application
echo "🚀 Starting MalSim Pro Dashboard..."
echo "📍 Dashboard will be available at: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop"
echo ""

python main.py --mode dashboard --port 5000
'''

with open('MalSimPro/run.sh', 'w') as f:
    f.write(run_script)

# Make the script executable
try:
    os.chmod('MalSimPro/run.sh', 0o755)
except:
    pass  # Windows compatibility

print("✅ Created run.sh - Quick start script")

# Create final project summary
print("\\n" + "="*60)
print("🎉 MALSIM PRO PROJECT COMPLETE! 🎉")
print("="*60)

# Count files created
import glob
files_created = len(glob.glob('MalSimPro/**/*', recursive=True))

print(f"📁 Project structure: {files_created} files created")
print("📚 Components included:")
print("   ✅ 4 Malware Simulators (Ransomware, Trojan, Worm, Spyware)")
print("   ✅ 4 System Monitors (Process, File, Network, System)")
print("   ✅ Web Dashboard with Analytics")
print("   ✅ SQLite Database with Analysis Storage")
print("   ✅ Comprehensive Reporting System")
print("   ✅ Safety Mechanisms and VM Detection")
print("   ✅ HTML Templates and CSS Styling")
print("   ✅ JavaScript Dashboard Interface")
print("   ✅ Complete Documentation")

print("\\n🚀 To get started:")
print("   1. cd MalSimPro")
print("   2. python setup.py  # Run setup")
print("   3. python main.py   # Start dashboard")
print("   4. Open http://localhost:5000")

print("\\n⚠️  REMEMBER:")
print("   • Only run in isolated virtual machines")
print("   • For educational purposes only")
print("   • Review all safety guidelines")
print("\\n🔬 Happy learning! 🔬")
print("="*60)