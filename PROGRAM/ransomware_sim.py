#!/usr/bin/env python3
"""
Ransomware Simulator - Educational Malware Behavior Simulation
SAFE VERSION - Only affects test directories and files

This simulator demonstrates ransomware behavior patterns:
- File encryption simulation
- Ransom note creation
- File extension changes
- Directory traversal
- Registry/system modification simulation
"""

import os
import sys
import time
import json
import shutil
import hashlib
import random
import threading
from datetime import datetime
from pathlib import Path

class RansomwareSimulator:
    def __init__(self, config=None):
        self.config = config or {}
        self.is_running = False
        self.test_dir = "/tmp/malsim_ransomware_test"
        self.encrypted_files = []
        self.ransom_note = """
╔══════════════════════════════════════╗
║         🔒 YOUR FILES ARE ENCRYPTED! ║
╚══════════════════════════════════════╝

ALL YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED!

📁 Documents, Pictures, Videos, Databases - ALL LOCKED!

💰 To decrypt your files, you need to pay:
   Bitcoin: 0.5 BTC (~$15,000)
   
📧 Contact: recovery@malsim-education.fake
   (This is FAKE - Educational simulation only!)

⚠️  DO NOT turn off your computer!
⚠️  DO NOT delete this file!
⚠️  DO NOT try to decrypt files manually!

🕐 You have 72 hours before the price DOUBLES!

═══════════════════════════════════════
🎓 EDUCATIONAL NOTICE: This is a safe simulation 
for cybersecurity learning. No real encryption occurred.
═══════════════════════════════════════
"""

    def setup_test_environment(self):
        """Create realistic test environment with fake user data"""
        print("🔧 Setting up test environment...")
        
        # Create test directory structure
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create subdirectories like real user folders
        folders = [
            "Documents", "Pictures", "Desktop", "Downloads", 
            "Music", "Videos", "Work", "Personal", "Backup"
        ]
        
        for folder in folders:
            folder_path = os.path.join(self.test_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Create fake files in each folder
            self.create_fake_files(folder_path, folder)
    
    def create_fake_files(self, folder_path, folder_type):
        """Create realistic fake files"""
        file_templates = {
            "Documents": [
                ("important_contract.doc", "IMPORTANT CONTRACT\n\nThis is a fake document for simulation..."),
                ("financial_report.xlsx", "Financial Data\nQ1: $50,000\nQ2: $75,000\n..."),
                ("passwords.txt", "Gmail: mypassword123\nBank: supersecret456\n..."),
                ("presentation.ppt", "Company Presentation\nSlide 1: Overview\n..."),
                ("resume.pdf", "John Doe Resume\nExperience: 5 years...\n")
            ],
            "Pictures": [
                ("family_vacation.jpg", "JPEG_FAKE_HEADER\nFamily vacation photo data..."),
                ("wedding_photos.png", "PNG_FAKE_HEADER\nWedding photo collection..."),
                ("graduation.gif", "GIF_FAKE_HEADER\nGraduation ceremony..."),
                ("baby_photos.bmp", "BMP_FAKE_HEADER\nBaby photos collection...")
            ],
            "Work": [
                ("project_files.zip", "ZIP_ARCHIVE\nProject source code and documents..."),
                ("database_backup.sql", "-- Database Backup\nCREATE TABLE users...\n"),
                ("client_data.csv", "Name,Email,Phone\nJohn,john@email.com,123...\n")
            ],
            "Personal": [
                ("diary.txt", "Personal Diary\nToday was a good day...\n"),
                ("tax_documents.pdf", "Tax Return 2024\nIncome: $65,000...\n")
            ]
        }
        
        if folder_type in file_templates:
            for filename, content in file_templates[folder_type]:
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'w') as f:
                    f.write(content + "\n" + "A" * 1000)  # Add padding to make files bigger
    
    def simulate_file_discovery(self):
        """Simulate ransomware discovering and cataloging files"""
        print("🔍 Discovering files to encrypt...")
        discovered_files = []
        
        for root, dirs, files in os.walk(self.test_dir):
            for file in files:
                if not file.endswith('.ENCRYPTED') and not file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    discovered_files.append(file_path)
                    print(f"   📁 Found: {file_path}")
                    time.sleep(0.1)  # Simulate processing time
        
        return discovered_files
    
    def simulate_encryption(self, file_path):
        """Simulate file encryption process"""
        try:
            # Read original file
            with open(file_path, 'rb') as f:
                original_data = f.read()
            
            # Simulate encryption (just reverse bytes + add header)
            fake_encrypted = b"MALSIM_ENCRYPTED_HEADER_" + original_data[::-1]
            
            # Write "encrypted" version
            encrypted_path = file_path + ".ENCRYPTED"
            with open(encrypted_path, 'wb') as f:
                f.write(fake_encrypted)
            
            # Remove original
            os.remove(file_path)
            
            # Log the action
            self.encrypted_files.append({
                'original': file_path,
                'encrypted': encrypted_path,
                'size': len(original_data),
                'timestamp': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Encryption failed for {file_path}: {e}")
            return False
    
    def create_ransom_notes(self):
        """Create ransom notes in multiple locations"""
        print("📝 Creating ransom notes...")
        
        note_locations = [
            os.path.join(self.test_dir, "READ_ME_FOR_DECRYPT.txt"),
            os.path.join(self.test_dir, "Desktop", "DECRYPT_INSTRUCTIONS.txt"),
            os.path.join(self.test_dir, "Documents", "HOW_TO_RECOVER_FILES.txt"),
        ]
        
        for location in note_locations:
            try:
                with open(location, 'w') as f:
                    f.write(self.ransom_note)
                print(f"   📋 Created ransom note: {location}")
            except Exception as e:
                print(f"❌ Failed to create ransom note at {location}: {e}")
    
    def simulate_system_changes(self):
        """Simulate system-level changes (safely)"""
        print("⚙️ Simulating system modifications...")
        
        # Create fake registry changes log
        registry_log = os.path.join(self.test_dir, "registry_changes.log")
        registry_changes = [
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\MalSim = C:\\temp\\malsim.exe",
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DisableTaskMgr = 1",
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DisableCMD = 1"
        ]
        
        with open(registry_log, 'w') as f:
            f.write("SIMULATED REGISTRY CHANGES:\n")
            for change in registry_changes:
                f.write(f"ADDED: {change}\n")
                print(f"   🔧 Simulated: {change}")
                time.sleep(0.5)
    
    def simulate_network_communication(self):
        """Simulate C&C server communication"""
        print("🌐 Simulating network communication...")
        
        fake_servers = [
            "185.159.158.1:8080",
            "tor://3g2upl4pq6kufc4m.onion:9050",
            "192.168.1.100:4444"
        ]
        
        for server in fake_servers:
            print(f"   📡 Attempting connection to C&C server: {server}")
            time.sleep(1)
            print(f"   ✅ Sent victim info to: {server}")
    
    def run_simulation(self, duration=300):
        """Main simulation execution"""
        self.is_running = True
        start_time = datetime.now()
        results = {
            'type': 'ransomware',
            'start_time': start_time.isoformat(),
            'events': [],
            'files_affected': 0,
            'directories_created': 0,
            'network_connections': 0,
            'system_changes': 0,
            'threat_level': 'CRITICAL'
        }
        
        try:
            print("🔥 STARTING RANSOMWARE SIMULATION")
            print("=" * 50)
            
            # Phase 1: Environment Setup
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'initialization',
                'action': 'Setting up test environment',
                'details': 'Creating fake user directories and files'
            })
            self.setup_test_environment()
            
            if not self.is_running:
                return results
            
            # Phase 2: File Discovery
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'discovery',
                'action': 'Scanning for files to encrypt',
                'details': 'Enumerating target file types'
            })
            files_to_encrypt = self.simulate_file_discovery()
            time.sleep(2)
            
            if not self.is_running:
                return results
            
            # Phase 3: System Modification
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'system_modification',
                'action': 'Modifying system settings',
                'details': 'Disabling security features and adding persistence'
            })
            self.simulate_system_changes()
            results['system_changes'] = 3
            
            if not self.is_running:
                return results
            
            # Phase 4: Encryption Process
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'encryption',
                'action': 'Starting file encryption',
                'details': f'Beginning encryption of {len(files_to_encrypt)} files'
            })
            
            for i, file_path in enumerate(files_to_encrypt[:20]):  # Limit for demo
                if not self.is_running:
                    break
                    
                print(f"🔒 Encrypting ({i+1}/{len(files_to_encrypt)}): {os.path.basename(file_path)}")
                
                if self.simulate_encryption(file_path):
                    results['events'].append({
                        'time': datetime.now().isoformat(),
                        'phase': 'encryption',
                        'action': 'File encrypted',
                        'details': f'Encrypted: {os.path.basename(file_path)}'
                    })
                    results['files_affected'] += 1
                
                time.sleep(random.uniform(0.5, 2.0))  # Realistic encryption timing
            
            if not self.is_running:
                return results
            
            # Phase 5: Ransom Note Creation
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'ransom',
                'action': 'Creating ransom notes',
                'details': 'Placing ransom notes in multiple locations'
            })
            self.create_ransom_notes()
            
            # Phase 6: Network Communication
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'communication',
                'action': 'Contacting C&C servers',
                'details': 'Reporting successful infection'
            })
            self.simulate_network_communication()
            results['network_connections'] = 3
            
            # Final Results
            results['end_time'] = datetime.now().isoformat()
            results['duration'] = (datetime.now() - start_time).total_seconds()
            results['directories_created'] = len(os.listdir(self.test_dir))
            
            print("\n🎯 RANSOMWARE SIMULATION COMPLETED")
            print(f"📊 Files affected: {results['files_affected']}")
            print(f"📂 Test directory: {self.test_dir}")
            print(f"⏱️ Duration: {results['duration']:.1f} seconds")
            print("\n⚠️ REMEMBER: This was a SAFE simulation for education!")
            
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
                shutil.rmtree(self.test_dir)
                print(f"🧹 Cleaned up test directory: {self.test_dir}")
        except Exception as e:
            print(f"❌ Cleanup failed: {e}")

if __name__ == "__main__":
    # Standalone test
    simulator = RansomwareSimulator()
    print("🔬 Testing Ransomware Simulator")
    results = simulator.run_simulation(60)
    print(f"\n📋 Results: {json.dumps(results, indent=2)}")
    
    input("\nPress Enter to cleanup...")
    simulator.cleanup()
