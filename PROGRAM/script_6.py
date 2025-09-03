# Create the ransomware simulator
ransomware_sim_content = '''"""
Ransomware Simulator for MalSim Pro
Simulates ransomware behavior safely for educational purposes

⚠️  WARNING: Educational use only. Only run in isolated VMs.
"""

import os
import time
import random
import shutil
from datetime import datetime
from typing import Dict, Any

class RansomwareSimulator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config.get('simulation_settings', {}).get('ransomware', {})
        self.test_dir = './test_files'
        self.results = {'encrypted_files': [], 'ransom_notes': [], 'actions': []}
        
        # Ensure test directory exists
        os.makedirs(self.test_dir, exist_ok=True)
    
    def run_simulation(self, duration: int = 300) -> Dict[str, Any]:
        """Run ransomware simulation"""
        print("🔒 Starting Ransomware Simulation")
        print("   ⚠️  This is a SAFE simulation - no real encryption!")
        
        start_time = datetime.now()
        
        try:
            # Phase 1: Create test files
            self._create_test_files()
            
            # Phase 2: Simulate file discovery
            self._simulate_file_discovery()
            
            # Phase 3: Simulate encryption process
            self._simulate_encryption()
            
            # Phase 4: Create ransom notes
            self._create_ransom_notes()
            
            # Phase 5: Simulate persistence
            self._simulate_persistence()
            
            # Phase 6: Simulate network communication
            self._simulate_c2_communication()
            
            end_time = datetime.now()
            
            self.results.update({
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration': (end_time - start_time).total_seconds(),
                'simulation_type': 'ransomware',
                'status': 'completed'
            })
            
        except Exception as e:
            self.results['error'] = str(e)
            self.results['status'] = 'failed'
        
        return self.results
    
    def _create_test_files(self):
        """Create test files for encryption simulation"""
        extensions = self.config.get('encrypt_extensions', ['.txt', '.doc', '.pdf'])
        file_count = self.config.get('test_files_count', 10)
        
        for i in range(file_count):
            ext = random.choice(extensions)
            filename = f"test_document_{i}{ext}"
            filepath = os.path.join(self.test_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(f"This is test content for file {i}\\n")
                f.write("IMPORTANT: This is simulated data for educational purposes.\\n")
                f.write("Real ransomware would encrypt actual user files.\\n")
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'created_test_files',
            'count': file_count
        })
    
    def _simulate_file_discovery(self):
        """Simulate file system scanning"""
        print("🔍 Scanning for target files...")
        time.sleep(2)
        
        target_files = []
        for root, dirs, files in os.walk(self.test_dir):
            for file in files:
                if any(file.endswith(ext) for ext in self.config.get('encrypt_extensions', [])):
                    target_files.append(os.path.join(root, file))
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'file_discovery',
            'targets_found': len(target_files)
        })
    
    def _simulate_encryption(self):
        """Simulate file encryption (safe - just renames files)"""
        print("🔐 Simulating file encryption...")
        
        encrypted_count = 0
        for root, dirs, files in os.walk(self.test_dir):
            for file in files:
                if any(file.endswith(ext) for ext in self.config.get('encrypt_extensions', [])):
                    if not file.endswith('.encrypted'):
                        filepath = os.path.join(root, file)
                        new_filepath = filepath + '.encrypted'
                        
                        # Simulate encryption by renaming
                        shutil.move(filepath, new_filepath)
                        
                        self.results['encrypted_files'].append(new_filepath)
                        encrypted_count += 1
                        
                        # Simulate encryption delay
                        time.sleep(0.5)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'file_encryption',
            'files_encrypted': encrypted_count
        })
    
    def _create_ransom_notes(self):
        """Create ransom note files"""
        ransom_text = self.config.get('ransom_note', 
            "🔒 Your files have been encrypted! (SIMULATION ONLY)")
        
        note_content = f'''
═══════════════════════════════════════════════════════════
🚨 RANSOMWARE SIMULATION - EDUCATIONAL PURPOSES ONLY 🚨
═══════════════════════════════════════════════════════════

