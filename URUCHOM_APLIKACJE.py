#!/usr/bin/env python3
"""
🛡️ SAFETY CONTENT CREATOR PREMIUM v2.0
Instrukcja uruchomienia - Kliknij dwukrotnie lub uruchom w terminalu
"""

import os
import sys
import webbrowser
from threading import Timer

# Dodaj folder do Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    """Otwórz przeglądarkę po 3 sekundach"""
    webbrowser.open('http://localhost:5003')

def main():
    print("🛡️  SAFETY CONTENT CREATOR PREMIUM v2.0")
    print("=" * 60)
    print("🚀 Uruchamianie zaawansowanej aplikacji...")
    print("📱 Generator treści Instagram dla Inżynierii Bezpieczeństwa")
    print()
    
    try:
        # Import aplikacji
        from app import app, COMPANY_SPECIALIZATIONS, POST_TEMPLATES
        
        print("✅ Moduły załadowane pomyślnie!")
        print("✅ AI Content Generator: READY")
        print("✅ Premium UI: LOADED")
        print("✅ Advanced Features: ACTIVE")
        print()
        print("🌐 Otwieranie przeglądarki...")
        print("📍 Adres: http://localhost:5003")
        print("💡 Aby zatrzymać: Ctrl+C")
        print("=" * 60)
        
        # Otwórz przeglądarkę po 3 sekundach
        Timer(3.0, open_browser).start()
        
        # Uruchom aplikację Flask
        app.run(
            host='0.0.0.0',
            port=5003,
            debug=False,  # Wyłączamy debug dla stabilności
            use_reloader=False,  # Wyłączamy auto-reload
            threaded=True  # Włączamy obsługę wielu połączeń
        )
        
    except ImportError as e:
        print(f"❌ Błąd importu modułów: {e}")
        print()
        print("💡 Zainstaluj wymagane biblioteki:")
        print("   python3 -m pip install flask requests pillow python-dotenv")
        print()
        print("🔧 Lub użyj prostej wersji testowej:")
        print("   python3 -c \"exec(open('test_simple.py').read())\"")
        
    except Exception as e:
        print(f"❌ Błąd uruchamiania: {e}")
        print("💡 Sprawdź czy port 5003 nie jest zajęty")
        print("💡 Lub zmień port w kodzie na inny (np. 5006)")

if __name__ == '__main__':
    main()
