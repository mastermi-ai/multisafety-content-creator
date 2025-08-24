// Główny skrypt aplikacji Safety Content Creator
document.addEventListener('DOMContentLoaded', function () {
    initializeApp();
});

// currentImageData usunięte - obrazy wyłączone

function initializeApp() {
    // Inicjalizacja zakładek
    initializeTabs();

    // Inicjalizacja formularzy
    initializeForms();

    // Inicjalizacja animacji
    initializeAnimations();
}

// === OBSŁUGA ZAKŁADEK ===
function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function () {
            const targetTab = this.getAttribute('data-tab');

            // Usuń aktywne klasy
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Dodaj aktywne klasy
            this.classList.add('active');
            document.getElementById(targetTab).classList.add('active');

            // Animacja przejścia
            document.getElementById(targetTab).style.animation = 'fadeInUp 0.5s ease';
        });
    });
}

// === OBSŁUGA FORMULARZY ===
function initializeForms() {
    // Formularz postów
    const postForm = document.getElementById('postForm');
    if (postForm) {
        postForm.addEventListener('submit', handlePostGeneration);
    }

    // Formularz reelsów usunięty - skupiamy się na postach

    // Content tabs
    initializeContentTabs();
}

function initializeContentTabs() {
    const contentTabs = document.querySelectorAll('.content-tab');
    const contentPanels = document.querySelectorAll('.content-panel');

    contentTabs.forEach(tab => {
        tab.addEventListener('click', function () {
            const targetContent = this.getAttribute('data-content');

            // Remove active classes
            contentTabs.forEach(t => t.classList.remove('active'));
            contentPanels.forEach(p => p.classList.remove('active'));

            // Add active classes
            this.classList.add('active');
            document.getElementById(targetContent + 'Content').classList.add('active');
        });
    });
}

