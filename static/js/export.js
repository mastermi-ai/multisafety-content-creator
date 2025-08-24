/**
 * Dodatkowe funkcje eksportu dla Safety Content Creator
 */

// Eksport do formatów Instagram
function exportToInstagramStory() {
    if (!currentImageData) {
        showToast('Brak obrazu do eksportu', 'error');
        return;
    }
    
    // Konwersja do formatu Instagram Story (1080x1920)
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 1080;
    canvas.height = 1920;
    
    const img = new Image();
    img.onload = function() {
        // Wypełnij tło gradientem
        const gradient = ctx.createLinearGradient(0, 0, 0, 1920);
        gradient.addColorStop(0, '#667eea');
        gradient.addColorStop(1, '#764ba2');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, 1080, 1920);
        
        // Narysuj oryginalny obraz na środku
        const imageSize = 800;
        const x = (1080 - imageSize) / 2;
        const y = (1920 - imageSize) / 2;
        ctx.drawImage(img, x, y, imageSize, imageSize);
        
        // Dodaj tekst na dole
        ctx.fillStyle = 'white';
        ctx.font = 'bold 32px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('INŻYNIERIA BEZPIECZEŃSTWA', 540, 1800);
        ctx.font = '24px Arial';
        ctx.fillText('Więcej na multisafety.pl', 540, 1840);
        
        // Pobierz obraz
        const link = document.createElement('a');
        link.download = `safety-story-${Date.now()}.png`;
        link.href = canvas.toDataURL();
        link.click();
        
        showToast('Instagram Story pobrana!', 'success');
    };
    img.src = `data:image/png;base64,${currentImageData}`;
}

function exportPostWithHashtags() {
    const postText = document.getElementById('postText');
    const hashtags = document.getElementById('postHashtags');
    
    if (!postText || !hashtags) {
        showToast('Brak treści do eksportu', 'error');
        return;
    }
    
    const fullText = postText.textContent;
    const hashtagText = Array.from(hashtags.children)
        .map(span => span.textContent)
        .join(' ');
    
    const completePost = `${fullText}\n\n${hashtagText}\n\n📧 Kontakt: multisafety.pl\n#InżynieriaBezpieczeństwa #Eksperci`;
    
    // Skopiuj do schowka
    if (navigator.clipboard) {
        navigator.clipboard.writeText(completePost).then(() => {
            showToast('Kompletny post skopiowany z hashtagami!', 'success');
        });
    } else {
        fallbackCopyToClipboard(completePost);
    }
}

function generateMultipleSizes() {
    if (!currentImageData) {
        showToast('Brak obrazu do eksportu', 'error');
        return;
    }
    
    const sizes = [
        { name: 'Instagram Post', width: 1080, height: 1080 },
        { name: 'Instagram Story', width: 1080, height: 1920 },
        { name: 'Facebook Post', width: 1200, height: 630 },
        { name: 'LinkedIn Post', width: 1200, height: 627 }
    ];
    
    const img = new Image();
    img.onload = function() {
        sizes.forEach(size => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = size.width;
            canvas.height = size.height;
            
            // Tło gradientowe
            const gradient = ctx.createLinearGradient(0, 0, 0, size.height);
            gradient.addColorStop(0, '#667eea');
            gradient.addColorStop(1, '#764ba2');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, size.width, size.height);
            
            // Skalowanie obrazu
            const scale = Math.min(size.width / 1080, size.height / 1080) * 0.8;
            const scaledWidth = 1080 * scale;
            const scaledHeight = 1080 * scale;
            const x = (size.width - scaledWidth) / 2;
            const y = (size.height - scaledHeight) / 2;
            
            ctx.drawImage(img, x, y, scaledWidth, scaledHeight);
            
            // Pobierz obraz
            const link = document.createElement('a');
            link.download = `safety-${size.name.toLowerCase().replace(' ', '-')}-${Date.now()}.png`;
            link.href = canvas.toDataURL();
            link.click();
        });
        
        showToast('Wszystkie formaty pobrane!', 'success');
    };
    img.src = `data:image/png;base64,${currentImageData}`;
}

