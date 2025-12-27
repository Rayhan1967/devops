"""
Simple Flask Application for DevOps Project
"""
from flask import Flask, jsonify, request
import os
import sys
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'devops-app',
        'timestamp': datetime.utcnow().isoformat(),
        'version': os.getenv('APP_VERSION', '1.0.0')
    }), 200

@app.route('/api/v1/info')
def get_info():
    """Get application information"""
    return jsonify({
        'app_name': 'DevOps Project App',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': os.getenv('HOSTNAME', 'localhost'),
        'python_version': sys.version
    }), 200

@app.route('/api/v1/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing"""
    data = request.get_json() or {}
    return jsonify({
        'message': 'Echo successful',
        'received_data': data,
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/v1/metrics')
def metrics():
    """Simple metrics endpoint"""
    return jsonify({
        'requests_processed': 0,
        'uptime': 'N/A',
        'memory_usage': 'N/A'
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)

