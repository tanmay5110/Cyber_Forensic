# Fix the ransomware simulator with proper characters
ransomware_sim_content = '''"""
Ransomware Simulator for MalSim Pro
Simulates ransomware behavior safely for educational purposes

WARNING: Educational use only. Only run in isolated VMs.
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
        
        note_content = f"""
==================================================================
🚨 RANSOMWARE SIMULATION - EDUCATIONAL PURPOSES ONLY 🚨
==================================================================

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

==================================================================
        """
        
        # Create ransom notes in test directory
        note_location = os.path.join(self.test_dir, 'README_RANSOM.txt')
        
        try:
            with open(note_location, 'w') as f:
                f.write(note_content)
            self.results['ransom_notes'].append(note_location)
        except Exception as e:
            print(f"Could not create ransom note: {e}")
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'ransom_notes_created',
            'locations': 1
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

print("✅ Created ransomware_sim.py - Safe ransomware behavior simulation (fixed)")

# Create spyware simulator
spyware_sim_content = '''"""
Spyware Simulator for MalSim Pro
Simulates spyware data collection behavior

WARNING: Educational use only. Only run in isolated VMs.
"""

import os
import time
import random
from datetime import datetime
from typing import Dict, Any

class SpywareSimulator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config.get('simulation_settings', {}).get('spyware', {})
        self.results = {'keylog_data': [], 'screenshots': [], 'browser_data': [], 'actions': []}
        self.log_dir = './logs'
        
        # Ensure log directory exists
        os.makedirs(self.log_dir, exist_ok=True)
    
    def run_simulation(self, duration: int = 300) -> Dict[str, Any]:
        """Run spyware simulation"""
        print("👁️  Starting Spyware Simulation")
        print("   ⚠️  This is a SAFE simulation - no real data theft!")
        
        start_time = datetime.now()
        
        try:
            # Phase 1: Simulate keylogger
            self._simulate_keylogger()
            
            # Phase 2: Simulate screen capture
            self._simulate_screen_capture()
            
            # Phase 3: Simulate browser data harvesting
            if self.config.get('browser_data_simulation', True):
                self._simulate_browser_harvesting()
            
            # Phase 4: Simulate credential harvesting
            if self.config.get('credential_harvest_simulation', True):
                self._simulate_credential_harvesting()
            
            # Phase 5: Simulate data exfiltration
            self._simulate_data_exfiltration()
            
            end_time = datetime.now()
            
            self.results.update({
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration': (end_time - start_time).total_seconds(),
                'simulation_type': 'spyware',
                'status': 'completed'
            })
            
        except Exception as e:
            self.results['error'] = str(e)
            self.results['status'] = 'failed'
        
        return self.results
    
    def _simulate_keylogger(self):
        """Simulate keylogger data collection"""
        print("⌨️  Simulating keylogger...")
        
        duration = self.config.get('keylog_duration', 60)
        fake_keystrokes = [
            "password123",
            "user@company.com", 
            "confidential document",
            "banking login",
            "credit card: 4111-****-****-1234",
            "social security: ***-**-1234",
            "how to detect spyware",
            "antivirus download"
        ]
        
        log_file = os.path.join(self.log_dir, 'keylog_simulation.txt')
        
        with open(log_file, 'w') as f:
            f.write("SIMULATED KEYLOGGER DATA - EDUCATIONAL ONLY\\n")
            f.write(f"Started: {datetime.now()}\\n\\n")
            
            for i in range(min(8, duration // 10)):
                keystroke = random.choice(fake_keystrokes)
                timestamp = datetime.now().isoformat()
                
                entry = f"[{timestamp}] App: notepad.exe | Keys: {keystroke}\\n"
                f.write(entry)
                
                self.results['keylog_data'].append({
                    'timestamp': timestamp,
                    'application': 'notepad.exe',
                    'data': keystroke
                })
                
                time.sleep(2)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'keylogger_simulation',
            'duration': duration,
            'entries_captured': len(self.results['keylog_data']),
            'log_file': log_file
        })
    
    def _simulate_screen_capture(self):
        """Simulate screen capture functionality"""
        print("📸 Simulating screen capture...")
        
        interval = self.config.get('screenshot_interval', 10)
        capture_count = 5
        
        for i in range(capture_count):
            screenshot_name = f"screenshot_{i}_{datetime.now().strftime('%H%M%S')}.png"
            
            # Simulate screenshot (just create empty file)
            screenshot_path = os.path.join(self.log_dir, screenshot_name)
            with open(screenshot_path, 'w') as f:
                f.write("SIMULATED SCREENSHOT FILE\\n")
                f.write(f"Captured at: {datetime.now()}\\n")
            
            self.results['screenshots'].append({
                'timestamp': datetime.now().isoformat(),
                'filename': screenshot_name,
                'size': '1024x768',
                'application': 'desktop'
            })
            
            time.sleep(interval // capture_count)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'screen_capture',
            'captures_taken': capture_count,
            'interval': interval
        })
    
    def _simulate_browser_harvesting(self):
        """Simulate browser data harvesting"""
        print("🌐 Simulating browser data harvesting...")
        
        fake_browser_data = [
            {'type': 'password', 'site': 'facebook.com', 'username': 'user123'},
            {'type': 'password', 'site': 'gmail.com', 'username': 'user@email.com'},
            {'type': 'cookie', 'site': 'amazon.com', 'value': 'session_abc123'},
            {'type': 'autofill', 'field': 'credit_card', 'value': '4111****1234'},
            {'type': 'history', 'url': 'https://bank.example.com/login'},
            {'type': 'bookmark', 'title': 'Online Banking', 'url': 'https://bank.com'}
        ]
        
        browser_log = os.path.join(self.log_dir, 'browser_data_simulation.txt')
        
        with open(browser_log, 'w') as f:
            f.write("SIMULATED BROWSER DATA HARVEST - EDUCATIONAL ONLY\\n")
            f.write(f"Harvested: {datetime.now()}\\n\\n")
            
            for data in fake_browser_data:
                f.write(f"{data}\\n")
                
                self.results['browser_data'].append({
                    'timestamp': datetime.now().isoformat(),
                    'data_type': data['type'],
                    'details': data
                })
                
                time.sleep(1)
        
        self.results['actions'].append({
            'timestamp': datetime.now().isoformat(),
            'action': 'browser_harvesting',
            'data_stolen': len(fake_browser_data),
            'log_file': browser_log
        })
    
    def _simulate_credential_harvesting(self):
        """Simulate credential harvesting from various sources"""
        print("🔑 Simulating credential harvesting...")
        
        credential_sources = [
            'windows_credential_manager',
            'browser_saved_passwords', 
            'email_client_passwords',
            'ftp_client_passwords',
            'wifi_passwords'
        ]
        
        for source in credential_sources:
            self.results['actions'].append({
                'timestamp': datetime.now().isoformat(),
                'action': 'credential_harvest',
                'source': source,
                'credentials_found': random.randint(2, 15)
            })
            time.sleep(1)
    
    def _simulate_data_exfiltration(self):
        """Simulate data exfiltration"""
        print("📤 Simulating data exfiltration...")
        
        exfil_methods = [
            {'method': 'email', 'destination': 'attacker@evil.com'},
            {'method': 'ftp_upload', 'destination': 'ftp.badsite.com'},
            {'method': 'http_post', 'destination': 'collector.malware.net'}
        ]
        
        for method in exfil_methods:
            self.results['actions'].append({
                'timestamp': datetime.now().isoformat(),
                'action': 'data_exfiltration',
                'method': method['method'],
                'destination': method['destination'],
                'data_size': f"{random.randint(100, 5000)}KB"
            })
            time.sleep(2)
'''

with open('MalSimPro/simulators/spyware_sim.py', 'w') as f:
    f.write(spyware_sim_content)

print("✅ Created spyware_sim.py - Spyware data collection simulation")