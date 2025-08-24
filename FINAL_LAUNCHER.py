#!/usr/bin/env python3
"""
🛡️ CONTENT CREATOR DLA INŻYNIERII BEZPIECZEŃSTWA v3.0
PREMIUM LAUNCHER - ELIMINUJE GRAFIKÓW!
by Dominika Kicia
"""

import os
import sys
import webbrowser
from threading import Timer

# Setup path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    """Open browser after 3 seconds"""
    webbrowser.open('http://localhost:5003')

def main():
    print("🛡️  CONTENT CREATOR DLA INŻYNIERII BEZPIECZEŃSTWA v5.0")
    print("=" * 80)
    print("📝 PREMIUM CONTENT: 60+ expert variants")
    print("🤖 SMART RANDOMIZATION: Always fresh, never repetitive") 
    print("📱 CORPORATE INSTAGRAM: Professional text content")
    print("🎯 FOCUS: High-quality business copywriting")
    print("👑 by Dominika Kicia")
    print("=" * 80)
    print()
    
    try:
        # Import and setup
        from app import app
        
        print("✅ All modules loaded successfully!")
        print("✅ Premium content library: LOADED")
        print("✅ Intelligent randomization: READY")
        print("📝 60+ Expert content variants: READY")
        print("💼 READY FOR: Corporate Instagram - premium text content!")
        print("📱 BUSINESS LEVEL: High-quality copywriting!")
        print()
        print("🌐 Opening browser in 3 seconds...")
        print("📍 Application URL: http://localhost:5003")
        print("💡 To stop: Press Ctrl+C")
        print("=" * 70)
        
        # Open browser
        Timer(3.0, open_browser).start()
        
        # Run Flask
        app.run(
            host='0.0.0.0',
            port=5003,
            debug=False,
            use_reloader=False,
            threaded=True
        )
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Install required packages:")
        print("   python3 -m pip install flask requests pillow python-dotenv")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Runtime Error: {e}")
        print("💡 Check if port 5003 is available")
        sys.exit(1)

if __name__ == '__main__':
    main()
