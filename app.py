"""
MultiSafety Content Creator - Enhanced v6.0
Profesjonalny generator treści Instagram dla multisafety.pl
"""

from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from ai_content_generator import ai_generator, ContentRequest
from enhanced_content_templates import ADVANCED_CONTENT_CATEGORIES, CANVA_EXPORT_FORMATS
from content_calendar import ContentCalendar, ScheduledPost, generate_content_report

# Ładowanie zmiennych środowiskowych
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize enhanced modules
content_calendar = ContentCalendar()

# ENHANCED MULTISAFETY SPECIALIZATIONS
MULTISAFETY_SPECIALIZATIONS = {
    "bhp_ppoz": {
        "name": "BHP i PPOŻ",
        "description": "Bezpieczeństwo i higiena pracy oraz przeciwpożarowe",
        "icon": "fas fa-hard-hat",
        "color": "#FF6B35",
        "keywords": ["BHP", "PPOŻ", "ISO 45001", "PIP", "szkolenia BHP", "ocena ryzyka"],
        "trending_topics": [
            "Nowe przepisy BHP 2025",
            "ISO 45001 - korzyści biznesowe",
            "Kary PIP - jak się chronić",
            "ROI inwestycji w BHP",
            "Digitalizacja dokumentacji BHP"
        ]
    },
    "it_security": {
        "name": "Cyberbezpieczeństwo i RODO",
        "description": "Ochrona danych, cyberbezpieczeństwo, zgodność z RODO",
        "icon": "fas fa-shield-alt",
        "color": "#2E86AB",
        "keywords": ["RODO", "cyberbezpieczeństwo", "ISO 27001", "IOD", "NIS2"],
        "trending_topics": [
            "NIS2 - nowe wymagania 2024",
            "AI Act i RODO - compliance",
            "Kary RODO - rekordy 2024",
            "Ransomware - ochrona firmy",
            "ISO 27001 - certyfikacja"
        ]
    },
    "ce_marking": {
        "name": "Znak CE i Eksport UE",
        "description": "Certyfikacja CE, dostęp do rynku europejskiego",
        "icon": "fas fa-certificate",
        "color": "#4ECDC4",
        "keywords": ["znak CE", "UE", "eksport", "certyfikacja", "normy europejskie"],
        "trending_topics": [
            "Cyber Resilience Act 2024",
            "Digital Product Passport",
            "CE dla produktów IT",
            "Nadzór rynku UE - statystyki",
            "Brexit a oznakowanie CE"
        ]
    },
    "equipment_supervision": {
        "name": "Dozór Urządzeń Technicznych",
        "description": "Dozór techniczny, instalacje, urządzenia pod ciśnieniem",
        "icon": "fas fa-tools",
        "color": "#96CEB4",
        "keywords": ["UDT", "dozór techniczny", "instalacje", "urządzenia"],
        "trending_topics": [
            "Nowe wymogi UDT 2024",
            "Instalacje wodorowe",
            "Energetyka odnawialna - dozór",
            "Digitalizacja przeglądów",
            "Heat pumps - wymagania"
        ]
    }
}

# ENHANCED POST TEMPLATES
ENHANCED_POST_TEMPLATES = {
    "tip": {
        "title": "💡 Ekspertowska Porada",
        "structure": "Statystyka + wyjaśnienie + korzyści + CTA",
        "engagement_boost": "+25%",
        "best_time": "Wtorek 8:00-9:00"
    },
    "warning": {
        "title": "⚠️ Ważne Ostrzeżenie",
        "structure": "Alarmujący fakt + konsekwencje + rozwiązanie + pilny CTA",
        "engagement_boost": "+40%",
        "best_time": "Poniedziałek 7:30-8:30"
    },
    "education": {
        "title": "📚 Profesjonalna Edukacja",
        "structure": "Problem branżowy + eksperckie wyjaśnienie + case study + CTA",
        "engagement_boost": "+30%",
        "best_time": "Środa 12:00-13:00"
    },
    "offer": {
        "title": "🔥 Ekskluzywna Oferta",
        "structure": "Value proposition + benefity + social proof + strong CTA",
        "engagement_boost": "+35%",
        "best_time": "Czwartek 17:00-18:00"
    },
    "case_study": {
        "title": "📊 Studium Przypadku",
        "structure": "Wyzwanie klienta + rozwiązanie + wyniki + lessons learned",
        "engagement_boost": "+45%",
        "best_time": "Piątek 10:00-11:00"
    },
    "industry_news": {
        "title": "📰 Aktualności Branżowe",
        "structure": "Breaking news + analiza eksperta + wpływ na biznes + CTA",
        "engagement_boost": "+20%",
        "best_time": "Poniedziałek 9:00-10:00"
    }
}