{ransom_text}

⚠️  THIS IS A SAFE SIMULATION FOR LEARNING PURPOSES ⚠️

In a real ransomware attack:
- All your files would be encrypted with strong encryption
- Attackers would demand payment in cryptocurrency  
- Recovery without backup would be nearly impossible
- System would be severely compromised

SIMULATION DETAILS:
- Your files are safe (just renamed with .encrypted)
- No real encryption has occurred
- This is for educational cyber forensics training
- Generated at: {datetime.now().isoformat()}

═══════════════════════════════════════════════════════════
        '''
        
        # Create ransom notes in multiple locations
        note_locations = [
            os.path.join(self.test_dir, 'README_RANSOM.txt'),
            os.path.join(os.path.expanduser('~'), 'Desktop', 'RANSOM_NOTE.txt') if os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop')) else None
        ]
        
        for location in note_locations:
            if location:
                try:
                    with open(location, 'w') as f:
                        f.write(note_content)
                    self.results['ransom_notes'].append(location)
                except:
                    pass  # Skip if can't write to location
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'ransom_notes_created',
            'locations': len([l for l in note_locations if l])
        })
    
    def _simulate_persistence(self):
        """Simulate persistence mechanisms"""
        print("🔗 Simulating persistence mechanisms...")
        time.sleep(1)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'persistence_simulation',
            'methods': ['registry_modification', 'startup_folder', 'scheduled_task']
        })
    
    def _simulate_c2_communication(self):
        """Simulate command and control communication"""
        print("📡 Simulating C2 communication...")
        time.sleep(2)
        
        fake_c2_servers = ['192.168.1.100', '10.0.0.50', '172.16.1.1']
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'c2_communication',
            'servers_contacted': fake_c2_servers,
            'data_sent': 'encryption_status,system_info,ransom_demand'
        })
'''

with open('MalSimPro/simulators/ransomware_sim.py', 'w') as f:
    f.write(ransomware_sim_content)

print("✅ Created ransomware_sim.py - Safe ransomware behavior simulation")

