# Create the CSS stylesheet
css_content = '''/* MalSim Pro Dashboard Styles */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #1a1a1a;
    color: #e0e0e0;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem 0;
    text-align: center;
}

.header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.subtitle {
    font-size: 1.1rem;
    opacity: 0.9;
}

/* Warning Banner */
.warning-banner {
    background-color: #ff6b35;
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: 500;
}

/* Dashboard Grid */
.dashboard-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    padding: 2rem 0;
}

.dashboard-grid > div {
    background: #2d2d2d;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

/* Statistics Section */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.stat-card {
    background: #3d3d3d;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    transition: transform 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-2px);
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: #4CAF50;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Sessions Section */
.sessions-list {
    max-height: 300px;
    overflow-y: auto;
    margin-top: 1rem;
}

.session-item {
    background: #3d3d3d;
    padding: 1rem;
    margin-bottom: 0.5rem;
    border-radius: 5px;
    border-left: 4px solid #667eea;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.session-info h4 {
    color: #667eea;
    margin-bottom: 0.25rem;
}

.session-meta {
    font-size: 0.85rem;
    opacity: 0.7;
}

.session-status {
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 500;
}

.status-completed { background-color: #4CAF50; color: white; }
.status-running { background-color: #ff9800; color: white; }
.status-failed { background-color: #f44336; color: white; }

/* Charts Section */
.charts-section {
    grid-column: 1 / -1;
}

.chart-container {
    background: #3d3d3d;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    height: 300px;
}

/* Actions Section */
.action-buttons {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.action-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: center;
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.action-btn.secondary {
    background: #555;
}

.action-btn.secondary:hover {
    background: #666;
}

/* Loading and Error States */
.loading {
    text-align: center;
    padding: 2rem;
    opacity: 0.7;
}

.error {
    color: #f44336;
    text-align: center;
    padding: 1rem;
}

/* Report Styles */
.report-content {
    max-width: 800px;
    margin: 0 auto;
}

.report-section {
    background: #2d2d2d;
    margin: 2rem 0;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.report-section h2 {
    color: #667eea;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #3d3d3d;
}

.summary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.summary-item {
    background: #3d3d3d;
    padding: 1rem;
    border-radius: 5px;
}

.report-actions {
    text-align: center;
    padding: 2rem 0;
}

.report-actions .action-btn {
    margin: 0 0.5rem;
}

/* Footer */
.footer {
    background: #2d2d2d;
    text-align: center;
    padding: 2rem 0;
    margin-top: 2rem;
    border-top: 1px solid #3d3d3d;
}

.footer p {
    margin: 0.5rem 0;
    opacity: 0.7;
}

/* Responsive Design */
@media (max-width: 768px) {
    .dashboard-grid {
        grid-template-columns: 1fr;
    }
    
    .header h1 {
        font-size: 2rem;
    }
    
    .action-buttons {
        grid-template-columns: 1fr;
    }
    
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Scrollbar Styling */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #2d2d2d;
}

::-webkit-scrollbar-thumb {
    background: #667eea;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #764ba2;
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.dashboard-grid > div {
    animation: fadeIn 0.6s ease forwards;
}
'''

with open('MalSimPro/static/css/style.css', 'w') as f:
    f.write(css_content)

print("✅ Created style.css - Complete dashboard styling")