# CONTENT QUALITY METRICS
QUALITY_METRICS = {
    "engagement_factors": {
        "emoji_count": {"min": 3, "max": 8, "weight": 0.1},
        "hashtag_count": {"min": 8, "max": 12, "weight": 0.15},
        "char_count": {"min": 800, "max": 1200, "weight": 0.2},
        "cta_presence": {"weight": 0.2},
        "statistics_presence": {"weight": 0.25},
        "expertise_level": {"weight": 0.1}
    },
    "seo_factors": {
        "keyword_density": {"weight": 0.3},
        "hashtag_relevance": {"weight": 0.25},
        "brand_mention": {"weight": 0.2},
        "content_freshness": {"weight": 0.15},
        "call_to_action": {"weight": 0.1}
    }
}

@app.route('/')
def index():
    """Strona główna - Enhanced"""
    return render_template('index.html',
                          specializations=MULTISAFETY_SPECIALIZATIONS,
                          templates=ENHANCED_POST_TEMPLATES)

@app.route('/generate_post', methods=['POST'])
def generate_post():
    """Enhanced post generation z premium features"""
    try:
        data = request.json
        specialization = data.get('specialization')
        template_type = data.get('template')
        custom_topic = data.get('topic', '')

        # Validation
        if specialization not in MULTISAFETY_SPECIALIZATIONS:
            return jsonify({'error': 'Nieprawidłowa specjalizacja'}), 400

        if template_type not in ENHANCED_POST_TEMPLATES:
            return jsonify({'error': 'Nieprawidłowy typ posta'}), 400

        spec_data = MULTISAFETY_SPECIALIZATIONS[specialization]
        template_data = ENHANCED_POST_TEMPLATES[template_type]

        # Enhanced content request
        content_request = ContentRequest(
            specialization=specialization,
            content_type='post',
            template_type=template_type,
            custom_topic=custom_topic,
            tone='professional',
            target_audience='business_leaders'
        )

        # Generate content using enhanced AI
        generated_content = ai_generator.generate_post_content(content_request)

        # Calculate enhanced quality scores
        engagement_score = calculate_enhanced_engagement_score(
            generated_content, specialization, template_type
        )

        seo_score = calculate_enhanced_seo_score(
            generated_content, specialization
        )

        # Generate analytics predictions
        analytics = generate_analytics_prediction(
            generated_content, specialization, template_type
        )

        return jsonify({
            'content': {
                'title': generated_content.title,
                'hook': generated_content.hook,
                'content': generated_content.main_content,
                'call_to_action': generated_content.call_to_action,
                'full_text': generated_content.full_text
            },
            'hashtags': generated_content.hashtags,
            'specialization': spec_data['name'],
            'template_info': template_data,
            'quality_scores': {
                'engagement': engagement_score,
                'seo': seo_score,
                'expert_level': calculate_expert_level(specialization),
                'viral_potential': calculate_viral_potential(generated_content)
            },
            'analytics': analytics,
            'optimization_tips': generate_optimization_tips(generated_content),
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'error': f'Błąd generowania: {str(e)}'}), 500

def calculate_enhanced_engagement_score(content, specialization, template_type):
    """Zaawansowane wyliczanie engagement score"""
    base_score = 85

    # Template bonus
    template_bonuses = {
        "warning": 15, "case_study": 12, "offer": 10,
        "tip": 8, "education": 6, "industry_news": 5
    }
    base_score += template_bonuses.get(template_type, 0)

    # Content analysis
    text = content.full_text.lower()

    # Statistics presence (+8)
    if any(char.isdigit() for char in text) and '%' in text:
        base_score += 8

    # Emotional triggers (+6)
    triggers = ['alarmujące', 'rekordowy', 'drastyczny', 'nowość', 'ekskluzywny']
    if any(trigger in text for trigger in triggers):
        base_score += 6

    # Hashtag optimization (+5)
    if 8 <= len(content.hashtags) <= 12:
        base_score += 5

    # Length optimization (+4)
    if 800 <= len(content.full_text) <= 1200:
        base_score += 4

    # MultiSafety branding (+3)
    if 'multisafety' in text:
        base_score += 3

    return min(base_score, 99)

