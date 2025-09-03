# Create the system monitor
system_monitor_content = '''"""
System Monitor for MalSim Pro
Monitors system activities during malware simulations
"""

import psutil
import time
import threading
from datetime import datetime
from typing import Dict, List, Any
import os

class SystemMonitor:
    def __init__(self):
        self.monitoring = False
        self.events = []
        self.monitor_thread = None
        self.start_time = None
        
    def start_monitoring(self):
        """Start system monitoring"""
        self.monitoring = True
        self.events = []
        self.start_time = datetime.now()
        
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print("🔍 System monitoring started")
    
    def stop_monitoring(self) -> List[Dict[str, Any]]:
        """Stop monitoring and return collected events"""
        self.monitoring = False
        
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        
        print(f"🛑 System monitoring stopped - Collected {len(self.events)} events")
        return self.events.copy()
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        last_processes = set()
        
        while self.monitoring:
            try:
                # Monitor processes
                current_processes = set()
                for proc in psutil.process_iter(['pid', 'name', 'ppid', 'cmdline', 'create_time']):
                    try:
                        proc_info = proc.info
                        current_processes.add(proc_info['pid'])
                        
                        # New process detected
                        if proc_info['pid'] not in last_processes:
                            self._log_event({
                                'type': 'process_created',
                                'timestamp': datetime.now().isoformat(),
                                'pid': proc_info['pid'],
                                'name': proc_info['name'],
                                'ppid': proc_info['ppid'],
                                'cmdline': ' '.join(proc_info['cmdline'] or []),
                                'create_time': proc_info['create_time']
                            })
                    
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        continue
                
                # Monitor system resources
                self._monitor_resources()
                
                last_processes = current_processes
                time.sleep(2)  # Monitor every 2 seconds
                
            except Exception as e:
                self._log_event({
                    'type': 'monitor_error',
                    'timestamp': datetime.now().isoformat(),
                    'error': str(e)
                })
                time.sleep(5)
    
    def _monitor_resources(self):
        """Monitor system resource usage"""
        try:
            cpu_percent = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Log high resource usage
            if cpu_percent > 80:
                self._log_event({
                    'type': 'high_cpu_usage',
                    'timestamp': datetime.now().isoformat(),
                    'cpu_percent': cpu_percent
                })
            
            if memory.percent > 80:
                self._log_event({
                    'type': 'high_memory_usage',
                    'timestamp': datetime.now().isoformat(),
                    'memory_percent': memory.percent,
                    'memory_available': memory.available
                })
                
        except Exception as e:
            pass  # Ignore resource monitoring errors
    
    def _log_event(self, event: Dict[str, Any]):
        """Log a monitoring event"""
        self.events.append(event)
        
        # Keep only last 1000 events to prevent memory issues
        if len(self.events) > 1000:
            self.events = self.events[-1000:]
'''

with open('MalSimPro/monitoring/system_monitor.py', 'w') as f:
    f.write(system_monitor_content)

print("✅ Created system_monitor.py - System monitoring with process tracking")

# Create file monitor
file_monitor_content = '''"""
File Monitor for MalSim Pro
Monitors file system changes during simulations
"""

import os
import time
import threading
from datetime import datetime
from typing import Dict, List, Any
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
    
    def on_created(self, event):
        self.callback({
            'type': 'file_created',
            'timestamp': datetime.now().isoformat(),
            'path': event.src_path,
            'is_directory': event.is_directory
        })
    
    def on_deleted(self, event):
        self.callback({
            'type': 'file_deleted',
            'timestamp': datetime.now().isoformat(),
            'path': event.src_path,
            'is_directory': event.is_directory
        })
    
    def on_modified(self, event):
        if not event.is_directory:
            self.callback({
                'type': 'file_modified',
                'timestamp': datetime.now().isoformat(),
                'path': event.src_path,
                'is_directory': event.is_directory
            })

class FileMonitor:
    def __init__(self, watch_paths=None):
        self.watch_paths = watch_paths or ['./test_files']
        self.events = []
        self.observer = Observer()
        self.monitoring = False
    
    def start_monitoring(self):
        """Start file system monitoring"""
        self.monitoring = True
        self.events = []
        
        handler = FileChangeHandler(self._log_event)
        
        for path in self.watch_paths:
            if os.path.exists(path):
                self.observer.schedule(handler, path, recursive=True)
        
        self.observer.start()
        print(f"📁 File monitoring started for {len(self.watch_paths)} paths")
    
    def stop_monitoring(self) -> List[Dict[str, Any]]:
        """Stop file monitoring and return events"""
        self.monitoring = False
        self.observer.stop()
        self.observer.join()
        
        print(f"📁 File monitoring stopped - {len(self.events)} file events")
        return self.events.copy()
    
    def _log_event(self, event: Dict[str, Any]):
        """Log a file system event"""
        self.events.append(event)
'''

with open('MalSimPro/monitoring/file_monitor.py', 'w') as f:
    f.write(file_monitor_content)

print("✅ Created file_monitor.py - File system change monitoring")