# Create the JavaScript for dashboard functionality
js_content = '''// MalSim Pro Dashboard JavaScript

class MalSimDashboard {
    constructor() {
        this.charts = {};
        this.refreshInterval = 5000; // 5 seconds
        this.init();
    }

    async init() {
        console.log('🔬 MalSim Pro Dashboard initializing...');
        
        // Load initial data
        await this.loadStatistics();
        await this.loadSessions();
        
        // Initialize charts
        this.initCharts();
        
        // Start auto-refresh
        this.startAutoRefresh();
        
        console.log('✅ Dashboard initialized successfully');
    }

    async loadStatistics() {
        try {
            const response = await fetch('/api/statistics');
            const stats = await response.json();
            
            this.updateStatistics(stats);
        } catch (error) {
            console.error('Error loading statistics:', error);
            this.showError('Failed to load statistics');
        }
    }

    updateStatistics(stats) {
        // Update stat cards
        const elements = {
            'total-sessions': this.getTotalSessions(stats),
            'sessions-today': stats.sessions_last_24h || 0,
            'active-simulations': 0, // Would be calculated from active sessions
            'threat-level': 'Medium'
        };

        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
                element.style.animation = 'none';
                element.offsetHeight; // Trigger reflow
                element.style.animation = 'fadeIn 0.5s ease';
            }
        });
    }

    getTotalSessions(stats) {
        if (stats.sessions_by_type) {
            return Object.values(stats.sessions_by_type).reduce((sum, count) => sum + count, 0);
        }
        return 0;
    }

    async loadSessions() {
        try {
            const response = await fetch('/api/sessions?limit=10');
            const sessions = await response.json();
            
            this.updateSessionsList(sessions);
        } catch (error) {
            console.error('Error loading sessions:', error);
            this.showError('Failed to load sessions');
        }
    }

    updateSessionsList(sessions) {
        const container = document.getElementById('sessions-list');
        
        if (!sessions || sessions.length === 0) {
            container.innerHTML = '<p class="loading">No sessions found. Start a simulation to see results here.</p>';
            return;
        }

        container.innerHTML = sessions.map(session => `
            <div class="session-item" onclick="viewSession('${session.session_id}')">
                <div class="session-info">
                    <h4>${this.formatSessionTitle(session)}</h4>
                    <div class="session-meta">
                        ${this.formatDate(session.created_at)} • Duration: ${session.duration || 0}s
                    </div>
                </div>
                <div class="session-status status-${session.status || 'completed'}">
                    ${(session.status || 'completed').toUpperCase()}
                </div>
            </div>
        `).join('');
    }

    formatSessionTitle(session) {
        const type = session.malware_type || 'Unknown';
        return `${type.charAt(0).toUpperCase() + type.slice(1)} Simulation`;
    }

    formatDate(dateString) {
        if (!dateString) return 'Unknown date';
        try {
            return new Date(dateString).toLocaleString();
        } catch {
            return 'Invalid date';
        }
    }

    initCharts() {
        this.initMalwareTypesChart();
        this.initActivityTimelineChart();
    }

    async initMalwareTypesChart() {
        try {
            const response = await fetch('/api/statistics');
            const stats = await response.json();
            
            const ctx = document.getElementById('malware-types-chart');
            if (!ctx) return;

            const data = stats.sessions_by_type || {};
            
            this.charts.malwareTypes = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(data).map(key => key.charAt(0).toUpperCase() + key.slice(1)),
                    datasets: [{
                        data: Object.values(data),
                        backgroundColor: [
                            '#FF6384',
                            '#36A2EB', 
                            '#FFCE56',
                            '#4BC0C0',
                            '#9966FF'
                        ],
                        borderWidth: 2,
                        borderColor: '#2d2d2d'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Malware Types Distribution',
                            color: '#e0e0e0'
                        },
                        legend: {
                            labels: {
                                color: '#e0e0e0'
                            }
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error initializing malware types chart:', error);
        }
    }

    async initActivityTimelineChart() {
        try {
            const response = await fetch('/api/analytics/timeline');
            const timelineData = await response.json();
            
            const ctx = document.getElementById('activity-timeline-chart');
            if (!ctx) return;

            // Process timeline data for chart
            const labels = timelineData.map(item => this.formatDate(item.timestamp));
            const data = timelineData.map(item => item.duration || 0);

            this.charts.activityTimeline = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Session Duration (seconds)',
                        data: data,
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Activity Timeline',
                            color: '#e0e0e0'
                        },
                        legend: {
                            labels: {
                                color: '#e0e0e0'
                            }
                        }
                    },
                    scales: {
                        x: {
                            ticks: { color: '#e0e0e0' },
                            grid: { color: '#3d3d3d' }
                        },
                        y: {
                            ticks: { color: '#e0e0e0' },
                            grid: { color: '#3d3d3d' }
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error initializing activity timeline chart:', error);
        }
    }

    startAutoRefresh() {
        setInterval(() => {
            this.loadStatistics();
            this.loadSessions();
        }, this.refreshInterval);
    }

    showError(message) {
        console.error(message);
        // Could show toast notification here
    }
}

// Global functions for button actions
window.startSimulation = function(type) {
    console.log(`Starting ${type} simulation...`);
    
    // Show loading state
    const button = event.target;
    const originalText = button.textContent;
    button.textContent = '⏳ Starting...';
    button.disabled = true;
    
    // Simulate API call
    setTimeout(() => {
        alert(`${type.charAt(0).toUpperCase() + type.slice(1)} simulation started!\\n\\nNote: In a real implementation, this would:\\n- Start the malware simulator\\n- Begin system monitoring\\n- Create a new session in the database`);
        
        button.textContent = originalText;
        button.disabled = false;
        
        // Refresh dashboard to show new session
        window.dashboard.loadSessions();
        window.dashboard.loadStatistics();
    }, 2000);
};

window.viewSession = function(sessionId) {
    console.log(`Viewing session: ${sessionId}`);
    window.location.href = `/report/${sessionId}`;
};

window.generateReport = function() {
    alert('Generate Report functionality\\n\\nThis would:\\n- Create comprehensive analysis report\\n- Export to PDF/HTML format\\n- Include charts and recommendations');
};

window.exportData = function() {
    alert('Export Data functionality\\n\\nThis would:\\n- Export session data to CSV/JSON\\n- Include all monitoring events\\n- Provide IOCs and artifacts');
};

// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', function() {
    window.dashboard = new MalSimDashboard();
});

// Handle page visibility for performance
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        console.log('Dashboard hidden - pausing updates');
    } else {
        console.log('Dashboard visible - resuming updates');
        window.dashboard.loadStatistics();
        window.dashboard.loadSessions();
    }
});
'''

with open('MalSimPro/static/js/dashboard.js', 'w') as f:
    f.write(js_content)

print("✅ Created dashboard.js - Complete dashboard functionality")