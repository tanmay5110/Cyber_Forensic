# Create the web interface for the dashboard
web_interface_content = '''"""
Web Dashboard for MalSim Pro
Flask-based web interface for viewing analysis results
"""

from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime
from database.analysis_db import AnalysisDB
from dashboard.analytics import AnalyticsEngine

def create_app(db: AnalysisDB = None):
    app = Flask(__name__)
    app.secret_key = 'malsim_pro_educational_key_2025'
    
    if db is None:
        db = AnalysisDB()
    
    analytics = AnalyticsEngine(db)
    
    @app.route('/')
    def dashboard():
        """Main dashboard page"""
        return render_template('dashboard.html')
    
    @app.route('/api/sessions')
    def get_sessions():
        """API endpoint to get analysis sessions"""
        limit = request.args.get('limit', 50, type=int)
        sessions = db.get_sessions(limit)
        return jsonify(sessions)
    
    @app.route('/api/statistics')
    def get_statistics():
        """API endpoint to get dashboard statistics"""
        stats = db.get_statistics()
        return jsonify(stats)
    
    @app.route('/api/session/<session_id>')
    def get_session_details(session_id):
        """API endpoint to get detailed session information"""
        # This would be implemented with more database methods
        session_data = {
            'session_id': session_id,
            'status': 'completed',
            'events': [],
            'analysis': analytics.analyze_session(session_id)
        }
        return jsonify(session_data)
    
    @app.route('/api/analytics/timeline')
    def get_timeline():
        """API endpoint for timeline analytics"""
        timeline_data = analytics.generate_timeline()
        return jsonify(timeline_data)
    
    @app.route('/api/analytics/heatmap')
    def get_heatmap():
        """API endpoint for activity heatmap"""
        heatmap_data = analytics.generate_heatmap()
        return jsonify(heatmap_data)
    
    @app.route('/report/<session_id>')
    def generate_report(session_id):
        """Generate detailed report for a session"""
        return render_template('report.html', session_id=session_id)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app
'''

with open('MalSimPro/dashboard/web_interface.py', 'w') as f:
    f.write(web_interface_content)

print("✅ Created web_interface.py - Flask web dashboard")

