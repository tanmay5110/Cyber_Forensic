# Create the main dashboard HTML template
dashboard_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MalSim Pro - Malware Analysis Dashboard</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>🔬 MalSim Pro</h1>
            <p class="subtitle">Educational Malware Simulation & Analysis Platform</p>
        </div>
    </header>

    <div class="warning-banner">
        ⚠️ <strong>Educational Tool:</strong> This platform simulates malware behavior safely for learning purposes. 
        All simulations are contained and pose no real threat.
    </div>

    <main class="container">
        <div class="dashboard-grid">
            <!-- Statistics Cards -->
            <div class="stats-section">
                <h2>📊 Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number" id="total-sessions">0</div>
                        <div class="stat-label">Total Sessions</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="sessions-today">0</div>
                        <div class="stat-label">Sessions Today</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="active-simulations">0</div>
                        <div class="stat-label">Active Simulations</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="threat-level">Medium</div>
                        <div class="stat-label">Avg Threat Level</div>
                    </div>
                </div>
            </div>

            <!-- Recent Sessions -->
            <div class="sessions-section">
                <h2>🗂️ Recent Sessions</h2>
                <div class="sessions-list" id="sessions-list">
                    <div class="loading">Loading sessions...</div>
                </div>
            </div>

            <!-- Charts Section -->
            <div class="charts-section">
                <h2>📈 Analytics</h2>
                <div class="chart-container">
                    <canvas id="malware-types-chart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="activity-timeline-chart"></canvas>
                </div>
            </div>

            <!-- Quick Actions -->
            <div class="actions-section">
                <h2>⚡ Quick Actions</h2>
                <div class="action-buttons">
                    <button class="action-btn" onclick="startSimulation('ransomware')">
                        🔒 Ransomware Simulation
                    </button>
                    <button class="action-btn" onclick="startSimulation('trojan')">
                        🎭 Trojan Simulation
                    </button>
                    <button class="action-btn" onclick="startSimulation('worm')">
                        🪱 Worm Simulation
                    </button>
                    <button class="action-btn" onclick="startSimulation('spyware')">
                        👁️ Spyware Simulation
                    </button>
                </div>
                <div class="action-buttons">
                    <button class="action-btn secondary" onclick="generateReport()">
                        📄 Generate Report
                    </button>
                    <button class="action-btn secondary" onclick="exportData()">
                        💾 Export Data
                    </button>
                </div>
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 MalSim Pro - Educational Malware Analysis Platform</p>
            <p>⚠️ For educational and research purposes only. Use only in isolated environments.</p>
        </div>
    </footer>

    <script src="/static/js/dashboard.js"></script>
</body>
</html>'''

with open('MalSimPro/templates/dashboard.html', 'w') as f:
    f.write(dashboard_html)

print("✅ Created dashboard.html - Main dashboard template")

# Create the report template
report_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MalSim Pro - Session Report</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>🔬 MalSim Pro - Session Report</h1>
            <p class="subtitle">Session ID: <span id="session-id">{{ session_id }}</span></p>
        </div>
    </header>

    <div class="warning-banner">
        ⚠️ <strong>Educational Simulation Report:</strong> This analysis is based on safe malware simulation data.
    </div>

    <main class="container">
        <div class="report-content">
            <div class="report-section">
                <h2>📊 Executive Summary</h2>
                <div id="executive-summary" class="loading">Loading report data...</div>
            </div>

            <div class="report-section">
                <h2>🔍 Detailed Analysis</h2>
                <div id="detailed-analysis" class="loading">Loading analysis...</div>
            </div>

            <div class="report-section">
                <h2>💡 Recommendations</h2>
                <div id="recommendations" class="loading">Loading recommendations...</div>
            </div>

            <div class="report-section">
                <h2>📋 Technical Details</h2>
                <div id="technical-details" class="loading">Loading technical data...</div>
            </div>
        </div>

        <div class="report-actions">
            <button onclick="window.print()" class="action-btn">🖨️ Print Report</button>
            <button onclick="downloadReport()" class="action-btn">💾 Download PDF</button>
            <button onclick="window.history.back()" class="action-btn secondary">← Back to Dashboard</button>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 MalSim Pro - Educational Malware Analysis Platform</p>
        </div>
    </footer>

    <script>
        // Load report data for the specific session
        const sessionId = "{{ session_id }}";
        
        async function loadReportData() {
            try {
                const response = await fetch(`/api/session/${sessionId}`);
                const data = await response.json();
                
                // Populate report sections
                document.getElementById('executive-summary').innerHTML = generateExecutiveSummary(data);
                document.getElementById('detailed-analysis').innerHTML = generateDetailedAnalysis(data);
                document.getElementById('recommendations').innerHTML = generateRecommendations(data);
                document.getElementById('technical-details').innerHTML = generateTechnicalDetails(data);
                
            } catch (error) {
                console.error('Error loading report data:', error);
                document.querySelectorAll('.loading').forEach(el => {
                    el.innerHTML = '<p class="error">Error loading report data</p>';
                });
            }
        }

        function generateExecutiveSummary(data) {
            return `
                <div class="summary-grid">
                    <div class="summary-item">
                        <strong>Simulation Type:</strong> ${data.session_id.includes('ransomware') ? 'Ransomware' : 'Unknown'}
                    </div>
                    <div class="summary-item">
                        <strong>Status:</strong> ${data.status}
                    </div>
                    <div class="summary-item">
                        <strong>Threat Level:</strong> ${data.analysis?.threat_level || 'Medium'}
                    </div>
                </div>
            `;
        }

        function generateDetailedAnalysis(data) {
            return `
                <p>This session simulated malware behavior in a controlled environment.</p>
                <h3>Key Findings:</h3>
                <ul>
                    <li>Simulation completed successfully</li>
                    <li>All activities contained within sandbox</li>
                    <li>No real system impact detected</li>
                </ul>
            `;
        }

        function generateRecommendations(data) {
            const recommendations = data.analysis?.recommendations || [
                'Review system logs for similar patterns',
                'Update security policies based on findings',
                'Conduct regular security training',
                'Implement additional monitoring controls'
            ];
            
            return `
                <ul>
                    ${recommendations.map(rec => `<li>${rec}</li>`).join('')}
                </ul>
            `;
        }

        function generateTechnicalDetails(data) {
            return `
                <pre>${JSON.stringify(data, null, 2)}</pre>
            `;
        }

        function downloadReport() {
            alert('PDF download functionality would be implemented here');
        }

        // Load data when page loads
        window.onload = loadReportData;
    </script>
</body>
</html>'''

with open('MalSimPro/templates/report.html', 'w') as f:
    f.write(report_html)

print("✅ Created report.html - Report template")