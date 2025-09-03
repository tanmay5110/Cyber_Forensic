# Create the database module
database_content = '''"""
Database module for MalSim Pro
Handles storage and retrieval of analysis sessions and results
"""

import sqlite3
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

class AnalysisDB:
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), 'malsim.db')
        
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Analysis sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                malware_type TEXT NOT NULL,
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP,
                duration INTEGER,
                status TEXT DEFAULT 'running',
                config_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Process events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS process_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                event_type TEXT NOT NULL,
                process_name TEXT,
                process_id INTEGER,
                parent_id INTEGER,
                command_line TEXT,
                details_json TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (session_id)
            )
        ''')
        
        # File events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                event_type TEXT NOT NULL,
                file_path TEXT NOT NULL,
                file_size INTEGER,
                file_hash TEXT,
                operation TEXT,
                details_json TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (session_id)
            )
        ''')
        
        # Network events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS network_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                event_type TEXT NOT NULL,
                protocol TEXT,
                src_ip TEXT,
                src_port INTEGER,
                dst_ip TEXT,
                dst_port INTEGER,
                data_size INTEGER,
                details_json TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (session_id)
            )
        ''')
        
        # System events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                event_type TEXT NOT NULL,
                category TEXT,
                description TEXT,
                severity TEXT DEFAULT 'info',
                details_json TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (session_id)
            )
        ''')
        
        # Indicators of Compromise (IOCs) table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS iocs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                ioc_type TEXT NOT NULL,
                ioc_value TEXT NOT NULL,
                description TEXT,
                confidence_score FLOAT DEFAULT 0.5,
                first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES sessions (session_id)
            )
        ''')
        
        conn.commit()
        conn.close()
        print("🗄️  Database initialized successfully")
    
    def save_analysis_session(self, session_data: Dict[str, Any]) -> str:
        """Save a new analysis session"""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{session_data['type']}"
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sessions (session_id, malware_type, start_time, duration, config_json)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            session_id,
            session_data['type'],
            session_data['timestamp'],
            session_data.get('duration', 0),
            json.dumps(session_data)
        ))
        
        conn.commit()
        conn.close()
        
        return session_id
    
    def save_process_event(self, session_id: str, event: Dict[str, Any]):
        """Save process monitoring event"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO process_events 
            (session_id, timestamp, event_type, process_name, process_id, parent_id, command_line, details_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            session_id,
            event.get('timestamp', datetime.now().isoformat()),
            event.get('event_type', 'unknown'),
            event.get('process_name', ''),
            event.get('process_id', 0),
            event.get('parent_id', 0),
            event.get('command_line', ''),
            json.dumps(event)
        ))
        
        conn.commit()
        conn.close()
    
    def save_file_event(self, session_id: str, event: Dict[str, Any]):
        """Save file system monitoring event"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO file_events 
            (session_id, timestamp, event_type, file_path, operation, details_json)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            session_id,
            event.get('timestamp', datetime.now().isoformat()),
            event.get('event_type', 'unknown'),
            event.get('file_path', ''),
            event.get('operation', ''),
            json.dumps(event)
        ))
        
        conn.commit()
        conn.close()
    
    def save_network_event(self, session_id: str, event: Dict[str, Any]):
        """Save network monitoring event"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO network_events 
            (session_id, timestamp, event_type, protocol, src_ip, src_port, dst_ip, dst_port, details_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            session_id,
            event.get('timestamp', datetime.now().isoformat()),
            event.get('event_type', 'unknown'),
            event.get('protocol', ''),
            event.get('src_ip', ''),
            event.get('src_port', 0),
            event.get('dst_ip', ''),
            event.get('dst_port', 0),
            json.dumps(event)
        ))
        
        conn.commit()
        conn.close()
    
    def get_sessions(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get recent analysis sessions"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM sessions 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (limit,))
        
        sessions = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return sessions
    
    def get_session_events(self, session_id: str) -> Dict[str, List[Dict[str, Any]]]:
        """Get all events for a specific session"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        events = {
            'processes': [],
            'files': [],
            'network': [],
            'system': []
        }
        
        # Get process events
        cursor.execute('SELECT * FROM process_events WHERE session_id = ? ORDER BY timestamp', (session_id,))
        events['processes'] = [dict(row) for row in cursor.fetchall()]
        
        # Get file events
        cursor.execute('SELECT * FROM file_events WHERE session_id = ? ORDER BY timestamp', (session_id,))
        events['files'] = [dict(row) for row in cursor.fetchall()]
        
        # Get network events
        cursor.execute('SELECT * FROM network_events WHERE session_id = ? ORDER BY timestamp', (session_id,))
        events['network'] = [dict(row) for row in cursor.fetchall()]
        
        # Get system events
        cursor.execute('SELECT * FROM system_events WHERE session_id = ? ORDER BY timestamp', (session_id,))
        events['system'] = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return events
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Count sessions by type
        cursor.execute('''
            SELECT malware_type, COUNT(*) as count 
            FROM sessions 
            GROUP BY malware_type
        ''')
        stats['sessions_by_type'] = dict(cursor.fetchall())
        
        # Total events
        cursor.execute('SELECT COUNT(*) FROM process_events')
        stats['total_process_events'] = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM file_events')
        stats['total_file_events'] = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM network_events')
        stats['total_network_events'] = cursor.fetchone()[0]
        
        # Recent activity
        cursor.execute('''
            SELECT COUNT(*) FROM sessions 
            WHERE created_at > datetime('now', '-24 hours')
        ''')
        stats['sessions_last_24h'] = cursor.fetchone()[0]
        
        conn.close()
        return stats
    
    def cleanup_old_sessions(self, days: int = 30):
        """Clean up sessions older than specified days"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_date = datetime.now() - timedelta(days=days)
        
        cursor.execute('DELETE FROM sessions WHERE created_at < ?', (cutoff_date,))
        deleted = cursor.rowcount
        
        conn.commit()
        conn.close()
        
        return deleted
'''

with open('MalSimPro/database/analysis_db.py', 'w') as f:
    f.write(database_content)

print("✅ Created analysis_db.py - Complete database module with SQLite")