// === GENEROWANIE POSTÓW ===
async function handlePostGeneration(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    // Uproszczony formularz - tylko podstawowe pola
    const data = {
        specialization: formData.get('specialization'),
        template: formData.get('template'),
        topic: formData.get('topic') || '',
        // tone, audience, focus usunięte - uproszczony formularz
    };

    // Walidacja
    if (!data.specialization || !data.template) {
        showToast('Proszę wypełnić wszystkie wymagane pola', 'error');
        return;
    }

    try {
        showLoading(true);

        const response = await fetch('/generate_post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();

        if (result.error) {
            throw new Error(result.error);
        }

        displayPostResults(result);
        showToast('Post został wygenerowany pomyślnie!', 'success');

    } catch (error) {
        console.error('Błąd podczas generowania posta:', error);
        showToast('Wystąpił błąd podczas generowania posta: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

function displayPostResults(data) {
    // Obrazy wyłączone - skupiamy się na treściach tekstowych
    // currentImageData = data.image; // Usunięte

    // Wyświetl tekst
    const textElement = document.getElementById('postText');
    textElement.textContent = data.content.full_text;

    // Wyświetl hashtagi
    const hashtagsElement = document.getElementById('postHashtags');
    hashtagsElement.innerHTML = data.hashtags.map(tag => `<span>${tag}</span>`).join('');

    // Update quality indicators with dynamic values
    updateQualityIndicators(data);

    // Update target audience in analysis - domyślnie kierownictwo
    const targetAudienceElement = document.getElementById('targetAudience');
    if (targetAudienceElement) {
        targetAudienceElement.textContent = 'Kierownictwo (CEO/CFO)';
    }

    // Pokaż sekcję wyników
    const resultsSection = document.getElementById('postResults');
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });

    // Animacja
    resultsSection.style.animation = 'fadeInUp 0.6s ease';
}

function updateQualityIndicators(data) {
    // Calculate engagement score based on content quality
    const textLength = data.content.full_text.length;
    const hashtagCount = data.hashtags.length;
    const hasNumbers = /\d/.test(data.content.full_text);
    const hasEmojis = /[\p{Emoji}]/u.test(data.content.full_text);

    let engagementScore = 85;
    if (textLength > 200 && textLength < 500) engagementScore += 5;
    if (hashtagCount >= 6 && hashtagCount <= 10) engagementScore += 3;
    if (hasNumbers) engagementScore += 4;
    if (hasEmojis) engagementScore += 3;

    // Calculate SEO score
    let seoScore = 88;
    if (hashtagCount >= 8) seoScore += 4;
    if (data.content.full_text.includes('#')) seoScore += 3;
    if (textLength > 150) seoScore += 5;

    // Update display
    document.getElementById('engagementScore').textContent = Math.min(engagementScore, 99) + '%';
    document.getElementById('seoScore').textContent = Math.min(seoScore, 99) + '%';

    // Expert level based on specialization
    const expertLevels = {
        'BHP i PPOŻ': 'Expert',
        'IT Security': 'Premium',
        'CE Marking': 'Advanced',
        'Equipment Supervision': 'Professional'
    };

    document.getElementById('expertScore').textContent = expertLevels[data.specialization] || 'Premium';
}

// === GENEROWANIE REELSÓW ===
// Funkcja usunięta - skupiamy się na postach Instagram

// Funkcja displayReelResults usunięta - skupiamy się na postach Instagram

// === FUNKCJE POMOCNICZE ===
function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    overlay.style.display = show ? 'flex' : 'none';
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type}`;

    // Pokaż toast
    requestAnimationFrame(() => {
        toast.classList.add('show');
    });

    // Ukryj po 4 sekundach
    setTimeout(() => {
        toast.classList.remove('show');
    }, 4000);
}

function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;

    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showToast('Tekst został skopiowany do schowka!', 'success');
        }).catch(() => {
            fallbackCopyToClipboard(text);
        });
    } else {
        fallbackCopyToClipboard(text);
    }
}

function fallbackCopyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
        document.execCommand('copy');
        showToast('Tekst został skopiowany do schowka!', 'success');
    } catch (err) {
        showToast('Nie udało się skopiować tekstu', 'error');
    }

    document.body.removeChild(textArea);
}

// Funkcja downloadImage usunięta - obrazy wyłączone

function generateNew() {
    // Ukryj wyniki
    document.getElementById('postResults').style.display = 'none';

    // Wyczyść formularz (opcjonalnie)
    const customTopicField = document.getElementById('topic');
    if (customTopicField) {
        customTopicField.value = '';
    }

    // Przewiń do góry formularza
    document.querySelector('.form-section').scrollIntoView({ behavior: 'smooth' });

    showToast('Możesz wygenerować nowy post!', 'success');
}

// Funkcja generateNewReel usunięta - reelsy wyłączone

// Funkcja copyReelConcept usunięta - reelsy wyłączone

// === ANIMACJE ===
function initializeAnimations() {
    // Animacje przy przewijaniu
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease';
            }
        });
    }, observerOptions);

    // Obserwuj sekcje
    document.querySelectorAll('.form-section, .results-section').forEach(section => {
        observer.observe(section);
    });
}

// === OBSŁUGA BŁĘDÓW ===
window.addEventListener('error', function (event) {
    console.error('Błąd JavaScript:', event.error);
    showToast('Wystąpił nieoczekiwany błąd', 'error');
});

// === RESPONSIVE MENU (na potrzeby przyszłego rozwoju) ===
function initializeResponsiveFeatures() {
    // Obsługa orientacji urządzenia
    window.addEventListener('orientationchange', function () {
        setTimeout(() => {
            // Odśwież animacje po zmianie orientacji
            const activeTab = document.querySelector('.tab-content.active');
            if (activeTab) {
                activeTab.style.animation = 'fadeInUp 0.3s ease';
            }
        }, 100);
    });
}

// Inicjalizacja funkcji responsywnych
document.addEventListener('DOMContentLoaded', initializeResponsiveFeatures);

// === ENHANCED CONTENT FUNCTIONS ===
async function generateEnhancedContent(category, subcategory) {
    try {
        showLoading();

        const response = await fetch('/api/enhanced-content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                category: category,
                subcategory: subcategory
            })
        });

        const data = await response.json();

        if (data.error) {
            showToast(data.error, 'error');
            return;
        }

        // Display enhanced content
        displayEnhancedContent(data);

        hideLoading();
        showToast('Enhanced content wygenerowany!', 'success');

    } catch (error) {
        hideLoading();
        showToast('Błąd podczas generowania enhanced content', 'error');
    }
}

function displayEnhancedContent(data) {
    // Show result section
    const resultSection = document.getElementById('enhancedResult');
    resultSection.style.display = 'block';

    // Update content
    document.getElementById('enhancedContentText').innerHTML = data.content.replace(/\n/g, '<br>');

    // Update Canva data
    document.getElementById('canvaFormat').textContent = data.canva_export.format;
    document.getElementById('canvaDimensions').textContent = data.canva_export.dimensions;
    document.getElementById('canvaTitle').textContent = data.canva_export.title;

    // Update engagement prediction
    document.getElementById('engagementScore').textContent = data.engagement_prediction + '%';

    // Store data for export
    window.currentEnhancedContent = data;
}

function exportToCanva() {
    if (!window.currentEnhancedContent) {
        showToast('Brak treści do eksportu', 'error');
        return;
    }

    const canvaData = window.currentEnhancedContent.canva_export;

    // Create export object
    const exportData = {
        title: canvaData.title,
        content: window.currentEnhancedContent.content,
        brand_colors: canvaData.brand_colors,
        dimensions: canvaData.dimensions,
        format: canvaData.format
    };

    // Download as JSON for Canva import
    const blob = new Blob([JSON.stringify(exportData, null, 2)], {
        type: 'application/json'
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `multisafety_content_${Date.now()}.json`;
    a.click();

    URL.revokeObjectURL(url);

    showToast('Plik eksportowany do Canva!', 'success');
}

// === CALENDAR FUNCTIONS ===
async function loadCalendar() {
    try {
        showLoading();

        const response = await fetch('/api/content-calendar');
        const data = await response.json();

        if (data.error) {
            showToast(data.error, 'error');
            return;
        }

        displayCalendar(data);
        hideLoading();

    } catch (error) {
        hideLoading();
        showToast('Błąd podczas ładowania kalendarza', 'error');
    }
}

function displayCalendar(data) {
    // Update month display
    document.getElementById('currentMonth').textContent =
        `${data.schedule.month} ${data.schedule.year}`;

    // Update optimal times
    const timeSlotsContainer = document.getElementById('optimalTimes');
    timeSlotsContainer.innerHTML = '';

    data.optimal_times.forEach(time => {
        const timeSlot = document.createElement('span');
        timeSlot.className = 'time-slot';
        timeSlot.textContent = time;
        timeSlotsContainer.appendChild(timeSlot);
    });

    // Simple calendar grid display
    const calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerHTML = '';

    // Create simple calendar view
    for (let i = 1; i <= 30; i++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'calendar-day';
        dayElement.textContent = i;

        // Mark days with posts
        const hasPost = data.schedule.posts.some(post => post.day === i);
        if (hasPost) {
            dayElement.classList.add('has-post');
        }

        calendarGrid.appendChild(dayElement);
    }
}

// === ANALYTICS FUNCTIONS ===
async function loadAnalytics() {
    try {
        showLoading();

        const response = await fetch('/api/analytics');
        const data = await response.json();

        if (data.error) {
            showToast(data.error, 'error');
            return;
        }

        displayAnalytics(data);
        hideLoading();

    } catch (error) {
        hideLoading();
        showToast('Błąd podczas ładowania analityki', 'error');
    }
}

function displayAnalytics(data) {
    // Update metric cards
    document.getElementById('totalPosts').textContent = data.total_posts;
    document.getElementById('avgEngagement').textContent = data.avg_engagement_rate + '%';
    document.getElementById('followerGrowth').textContent = '+' + data.follower_growth;
    document.getElementById('leadsGenerated').textContent = data.consultation_requests;

    // Update top posts
    const topPostsContainer = document.getElementById('topPosts');
    topPostsContainer.innerHTML = '';

    data.top_performing_posts.forEach(post => {
        const postItem = document.createElement('div');
        postItem.className = 'post-item';
        postItem.innerHTML = `
            <span>${post.title}</span>
            <span>${post.engagement_rate}%</span>
        `;
        topPostsContainer.appendChild(postItem);
    });

    // Update best hashtags
    const hashtagsContainer = document.getElementById('bestHashtags');
    hashtagsContainer.innerHTML = '';

    data.best_hashtags.forEach(hashtag => {
        const hashtagItem = document.createElement('div');
        hashtagItem.className = 'hashtag-item';
        hashtagItem.innerHTML = `
            <span>${hashtag.hashtag}</span>
            <span>${hashtag.avg_engagement}</span>
        `;
        hashtagsContainer.appendChild(hashtagItem);
    });
}
