"""
Enhanced AI Content Generator dla MultiSafety.pl
Profesjonalne treści Instagram z fokusem na BHP, RODO, CE, Dozór Urządzeń
"""

import os
import json
import random
from typing import Dict, List, Optional
from dataclasses import dataclass

# Próba importu bibliotek AI
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

@dataclass
class ContentRequest:
    """Struktura żądania treści"""
    specialization: str
    content_type: str  # 'post' lub 'reel'
    template_type: str
    custom_topic: Optional[str] = None
    tone: str = 'professional'
    target_audience: str = 'business'

@dataclass
class GeneratedContent:
    """Struktura wygenerowanej treści"""
    title: str
    hook: str
    main_content: str
    call_to_action: str
    hashtags: List[str]
    full_text: str

# PREMIUM CONTENT LIBRARY FOR MULTISAFETY.PL
MULTISAFETY_PREMIUM_CONTENT = {
    "bhp_ppoz": {
        "tips": [
            """💡 Czy wiesz, że każdy 1 zł wydany na BHP zwraca 2,2 zł oszczędności?

Badanie McKinsey 2024: Firmy z certyfikatem ISO 45001 osiągają:
📊 35% redukcję kosztów ubezpieczeń OC
📈 25% wzrost wydajności pracowników  
📉 45% spadek absencji chorobowej
⚖️ 100% ochronę przed karami PIP

🔥 ROI NAJWYŻSZY W:
• Systemy wczesnego ostrzegania (340% ROI)
• Szkolenia VR (280% ROI) 
• Automatyzacja raportowania BHP (250% ROI)

Nowe przepisy 2025: Elektroniczna dokumentacja BHP obowiązkowa. Czy jesteś gotowy?

🎯 EKSPRESS ANALIZA BHP
⚡ Diagnoza w 24h + konkretne wyliczenia ROI
💡 Bonus: 10 najczęstszych błędów w BHP
📧 Zapytaj: multisafety.pl""",

            """🚨 ALARMUJĄCE: 91% wypadków śmiertelnych przy pracy można było uniknąć!

PIP nałożył w 2024 roku kary na kwotę 127 mln zł. Największa: 300 000 zł dla firmy budowlanej za brak systemu BHP.

✅ Co chroni Twoją firmę:
• Ocena ryzyka zgodna z PN-N-18002
• Szkolenia BHP co 12 miesięcy (nowe przepisy 2025)
• Dokumentacja cyfrowa zgodna z ZRID
• System ISO 45001 (−35% kosztów ubezpieczeń)

⚖️ PAMIĘTAJ: Art. 207 KK = do 3 lat więzienia za sprowadzenie wypadku przy pracy.

🚀 BEZPŁATNY AUDIT BHP
✅ Analiza ryzyka + plan działania w 48h
💰 Potencjał oszczędności: 150-300k zł rocznie
📞 Sprawdź: multisafety.pl"""
        ],
        
        "warnings": [
            """⚠️ UWAGA! Nowe kary PIP 2025 - do 500 000 zł!

Od 1 stycznia 2025 drastycznie wzrastają kary za naruszenia BHP:
💸 Brak oceny ryzyka: 100 000 - 500 000 zł
💸 Nieprzeszkolony pracownik: 50 000 - 200 000 zł
💸 Brak dokumentacji: 30 000 - 150 000 zł

🚨 NAJCZĘSTSZE BŁĘDY 2024:
1. Brak aktualizacji oceny ryzyka (67% kar)
2. Nieważne szkolenia BHP (23% kar)  
3. Brak środków ochrony (10% kar)

✅ OCHRONA 100%:
• Kompleksowy audit BHP
• Aktualizacja dokumentacji
• System zarządzania ISO 45001

⏰ Zostało 30 dni do wejścia nowych przepisów!

🆘 EKSPRESOWA POMOC
📞 Konsultacja w 2h + plan ochrony
💼 Pełna zgodność w 7 dni
🌐 multisafety.pl"""
        ]
    },
    
    "it_security": {
        "tips": [
            """🛡️ RODO 2024: Kary wzrosły do rekordowego poziomu!

NAJWIĘKSZE KARY W POLSCE:
💸 9,6 mln zł - bank za naruszenia w systemach IT
💸 2,8 mln zł - telekom za brak zabezpieczeń
💸 1,2 mln zł - e-commerce za phishing

⚡ NOWE ZAGROŻENIA 2024:
• AI-powered ataki (+340%)
• Ransomware kosztuje średnio 4,5 mln USD
• Dyrektywa NIS2 - kary do 2% obrotu

🛡️ CO CHRONI TWOJĄ FIRMĘ:
✅ IOD (obowiązkowy dla 250+ osób)
✅ ISO 27001 (-80% ryzyka ataków)
✅ DPIA dla systemów HR
✅ Backup 3-2-1 rule

72 godziny na zgłoszenie naruszenia do IOD. Później = dodatkowa kara!

🚀 BEZPŁATNY AUDIT RODO
✅ Analiza obecnego stanu + gap analysis
💰 Oszczędności: -40% kosztów cyber insurance
📧 Sprawdź: multisafety.pl"""
        ]
    },
    
    "ce_marking": {
        "tips": [
            """🇪🇺 Rynek UE wart 15 bln EUR rocznie. Bez znaku CE = 0 EUR dla Twojej firmy!

ALARMUJĄCE STATYSTYKI 2024:
💸 Kary do 100 000 EUR za produkty bez CE
📈 +150% kosztów certyfikacji (8-12 miesięcy oczekiwania)
⚖️ Rozszerzona odpowiedzialność za cały cykl życia produktu
🔍 Nadzór rynku UE wycofał 2847 produktów

🚀 NOWE WYMAGANIA 2024/2025:
• Cyber Resilience Act - CE dla produktów IT
• Digital Product Passport obowiązkowy
• AI Act - compliance dla systemów AI
• Single Market Emergency Instrument

✅ DROGA DO SUKCESU:
1. Analiza dyrektyw UE dla Twojego produktu
2. Dokumentacja techniczna Annex II
3. Testy w akredytowanych laboratoriach  
4. Deklaracja zgodności WE
5. Nadzór post-market + vigilance

💰 ROI EKSPORTU:
Inwestycja 50k zł → Potencjał eksportu: miliony EUR rocznie

🚀 ŚCIEŻKA DO RYNKU UE
✅ Gap analysis + roadmapa certyfikacji
💡 Wsparcie w dokumentacji technicznej
⚡ Fast-track przez nasze kontakty w JN
📞 Sprawdź: multisafety.pl"""
        ]
    }
}

