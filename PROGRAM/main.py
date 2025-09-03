#!/usr/bin/env python3
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
import platform
from datetime import datetime

def load_config():
    """Load configuration from settings.json"""
    config_path = os.path.join(os.path.dirname(__file__), 'settings.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Configuration file not found. Creating default settings...")
        default_config = {
            "simulation": {"default_duration": 300, "safe_mode": True},
            "dashboard": {"host": "127.0.0.1", "port": 5000}
        }
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config

def safety_check():
    """Verify running in safe environment"""
    print("🔒 Performing safety checks...")
    
    # Basic VM detection
    vm_indicators = ['virtualbox', 'vmware', 'qemu', 'xen', 'kvm', 'virtual']
    system_info = platform.platform().lower()
    
    # For demo purposes, we'll be more lenient
    is_safe = any(indicator in system_info for indicator in vm_indicators)
    
    if not is_safe:
        print("⚠️  WARNING: VM environment not detected!")
        print("   This is an educational simulation platform.")
        print("   For maximum safety, please run in a virtual machine.")
        
        response = input("   Continue anyway for educational demo? (y/N): ")
        if response.lower() != 'y':
            print("❌ Exiting for safety. Please run in a VM environment.")
            sys.exit(1)
        else:
            print("✅ Continuing in educational demo mode...")
    else:
        print("✅ Safety check passed - VM environment detected")
    
    return True

def run_cli_simulation(sim_type, duration=300):
    """Run simulation from command line"""
    print(f"🔬 Starting {sim_type} simulation...")
    print(f"⏱️  Duration: {duration} seconds")
    print("📊 This would normally run the full simulation...")
    print("💡 For interactive experience, use dashboard mode instead!")
    print(f"   python {sys.argv[0]} --mode dashboard")
    return True

def start_dashboard(port=5000):
    """Start web dashboard"""
    print("🌐 Starting MalSim Pro Dashboard...")
    print(f"📱 Open your browser and go to: http://localhost:{port}")
    print("🔬 Use the web interface to start and monitor simulations")
    print("⚠️  Educational use only - Safe malware simulation platform")
    print()
    
    try:
        # Import and run the web interface
        from web_interface import create_app
        app = create_app()
        app.run(host='127.0.0.1', port=port, debug=False)
    except ImportError as e:
        print(f"❌ Failed to import web interface: {e}")
        print("   Make sure Flask is installed: pip install flask")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failed to start dashboard: {e}")
        sys.exit(1)

def main():
    """Main entry point"""
    print("🔬 MalSim Pro - Educational Malware Simulation Platform")
    print("=" * 60)
    
    parser = argparse.ArgumentParser(
        description='MalSim Pro - Educational Malware Simulation Platform',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --mode dashboard                    # Start web dashboard (recommended)
  %(prog)s --mode simulate --type ransomware  # Run CLI simulation
  %(prog)s --help                             # Show this help

Educational Use Only - Run in Virtual Machines Only!
        """
    )
    
    parser.add_argument('--mode', choices=['simulate', 'dashboard'], 
                       default='dashboard', 
                       help='Operation mode (default: dashboard)')
    parser.add_argument('--type', choices=['ransomware', 'trojan', 'worm', 'spyware'],
                       help='Malware type to simulate (required for simulate mode)')
    parser.add_argument('--duration', type=int, default=300,
                       help='Simulation duration in seconds (default: 300)')
    parser.add_argument('--port', type=int, default=5000,
                       help='Dashboard port (default: 5000)')

    args = parser.parse_args()

    # Load configuration
    config = load_config()
    
    # Safety check
    safety_check()
    
    print()
    
    if args.mode == 'simulate':
        if not args.type:
            print("❌ Please specify malware type with --type")
            print("   Available types: ransomware, trojan, worm, spyware")
            sys.exit(1)
        run_cli_simulation(args.type, args.duration)
    else:
        start_dashboard(args.port)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 MalSim Pro stopped by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
