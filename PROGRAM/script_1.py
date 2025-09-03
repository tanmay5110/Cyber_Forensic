# Create the main entry point file
main_py_content = '''#!/usr/bin/env python3
"""
MalSim Pro - Educational Malware Simulation and Analysis Platform
Created for cybersecurity education and research purposes only.

⚠️  WARNING: This tool is designed for educational purposes only.
    Only run in isolated virtual machines. Never run on production systems.

Author: Cybersecurity Research Team
Date: September 2025
"""

import os
import sys
import argparse
import json
from datetime import datetime
from flask import Flask

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulators.ransomware_sim import RansomwareSimulator
from simulators.trojan_sim import TrojanSimulator
from simulators.worm_sim import WormSimulator
from simulators.spyware_sim import SpywareSimulator
from monitoring.system_monitor import SystemMonitor
from dashboard.web_interface import create_app
from database.analysis_db import AnalysisDB

class MalSimPro:
    def __init__(self):
        self.config = self.load_config()
        self.db = AnalysisDB()
        self.monitor = SystemMonitor()
        self.simulators = {
            'ransomware': RansomwareSimulator,
            'trojan': TrojanSimulator,
            'worm': WormSimulator,
            'spyware': SpywareSimulator
        }
        
    def load_config(self):
        """Load configuration from settings.json"""
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'settings.json')
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def safety_check(self):
        """Verify running in safe environment"""
        if not self.is_vm_environment():
            print("❌ SAFETY ERROR: This tool must only run in a virtual machine!")
            print("   Please run in VirtualBox, VMware, or similar isolated environment.")
            sys.exit(1)
        
        print("✅ Safety check passed - VM environment detected")
        return True
    
    def is_vm_environment(self):
        """Check if running in VM (basic detection)"""
        # Check for common VM indicators
        vm_indicators = [
            'virtualbox', 'vmware', 'qemu', 'xen', 'kvm',
            'virtual', 'vm', 'sandbox'
        ]
        
        # Check system info
        import platform
        system_info = platform.platform().lower()
        
        return any(indicator in system_info for indicator in vm_indicators)
    
    def run_simulation(self, sim_type, duration=300):
        """Run malware simulation"""
        if sim_type not in self.simulators:
            print(f"❌ Unknown simulation type: {sim_type}")
            return False
        
        print(f"🔬 Starting {sim_type} simulation...")
        print(f"⏱️  Duration: {duration} seconds")
        
        # Initialize simulator
        simulator = self.simulators[sim_type](self.config)
        
        # Start monitoring
        self.monitor.start_monitoring()
        
        # Run simulation
        try:
            results = simulator.run_simulation(duration)
            
            # Stop monitoring
            monitoring_data = self.monitor.stop_monitoring()
            
            # Save results to database
            session_id = self.db.save_analysis_session({
                'type': sim_type,
                'duration': duration,
                'results': results,
                'monitoring_data': monitoring_data,
                'timestamp': datetime.now().isoformat()
            })
            
            print(f"✅ Simulation completed - Session ID: {session_id}")
            return session_id
            
        except Exception as e:
            print(f"❌ Simulation failed: {str(e)}")
            self.monitor.stop_monitoring()
            return False
    
    def start_dashboard(self, port=5000):
        """Start web dashboard"""
        print(f"🌐 Starting MalSim Pro Dashboard on port {port}")
        app = create_app(self.db)
        app.run(host='0.0.0.0', port=port, debug=True)

def main():
    parser = argparse.ArgumentParser(description='MalSim Pro - Malware Simulation Platform')
    parser.add_argument('--mode', choices=['simulate', 'dashboard'], 
                       default='dashboard', help='Operation mode')
    parser.add_argument('--type', choices=['ransomware', 'trojan', 'worm', 'spyware'],
                       help='Malware type to simulate')
    parser.add_argument('--duration', type=int, default=300,
                       help='Simulation duration in seconds')
    parser.add_argument('--port', type=int, default=5000,
                       help='Dashboard port')
    
    args = parser.parse_args()
    
    # Initialize MalSim Pro
    malsim = MalSimPro()
    
    # Safety check
    malsim.safety_check()
    
    if args.mode == 'simulate':
        if not args.type:
            print("❌ Please specify malware type with --type")
            sys.exit(1)
        malsim.run_simulation(args.type, args.duration)
    else:
        malsim.start_dashboard(args.port)

if __name__ == '__main__':
    main()
'''

# Write main.py file
with open('MalSimPro/main.py', 'w') as f:
    f.write(main_py_content)

print("✅ Created main.py - Entry point with CLI interface")