class AIContentGenerator:
    """Enhanced Generator treści AI dla MultiSafety.pl"""
    
    def __init__(self):
        self.ai_service = os.getenv('AI_SERVICE', 'premium')
        self.openai_client = None
        self.anthropic_client = None
        
        # Initialize AI clients if available
        if OPENAI_AVAILABLE and os.getenv('OPENAI_API_KEY'):
            openai.api_key = os.getenv('OPENAI_API_KEY')
            self.openai_client = openai
            
        if ANTHROPIC_AVAILABLE and os.getenv('ANTHROPIC_API_KEY'):
            self.anthropic_client = anthropic.Anthropic(
                api_key=os.getenv('ANTHROPIC_API_KEY')
            )

    def generate_post_content(self, request: ContentRequest) -> GeneratedContent:
        """Generuje treść posta dla MultiSafety.pl"""
        
        # Use AI if available, otherwise fallback to premium templates
        if self.openai_client or self.anthropic_client:
            return self._generate_ai_content(request)
        else:
            return self._generate_premium_template_content(request)
    
    def _generate_premium_template_content(self, request: ContentRequest) -> GeneratedContent:
        """Generuje treść z premium szablonów MultiSafety"""
        
        # Get content pool for specialization
        spec_content = MULTISAFETY_PREMIUM_CONTENT.get(
            request.specialization, 
            MULTISAFETY_PREMIUM_CONTENT['bhp_ppoz']
        )
        
        # Choose content based on template type
        if request.template_type == 'warning':
            content_pool = spec_content.get('warnings', spec_content.get('tips', []))
        else:
            content_pool = spec_content.get('tips', [])
        
        if not content_pool:
            # Fallback content
            selected_content = """💡 Profesjonalne rozwiązania w zakresie bezpieczeństwa

🔥 MultiSafety oferuje kompleksowe wsparcie w obszarze:
• BHP i PPOŻ
• Bezpieczeństwo informacji i RODO  
• Znak CE i dozór urządzeń
• Szkolenia i audyty

✅ Zaufało nam ponad 500 firm
📊 98% zadowolenia klientów
⚡ Wsparcie 24/7

🚀 SKONTAKTUJ SIĘ Z NAMI
📧 Bezpłatna konsultacja w 24h
🌐 multisafety.pl"""
        else:
            selected_content = random.choice(content_pool)
        
        # Custom topic integration
        if request.custom_topic:
            selected_content = f"📝 {request.custom_topic}\n\n{selected_content}"
        
        # Extract components
        lines = selected_content.split('\n')
        
        # Find title/hook (first line with emoji)
        title = lines[0] if lines else "MultiSafety - Profesjonalne Rozwiązania"
        hook = title
        
        # Main content (everything except hashtags)
        main_lines = []
        hashtag_lines = []
        
        for line in lines:
            if line.strip().startswith('#'):
                hashtag_lines.append(line.strip())
            else:
                main_lines.append(line)
        
        main_content = '\n'.join(main_lines)
        
        # Generate specialized hashtags
        hashtags = self._generate_specialized_hashtags(request.specialization)
        if hashtag_lines:
            # Extract hashtags from content
            for line in hashtag_lines:
                extracted = [tag.strip() for tag in line.split() if tag.startswith('#')]
                hashtags.extend(extracted)
        
        # Remove duplicates while preserving order
        unique_hashtags = []
        for tag in hashtags:
            if tag not in unique_hashtags:
                unique_hashtags.append(tag)
        hashtags = unique_hashtags[:12]  # Limit to 12 hashtags
        
        # CTA
        call_to_action = "🚀 Sprawdź: multisafety.pl\n📧 Bezpłatna konsultacja"
        
        # Full text
        full_text = f"{main_content}\n\n{call_to_action}\n\n{' '.join(hashtags[:12])}"
        
        return GeneratedContent(
            title=title,
            hook=hook,
            main_content=main_content,
            call_to_action=call_to_action,
            hashtags=hashtags[:12],
            full_text=full_text
        )
    
    def _generate_specialized_hashtags(self, specialization: str) -> List[str]:
        """Generuje specjalistyczne hashtagi dla danej dziedziny"""
        
        base_hashtags = ["#MultiSafety", "#BezpieczeństwoPracy", "#Compliance"]
        
        specialized_hashtags = {
            "bhp_ppoz": [
                "#BHP", "#PPOŻ", "#ISO45001", "#PIP", "#SzkoleniaBHP", 
                "#OcenaRyzyka", "#BezpiecznaFirma", "#OchronaPracowników",
                "#PrewencjaWypadków", "#ZarządzanieBHP"
            ],
            "it_security": [
                "#RODO", "#Cyberbezpieczeństwo", "#ISO27001", "#IOD", 
                "#OchronaDanych", "#NIS2", "#Prywatność", "#ITSecurity",
                "#BezpieczeństwoIT", "#GDPR"
            ],
            "ce_marking": [
                "#ZnakCE", "#CEMarking", "#UE", "#Eksport", "#Certyfikacja",
                "#NormyEuropejskie", "#Zgodność", "#RynekUE", "#ISO9001",
                "#DokumentacjaTechniczna"
            ],
            "equipment_supervision": [
                "#DozórTechniczny", "#InstalacjeElektryczne", "#Energetyka",
                "#BezpieczeństwoTechniczne", "#PreglądyTechniczne", "#UDT",
                "#InstalacjeGazowe", "#UrządzeniaElektryczne"
            ]
        }
        
        spec_tags = specialized_hashtags.get(specialization, specialized_hashtags["bhp_ppoz"])
        
        # Combine base + specialized (random selection)
        selected_spec = random.sample(spec_tags, min(8, len(spec_tags)))
        
        return base_hashtags + selected_spec

    def _generate_ai_content(self, request: ContentRequest) -> GeneratedContent:
        """Generuje treść używając AI (OpenAI/Anthropic)"""
        
        prompt = self._create_ai_prompt(request)
        
        try:
            if self.openai_client:
                response = self.openai_client.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Jesteś ekspertem w tworzeniu treści marketingowych dla firm z branży bezpieczeństwa pracy."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1000,
                    temperature=0.7
                )
                content = response.choices[0].message.content
                
            elif self.anthropic_client:
                response = self.anthropic_client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1000,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                content = response.content[0].text
            else:
                raise Exception("No AI service available")
                
            return self._parse_ai_response(content, request.specialization)
            
        except Exception as e:
            print(f"AI generation failed: {e}")
            # Fallback to premium templates
            return self._generate_premium_template_content(request)
    
    def _create_ai_prompt(self, request: ContentRequest) -> str:
        """Tworzy prompt dla AI"""
        
        specialization_context = {
            "bhp_ppoz": "BHP (Bezpieczeństwo i Higiena Pracy) oraz PPOŻ (Przeciwpożarowe)",
            "it_security": "Bezpieczeństwo informacji, RODO, cyberbezpieczeństwo",
            "ce_marking": "Znak CE, certyfikacja produktów dla rynku UE",
            "equipment_supervision": "Dozór techniczny urządzeń i instalacji"
        }
        
        context = specialization_context.get(request.specialization, "bezpieczeństwo pracy")
        
        prompt = f"""Stwórz profesjonalny post na Instagram dla firmy MultiSafety.pl specjalizującej się w {context}.

Wymagania:
- Typ posta: {request.template_type}
- Temat: {request.custom_topic or 'ogólny'}
- Ton: profesjonalny, ekspertowski
- Grupa docelowa: CEO, kierownictwo firm
- Długość: 800-1200 znaków
- Zawiera konkretne liczby/statystyki
- Call-to-action z multisafety.pl
- 8-12 relevantnych hashtagów

Format odpowiedzi:
TYTUŁ: [tytuł postu]
HOOK: [pierwsze zdanie przyciągające uwagę]
TREŚĆ: [główna treść]
CTA: [call to action]
HASHTAGI: [lista hashtagów]"""

        return prompt
    
    def _parse_ai_response(self, content: str, specialization: str) -> GeneratedContent:
        """Parsuje odpowiedź AI"""
        
        lines = content.split('\n')
        
        title = ""
        hook = ""
        main_content = ""
        call_to_action = ""
        hashtags = []
        
        current_section = ""
        
        for line in lines:
            line = line.strip()
            if line.upper().startswith('TYTUŁ:'):
                title = line[6:].strip()
                current_section = "title"
            elif line.upper().startswith('HOOK:'):
                hook = line[5:].strip()
                current_section = "hook"
            elif line.upper().startswith('TREŚĆ:'):
                main_content = line[6:].strip()
                current_section = "content"
            elif line.upper().startswith('CTA:'):
                call_to_action = line[4:].strip()
                current_section = "cta"
            elif line.upper().startswith('HASHTAGI:'):
                hashtag_line = line[9:].strip()
                hashtags = [tag.strip() for tag in hashtag_line.split() if tag.startswith('#')]
                current_section = "hashtags"
            elif line and current_section == "content":
                main_content += "\n" + line
            elif line and current_section == "cta":
                call_to_action += "\n" + line
        
        # Fallback values
        if not title:
            title = "MultiSafety - Profesjonalne Rozwiązania"
        if not hook:
            hook = title
        if not main_content:
            main_content = content[:500] + "..."
        if not call_to_action:
            call_to_action = "🚀 Sprawdź: multisafety.pl"
        if not hashtags:
            hashtags = self._generate_specialized_hashtags(specialization)
        
        full_text = f"{main_content}\n\n{call_to_action}\n\n{' '.join(hashtags[:12])}"
        
        return GeneratedContent(
            title=title,
            hook=hook,
            main_content=main_content,
            call_to_action=call_to_action,
            hashtags=hashtags[:12],
            full_text=full_text
        )

# Global instance
ai_generator = AIContentGenerator()