# Create trojan simulator
trojan_sim_content = '''"""
Trojan Simulator for MalSim Pro
Simulates trojan/backdoor behavior safely

⚠️  WARNING: Educational use only. Only run in isolated VMs.
"""

import os
import time
import socket
import threading
from datetime import datetime
from typing import Dict, Any

class TrojanSimulator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config.get('simulation_settings', {}).get('trojan', {})
        self.results = {'connections': [], 'keystrokes': [], 'actions': []}
        self.running = False
    
    def run_simulation(self, duration: int = 300) -> Dict[str, Any]:
        """Run trojan simulation"""
        print("🎭 Starting Trojan/Backdoor Simulation")
        print("   ⚠️  This is a SAFE simulation - no real backdoor!")
        
        start_time = datetime.now()
        self.running = True
        
        try:
            # Phase 1: Establish fake backdoor
            self._simulate_backdoor_creation()
            
            # Phase 2: Simulate keylogger
            if self.config.get('keylog_simulation', True):
                self._simulate_keylogger()
            
            # Phase 3: Simulate screen capture
            self._simulate_screen_capture()
            
            # Phase 4: Simulate data exfiltration
            if self.config.get('data_exfil_simulation', True):
                self._simulate_data_exfiltration()
            
            # Phase 5: Wait and simulate periodic communication
            self._simulate_periodic_communication(duration)
            
            end_time = datetime.now()
            
            self.results.update({
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration': (end_time - start_time).total_seconds(),
                'simulation_type': 'trojan',
                'status': 'completed'
            })
            
        except Exception as e:
            self.results['error'] = str(e)
            self.results['status'] = 'failed'
        
        return self.results
    
    def _simulate_backdoor_creation(self):
        """Simulate creating a backdoor connection"""
        port = self.config.get('fake_backdoor_port', 8888)
        
        print(f"🚪 Creating fake backdoor on port {port}")
        
        # Simulate network listener (doesn't actually listen)
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'backdoor_created',
            'port': port,
            'protocol': 'TCP'
        })
        
        time.sleep(2)
    
    def _simulate_keylogger(self):
        """Simulate keylogger functionality"""
        print("⌨️  Simulating keylogger...")
        
        fake_keystrokes = [
            "username: user123",
            "password: ********", 
            "email: user@example.com",
            "search: how to remove malware",
            "document: confidential_report.docx"
        ]
        
        for keystroke in fake_keystrokes:
            self.results['keystrokes'].append({
                'timestamp': datetime.now().isoformat(),
                'data': keystroke,
                'application': 'notepad.exe'
            })
            time.sleep(1)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'keylogger_started',
            'captured_entries': len(fake_keystrokes)
        })
    
    def _simulate_screen_capture(self):
        """Simulate screen capture functionality"""
        print("📸 Simulating screen capture...")
        
        capture_interval = self.config.get('screen_capture_interval', 30)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'screen_capture_started',
            'interval_seconds': capture_interval,
            'simulated_captures': 3
        })
        
        time.sleep(2)
    
    def _simulate_data_exfiltration(self):
        """Simulate data theft and exfiltration"""
        print("📤 Simulating data exfiltration...")
        
        fake_stolen_data = [
            {'type': 'browser_passwords', 'count': 15},
            {'type': 'saved_forms', 'count': 8},
            {'type': 'browser_cookies', 'count': 234},
            {'type': 'system_info', 'size': '2.1KB'},
            {'type': 'file_listing', 'files': 1247}
        ]
        
        for data in fake_stolen_data:
            self.results['actions'].append({
                'timestamp': datetime.now().isoformat(),
                'action': 'data_stolen',
                'data_type': data['type'],
                'details': data
            })
            time.sleep(1)
    
    def _simulate_periodic_communication(self, duration: int):
        """Simulate periodic C2 communication"""
        print("📡 Simulating C2 communication...")
        
        c2_servers = ['badsite.evil', '192.168.100.1', 'c2.malicious.com']
        
        # Simulate communication every 30 seconds
        comm_count = 0
        elapsed = 0
        
        while elapsed < min(duration, 120):  # Cap at 2 minutes for demo
            time.sleep(30)
            elapsed += 30
            comm_count += 1
            
            self.results['connections'].append({
                'timestamp': datetime.now().isoformat(),
                'type': 'c2_communication',
                'server': c2_servers[comm_count % len(c2_servers)],
                'port': 443,
                'data_sent': f'heartbeat_{comm_count}',
                'data_received': 'commands_pending'
            })
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'periodic_communication_completed',
            'total_communications': comm_count
        })
'''

with open('MalSimPro/simulators/trojan_sim.py', 'w') as f:
    f.write(trojan_sim_content)

print("✅ Created trojan_sim.py - Trojan/backdoor behavior simulation")

