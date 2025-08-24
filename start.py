#!/usr/bin/env python3
"""
Safety Content Creator - Startup Script
Uruchomienie aplikacji do generowania treści Instagram
"""

import os
import sys
import webbrowser
from threading import Timer

# Dodaj bieżący katalog do PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    """Otwórz przeglądarkę po 2 sekundach"""
    webbrowser.open('http://localhost:5002')

if __name__ == '__main__':
    print("🛡️  Safety Content Creator")
    print("=" * 50)
    print("Uruchamianie aplikacji...")
    print("📱 Generator treści Instagram dla Inżynierii Bezpieczeństwa")
    print()
    
    # Uruchom aplikację
    try:
        from app import app
        
        print("✅ Aplikacja załadowana pomyślnie!")
        print("🌐 Otwieranie przeglądarki...")
        print("📍 Adres: http://localhost:5002")
        print()
        print("💡 Aby zatrzymać aplikację, naciśnij Ctrl+C")
        print("=" * 50)
        
        # Otwórz przeglądarkę po 2 sekundach
        Timer(2.0, open_browser).start()
        
        # Uruchom serwer Flask
        app.run(debug=True, host='0.0.0.0', port=5002, use_reloader=False)
        
    except ImportError as e:
        print(f"❌ Błąd importu: {e}")
        print("💡 Sprawdź czy wszystkie zależności są zainstalowane:")
        print("   python3 -m pip install flask requests pillow python-dotenv")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Błąd uruchamiania: {e}")
        sys.exit(1)
