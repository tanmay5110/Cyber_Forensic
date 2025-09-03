# Fix the database module with proper indentation
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
        cursor.execute("""
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
        """)
        
        # Process events table
        cursor.execute("""
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
        """)
        
        conn.commit()
        conn.close()
        print("🗄️  Database initialized successfully")
    
    def save_analysis_session(self, session_data: Dict[str, Any]) -> str:
        """Save a new analysis session"""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{session_data['type']}"
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO sessions (session_id, malware_type, start_time, duration, config_json)
            VALUES (?, ?, ?, ?, ?)
        """, (
            session_id,
            session_data['type'],
            session_data['timestamp'],
            session_data.get('duration', 0),
            json.dumps(session_data)
        ))
        
        conn.commit()
        conn.close()
        
        return session_id
    
    def get_sessions(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get recent analysis sessions"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM sessions 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (limit,))
        
        sessions = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return sessions
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Count sessions by type
        cursor.execute("""
            SELECT malware_type, COUNT(*) as count 
            FROM sessions 
            GROUP BY malware_type
        """)
        stats['sessions_by_type'] = dict(cursor.fetchall())
        
        # Recent activity
        cursor.execute("""
            SELECT COUNT(*) FROM sessions 
            WHERE created_at > datetime('now', '-24 hours')
        """)
        stats['sessions_last_24h'] = cursor.fetchone()[0]
        
        conn.close()
        return stats
'''

with open('MalSimPro/database/analysis_db.py', 'w') as f:
    f.write(database_content)

print("✅ Created analysis_db.py - Database module fixed")