#!/usr/bin/env python3
"""
Worm Simulator - Educational Network Worm Behavior Simulation
SAFE VERSION - Simulates network scanning and propagation attempts

This simulator demonstrates worm behavior patterns:
- Network scanning
- Vulnerability exploitation attempts
- Self-replication simulation
- Lateral movement
- Network disruption
"""

import os
import sys
import time
import json
import random
import threading
from datetime import datetime

class WormSimulator:
    def __init__(self, config=None):
        self.config = config or {}
        self.is_running = False
        self.test_dir = "/tmp/malsim_worm_test"
        self.infected_hosts = []
        self.network_scans = []
        
    def setup_test_environment(self):
        """Create test environment for worm simulation"""
        print("🔧 Setting up worm test environment...")
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create fake network topology
        network_map = {
            "192.168.1.0/24": {
                "192.168.1.1": {"type": "router", "os": "Linux", "services": ["ssh", "http"]},
                "192.168.1.10": {"type": "server", "os": "Windows Server", "services": ["smb", "rdp", "sql"]},
                "192.168.1.50": {"type": "workstation", "os": "Windows 10", "services": ["smb", "rdp"]},
                "192.168.1.75": {"type": "workstation", "os": "Ubuntu", "services": ["ssh", "ftp"]},
                "192.168.1.100": {"type": "printer", "os": "Embedded", "services": ["http", "snmp"]}
            }
        }
        
        network_file = os.path.join(self.test_dir, "network_topology.json")
        with open(network_file, 'w') as f:
            json.dump(network_map, f, indent=2)
            
        return network_map
    
    def simulate_network_scanning(self, network_map):
        """Simulate aggressive network scanning"""
        print("🔍 Starting network reconnaissance...")
        
        scan_techniques = [
            "TCP SYN Scan",
            "UDP Scan", 
            "Ping Sweep",
            "Port Scan",
            "Service Detection",
            "OS Fingerprinting",
            "Vulnerability Scan"
        ]
        
        for subnet, hosts in network_map.items():
            print(f"   🌐 Scanning subnet: {subnet}")
            
            for ip, info in hosts.items():
                if not self.is_running:
                    break
                    
                print(f"   🎯 Scanning host: {ip}")
                
                for technique in scan_techniques:
                    scan_result = {
                        'timestamp': datetime.now().isoformat(),
                        'target_ip': ip,
                        'technique': technique,
                        'os_detected': info['os'],
                        'services_found': info['services'],
                        'vulnerabilities': self.detect_vulnerabilities(info)
                    }
                    
                    self.network_scans.append(scan_result)
                    print(f"     📡 {technique}: {ip} ({info['os']}) - {len(scan_result['vulnerabilities'])} vulns found")
                    time.sleep(random.uniform(0.5, 1.5))
        
        return len(self.network_scans)
    
    def detect_vulnerabilities(self, host_info):
        """Simulate vulnerability detection"""
        possible_vulns = {
            "Windows Server": [
                "MS17-010 (EternalBlue)",
                "CVE-2020-1472 (Zerologon)",
                "CVE-2019-0708 (BlueKeep)",
                "SMB NULL Session"
            ],
            "Windows 10": [
                "MS17-010 (EternalBlue)",
                "CVE-2019-0708 (BlueKeep)",
                "Weak RDP Configuration"
            ],
            "Ubuntu": [
                "CVE-2021-4034 (PwnKit)",
                "Weak SSH Configuration",
                "Unpatched Sudo"
            ],
            "Linux": [
                "CVE-2021-4034 (PwnKit)",
                "Weak SSH Keys",
                "Default Credentials"
            ],
            "Embedded": [
                "Default Credentials",
                "Weak Authentication",
                "Unencrypted Communication"
            ]
        }
        
        os_type = host_info['os']
        available_vulns = possible_vulns.get(os_type, ["Unknown vulnerability"])
        
        # Randomly select 1-3 vulnerabilities
        num_vulns = random.randint(1, min(3, len(available_vulns)))
        return random.sample(available_vulns, num_vulns)
    
    def simulate_exploitation(self):
        """Simulate exploitation attempts"""
        print("💥 Attempting exploitation...")
        
        successful_infections = []
        
        for scan in self.network_scans:
            if not self.is_running:
                break
                
            target_ip = scan['target_ip']
            vulnerabilities = scan['vulnerabilities']
            
            for vuln in vulnerabilities:
                if not self.is_running:
                    break
                    
                print(f"   🔓 Exploiting {vuln} on {target_ip}")
                
                # Simulate exploitation success rate
                success_rate = {
                    "MS17-010": 0.9,
                    "CVE-2021-4034": 0.8,
                    "Default Credentials": 0.7,
                    "Weak SSH Configuration": 0.6
                }
                
                base_success = 0.3  # Default success rate
                actual_success = success_rate.get(vuln.split()[0], base_success)
                
                if random.random() < actual_success:
                    infection = {
                        'timestamp': datetime.now().isoformat(),
                        'target_ip': target_ip,
                        'vulnerability': vuln,
                        'method': 'Remote Code Execution',
                        'status': 'SUCCESS'
                    }
                    successful_infections.append(infection)
                    self.infected_hosts.append(target_ip)
                    
                    print(f"   ✅ Successfully infected: {target_ip}")
                    self.simulate_worm_installation(target_ip)
                    
                else:
                    print(f"   ❌ Exploitation failed: {target_ip}")
                
                time.sleep(random.uniform(1, 3))
        
        return successful_infections
    
    def simulate_worm_installation(self, target_ip):
        """Simulate worm installation on infected host"""
        print(f"   📦 Installing worm on {target_ip}")
        
        worm_files = [
            "worm_payload.exe",
            "network_scanner.dll", 
            "propagation_module.bin",
            "persistence_script.vbs"
        ]
        
        for worm_file in worm_files:
            file_path = os.path.join(self.test_dir, f"{target_ip}_{worm_file}")
            worm_content = f"""
FAKE WORM COMPONENT - {worm_file}
Target Host: {target_ip}
Installation Time: {datetime.now()}
Capabilities: Network scanning, Self-replication, Data theft
Next Targets: Calculate new subnet ranges
Persistence: Service installation, Registry modification
"""
            with open(file_path, 'w') as f:
                f.write(worm_content)
            
            print(f"     📁 Installed: {worm_file}")
            time.sleep(0.3)
    
    def simulate_lateral_movement(self):
        """Simulate lateral movement and further propagation"""
        print("🚀 Simulating lateral movement...")
        
        lateral_actions = []
        
        for infected_ip in self.infected_hosts:
            if not self.is_running:
                break
                
            print(f"   🔄 Using {infected_ip} as pivot point")
            
            # Simulate discovering new network ranges
            new_ranges = [
                "10.0.0.0/24",
                "172.16.0.0/24", 
                "192.168.2.0/24"
            ]
            
            for network_range in new_ranges:
                action = {
                    'timestamp': datetime.now().isoformat(),
                    'pivot_host': infected_ip,
                    'action': 'Network Discovery',
                    'target_range': network_range,
                    'new_hosts_found': random.randint(3, 15)
                }
                lateral_actions.append(action)
                
                print(f"     🌐 Discovered {action['new_hosts_found']} hosts in {network_range}")
                time.sleep(1)
        
        return lateral_actions
    
    def simulate_payload_delivery(self):
        """Simulate malicious payload delivery"""
        print("📦 Delivering secondary payloads...")
        
        payloads = [
            {"name": "Cryptocurrency Miner", "impact": "HIGH CPU usage"},
            {"name": "Data Harvester", "impact": "Sensitive file theft"},
            {"name": "DDoS Bot", "impact": "Network disruption"},
            {"name": "Backdoor", "impact": "Persistent access"}
        ]
        
        delivered_payloads = []
        
        for infected_ip in self.infected_hosts:
            if not self.is_running:
                break
                
            # Each infected host gets 1-2 random payloads
            num_payloads = random.randint(1, 2)
            selected_payloads = random.sample(payloads, num_payloads)
            
            for payload in selected_payloads:
                delivery = {
                    'timestamp': datetime.now().isoformat(),
                    'target_host': infected_ip,
                    'payload_name': payload['name'],
                    'expected_impact': payload['impact'],
                    'delivery_method': 'Direct Installation'
                }
                delivered_payloads.append(delivery)
                
                print(f"   💣 Delivered '{payload['name']}' to {infected_ip}")
                time.sleep(0.5)
        
        return delivered_payloads
    
    def run_simulation(self, duration=300):
        """Main worm simulation execution"""
        self.is_running = True
        start_time = datetime.now()
        results = {
            'type': 'worm',
            'start_time': start_time.isoformat(),
            'events': [],
            'hosts_scanned': 0,
            'hosts_infected': 0,
            'network_connections': 0,
            'payloads_delivered': 0,
            'threat_level': 'CRITICAL'
        }
        
        try:
            print("🪱 STARTING NETWORK WORM SIMULATION")
            print("=" * 50)
            
            # Phase 1: Environment Setup
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'initialization',
                'action': 'Setting up network environment',
                'details': 'Creating fake network topology'
            })
            network_map = self.setup_test_environment()
            
            # Phase 2: Network Scanning
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'reconnaissance',
                'action': 'Scanning network for targets',
                'details': 'Performing comprehensive network reconnaissance'
            })
            scans_performed = self.simulate_network_scanning(network_map)
            results['hosts_scanned'] = scans_performed
            results['network_connections'] = scans_performed * 3  # Multiple connections per scan
            
            if not self.is_running:
                return results
            
            # Phase 3: Exploitation
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'exploitation',
                'action': 'Exploiting vulnerabilities',
                'details': 'Attempting to infect discovered hosts'
            })
            successful_infections = self.simulate_exploitation()
            results['hosts_infected'] = len(successful_infections)
            
            if not self.is_running:
                return results
            
            # Phase 4: Lateral Movement
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'lateral_movement',
                'action': 'Expanding through network',
                'details': 'Using infected hosts to find new targets'
            })
            lateral_actions = self.simulate_lateral_movement()
            
            # Phase 5: Payload Delivery
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'payload_delivery',
                'action': 'Delivering secondary payloads',
                'details': 'Installing additional malicious components'
            })
            delivered_payloads = self.simulate_payload_delivery()
            results['payloads_delivered'] = len(delivered_payloads)
            
            # Final Results
            results['end_time'] = datetime.now().isoformat()
            results['duration'] = (datetime.now() - start_time).total_seconds()
            
            print("
🎯 WORM SIMULATION COMPLETED")
            print(f"🔍 Hosts scanned: {results['hosts_scanned']}")
            print(f"💥 Hosts infected: {results['hosts_infected']}")
            print(f"🌐 Network connections: {results['network_connections']}")
            print(f"💣 Payloads delivered: {results['payloads_delivered']}")
            print(f"📂 Test directory: {self.test_dir}")
            print("
⚠️ REMEMBER: This was a SAFE simulation for education!")
            
            return results
            
        except Exception as e:
            print(f"❌ Simulation error: {e}")
            results['error'] = str(e)
            return results
        
        finally:
            self.is_running = False
    
    def cleanup(self):
        """Clean up test environment"""
        try:
            if os.path.exists(self.test_dir):
                import shutil
                shutil.rmtree(self.test_dir)
                print(f"🧹 Cleaned up test directory: {self.test_dir}")
        except Exception as e:
            print(f"❌ Cleanup failed: {e}")

if __name__ == "__main__":
    # Standalone test
    simulator = WormSimulator()
    print("🔬 Testing Worm Simulator")
    results = simulator.run_simulation(60)
    print(f"
📋 Results: {json.dumps(results, indent=2)}")
    
    input("
Press Enter to cleanup...")
    simulator.cleanup()