# Create network monitor
network_monitor_content = '''"""
Network Monitor for MalSim Pro
Monitors network connections during simulations
"""

import psutil
import socket
import time
import threading
from datetime import datetime
from typing import Dict, List, Any

class NetworkMonitor:
    def __init__(self):
        self.monitoring = False
        self.events = []
        self.monitor_thread = None
        self.last_connections = set()
    
    def start_monitoring(self):
        """Start network monitoring"""
        self.monitoring = True
        self.events = []
        self.last_connections = set()
        
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print("🌐 Network monitoring started")
    
    def stop_monitoring(self) -> List[Dict[str, Any]]:
        """Stop monitoring and return events"""
        self.monitoring = False
        
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        
        print(f"🌐 Network monitoring stopped - {len(self.events)} network events")
        return self.events.copy()
    
    def _monitor_loop(self):
        """Monitor network connections"""
        while self.monitoring:
            try:
                current_connections = set()
                
                for conn in psutil.net_connections():
                    if conn.status == 'ESTABLISHED':
                        conn_key = (conn.laddr.ip if conn.laddr else '',
                                  conn.laddr.port if conn.laddr else 0,
                                  conn.raddr.ip if conn.raddr else '',
                                  conn.raddr.port if conn.raddr else 0)
                        
                        current_connections.add(conn_key)
                        
                        # New connection detected
                        if conn_key not in self.last_connections:
                            self._log_event({
                                'type': 'connection_established',
                                'timestamp': datetime.now().isoformat(),
                                'local_ip': conn.laddr.ip if conn.laddr else '',
                                'local_port': conn.laddr.port if conn.laddr else 0,
                                'remote_ip': conn.raddr.ip if conn.raddr else '',
                                'remote_port': conn.raddr.port if conn.raddr else 0,
                                'pid': conn.pid
                            })
                
                # Check for closed connections
                for conn_key in self.last_connections - current_connections:
                    self._log_event({
                        'type': 'connection_closed',
                        'timestamp': datetime.now().isoformat(),
                        'connection': conn_key
                    })
                
                self.last_connections = current_connections
                time.sleep(3)  # Check every 3 seconds
                
            except Exception as e:
                time.sleep(5)
    
    def _log_event(self, event: Dict[str, Any]):
        """Log a network event"""
        self.events.append(event)
        
        # Keep only last 500 network events
        if len(self.events) > 500:
            self.events = self.events[-500:]
'''

with open('MalSimPro/monitoring/network_monitor.py', 'w') as f:
    f.write(network_monitor_content)

print("✅ Created network_monitor.py - Network connection monitoring")

# Create process monitor
process_monitor_content = '''"""
Process Monitor for MalSim Pro
Detailed process monitoring and analysis
"""

import psutil
import time
import threading
from datetime import datetime
from typing import Dict, List, Any

class ProcessMonitor:
    def __init__(self):
        self.monitoring = False
        self.events = []
        self.monitor_thread = None
        self.process_tree = {}
    
    def start_monitoring(self):
        """Start process monitoring"""
        self.monitoring = True
        self.events = []
        
        self.monitor_thread = threading.Thread(target=self._monitor_processes)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print("⚙️  Process monitoring started")
    
    def stop_monitoring(self) -> List[Dict[str, Any]]:
        """Stop monitoring and return events"""
        self.monitoring = False
        
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        
        print(f"⚙️  Process monitoring stopped - {len(self.events)} process events")
        return self.events.copy()
    
    def _monitor_processes(self):
        """Monitor process creation and behavior"""
        known_processes = set()
        
        while self.monitoring:
            try:
                current_processes = set()
                
                for proc in psutil.process_iter(['pid', 'name', 'ppid', 'cmdline', 
                                               'create_time', 'cpu_percent', 'memory_percent']):
                    try:
                        proc_info = proc.info
                        pid = proc_info['pid']
                        current_processes.add(pid)
                        
                        # New process
                        if pid not in known_processes:
                            self._log_event({
                                'type': 'process_start',
                                'timestamp': datetime.now().isoformat(),
                                'pid': pid,
                                'name': proc_info['name'],
                                'ppid': proc_info['ppid'],
                                'cmdline': ' '.join(proc_info['cmdline'] or []),
                                'create_time': proc_info['create_time']
                            })
                        
                        # Monitor suspicious behavior
                        self._check_suspicious_behavior(proc, proc_info)
                        
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                
                # Detect terminated processes
                for pid in known_processes - current_processes:
                    self._log_event({
                        'type': 'process_exit',
                        'timestamp': datetime.now().isoformat(),
                        'pid': pid
                    })
                
                known_processes = current_processes
                time.sleep(2)
                
            except Exception as e:
                time.sleep(5)
    
    def _check_suspicious_behavior(self, proc, proc_info):
        """Check for suspicious process behavior"""
        try:
            # High CPU usage
            if proc_info['cpu_percent'] > 90:
                self._log_event({
                    'type': 'high_cpu_process',
                    'timestamp': datetime.now().isoformat(),
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'cpu_percent': proc_info['cpu_percent']
                })
            
            # Suspicious process names
            suspicious_names = ['cmd.exe', 'powershell.exe', 'rundll32.exe', 'regsvr32.exe']
            if proc_info['name'] in suspicious_names:
                self._log_event({
                    'type': 'suspicious_process',
                    'timestamp': datetime.now().isoformat(),
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'cmdline': ' '.join(proc_info['cmdline'] or [])
                })
                
        except Exception:
            pass
    
    def _log_event(self, event: Dict[str, Any]):
        """Log a process event"""
        self.events.append(event)
        
        # Keep only last 1000 events
        if len(self.events) > 1000:
            self.events = self.events[-1000:]
'''

with open('MalSimPro/monitoring/process_monitor.py', 'w') as f:
    f.write(process_monitor_content)

print("✅ Created process_monitor.py - Detailed process behavior monitoring")