def calculate_enhanced_seo_score(content, specialization):
    """Zaawansowane wyliczanie SEO score"""
    base_score = 88

    # Keyword relevance
    spec_keywords = MULTISAFETY_SPECIALIZATIONS[specialization]['keywords']
    text = content.full_text.lower()

    keyword_matches = sum(1 for keyword in spec_keywords if keyword.lower() in text)
    base_score += min(keyword_matches * 2, 8)

    # Hashtag SEO value (+6)
    valuable_hashtags = ['#MultiSafety', '#BHP', '#RODO', '#ZnakCE', '#ISO45001']
    hashtag_value = sum(1 for tag in content.hashtags if tag in valuable_hashtags)
    base_score += min(hashtag_value * 2, 6)

    # Content freshness (+4)
    current_year = datetime.now().year
    if str(current_year) in text or str(current_year + 1) in text:
        base_score += 4

    return min(base_score, 98)

def calculate_expert_level(specialization):
    """Określa poziom ekspertyzy"""
    expert_levels = {
        "bhp_ppoz": "Premium Expert",
        "it_security": "Advanced Specialist",
        "ce_marking": "EU Compliance Expert",
        "equipment_supervision": "Technical Authority"
    }
    return expert_levels.get(specialization, "Professional")

def calculate_viral_potential(content):
    """Oblicza potencjał viralowy"""
    score = 0
    text = content.full_text.lower()

    # Shock value
    shock_words = ['alarmujące', '91%', 'rekordowy', 'drastyczny']
    score += sum(5 for word in shock_words if word in text)

    # Call to action strength
    if 'bezpłatny' in text or 'darmowy' in text:
        score += 8

    # Time urgency
    urgent_words = ['teraz', 'dziś', '24h', 'pilne']
    score += sum(3 for word in urgent_words if word in text)

    return min(score, 85)

def generate_analytics_prediction(content, specialization, template_type):
    """Generuje przewidywania analityczne"""

    base_reach = {
        "bhp_ppoz": 1200, "it_security": 950,
        "ce_marking": 800, "equipment_supervision": 650
    }

    template_multipliers = {
        "warning": 1.6, "case_study": 1.4, "offer": 1.3,
        "tip": 1.2, "education": 1.1, "industry_news": 1.0
    }

    estimated_reach = int(base_reach[specialization] * template_multipliers[template_type])
    estimated_engagement = int(estimated_reach * 0.07)  # 7% engagement rate

    return {
        "estimated_reach": f"{estimated_reach:,} - {int(estimated_reach * 1.5):,}",
        "estimated_likes": f"{int(estimated_engagement * 0.6):,} - {int(estimated_engagement * 0.8):,}",
        "estimated_comments": f"{int(estimated_engagement * 0.15):,} - {int(estimated_engagement * 0.25):,}",
        "estimated_shares": f"{int(estimated_engagement * 0.05):,} - {int(estimated_engagement * 0.1):,}",
        "best_posting_time": ENHANCED_POST_TEMPLATES[template_type]["best_time"],
        "engagement_boost": ENHANCED_POST_TEMPLATES[template_type]["engagement_boost"]
    }

def generate_optimization_tips(content):
    """Generuje tips optymalizacyjne"""
    tips = []

    text = content.full_text

    if len(text) < 800:
        tips.append("💡 Rozbuduj treść do 800-1200 znaków dla lepszego zasięgu")

    if len(content.hashtags) < 8:
        tips.append("🏷️ Dodaj więcej hashtagów (optimalnie 8-12)")

    if not any(char.isdigit() for char in text):
        tips.append("📊 Dodaj konkretne liczby/statystyki dla większej wiarygodności")

    if 'multisafety' not in text.lower():
        tips.append("🏢 Wzmocnij branding - dodaj wzmiankę o MultiSafety")

    emoji_count = sum(1 for char in text if ord(char) > 127)
    if emoji_count < 3:
        tips.append("😊 Dodaj emoji dla lepszego engagement (3-8 optimal)")

    if not tips:
        tips.append("✅ Post jest dobrze zoptymalizowany!")

    return tips