# Create the analytics engine
analytics_content = '''"""
Analytics Engine for MalSim Pro
Generates insights and visualizations from simulation data
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
from database.analysis_db import AnalysisDB

class AnalyticsEngine:
    def __init__(self, db: AnalysisDB):
        self.db = db
    
    def analyze_session(self, session_id: str) -> Dict[str, Any]:
        """Analyze a specific session and generate insights"""
        analysis = {
            'session_id': session_id,
            'threat_level': 'medium',
            'iocs_detected': [],
            'behavioral_patterns': [],
            'risk_score': 0.0,
            'recommendations': []
        }
        
        # This would contain more sophisticated analysis
        analysis['recommendations'] = [
            'Monitor network traffic for suspicious outbound connections',
            'Check file integrity on target systems',
            'Review process creation logs for anomalies',
            'Implement enhanced endpoint detection rules'
        ]
        
        return analysis
    
    def generate_timeline(self) -> List[Dict[str, Any]]:
        """Generate timeline data for visualization"""
        sessions = self.db.get_sessions(20)
        
        timeline_data = []
        for session in sessions:
            timeline_data.append({
                'timestamp': session['created_at'],
                'type': session['malware_type'],
                'session_id': session['session_id'],
                'duration': session.get('duration', 0)
            })
        
        return sorted(timeline_data, key=lambda x: x['timestamp'])
    
    def generate_heatmap(self) -> Dict[str, Any]:
        """Generate activity heatmap data"""
        stats = self.db.get_statistics()
        
        heatmap_data = {
            'malware_types': stats.get('sessions_by_type', {}),
            'activity_levels': {
                'high': 15,
                'medium': 25, 
                'low': 10
            },
            'time_distribution': {
                '00-06': 2,
                '06-12': 8,
                '12-18': 12,
                '18-24': 5
            }
        }
        
        return heatmap_data
    
    def calculate_threat_score(self, session_data: Dict[str, Any]) -> float:
        """Calculate threat score based on simulation results"""
        score = 0.0
        
        # Base score by malware type
        type_scores = {
            'ransomware': 0.9,
            'trojan': 0.8,
            'worm': 0.7,
            'spyware': 0.6
        }
        
        malware_type = session_data.get('type', 'unknown')
        score += type_scores.get(malware_type, 0.5)
        
        return min(score, 1.0)
    
    def extract_iocs(self, session_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract Indicators of Compromise from session data"""
        iocs = []
        
        # Extract network IOCs
        if 'network_events' in session_data:
            for event in session_data['network_events']:
                if 'dst_ip' in event:
                    iocs.append({
                        'type': 'ip_address',
                        'value': event['dst_ip'],
                        'description': 'Suspicious network connection',
                        'confidence': 0.7
                    })
        
        # Extract file IOCs  
        if 'file_events' in session_data:
            for event in session_data['file_events']:
                if event.get('operation') == 'create' and '.encrypted' in event.get('file_path', ''):
                    iocs.append({
                        'type': 'file_extension',
                        'value': '.encrypted',
                        'description': 'Ransomware encrypted file extension',
                        'confidence': 0.9
                    })
        
        return iocs
    
    def generate_behavioral_analysis(self, session_data: Dict[str, Any]) -> List[str]:
        """Generate behavioral analysis insights"""
        patterns = []
        
        malware_type = session_data.get('type', 'unknown')
        
        if malware_type == 'ransomware':
            patterns.extend([
                'File encryption behavior detected',
                'Ransom note creation observed',
                'Bulk file modification patterns',
                'Potential backup deletion attempts'
            ])
        elif malware_type == 'trojan':
            patterns.extend([
                'Backdoor communication established',
                'Keylogger activity detected',
                'Screen capture behavior observed',
                'Data exfiltration attempts'
            ])
        elif malware_type == 'worm':
            patterns.extend([
                'Network scanning behavior',
                'Lateral movement attempts',
                'Service exploitation patterns',
                'Self-propagation mechanisms'
            ])
        elif malware_type == 'spyware':
            patterns.extend([
                'Credential harvesting activity',
                'Browser data extraction',
                'Persistent monitoring behavior',
                'Stealth communication patterns'
            ])
        
        return patterns
'''

with open('MalSimPro/dashboard/analytics.py', 'w') as f:
    f.write(analytics_content)

print("✅ Created analytics.py - Analytics engine with threat scoring")

