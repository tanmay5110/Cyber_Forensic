#!/usr/bin/env python3
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

    print("\n" + "=" * 50)
    print("✅ MalSim Pro setup completed successfully!")
    print("\n📚 Next steps:")
    print("1. Review the README.md for usage instructions")
    print("2. Start the dashboard: python main.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\n⚠️  Remember: Only use in isolated virtual machines!")

if __name__ == "__main__":
    main()
