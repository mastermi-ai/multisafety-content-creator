#!/usr/bin/env python3
"""
Simple launcher for Safety Content Creator
"""

import os
import sys

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

print("🛡️  Safety Content Creator PREMIUM v2.0")
print("=" * 60)
print("🚀 Uruchamianie aplikacji...")

try:
    # Import Flask app
    from app import app
    
    print("✅ Aplikacja załadowana pomyślnie!")
    print("🌐 Serwer uruchamiany...")
    print("📍 Adres: http://localhost:5002")
    print("💡 Aby zatrzymać aplikację: Ctrl+C")
    print("=" * 60)
    
    # Run Flask app
    app.run(
        host='0.0.0.0', 
        port=5002, 
        debug=False,  # Wyłączamy debug dla stabilności
        use_reloader=False
    )
    
except ImportError as e:
    print(f"❌ Błąd importu: {e}")
    print("💡 Zainstaluj wymagane biblioteki:")
    print("   python3 -m pip install flask requests pillow python-dotenv")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ Błąd uruchamiania: {e}")
    print("💡 Sprawdź czy port 5002 nie jest zajęty")
    sys.exit(1)