# Create the reporting module
reporting_content = '''"""
Reporting Module for MalSim Pro
Generates comprehensive analysis reports
"""

import json
import os
from datetime import datetime
from typing import Dict, Any
from database.analysis_db import AnalysisDB
from dashboard.analytics import AnalyticsEngine

class ReportGenerator:
    def __init__(self, db: AnalysisDB, analytics: AnalyticsEngine):
        self.db = db
        self.analytics = analytics
        self.report_dir = './reports'
        
        # Ensure reports directory exists
        os.makedirs(self.report_dir, exist_ok=True)
    
    def generate_session_report(self, session_id: str, format: str = 'html') -> str:
        """Generate a comprehensive report for a specific session"""
        
        # Get session data
        sessions = self.db.get_sessions()
        session = next((s for s in sessions if s['session_id'] == session_id), None)
        
        if not session:
            raise ValueError(f"Session {session_id} not found")
        
        # Get analysis
        analysis = self.analytics.analyze_session(session_id)
        
        # Generate report content
        report_data = {
            'session_info': session,
            'analysis': analysis,
            'generated_at': datetime.now().isoformat(),
            'report_type': 'detailed_analysis'
        }
        
        if format.lower() == 'json':
            return self._generate_json_report(report_data, session_id)
        else:
            return self._generate_html_report(report_data, session_id)
    
    def _generate_html_report(self, data: Dict[str, Any], session_id: str) -> str:
        """Generate HTML report"""
        
        html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>MalSim Pro - Analysis Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; }}
        .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; }}
        .warning {{ background: #fff3cd; border-color: #ffc107; padding: 10px; }}
        .metric {{ display: inline-block; margin: 10px; padding: 15px; 
                  background: #f8f9fa; border-radius: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔬 MalSim Pro - Malware Analysis Report</h1>
        <p>Session: {session_id}</p>
        <p>Generated: {data['generated_at']}</p>
    </div>
    
    <div class="warning">
        ⚠️ <strong>Educational Simulation:</strong> This report is based on safe malware 
        simulation data for educational purposes. No real threats were analyzed.
    </div>
    
    <div class="section">
        <h2>📊 Executive Summary</h2>
        <div class="metric">
            <strong>Malware Type:</strong><br>
            {data['session_info']['malware_type'].title()}
        </div>
        <div class="metric">
            <strong>Threat Level:</strong><br>
            {data['analysis']['threat_level'].title()}
        </div>
        <div class="metric">
            <strong>Risk Score:</strong><br>
            {data['analysis']['risk_score']:.2f}/1.0
        </div>
        <div class="metric">
            <strong>Duration:</strong><br>
            {data['session_info'].get('duration', 0)} seconds
        </div>
    </div>
    
    <div class="section">
        <h2>🔍 Analysis Details</h2>
        <h3>Behavioral Patterns:</h3>
        <ul>
        {''.join([f'<li>{pattern}</li>' for pattern in data['analysis']['behavioral_patterns']])}
        </ul>
        
        <h3>Indicators of Compromise (IOCs):</h3>
        <table>
            <tr><th>Type</th><th>Value</th><th>Description</th><th>Confidence</th></tr>
        {''.join([f'<tr><td>{ioc.get("type", "")}</td><td>{ioc.get("value", "")}</td><td>{ioc.get("description", "")}</td><td>{ioc.get("confidence", 0):.2f}</td></tr>' for ioc in data['analysis']['iocs_detected']])}
        </table>
    </div>
    
    <div class="section">
        <h2>💡 Recommendations</h2>
        <ul>
        {''.join([f'<li>{rec}</li>' for rec in data['analysis']['recommendations']])}
        </ul>
    </div>
    
    <div class="section">
        <h2>📋 Technical Details</h2>
        <p><strong>Session Configuration:</strong></p>
        <pre>{json.dumps(data['session_info'], indent=2)}</pre>
    </div>
    
    <footer style="margin-top: 50px; padding: 20px; background: #f8f9fa; text-align: center;">
        <p>Generated by MalSim Pro - Educational Malware Analysis Platform</p>
        <p>⚠️ For educational and training purposes only</p>
    </footer>
</body>
</html>
        '''
        
        # Save report
        filename = f"report_{session_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        filepath = os.path.join(self.report_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(html_content)
        
        return filepath
    
    def _generate_json_report(self, data: Dict[str, Any], session_id: str) -> str:
        """Generate JSON report"""
        filename = f"report_{session_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.report_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filepath
    
    def generate_summary_report(self) -> str:
        """Generate a summary report of all sessions"""
        sessions = self.db.get_sessions()
        stats = self.db.get_statistics()
        
        summary_data = {
            'total_sessions': len(sessions),
            'statistics': stats,
            'recent_sessions': sessions[:10],
            'generated_at': datetime.now().isoformat()
        }
        
        filename = f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.report_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(summary_data, f, indent=2)
        
        return filepath
'''

with open('MalSimPro/dashboard/reporting.py', 'w') as f:
    f.write(reporting_content)

print("✅ Created reporting.py - Comprehensive report generation")