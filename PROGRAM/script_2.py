# Create the configuration file
config_content = '''{
    "app_name": "MalSim Pro",
    "version": "1.0.0",
    "description": "Educational Malware Simulation and Analysis Platform",
    
    "security": {
        "vm_required": true,
        "max_simulation_time": 3600,
        "safe_directories": [
            "./test_files",
            "./logs", 
            "./reports"
        ],
        "blocked_directories": [
            "/home",
            "/Users",
            "C:\\\\Users",
            "/root"
        ]
    },
    
    "simulation_settings": {
        "ransomware": {
            "encrypt_extensions": [".txt", ".doc", ".pdf", ".jpg"],
            "ransom_note": "🔒 Your files have been encrypted! (SIMULATION ONLY)",
            "fake_encryption": true,
            "test_files_count": 10
        },
        "trojan": {
            "fake_backdoor_port": 8888,
            "keylog_simulation": true,
            "screen_capture_interval": 30,
            "data_exfil_simulation": true
        },
        "worm": {
            "scan_range": "127.0.0.1",
            "propagation_ports": [22, 80, 443, 445],
            "fake_exploit_attempts": 5
        },
        "spyware": {
            "keylog_duration": 60,
            "screenshot_interval": 10,
            "browser_data_simulation": true,
            "credential_harvest_simulation": true
        }
    },
    
    "monitoring": {
        "process_monitoring": true,
        "file_monitoring": true,
        "network_monitoring": true,
        "registry_monitoring": true,
        "memory_monitoring": true,
        "log_level": "INFO"
    },
    
    "dashboard": {
        "theme": "dark",
        "refresh_interval": 5,
        "max_sessions_display": 50,
        "chart_types": ["timeline", "heatmap", "network_graph"]
    },
    
    "database": {
        "type": "sqlite",
        "path": "./database/malsim.db",
        "backup_enabled": true,
        "retention_days": 30
    },
    
    "reporting": {
        "formats": ["html", "pdf", "json"],
        "include_screenshots": true,
        "include_network_analysis": true,
        "template_dir": "./templates"
    }
}'''

with open('MalSimPro/config/settings.json', 'w') as f:
    f.write(config_content)

print("✅ Created settings.json - Complete configuration file")

# Create requirements.txt for dependencies
requirements_content = '''flask==2.3.2
matplotlib==3.7.1
plotly==5.15.0
psutil==5.9.5
requests==2.31.0
sqlite3
watchdog==3.0.0
Pillow==10.0.0
reportlab==4.0.4
jinja2==3.1.2
pandas==2.0.3
numpy==1.24.3
'''

with open('MalSimPro/requirements.txt', 'w') as f:
    f.write(requirements_content)

print("✅ Created requirements.txt - Python dependencies")