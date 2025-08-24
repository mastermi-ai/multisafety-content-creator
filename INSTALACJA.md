# 🚀 Instrukcja Instalacji - Safety Content Creator

## Wymagania Systemowe

### macOS / iOS (iPad)
- macOS 10.15+ lub iPadOS 13+
- Python 3.9 lub nowszy
- Przeglądarka Safari/Chrome/Firefox

### Windows
- Windows 10 lub nowszy
- Python 3.9 lub nowszy
- Przeglądarka Chrome/Edge/Firefox

### Linux
- Ubuntu 20.04+ / Debian 11+ / CentOS 8+
- Python 3.9 lub nowszy
- Przeglądarka Firefox/Chrome

## 📦 Instalacja Krok po Kroku

### 1. Pobranie Aplikacji
```bash
# Jeśli masz dostęp do repozytorium
git clone <repository_url>
cd SafetyContentCreator

# Lub skopiuj wszystkie pliki do folderu SafetyContentCreator
```

### 2. Instalacja Python (jeśli brakuje)

#### macOS
```bash
# Sprawdź wersję Python
python3 --version

# Jeśli Python nie jest zainstalowany, zainstaluj przez Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

#### Windows
1. Pobierz Python z [python.org](https://python.org/downloads/)
2. Podczas instalacji zaznacz "Add Python to PATH"
3. Sprawdź w cmd: `python --version`

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 3. Instalacja Zależności

```bash
# Przejdź do katalogu aplikacji
cd SafetyContentCreator

# Zainstaluj wymagane biblioteki
python3 -m pip install flask requests pillow python-dotenv

# Lub użyj pliku requirements.txt
python3 -m pip install -r requirements.txt
```

### 4. Konfiguracja AI (Opcjonalna)

```bash
# Skopiuj plik konfiguracyjny
cp config_example.env .env

# Edytuj plik .env i dodaj klucze API
nano .env  # lub użyj innego edytora
```

Zawartość pliku `.env`:
```env
# Wybierz jeden z serwisów AI
OPENAI_API_KEY=sk-your-openai-key-here
# lub
ANTHROPIC_API_KEY=sk-ant-your-claude-key-here

# Wybór serwisu
AI_SERVICE=openai  # lub anthropic lub mock
```

## 🚀 Uruchomienie Aplikacji

### Metoda 1: Skrypt Startowy (Zalecana)
```bash
python3 start.py
```

### Metoda 2: Bezpośrednio
```bash
python3 app.py
```

### Metoda 3: iPadOS/iOS (Safari)
1. Uruchom aplikację na komputerze w tej samej sieci
2. Znajdź adres IP komputera: `ifconfig` (macOS/Linux) lub `ipconfig` (Windows)
3. Na iPadzie otwórz Safari i wejdź na: `http://[IP_KOMPUTERA]:5000`

## 🌐 Dostęp do Aplikacji

Po uruchomieniu aplikacja będzie dostępna pod adresem:
- **Lokalnie**: http://localhost:5000
- **W sieci**: http://[IP_KOMPUTERA]:5000

Aplikacja automatycznie otworzy się w przeglądarce.

## 🔧 Rozwiązywanie Problemów

### Problem: "command not found: python3"
**Rozwiązanie**:
```bash
# macOS - sprawdź czy Python jest w PATH
which python3
export PATH="/usr/local/bin:$PATH"

# Windows - użyj py zamiast python3
py app.py
```

### Problem: "No module named 'flask'"
**Rozwiązanie**:
```bash
# Upewnij się że instalujesz w poprawnym środowisku Python
python3 -m pip install --user flask requests pillow python-dotenv
```

### Problem: "Permission denied"
**Rozwiązanie**:
```bash
# Nadaj uprawnienia do plików
chmod +x start.py
chmod 755 app.py
```

### Problem: "Port 5000 already in use"
**Rozwiązanie**:
```bash
# Znajdź i zabij proces używający portu 5000
lsof -ti:5000 | xargs kill -9

# Lub zmień port w app.py na inny (np. 5001)
```

### Problem: AI nie działa
**Rozwiązanie**:
- Sprawdź klucze API w pliku `.env`
- Aplikacja działa też bez AI (tryb mock)
- Sprawdź połączenie internetowe

## 📱 Instalacja na iPadzie

### Opcja 1: Serwer Zdalny
1. Uruchom aplikację na komputerze
2. Udostępnij przez sieć WiFi
3. Otwórz Safari na iPadzie
4. Dodaj do ekranu głównego (ikona "Udostępnij" → "Dodaj do ekranu głównego")

### Opcja 2: Aplikacja PWA
1. Otwórz aplikację w Safari na iPadzie
2. Naciśnij przycisk "Udostępnij"
3. Wybierz "Dodaj do ekranu głównego"
4. Aplikacja będzie działać jak natywna aplikacja

## 🎯 Pierwsza Konfiguracja

1. **Uruchom aplikację**: `python3 start.py`
2. **Otwórz przeglądarkę**: http://localhost:5000
3. **Wybierz specjalizację**: BHP, IT Security, Znak CE, lub Dozór Urządzeń
4. **Wybierz typ treści**: Post lub Reels
5. **Wygeneruj pierwszą treść**: Kliknij "Wygeneruj"
6. **Przetestuj eksport**: Pobierz obrazek i skopiuj tekst

## 🔐 Bezpieczeństwo

- Aplikacja działa lokalnie - dane nie są wysyłane na zewnętrzne serwery
- Klucze API są przechowywane lokalnie w pliku `.env`
- Brak śledzenia użytkowników
- Wszystkie dane są generowane w czasie rzeczywistym

## 📈 Optymalizacja Wydajności

### Dla lepszej wydajności:
```bash
# Użyj produkcyjnego serwera WSGI
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Cache dla obrazów:
- Obrazy są generowane w czasie rzeczywistym
- Rozważ zapisywanie cache'u w folderze `static/cache/`

## 🆘 Pomoc Techniczna

### Logi aplikacji:
```bash
# Uruchom z debugowaniem
FLASK_ENV=development python3 app.py
```

### Sprawdzenie instalacji:
```bash
python3 -c "import flask, requests, PIL; print('✅ Wszystkie biblioteki zainstalowane')"
```

### Reset aplikacji:
```bash
# Usuń cache i pliki tymczasowe
rm -rf __pycache__/
rm -rf .env
cp config_example.env .env
```

## 📞 Kontakt

W przypadku problemów technicznych:
- 📧 Email: support@multisafety.pl  
- 🌐 Website: https://multisafety.pl
- 📱 Telefon: +48 XXX XXX XXX

---

**Aplikacja została stworzona specjalnie dla firmy Inżynieria Bezpieczeństwa 🛡️**
