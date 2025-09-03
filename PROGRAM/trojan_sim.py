#!/usr/bin/env python3
"""
Trojan/Backdoor Simulator - Educational Malware Behavior Simulation
SAFE VERSION - Simulates backdoor and data theft behaviors

This simulator demonstrates trojan behavior patterns:
- Backdoor installation
- Keylogger simulation
- Data exfiltration
- Remote access simulation
- Stealth operations
"""

import os
import sys
import time
import json
import random
import socket
import threading
from datetime import datetime
from pathlib import Path

class TrojanSimulator:
    def __init__(self, config=None):
        self.config = config or {}
        self.is_running = False
        self.test_dir = "/tmp/malsim_trojan_test"
        self.keylog_data = []
        self.stolen_data = []
        self.backdoor_active = False
        
    def setup_test_environment(self):
        """Create test environment for trojan simulation"""
        print("🔧 Setting up trojan test environment...")
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create fake sensitive files
        sensitive_files = {
            "browser_passwords.txt": "Chrome Saved Passwords:\nfacebook.com: user123:pass456\ngmail.com: john@email.com:secret789\n",
            "banking_info.txt": "Bank Account: 1234567890\nRouting: 987654321\nPIN: 1234\n",
            "crypto_wallet.txt": "Bitcoin Wallet: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa\nSeed: abandon ability able about above absent absorb abstract\n",
            "ssh_keys.txt": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...\n",
            "work_documents.txt": "Company Secrets:\nProject X Budget: $2M\nClient List: Apple, Google, Microsoft\n"
        }
        
        for filename, content in sensitive_files.items():
            file_path = os.path.join(self.test_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
    
    def simulate_backdoor_installation(self):
        """Simulate backdoor installation process"""
        print("🚪 Installing backdoor...")
        
        # Create fake backdoor files
        backdoor_files = [
            "svchost_backup.exe",  # Disguised as system file
            "update_manager.dll",  # Fake update component
            "system32_cache.tmp"   # Hidden system file
        ]
        
        for backdoor_file in backdoor_files:
            file_path = os.path.join(self.test_dir, backdoor_file)
            backdoor_content = f"""
FAKE BACKDOOR PAYLOAD - {backdoor_file}
Created: {datetime.now()}
Capabilities: Remote shell, File transfer, Keylogging
C&C Server: 192.168.1.100:4444
Persistence: Registry Run key
Encryption: XOR with key 0xAB
"""
            with open(file_path, 'w') as f:
                f.write(backdoor_content)
            
            print(f"   📁 Created: {backdoor_file}")
            time.sleep(0.5)
        
        self.backdoor_active = True
        return len(backdoor_files)
    
    def simulate_keylogger(self):
        """Simulate keylogger capturing user input"""
        print("⌨️ Starting keylogger...")
        
        # Simulate captured keystrokes
        fake_keystrokes = [
            "chrome.exe - facebook.com login",
            "Username: john.doe@email.com",
            "Password: MySecretPass123!",
            "gmail.com - composing email",
            "To: boss@company.com",
            "Subject: Confidential Project Update",
            "Message: The new product launch...",
            "notepad.exe - personal notes",
            "Bitcoin wallet password: crypto2024secure",
            "Bank PIN entered: 1234",
            "Credit card: 4532-1234-5678-9012",
            "Excel - financial_data.xlsx",
            "Salary information: $85,000",
            "Tax ID: 123-45-6789"
        ]
        
        for i, keystroke in enumerate(fake_keystrokes):
            if not self.is_running:
                break
                
            timestamp = datetime.now()
            self.keylog_data.append({
                'timestamp': timestamp.isoformat(),
                'application': keystroke.split(' - ')[0] if ' - ' in keystroke else 'system',
                'data': keystroke,
                'sensitive': any(word in keystroke.lower() for word in ['password', 'pin', 'credit', 'social'])
            })
            
            print(f"   📝 Captured: {keystroke}")
            time.sleep(random.uniform(1, 3))
        
        # Save keylog data
        keylog_file = os.path.join(self.test_dir, "keylog_data.log")
        with open(keylog_file, 'w') as f:
            json.dump(self.keylog_data, f, indent=2)
            
        return len(self.keylog_data)
    
    def simulate_data_theft(self):
        """Simulate stealing sensitive data"""
        print("🕵️ Stealing sensitive data...")
        
        # Target file types and locations
        target_patterns = [
            "*.txt", "*.doc", "*.pdf", "*.xlsx", 
            "*password*", "*bank*", "*crypto*", "*key*"
        ]
        
        for root, dirs, files in os.walk(self.test_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                
                # Simulate analyzing file content
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content_preview = f.read(200)  # First 200 chars
                
                self.stolen_data.append({
                    'file': file_path,
                    'size': file_size,
                    'timestamp': datetime.now().isoformat(),
                    'content_preview': content_preview,
                    'risk_level': self.assess_risk_level(file, content_preview)
                })
                
                print(f"   💾 Stolen: {file} ({file_size} bytes)")
                time.sleep(0.5)
        
        return len(self.stolen_data)
    
    def assess_risk_level(self, filename, content):
        """Assess the risk level of stolen data"""
        high_risk_keywords = ['password', 'bank', 'credit', 'ssn', 'social', 'crypto', 'wallet', 'key']
        medium_risk_keywords = ['confidential', 'secret', 'personal', 'private', 'salary']
        
        filename_lower = filename.lower()
        content_lower = content.lower()
        
        if any(keyword in filename_lower or keyword in content_lower for keyword in high_risk_keywords):
            return 'HIGH'
        elif any(keyword in filename_lower or keyword in content_lower for keyword in medium_risk_keywords):
            return 'MEDIUM'
        else:
            return 'LOW'
    
    def simulate_c2_communication(self):
        """Simulate command and control server communication"""
        print("📡 Establishing C&C communication...")
        
        c2_servers = [
            {'host': '192.168.1.100', 'port': 4444, 'type': 'Primary C&C'},
            {'host': '10.0.0.50', 'port': 8080, 'type': 'Backup C&C'},
            {'host': 'evil-domain.com', 'port': 443, 'type': 'HTTPS C&C'}
        ]
        
        communications = []
        
        for server in c2_servers:
            print(f"   🔗 Connecting to {server['type']}: {server['host']}:{server['port']}")
            
            # Simulate connection attempt
            time.sleep(1)
            
            # Simulate data exchange
            message = {
                'victim_id': 'VM_' + str(random.randint(10000, 99999)),
                'os': 'Linux Ubuntu 24.04',
                'hostname': 'victim-machine',
                'ip': '192.168.1.75',
                'data_stolen': len(self.stolen_data),
                'keylog_entries': len(self.keylog_data),
                'timestamp': datetime.now().isoformat()
            }
            
            communications.append({
                'server': server,
                'message': message,
                'status': 'SUCCESS',
                'response': 'COMMANDS_RECEIVED'
            })
            
            print(f"   ✅ Data sent to {server['host']}")
            print(f"   📥 Received commands from server")
            time.sleep(1)
        
        return communications
    
    def simulate_remote_shell(self):
        """Simulate remote shell access"""
        print("💻 Simulating remote shell access...")
        
        fake_commands = [
            "whoami",
            "pwd", 
            "ls -la /home",
            "cat /etc/passwd",
            "ps aux | grep -v grep",
            "netstat -an",
            "crontab -l",
            "history",
            "find / -name '*.txt' 2>/dev/null | head -10",
            "cat /proc/version"
        ]
        
        shell_log = []
        
        for command in fake_commands:
            if not self.is_running:
                break
                
            print(f"   🖥️ Executing: {command}")
            
            # Simulate command output
            fake_output = self.generate_fake_output(command)
            
            shell_log.append({
                'timestamp': datetime.now().isoformat(),
                'command': command,
                'output': fake_output
            })
            
            time.sleep(random.uniform(0.5, 2))
        
        # Save shell log
        shell_log_file = os.path.join(self.test_dir, "remote_shell.log")
        with open(shell_log_file, 'w') as f:
            json.dump(shell_log, f, indent=2)
        
        return len(shell_log)
    
    def generate_fake_output(self, command):
        """Generate realistic fake command output"""
        outputs = {
            "whoami": "victim-user",
            "pwd": "/home/victim-user",
            "ls -la /home": "drwxr-xr-x 3 root root 4096 Sep 4 user1\ndrwxr-xr-x 3 root root 4096 Sep 4 victim-user",
            "ps aux | grep -v grep": "root 1 0.0 0.1 systemd\nvictim-user 1234 5.2 2.1 firefox\nvictim-user 5678 0.1 0.5 keylogger",
            "netstat -an": "tcp 0.0.0.0:22 LISTEN\ntcp 192.168.1.75:4444 ESTABLISHED",
        }
        return outputs.get(command, f"Command '{command}' executed successfully")
    
    def run_simulation(self, duration=300):
        """Main trojan simulation execution"""
        self.is_running = True
        start_time = datetime.now()
        results = {
            'type': 'trojan',
            'start_time': start_time.isoformat(),
            'events': [],
            'files_affected': 0,
            'network_connections': 0,
            'data_stolen': 0,
            'keylog_entries': 0,
            'threat_level': 'HIGH'
        }
        
        try:
            print("🐴 STARTING TROJAN/BACKDOOR SIMULATION")
            print("=" * 50)
            
            # Phase 1: Environment Setup
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'initialization',
                'action': 'Setting up test environment',
                'details': 'Creating fake sensitive files'
            })
            self.setup_test_environment()
            
            # Phase 2: Backdoor Installation
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'installation',
                'action': 'Installing backdoor',
                'details': 'Creating persistent access mechanism'
            })
            backdoor_files = self.simulate_backdoor_installation()
            results['files_affected'] += backdoor_files
            
            if not self.is_running:
                return results
            
            # Phase 3: Data Theft
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'data_theft',
                'action': 'Stealing sensitive data',
                'details': 'Searching and exfiltrating user files'
            })
            stolen_count = self.simulate_data_theft()
            results['data_stolen'] = stolen_count
            
            # Phase 4: Keylogger
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'keylogging',
                'action': 'Starting keylogger',
                'details': 'Capturing user keystrokes'
            })
            keylog_count = self.simulate_keylogger()
            results['keylog_entries'] = keylog_count
            
            if not self.is_running:
                return results
            
            # Phase 5: C&C Communication
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'communication',
                'action': 'Contacting C&C servers',
                'details': 'Sending stolen data and receiving commands'
            })
            communications = self.simulate_c2_communication()
            results['network_connections'] = len(communications)
            
            # Phase 6: Remote Shell
            results['events'].append({
                'time': datetime.now().isoformat(),
                'phase': 'remote_access',
                'action': 'Providing remote shell access',
                'details': 'Executing commands from attacker'
            })
            shell_commands = self.simulate_remote_shell()
            
            # Final Results
            results['end_time'] = datetime.now().isoformat()
            results['duration'] = (datetime.now() - start_time).total_seconds()
            
            print("\n🎯 TROJAN SIMULATION COMPLETED")
            print(f"📊 Files affected: {results['files_affected']}")
            print(f"💾 Data items stolen: {results['data_stolen']}")
            print(f"⌨️ Keylog entries: {results['keylog_entries']}")
            print(f"🌐 Network connections: {results['network_connections']}")
            print(f"📂 Test directory: {self.test_dir}")
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
                import shutil
                shutil.rmtree(self.test_dir)
                print(f"🧹 Cleaned up test directory: {self.test_dir}")
        except Exception as e:
            print(f"❌ Cleanup failed: {e}")

if __name__ == "__main__":
    # Standalone test
    simulator = TrojanSimulator()
    print("🔬 Testing Trojan Simulator")
    results = simulator.run_simulation(60)
    print(f"\n📋 Results: {json.dumps(results, indent=2)}")
    
    input("\nPress Enter to cleanup...")
    simulator.cleanup()
