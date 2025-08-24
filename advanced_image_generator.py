"""
ADVANCED IMAGE GENERATOR - VIRAL READY GRAPHICS
Tworzenie przyciągających wzrok obrazów Instagram gotowych do viral
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io
import base64
import os
import random
import math

class ViralImageGenerator:
    """Generator obrazów gotowych do viral na Instagram"""
    
    def __init__(self):
        self.fonts_loaded = False
        self.load_fonts()
        
        # VIRAL COLOR SCHEMES - psychologia kolorów dla engagement
        self.viral_schemes = {
            'bhp_ppoz': {
                'primary': ['#FF6B35', '#FF8E53', '#FFA500'],  # Energetyczne pomarańcze
                'secondary': ['#FFD700', '#FFF8DC', '#FFEB3B'],  # Złote akcenty
                'danger': ['#E74C3C', '#C0392B', '#FF1744'],  # Czerwone alarmy
                'background': ['#1A1A1A', '#2C3E50', '#34495E']  # Ciemne, profesjonalne
            },
            'it_security': {
                'primary': ['#00D4AA', '#00BCD4', '#4ECDC4'],  # Cyjan/turkus tech
                'secondary': ['#667EEA', '#764BA2', '#9B59B6'],  # Fioletowe gradients
                'danger': ['#E91E63', '#FF5722', '#F44336'],  # Różowe/czerwone alerty
                'background': ['#0F1419', '#1E3A8A', '#111827']  # Tech dark blue
            },
            'ce_marking': {
                'primary': ['#4ECDC4', '#45B7D1', '#96CEB4'],  # EU blues/greens
                'secondary': ['#F39C12', '#E67E22', '#D35400'],  # Pomarańczowe akcenty
                'danger': ['#E74C3C', '#8E44AD', '#9B59B6'],  # Fioletowo-czerwone
                'background': ['#2C3E50', '#34495E', '#1B2631']  # Eleganckie szare
            },
            'equipment_supervision': {
                'primary': ['#2ECC71', '#27AE60', '#16A085'],  # Zielone "bezpieczne"
                'secondary': ['#F1C40F', '#F39C12', '#E67E22'],  # Żółto-pomarańczowe
                'danger': ['#E74C3C', '#C0392B', '#A93226'],  # Czerwone niebezpieczeństwo
                'background': ['#1C2833', '#273746', '#212F3D']  # Przemysłowe granat
            }
        }
        
        # VIRAL LAYOUTS - sprawdzone układy na wysokie engagement
        self.viral_layouts = [
            'split_dramatic',      # Podział 70/30 z dramatycznym kontrastem
            'centered_burst',      # Centralny element z promieniami
            'diagonal_impact',     # Układ diagonalny z mocnym akcentem
            'grid_modern',         # Nowoczesna siatka z przestrzenią
            'circle_focus',        # Okrągły focus point
            'triangle_power',      # Trójkąty - psychologia mocy
            'waves_dynamic'        # Dynamiczne fale
        ]

    def load_fonts(self):
        """Załaduj czcionki systemowe"""
        self.fonts = {}
        try:
            # macOS system fonts
            font_paths = [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Arial.ttf", 
                "/System/Library/Fonts/Impact.ttf",
                "/System/Library/Fonts/Futura.ttc"
            ]
            
            for path in font_paths:
                if os.path.exists(path):
                    self.fonts['title'] = ImageFont.truetype(path, 72)
                    self.fonts['subtitle'] = ImageFont.truetype(path, 48)
                    self.fonts['body'] = ImageFont.truetype(path, 36)
                    self.fonts['caption'] = ImageFont.truetype(path, 24)
                    break
            
            if not self.fonts:
                # Fallback do default font
                self.fonts = {
                    'title': ImageFont.load_default(),
                    'subtitle': ImageFont.load_default(),
                    'body': ImageFont.load_default(),
                    'caption': ImageFont.load_default()
                }
                
        except Exception as e:
            print(f"Font loading error: {e}")
            self.fonts = {
                'title': ImageFont.load_default(),
                'subtitle': ImageFont.load_default(),
                'body': ImageFont.load_default(),
                'caption': ImageFont.load_default()
            }

    def generate_viral_image(self, specialization, hook_text, main_stat, call_to_action):
        """
        Generuje viral-ready obraz Instagram
        
        Args:
            specialization: Klucz specjalizacji (bhp_ppoz, it_security, etc.)
            hook_text: Główny hook przyciągający uwagę
            main_stat: Kluczowa statystyka/liczba
            call_to_action: Wezwanie do działania
        """
        
        # Wybierz losowy viral layout
        layout = random.choice(self.viral_layouts)
        colors = self.viral_schemes.get(specialization, self.viral_schemes['bhp_ppoz'])
        
        # Utwórz obraz 1080x1080
        img = Image.new('RGB', (1080, 1080), '#000000')
        draw = ImageDraw.Draw(img)
        
        # Generuj background według wybranego layoutu
        if layout == 'split_dramatic':
            img = self._create_split_dramatic(img, draw, colors)
        elif layout == 'centered_burst':
            img = self._create_centered_burst(img, draw, colors)
        elif layout == 'diagonal_impact':
            img = self._create_diagonal_impact(img, draw, colors)
        elif layout == 'grid_modern':
            img = self._create_grid_modern(img, draw, colors)
        elif layout == 'circle_focus':
            img = self._create_circle_focus(img, draw, colors)
        elif layout == 'triangle_power':
            img = self._create_triangle_power(img, draw, colors)
        else:  # waves_dynamic
            img = self._create_waves_dynamic(img, draw, colors)
        
        # Odśwież draw object po zmianach background
        draw = ImageDraw.Draw(img)
        
        # Dodaj content - VIRAL TEXT PLACEMENT
        self._add_viral_text(draw, hook_text, main_stat, call_to_action, colors, layout)
        
        # Dodaj viral elements (emoji, icons, shapes)
        self._add_viral_elements(draw, colors, specialization)
        
        # Post-processing effects
        img = self._apply_viral_effects(img)
        
        return img

    def _create_split_dramatic(self, img, draw, colors):
        """Dramatyczny podział z gradientem"""
        # Gradient background
        for y in range(1080):
            factor = y / 1080
            if y < 540:  # Górna połowa
                color = self._interpolate_color(colors['background'][0], colors['primary'][0], factor * 2)
            else:  # Dolna połowa
                color = self._interpolate_color(colors['primary'][0], colors['secondary'][0], (factor - 0.5) * 2)
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Diagonal split line
        points = [(0, 400), (1080, 600), (1080, 650), (0, 450)]
        draw.polygon(points, fill=colors['danger'][0])
        
        return img

    def _create_centered_burst(self, img, draw, colors):
        """Centralny burst z promieniami"""
        center_x, center_y = 540, 540
        
        # Radial gradient background
        for radius in range(0, 800, 5):
            factor = radius / 800
            color = self._interpolate_color(colors['primary'][0], colors['background'][0], factor)
            draw.ellipse([center_x - radius, center_y - radius, 
                         center_x + radius, center_y + radius], fill=color)
        
        # Burst rays
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = center_x + 200 * math.cos(rad)
            y1 = center_y + 200 * math.sin(rad)
            x2 = center_x + 400 * math.cos(rad)
            y2 = center_y + 400 * math.sin(rad)
            draw.line([(x1, y1), (x2, y2)], fill=colors['secondary'][0], width=8)
        
        return img

    def _create_diagonal_impact(self, img, draw, colors):
        """Diagonal impact layout"""
        # Diagonal sections
        points1 = [(0, 0), (800, 0), (600, 1080), (0, 1080)]
        draw.polygon(points1, fill=colors['primary'][0])
        
        points2 = [(800, 0), (1080, 0), (1080, 1080), (600, 1080)]
        draw.polygon(points2, fill=colors['secondary'][0])
        
        # Accent triangle
        points3 = [(700, 200), (900, 400), (700, 600)]
        draw.polygon(points3, fill=colors['danger'][0])
        
        return img

    def _create_grid_modern(self, img, draw, colors):
        """Nowoczesna siatka"""
        # Grid background
        grid_size = 180
        for x in range(0, 1080, grid_size):
            for y in range(0, 1080, grid_size):
                color_idx = ((x // grid_size) + (y // grid_size)) % 3
                if color_idx == 0:
                    color = colors['primary'][0]
                elif color_idx == 1:
                    color = colors['secondary'][0]
                else:
                    color = colors['background'][0]
                
                draw.rectangle([x, y, x + grid_size - 10, y + grid_size - 10], 
                              fill=color, outline=colors['danger'][0], width=3)
        
        return img

    def _create_circle_focus(self, img, draw, colors):
        """Okrągły focus point"""
        # Background gradient
        for radius in range(540, 0, -10):
            factor = (540 - radius) / 540
            color = self._interpolate_color(colors['background'][0], colors['primary'][0], factor)
            draw.ellipse([540 - radius, 540 - radius, 540 + radius, 540 + radius], fill=color)
        
        # Focus circle
        draw.ellipse([340, 340, 740, 740], fill=colors['secondary'][0], outline=colors['danger'][0], width=15)
        
        return img

    def _create_triangle_power(self, img, draw, colors):
        """Trójkąty - psychologia mocy"""
        # Background
        draw.rectangle([0, 0, 1080, 1080], fill=colors['background'][0])
        
        # Large triangles
        triangles = [
            [(0, 0), (540, 540), (0, 1080)],      # Lewy
            [(1080, 0), (1080, 1080), (540, 540)],  # Prawy
            [(540, 0), (1080, 540), (0, 540)]       # Górny
        ]
        
        colors_list = [colors['primary'][0], colors['secondary'][0], colors['danger'][0]]
        for i, triangle in enumerate(triangles):
            draw.polygon(triangle, fill=colors_list[i])
        
        return img

    def _create_waves_dynamic(self, img, draw, colors):
        """Dynamiczne fale"""
        # Wave background
        for y in range(0, 1080, 20):
            wave_offset = 50 * math.sin(y * 0.01)
            points = []
            for x in range(0, 1080, 10):
                wave_y = y + wave_offset * math.sin(x * 0.02)
                points.append((x, wave_y))
            
            color_factor = (y % 300) / 300
            color = self._interpolate_color(colors['primary'][0], colors['secondary'][0], color_factor)
            
            # Draw wave segment
            if len(points) > 1:
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i + 1]], fill=color, width=25)
        
        return img

    def _add_viral_text(self, draw, hook_text, main_stat, call_to_action, colors, layout):
        """Dodaj tekst w viral-friendly sposób"""
        
        # GŁÓWNA STATYSTYKA - największa, najbardziej widoczna
        if main_stat:
            # Wyciągnij liczbę ze statystyki
            import re
            numbers = re.findall(r'\d+(?:[\.,]\d+)*', main_stat)
            if numbers:
                big_number = numbers[0]
                
                # Gigantyczna liczba na środku/górze
                bbox = draw.textbbox((0, 0), big_number, font=self.fonts['title'])
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                x = (1080 - text_width) // 2
                y = 150 if layout in ['split_dramatic', 'diagonal_impact'] else 200
                
                # Shadow effect
                draw.text((x + 5, y + 5), big_number, fill='#000000', font=self.fonts['title'])
                # Main text
                draw.text((x, y), big_number, fill=colors['danger'][0], font=self.fonts['title'])
        
        # HOOK TEXT - przyciągający wzrok
        if hook_text:
            # Podziel na linie i znajdź najważniejsze słowa
            words = hook_text.split()
            important_words = []
            
            # Szukaj ważnych słów (liczby, %, EUR, zł, etc.)
            for word in words:
                if any(char.isdigit() for char in word) or word in ['EUR', 'zł', '%', 'mln', 'tys']:
                    important_words.append(word)
            
            # Tekst hook w środkowej części
            lines = self._wrap_text(hook_text, self.fonts['subtitle'], 800)
            y_start = 400 if layout in ['centered_burst', 'circle_focus'] else 500
            
            for i, line in enumerate(lines[:3]):  # Max 3 linie
                bbox = draw.textbbox((0, 0), line, font=self.fonts['subtitle'])
                text_width = bbox[2] - bbox[0]
                x = (1080 - text_width) // 2
                y = y_start + i * 60
                
                # Shadow
                draw.text((x + 3, y + 3), line, fill='#00000080', font=self.fonts['subtitle'])
                # Main text
                draw.text((x, y), line, fill='#FFFFFF', font=self.fonts['subtitle'])
        
        # CALL TO ACTION - dolna część
        if call_to_action:
            # Wyciągnij pierwszą linię CTA
            cta_lines = call_to_action.split('\n')
            main_cta = cta_lines[0] if cta_lines else call_to_action
            
            bbox = draw.textbbox((0, 0), main_cta, font=self.fonts['body'])
            text_width = bbox[2] - bbox[0]
            x = (1080 - text_width) // 2
            y = 850
            
            # CTA background box
            padding = 20
            draw.rectangle([x - padding, y - padding, x + text_width + padding, y + 50 + padding],
                          fill=colors['secondary'][0], outline=colors['danger'][0], width=4)
            
            # CTA text
            draw.text((x, y), main_cta, fill='#000000', font=self.fonts['body'])

    def _add_viral_elements(self, draw, colors, specialization):
        """Dodaj viral elements (ikony, kształty, akcenty)"""
        
        # Emoji/ikony w zależności od specjalizacji
        icons = {
            'bhp_ppoz': ['⚠️', '🚨', '⛑️', '🔥', '📊'],
            'it_security': ['🔒', '🛡️', '💻', '🚨', '⚡'],
            'ce_marking': ['✅', '🇪🇺', '📋', '🔍', '⭐'],
            'equipment_supervision': ['⚡', '🔧', '📊', '🏭', '🔍']
        }
        
        spec_icons = icons.get(specialization, icons['bhp_ppoz'])
        
        # Dodaj ikony w narożnikach
        positions = [(50, 50), (980, 50), (50, 980), (980, 980)]
        for i, pos in enumerate(positions[:3]):  # Max 3 ikony
            if i < len(spec_icons):
                # Ikona tło
                draw.ellipse([pos[0] - 30, pos[1] - 30, pos[0] + 30, pos[1] + 30],
                           fill=colors['secondary'][0], outline=colors['danger'][0], width=5)
                
                # Emoji można dodać jako tekst (uproszczone)
                icon = spec_icons[i]
                bbox = draw.textbbox((0, 0), icon, font=self.fonts['body'])
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                draw.text((pos[0] - text_width//2, pos[1] - text_height//2), 
                         icon, fill='#000000', font=self.fonts['body'])

    def _apply_viral_effects(self, img):
        """Zastosuj efekty post-processing dla viral appeal"""
        
        # Zwiększ kontrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.3)
        
        # Zwiększ nasycenie kolorów
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.2)
        
        # Lekkie wyostrzenie
        img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
        
        return img

    def _interpolate_color(self, color1, color2, factor):
        """Interpoluj między dwoma kolorami hex"""
        try:
            if isinstance(color1, str) and color1.startswith('#'):
                r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
            else:
                r1, g1, b1 = color1 if isinstance(color1, tuple) else (255, 255, 255)
                
            if isinstance(color2, str) and color2.startswith('#'):
                r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
            else:
                r2, g2, b2 = color2 if isinstance(color2, tuple) else (0, 0, 0)
            
            r = int(r1 + (r2 - r1) * factor)
            g = int(g1 + (g2 - g1) * factor)
            b = int(b1 + (b2 - b1) * factor)
            
            return f'#{r:02x}{g:02x}{b:02x}'
        except:
            return '#666666'  # Fallback color

    def _wrap_text(self, text, font, max_width):
        """Podziel tekst na linie"""
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            bbox = ImageDraw.Draw(Image.new('RGB', (1, 1))).textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines

    def generate_image_base64(self, specialization, hook_text, main_stat, call_to_action="Skontaktuj się z nami!"):
        """Generuj obraz i zwróć jako base64"""
        try:
            img = self.generate_viral_image(specialization, hook_text, main_stat, call_to_action)
            
            # Konwertuj do base64
            img_io = io.BytesIO()
            img.save(img_io, 'PNG', quality=95)
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            
            return img_base64
            
        except Exception as e:
            print(f"Image generation error: {e}")
            # Fallback - prosty obraz
            return self._generate_fallback_image(specialization, hook_text)

    def _generate_fallback_image(self, specialization, hook_text):
        """Prosty fallback obraz"""
        img = Image.new('RGB', (1080, 1080), '#667eea')
        draw = ImageDraw.Draw(img)
        
        # Prosty tekst
        text = "Safety Content Creator"
        bbox = draw.textbbox((0, 0), text, font=self.fonts['title'])
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 400
        
        draw.text((x, y), text, fill='white', font=self.fonts['title'])
        
        # Base64
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

# Singleton instance
viral_image_generator = ViralImageGenerator()