# API Endpoint for trending topics
@app.route('/api/trending_topics/<specialization>')
def get_trending_topics(specialization):
    """Zwraca trending topics dla specjalizacji"""
    if specialization in MULTISAFETY_SPECIALIZATIONS:
        topics = MULTISAFETY_SPECIALIZATIONS[specialization]['trending_topics']
        return jsonify({'trending_topics': topics})
    return jsonify({'error': 'Invalid specialization'}), 400

# Health check endpoint
@app.route('/health')
def health_check():
    """Health check dla aplikacji"""
    return jsonify({
        'status': 'healthy',
        'version': '6.0',
        'features': ['enhanced_ai', 'premium_templates', 'analytics_prediction'],
        'timestamp': datetime.now().isoformat()
    })

# === ENHANCED API ENDPOINTS ===

@app.route('/api/enhanced-content', methods=['POST'])
def generate_enhanced_content():
    """Generuj zaawansowaną treść z nowych szablonów"""
    try:
        data = request.get_json()
        category = data.get('category', 'case_studies')
        subcategory = data.get('subcategory', 'manufacturing')

        content_pool = ADVANCED_CONTENT_CATEGORIES.get(category, {}).get(subcategory, [])

        if content_pool:
            import random
            selected_content = random.choice(content_pool)

            # Parse content
            lines = selected_content.split('\n')
            title = lines[0] if lines else "Professional Content"

            # Extract hashtags from content
            hashtags = []
            for line in lines:
                if line.startswith('#'):
                    hashtags = [tag.strip() for tag in line.split() if tag.startswith('#')]
                    break

            # Generate Canva export data
            canva_data = {
                "format": "instagram_post",
                "dimensions": "1080x1080",
                "title": title.replace('📊', '').replace('🏭', '').strip(),
                "content_preview": selected_content[:200] + "...",
                "brand_colors": ["#667eea", "#764ba2", "#ffffff"]
            }

            return jsonify({
                'content': selected_content,
                'title': title,
                'hashtags': hashtags,
                'category': category,
                'subcategory': subcategory,
                'canva_export': canva_data,
                'engagement_prediction': 85 + (len(hashtags) * 5)
            })
        else:
            return jsonify({'error': 'Brak treści dla wybranej kategorii'})

    except Exception as e:
        return jsonify({'error': f'Błąd: {str(e)}'})

@app.route('/api/content-calendar', methods=['GET'])
def get_content_calendar():
    """Pobierz kalendarz treści"""
    try:
        year = int(request.args.get('year', datetime.now().year))
        month = int(request.args.get('month', datetime.now().month))

        schedule = content_calendar.get_monthly_schedule(year, month)
        optimal_times = content_calendar.suggest_optimal_times('instagram')

        return jsonify({
            'schedule': schedule,
            'optimal_times': optimal_times
        })

    except Exception as e:
        return jsonify({'error': f'Błąd kalendarza: {str(e)}'})

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Pobierz analitykę treści"""
    try:
        from datetime import timedelta

        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)

        report = generate_content_report(start_date, end_date)

        return jsonify(report)

    except Exception as e:
        return jsonify({'error': f'Błąd analityki: {str(e)}'})

if __name__ == '__main__':
    # Ensure directories exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)

    print("🛡️  MultiSafety Content Creator v6.0 - Enhanced")
    print("=" * 60)
    print("🎯 NOWE FUNKCJE:")
    print("   ✅ Premium AI content generation")
    print("   ✅ Enhanced analytics prediction")
    print("   ✅ Viral potential scoring")
    print("   ✅ SEO optimization tips")
    print("   ✅ Expert-level templates")
    print("🌐 URL: http://localhost:5002")
    print("📱 Profesjonalne treści dla multisafety.pl")
    print("=" * 60)

    app.run(debug=True, host='0.0.0.0', port=5002)