// Eksport harmonogramu postów
function exportContentCalendar() {
    const specializations = ['bhp_ppoz', 'it_security', 'ce_marking', 'equipment_supervision'];
    const templates = ['tip', 'warning', 'education', 'offer'];
    
    let calendar = 'HARMONOGRAM TREŚCI - SAFETY CONTENT CREATOR\n';
    calendar += '=' * 60 + '\n\n';
    
    const currentDate = new Date();
    
    for (let week = 0; week < 4; week++) {
        calendar += `TYDZIEŃ ${week + 1}\n`;
        calendar += '-' * 20 + '\n';
        
        for (let day = 0; day < 7; day++) {
            const date = new Date(currentDate);
            date.setDate(date.getDate() + (week * 7) + day);
            
            const spec = specializations[day % specializations.length];
            const template = templates[day % templates.length];
            
            calendar += `${date.toLocaleDateString('pl-PL')}: `;
            calendar += `${getSpecializationName(spec)} - ${getTemplateName(template)}\n`;
        }
        calendar += '\n';
    }
    
    calendar += 'HASHTAGI PODSTAWOWE:\n';
    calendar += '#InżynieriaBezpieczeństwa #Eksperci #Konsultacje #BezpłatnaWycena\n\n';
    
    calendar += 'NAJLEPSZE GODZINY PUBLIKACJI:\n';
    calendar += '- Poniedziałek-Piątek: 8:00, 12:00, 17:00\n';
    calendar += '- Weekend: 10:00, 15:00\n\n';
    
    calendar += 'Wygenerowano: ' + new Date().toLocaleString('pl-PL');
    
    // Pobierz jako plik tekstowy
    const blob = new Blob([calendar], { type: 'text/plain;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `harmonogram-treści-${Date.now()}.txt`;
    link.click();
    
    showToast('Harmonogram treści pobrany!', 'success');
}

function getSpecializationName(key) {
    const names = {
        'bhp_ppoz': 'BHP i PPOŻ',
        'it_security': 'IT Security',
        'ce_marking': 'Znak CE',
        'equipment_supervision': 'Dozór Urządzeń'
    };
    return names[key] || 'Bezpieczeństwo';
}

function getTemplateName(key) {
    const names = {
        'tip': 'Porada',
        'warning': 'Ostrzeżenie',
        'education': 'Edukacja',
        'offer': 'Oferta'
    };
    return names[key] || 'Post';
}

// Dodaj przyciski eksportu do interfejsu
document.addEventListener('DOMContentLoaded', function() {
    // Dodaj dodatkowe przyciski eksportu po wygenerowaniu posta
    const originalDisplayResults = displayPostResults;
    window.displayPostResults = function(data) {
        originalDisplayResults(data);
        addExportButtons();
    };
});

function addExportButtons() {
    const actionButtons = document.querySelector('.action-buttons');
    if (!actionButtons) return;
    
    // Sprawdź czy przyciski już istnieją
    if (actionButtons.querySelector('.btn-export-story')) return;
    
    // Przycisk Instagram Story
    const storyBtn = document.createElement('button');
    storyBtn.className = 'btn-export-story';
    storyBtn.innerHTML = '<i class="fas fa-mobile-alt"></i> Instagram Story';
    storyBtn.onclick = exportToInstagramStory;
    storyBtn.style.borderColor = '#E4405F';
    storyBtn.style.color = '#E4405F';
    
    // Przycisk wielokrotny eksport
    const multiBtn = document.createElement('button');
    multiBtn.className = 'btn-export-multi';
    multiBtn.innerHTML = '<i class="fas fa-images"></i> Wszystkie Formaty';
    multiBtn.onclick = generateMultipleSizes;
    multiBtn.style.borderColor = '#1877F2';
    multiBtn.style.color = '#1877F2';
    
    // Przycisk harmonogram
    const calendarBtn = document.createElement('button');
    calendarBtn.className = 'btn-export-calendar';
    calendarBtn.innerHTML = '<i class="fas fa-calendar"></i> Harmonogram';
    calendarBtn.onclick = exportContentCalendar;
    calendarBtn.style.borderColor = '#0077B5';
    calendarBtn.style.color = '#0077B5';
    
    actionButtons.appendChild(storyBtn);
    actionButtons.appendChild(multiBtn);
    actionButtons.appendChild(calendarBtn);
}
