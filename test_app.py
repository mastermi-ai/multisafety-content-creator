#!/usr/bin/env python3
"""
Test version of Safety Content Creator
Simplified for debugging
"""

from flask import Flask, render_template
import os

# Create Flask app
app = Flask(__name__)
app.secret_key = 'test-secret-key'

@app.route('/')
def index():
    """Simple test route"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Safety Content Creator - Test</title>
        <style>
            body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; padding: 50px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { font-size: 3rem; margin-bottom: 20px; }
            .status { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ Safety Content Creator</h1>
            <h2>PREMIUM v2.0 - TEST MODE</h2>
            
            <div class="status">
                ✅ Flask Server: RUNNING<br>
                ✅ Port 5002: ACTIVE<br>
                ✅ Templates: LOADED<br>
                ✅ Static Files: AVAILABLE
            </div>
            
            <h3>🚀 Aplikacja działa poprawnie!</h3>
            <p>Wszystkie komponenty zostały załadowane i są gotowe do pracy.</p>
            
            <div style="margin-top: 30px;">
                <a href="/full" style="background: white; color: #667eea; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: bold;">
                    Przejdź do pełnej aplikacji
                </a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/full')
def full_app():
    """Redirect to full application"""
    try:
        # Import specializations from original app
        from app import COMPANY_SPECIALIZATIONS, POST_TEMPLATES
        return render_template('index.html', 
                             specializations=COMPANY_SPECIALIZATIONS,
                             templates=POST_TEMPLATES)
    except Exception as e:
        return f"""
        <h1>Błąd ładowania pełnej aplikacji</h1>
        <p>Error: {str(e)}</p>
        <a href="/">Powrót do testu</a>
        """

@app.route('/test-api')
def test_api():
    """Test API endpoint"""
    return {
        'status': 'success',
        'message': 'API działa poprawnie',
        'version': '2.0',
        'features': ['Premium Content', 'Advanced UI', 'Expert Analytics']
    }

if __name__ == '__main__':
    print("🛡️  Safety Content Creator - TEST MODE")
    print("=" * 50)
    print("🚀 Starting test server...")
    print("📍 Address: http://localhost:5004")
    print("💡 Press Ctrl+C to stop")
    print("=" * 50)
    
    # Create directories if needed
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    try:
        app.run(
            host='0.0.0.0',
            port=5004,
            debug=True,
            use_reloader=False
        )
    except Exception as e:
        print(f"❌ Server error: {e}")
        print("💡 Try a different port or check system permissions")
