#!/usr/bin/env python3
"""
MalSim Pro Web Interface
Simple Flask-based dashboard for malware simulation
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for, render_template_string
import json
import os
import sys
import time
import threading
from datetime import datetime
import sqlite3

class SimpleDB:
    def __init__(self):
        self.db_path = "malsim_analysis.db"
        self.init_db()
    
    def init_db(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS simulations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                status TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT,
                duration INTEGER,
                results TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_simulation(self, sim_type, status="running"):
        """Add new simulation record"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO simulations (type, status, start_time) VALUES (?, ?, ?)",
            (sim_type, status, datetime.now().isoformat())
        )
        
        sim_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return sim_id
    
    def update_simulation(self, sim_id, status, results=None):
        """Update simulation record"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if results:
            cursor.execute(
                "UPDATE simulations SET status=?, end_time=?, results=? WHERE id=?",
                (status, datetime.now().isoformat(), json.dumps(results), sim_id)
            )
        else:
            cursor.execute(
                "UPDATE simulations SET status=?, end_time=? WHERE id=?",
                (status, datetime.now().isoformat(), sim_id)
            )
        
        conn.commit()
        conn.close()
    
    def get_simulations(self, limit=50):
        """Get simulation records"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM simulations ORDER BY start_time DESC LIMIT ?",
            (limit,)
        )
        
        results = cursor.fetchall()
        conn.close()
        
        # Convert to dict format
        simulations = []
        for row in results:
            simulations.append({
                'id': row[0],
                'type': row[1],
                'status': row[2],
                'start_time': row[3],
                'end_time': row[4],
                'duration': row[5],
                'results': json.loads(row[6]) if row[6] else {}
            })
        
        return simulations

