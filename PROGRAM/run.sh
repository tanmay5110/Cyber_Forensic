#!/bin/bash
# MalSim Pro Quick Start Script

echo "🔬 MalSim Pro - Educational Malware Simulation Platform"
echo "=================================================="

# Check if running in VM (basic check)
echo "🔍 Checking environment..."

# Check for common VM indicators
if [ -d "/proc/vz" ] || grep -q "hypervisor" /proc/cpuinfo 2>/dev/null || [ -d "/proc/xen" ]; then
    echo "✅ Virtual environment detected"
else
    echo "⚠️  WARNING: Virtual environment not clearly detected"
    echo "This tool should only be run in isolated VMs!"
    read -p "Continue anyway? (y/N): " confirm
    if [[ $confirm != [yY] ]]; then
        echo "❌ Exiting for safety"
        exit 1
    fi
fi

# Start the application
echo "🚀 Starting MalSim Pro Dashboard..."
echo "📍 Dashboard will be available at: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop"
echo ""

python main.py --mode dashboard --port 5000