# Create worm simulator  
worm_sim_content = '''"""
Worm Simulator for MalSim Pro
Simulates network worm propagation behavior

⚠️  WARNING: Educational use only. Only run in isolated VMs.
"""

import os
import time
import socket
import random
from datetime import datetime
from typing import Dict, Any, List

class WormSimulator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config.get('simulation_settings', {}).get('worm', {})
        self.results = {'scan_results': [], 'propagation_attempts': [], 'actions': []}
    
    def run_simulation(self, duration: int = 300) -> Dict[str, Any]:
        """Run worm simulation"""
        print("🪱 Starting Network Worm Simulation")
        print("   ⚠️  This is a SAFE simulation - no real propagation!")
        
        start_time = datetime.now()
        
        try:
            # Phase 1: Network discovery
            self._simulate_network_scan()
            
            # Phase 2: Vulnerability scanning
            self._simulate_vulnerability_scan()
            
            # Phase 3: Exploitation attempts
            self._simulate_exploitation_attempts()
            
            # Phase 4: Propagation simulation
            self._simulate_propagation()
            
            # Phase 5: Payload deployment
            self._simulate_payload_deployment()
            
            end_time = datetime.now()
            
            self.results.update({
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration': (end_time - start_time).total_seconds(),
                'simulation_type': 'worm',
                'status': 'completed'
            })
            
        except Exception as e:
            self.results['error'] = str(e)
            self.results['status'] = 'failed'
        
        return self.results
    
    def _simulate_network_scan(self):
        """Simulate network scanning for targets"""
        print("🌐 Scanning network for targets...")
        
        scan_range = self.config.get('scan_range', '127.0.0.1')
        
        # Simulate finding hosts
        fake_hosts = [
            '192.168.1.100', '192.168.1.101', '192.168.1.102',
            '10.0.0.10', '10.0.0.11', '172.16.1.5'
        ]
        
        for host in fake_hosts:
            self.results['scan_results'].append({
                'timestamp': datetime.now().isoformat(),
                'host': host,
                'status': 'alive',
                'response_time': random.uniform(1.0, 50.0)
            })
            time.sleep(0.5)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'network_scan',
            'hosts_found': len(fake_hosts),
            'scan_range': scan_range
        })
    
    def _simulate_vulnerability_scan(self):
        """Simulate vulnerability scanning"""
        print("🔍 Scanning for vulnerabilities...")
        
        ports = self.config.get('propagation_ports', [22, 80, 443, 445])
        vulnerabilities = [
            'SMB_EternalBlue', 'SSH_WeakAuth', 'HTTP_RCE', 'FTP_Anonymous'
        ]
        
        for host in ['192.168.1.100', '192.168.1.101']:
            for port in ports:
                vuln = random.choice(vulnerabilities)
                
                self.results['scan_results'].append({
                    'timestamp': datetime.now().isoformat(),
                    'host': host,
                    'port': port,
                    'service': f'service_{port}',
                    'vulnerability': vuln,
                    'exploitable': random.choice([True, False])
                })
                time.sleep(1)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'vulnerability_scan',
            'ports_scanned': len(ports),
            'vulnerabilities_found': len(vulnerabilities)
        })
    
    def _simulate_exploitation_attempts(self):
        """Simulate exploitation attempts"""
        print("💥 Simulating exploitation attempts...")
        
        exploit_attempts = self.config.get('fake_exploit_attempts', 5)
        
        for i in range(exploit_attempts):
            target_host = f'192.168.1.{100 + i}'
            exploit_type = random.choice(['buffer_overflow', 'code_injection', 'privilege_escalation'])
            
            self.results['propagation_attempts'].append({
                'timestamp': datetime.now().isoformat(),
                'target': target_host,
                'exploit_type': exploit_type,
                'success': random.choice([True, False]),
                'payload_deployed': random.choice([True, False])
            })
            
            time.sleep(2)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'exploitation_phase',
            'attempts': exploit_attempts,
            'success_rate': '60%'
        })
    
    def _simulate_propagation(self):
        """Simulate worm propagation"""
        print("🔄 Simulating worm propagation...")
        
        propagation_methods = [
            'file_share_infection',
            'email_mass_mailing', 
            'removable_media_infection',
            'network_service_exploitation'
        ]
        
        for method in propagation_methods:
            self.results['actions'].append({
                'timestamp': datetime.now().isoformat(),
                'action': 'propagation_attempt',
                'method': method,
                'targets_infected': random.randint(1, 5),
                'success': True
            })
            time.sleep(1)
    
    def _simulate_payload_deployment(self):
        """Simulate payload deployment on infected systems"""
        print("📦 Deploying payload on infected systems...")
        
        payloads = [
            'cryptocurrency_miner',
            'data_harvester',
            'additional_backdoor',
            'ddos_bot'
        ]
        
        for payload in payloads:
            self.results['actions'].append({
                'timestamp': datetime.now().isoformat(),
                'action': 'payload_deployment',
                'payload_type': payload,
                'systems_affected': random.randint(2, 8),
                'persistence_method': 'service_installation'
            })
            time.sleep(1)
'''

with open('MalSimPro/simulators/worm_sim.py', 'w') as f:
    f.write(worm_sim_content)

print("✅ Created worm_sim.py - Network worm propagation simulation")