class MalwareSimulator:
    """Simple malware behavior simulator"""
    
    def __init__(self, sim_type):
        self.sim_type = sim_type
        self.is_running = False
        
    def run_simulation(self, duration=300):
        """Run malware simulation safely"""
        self.is_running = True
        
        print(f"🔬 Starting {self.sim_type} simulation...")
        
        # Use the dedicated simulator classes
        if self.sim_type == 'ransomware':
            from ransomware_sim import RansomwareSimulator
            simulator = RansomwareSimulator()
            return simulator.run_simulation(duration)
        elif self.sim_type == 'trojan':
            from trojan_sim import TrojanSimulator
            simulator = TrojanSimulator()
            return simulator.run_simulation(duration)
        elif self.sim_type == 'worm':
            from worm_sim import WormSimulator
            simulator = WormSimulator()
            return simulator.run_simulation(duration)
        elif self.sim_type == 'spyware':
            results = self._simulate_spyware(duration)
        else:
            # Fallback to basic simulation
            results = {
                'type': self.sim_type,
                'start_time': datetime.now().isoformat(),
                'events': [],
                'files_affected': 0,
                'processes_spawned': 0,
                'network_connections': 0,
                'threat_level': 'LOW'
            }
        
        results['end_time'] = datetime.now().isoformat()
        results['duration'] = duration
        self.is_running = False
        
        return results
    
    def _simulate_ransomware(self, duration):
        """Simulate ransomware behavior"""
        events = []
        
        # Create test directory
        test_dir = "/tmp/malsim_test"
        os.makedirs(test_dir, exist_ok=True)
        
        # Simulate file operations
        for i in range(min(10, duration//30)):
            time.sleep(1)
            filename = f"test_file_{i}.txt"
            filepath = os.path.join(test_dir, filename)
            
            # Create fake file
            with open(filepath, 'w') as f:
                f.write(f"Test data for simulation {i}")
            
            events.append({
                'time': datetime.now().isoformat(),
                'type': 'file_encrypt',
                'target': filepath,
                'description': f'Encrypted file: {filename}'
            })
            
            if not self.is_running:
                break
        
        # Cleanup
        import shutil
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        
        return {
            'type': 'ransomware',
            'events': events,
            'files_affected': len(events),
            'processes_spawned': 2,
            'network_connections': 1,
            'threat_level': 'HIGH'
        }
    
    def _simulate_trojan(self, duration):
        """Simulate trojan behavior"""
        events = []
        
        for i in range(min(5, duration//60)):
            time.sleep(1)
            events.append({
                'time': datetime.now().isoformat(),
                'type': 'backdoor_connection',
                'target': f'192.168.1.{100+i}',
                'description': f'Attempted backdoor connection to remote server'
            })
            
            if not self.is_running:
                break
        
        return {
            'type': 'trojan',
            'events': events,
            'files_affected': 3,
            'processes_spawned': 4,
            'network_connections': len(events),
            'threat_level': 'MEDIUM'
        }
    
    def _simulate_worm(self, duration):
        """Simulate worm behavior"""
        events = []
        
        for i in range(min(8, duration//40)):
            time.sleep(1)
            events.append({
                'time': datetime.now().isoformat(),
                'type': 'network_scan',
                'target': f'192.168.1.{i+1}',
                'description': f'Scanning network host for vulnerabilities'
            })
            
            if not self.is_running:
                break
        
        return {
            'type': 'worm',
            'events': events,
            'files_affected': 1,
            'processes_spawned': 3,
            'network_connections': len(events),
            'threat_level': 'HIGH'
        }
    
    def _simulate_spyware(self, duration):
        """Simulate spyware behavior"""
        events = []
        
        for i in range(min(15, duration//20)):
            time.sleep(1)
            events.append({
                'time': datetime.now().isoformat(),
                'type': 'data_collection',
                'target': f'keystrokes_{i}',
                'description': f'Captured user input data'
            })
            
            if not self.is_running:
                break
        
        return {
            'type': 'spyware',
            'events': events,
            'files_affected': 0,
            'processes_spawned': 1,
            'network_connections': 3,
            'threat_level': 'MEDIUM'
        }

# Global variables for simulation state
db = SimpleDB()
current_simulations = {}

def create_app():
    """Create Flask application"""
    app = Flask(__name__)
    app.secret_key = 'malsim_pro_demo_key'
    
    @app.route('/')
    def dashboard():
        """Main dashboard"""
        simulations = db.get_simulations(10)
        return render_template_string(DASHBOARD_HTML, simulations=simulations)
    
    @app.route('/api/start_simulation', methods=['POST'])
    def start_simulation():
        """Start a new simulation"""
        data = request.get_json()
        sim_type = data.get('type', 'ransomware')
        duration = data.get('duration', 30)  # Short duration for demo
        
        # Create simulation record
        sim_id = db.add_simulation(sim_type, "running")
        
        # Start simulation in background thread
        simulator = MalwareSimulator(sim_type)
        current_simulations[sim_id] = simulator
        
        def run_sim():
            try:
                results = simulator.run_simulation(duration)
                db.update_simulation(sim_id, "completed", results)
            except Exception as e:
                db.update_simulation(sim_id, "failed", {"error": str(e)})
            finally:
                if sim_id in current_simulations:
                    del current_simulations[sim_id]
        
        thread = threading.Thread(target=run_sim)
        thread.daemon = True
        thread.start()
        
        return jsonify({'success': True, 'simulation_id': sim_id})
    
    @app.route('/api/simulations')
    def get_simulations():
        """Get simulation list"""
        simulations = db.get_simulations()
        return jsonify(simulations)
    
    @app.route('/api/stop_simulation', methods=['POST'])
    def stop_simulation():
        """Stop running simulation"""
        data = request.get_json()
        sim_id = data.get('simulation_id')
        
        if sim_id and sim_id in current_simulations:
            current_simulations[sim_id].is_running = False
            db.update_simulation(sim_id, "stopped")
            return jsonify({'success': True})
        
        return jsonify({'success': False, 'error': 'Simulation not found'})
    
    return app

# Simple HTML template
DASHBOARD_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>MalSim Pro - Educational Malware Simulation Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .simulation-panel { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .button { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin: 5px; }
        .button:hover { background: #2980b9; }
        .button.danger { background: #e74c3c; }
        .button.danger:hover { background: #c0392b; }
        .status { padding: 5px 10px; border-radius: 3px; color: white; }
        .status.running { background: #f39c12; }
        .status.completed { background: #27ae60; }
        .status.failed { background: #e74c3c; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #34495e; color: white; }
        .warning { background: #fff3cd; border: 1px solid #ffeaa7; color: #856404; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔬 MalSim Pro - Educational Malware Simulation Platform</h1>
        <p>Safe, controlled malware behavior simulation for cybersecurity education</p>
    </div>
    
    <div class="warning">
        <strong>⚠️ EDUCATIONAL USE ONLY:</strong> This platform simulates malware behavior for learning purposes. 
        All simulations are safe and contained. Only use in virtual machines or isolated environments.
    </div>
    
    <div class="simulation-panel">
        <h2>🚀 Start New Simulation</h2>
        <p>Choose a malware type to simulate and observe its behavior patterns:</p>
        
        <button class="button" onclick="startSimulation('ransomware')">
            🔒 Ransomware Simulation
        </button>
        <button class="button" onclick="startSimulation('trojan')">
            🐴 Trojan Simulation
        </button>
        <button class="button" onclick="startSimulation('worm')">
            🪱 Worm Simulation
        </button>
        <button class="button" onclick="startSimulation('spyware')">
            👁️ Spyware Simulation
        </button>
        
        <div id="status" style="margin-top: 20px;"></div>
    </div>
    
    <div class="simulation-panel">
        <h2>📊 Recent Simulations</h2>
        <button class="button" onclick="refreshData()">🔄 Refresh</button>
        
        <table id="simulationsTable">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Status</th>
                    <th>Start Time</th>
                    <th>Duration</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for sim in simulations %}
                <tr>
                    <td>{{ sim.id }}</td>
                    <td>{{ sim.type }}</td>
                    <td><span class="status {{ sim.status }}">{{ sim.status }}</span></td>
                    <td>{{ sim.start_time[:19] if sim.start_time else '' }}</td>
                    <td>{{ sim.duration }}s</td>
                    <td>
                        {% if sim.status == 'running' %}
                        <button class="button danger" onclick="stopSimulation({{ sim.id }})">Stop</button>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <script>
        function startSimulation(type) {
            document.getElementById('status').innerHTML = `<p>🔬 Starting ${type} simulation...</p>`;
            
            fetch('/api/start_simulation', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({type: type, duration: 30})
            })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    document.getElementById('status').innerHTML = 
                        `<p>✅ ${type} simulation started! ID: ${data.simulation_id}</p>`;
                    setTimeout(refreshData, 2000);
                } else {
                    document.getElementById('status').innerHTML = 
                        `<p>❌ Failed to start simulation</p>`;
                }
            });
        }
        
        function stopSimulation(simId) {
            fetch('/api/stop_simulation', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({simulation_id: simId})
            })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    refreshData();
                }
            });
        }
        
        function refreshData() {
            location.reload();
        }
        
        // Auto-refresh every 10 seconds
        setInterval(refreshData, 10000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app = create_app()
    print("🌐 Starting MalSim Pro Dashboard...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⚠️  Educational use only - Safe malware simulation platform")
    app.run(host='127.0.0.1', port=5000, debug=True)
