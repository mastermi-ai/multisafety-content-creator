"""
PROFESSIONAL INSTAGRAM GRAPHICS - GOOGLE GEMINI AI LEVEL
Profesjonalne grafiki firmowe na poziomie multisafety.pl
Eliminuje potrzebę grafików - tworzy content godny firmowego Instagrama
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io
import base64
import os
import random
import math

class ProfessionalInstagramGraphics:
    """Generator profesjonalnych grafik firmowych na poziomie Google Gemini AI"""
    
    def __init__(self):
        self.load_professional_fonts()
        
        # PROFESJONALNE KOLORY FIRMOWE - inspirowane multisafety.pl
        self.professional_palettes = {
            'bhp_ppoz': {
                'primary': '#2C3E50',      # Profesjonalny granat
                'secondary': '#E74C3C',    # Bezpieczeństwo czerwony
                'accent': '#F39C12',       # Ostrzeżenie pomarańczowy
                'success': '#27AE60',      # Sukces zielony
                'dark': '#1A252F',         # Głęboki granat
                'light': '#FFFFFF',        # Czysta biel
                'gray': '#95A5A6',         # Profesjonalny szary
                'background': '#F8F9FA'    # Jasne tło
            },
            'it_security': {
                'primary': '#34495E',      # Cyber granat
                'secondary': '#3498DB',    # Tech niebieski
                'accent': '#E91E63',       # Cyber różowy
                'success': '#00BCD4',      # Cyjan
                'dark': '#2C3E50',         # Głęboki cyber
                'light': '#FFFFFF',
                'gray': '#7F8C8D',
                'background': '#F5F7FA'
            },
            'ce_marking': {
                'primary': '#2980B9',      # EU niebieski
                'secondary': '#F1C40F',    # Certyfikacja złoty
                'accent': '#E67E22',       # EU pomarańczowy
                'success': '#16A085',      # Zatwierdzenie zielony
                'dark': '#1B4F72',
                'light': '#FFFFFF',
                'gray': '#85929E',
                'background': '#F8F9FA'
            },
            'equipment_supervision': {
                'primary': '#27AE60',      # Przemysł zielony
                'secondary': '#F39C12',    # Przemysł pomarańczowy
                'accent': '#E74C3C',       # Niebezpieczeństwo czerwony
                'success': '#2ECC71',      # Bezpieczeństwo zielony
                'dark': '#145A32',
                'light': '#FFFFFF',
                'gray': '#7D6608',
                'background': '#F4F6F6'
            }
        }
        
        # PROFESJONALNE LAYOUTY FIRMOWE
        self.professional_layouts = [
            'corporate_clean',        # Czysty korporacyjny
            'business_report',        # Raport biznesowy
            'professional_card',      # Profesjonalna karta
            'executive_presentation', # Prezentacja executive
            'industry_standard',      # Standard branżowy
            'modern_business',        # Nowoczesny biznes
            'premium_corporate',      # Premium korporacyjny
            'expert_consultation'     # Konsultacja ekspercka
        ]

    def load_professional_fonts(self):
        """Załaduj profesjonalne czcionki firmowe"""
        self.fonts = {}
        
        # macOS professional fonts
        font_paths = {
            'title': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Arial.ttf",
                "/System/Library/Fonts/Futura.ttc"
            ],
            'subtitle': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Arial.ttf"
            ],
            'body': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Arial.ttf"
            ],
            'accent': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Arial.ttf"
            ]
        }
        
        for font_type, paths in font_paths.items():
            for path in paths:
                if os.path.exists(path):
                    try:
                        if font_type == 'title':
                            self.fonts[font_type] = ImageFont.truetype(path, 72)
                        elif font_type == 'subtitle':
                            self.fonts[font_type] = ImageFont.truetype(path, 48)
                        elif font_type == 'body':
                            self.fonts[font_type] = ImageFont.truetype(path, 36)
                        elif font_type == 'accent':
                            self.fonts[font_type] = ImageFont.truetype(path, 96)
                        break
                    except:
                        continue
        
        # Fallback fonts
        for font_type in font_paths.keys():
            if font_type not in self.fonts:
                self.fonts[font_type] = ImageFont.load_default()

    def generate_professional_image(self, specialization, hook_text, main_stat, call_to_action):
        """
        Generuje profesjonalną grafikę firmową na poziomie Google Gemini AI
        """
        
        layout = random.choice(self.professional_layouts)
        palette = self.professional_palettes.get(specialization, self.professional_palettes['bhp_ppoz'])
        
        # Utwórz profesjonalny canvas 1080x1080
        img = Image.new('RGB', (1080, 1080), palette['background'])
        
        # Generuj profesjonalny background według layoutu
        if layout == 'corporate_clean':
            img = self._create_corporate_clean(img, palette)
        elif layout == 'business_report':
            img = self._create_business_report(img, palette)
        elif layout == 'professional_card':
            img = self._create_professional_card(img, palette)
        elif layout == 'executive_presentation':
            img = self._create_executive_presentation(img, palette)
        elif layout == 'industry_standard':
            img = self._create_industry_standard(img, palette)
        elif layout == 'modern_business':
            img = self._create_modern_business(img, palette)
        elif layout == 'premium_corporate':
            img = self._create_premium_corporate(img, palette)
        else:  # expert_consultation
            img = self._create_expert_consultation(img, palette)
        
        # Dodaj profesjonalny content
        self._add_professional_content(img, hook_text, main_stat, call_to_action, palette, layout)
        
        # Profesjonalne post-processing
        img = self._apply_professional_effects(img)
        
        return img

    def _create_corporate_clean(self, img, palette):
        """Czysty korporacyjny design - minimalistyczny i profesjonalny"""
        draw = ImageDraw.Draw(img)
        
        # Czyste tło
        draw.rectangle([0, 0, 1080, 1080], fill=palette['background'])
        
        # Subtelny header z gradientem
        header_height = 200
        for y in range(header_height):
            factor = y / header_height
            color = self._interpolate_color(palette['primary'], palette['secondary'], factor)
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Profesjonalne linie akcentujące
        # Górna linia
        draw.line([(0, header_height), (1080, header_height)], fill=palette['accent'], width=3)
        
        # Centralna content area
        content_area = [80, header_height + 40, 1000, 800]
        
        # Subtelny shadow
        shadow_offset = 8
        shadow_area = [content_area[0] + shadow_offset, content_area[1] + shadow_offset,
                      content_area[2] + shadow_offset, content_area[3] + shadow_offset]
        draw.rectangle(shadow_area, fill=palette['gray'] + '20')
        
        # Main content box
        draw.rectangle(content_area, fill=palette['light'], outline=palette['primary'], width=2)
        
        # Subtelne linie wewnętrzne
        inner_margin = 30
        inner_rect = [content_area[0] + inner_margin, content_area[1] + inner_margin,
                     content_area[2] - inner_margin, content_area[3] - inner_margin]
        draw.rectangle(inner_rect, outline=palette['gray'] + '40', width=1)
        
        return img

    def _create_business_report(self, img, palette):
        """Raport biznesowy - profesjonalny i czytelny"""
        draw = ImageDraw.Draw(img)
        
        # Profesjonalne tło
        draw.rectangle([0, 0, 1080, 1080], fill=palette['light'])
        
        # Header z logo area
        header_height = 180
        
        # Header background
        draw.rectangle([0, 0, 1080, header_height], fill=palette['primary'])
        
        # Subtelny pattern w headerze
        for x in range(0, 1080, 40):
            draw.line([(x, 0), (x, header_height)], fill=palette['primary'] + '80', width=1)
        
        # Content sections
        sections = [
            [60, header_height + 30, 520, 750],  # Left section
            [560, header_height + 30, 1020, 750]  # Right section
        ]
        
        for section in sections:
            # Profesjonalne shadow
            shadow_offset = 6
            shadow_area = [section[0] + shadow_offset, section[1] + shadow_offset,
                          section[2] + shadow_offset, section[3] + shadow_offset]
            draw.rectangle(shadow_area, fill=palette['gray'] + '30')
            
            # Main section
            draw.rectangle(section, fill=palette['light'], outline=palette['primary'], width=2)
            
            # Section header
            section_header = [section[0], section[1], section[2], section[1] + 50]
            draw.rectangle(section_header, fill=palette['secondary'] + '20')
            draw.line([(section[0], section[1] + 50), (section[2], section[1] + 50)], 
                     fill=palette['secondary'], width=2)
        
        # Footer
        footer_y = 800
        draw.rectangle([0, footer_y, 1080, 1080], fill=palette['primary'])
        
        return img

    def _create_professional_card(self, img, palette):
        """Profesjonalna karta - clean i business-ready"""
        draw = ImageDraw.Draw(img)
        
        # Clean background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['background'])
        
        # Central card with professional proportions
        card_width = 900
        card_height = 700
        card_x = (1080 - card_width) // 2
        card_y = (1080 - card_height) // 2
        
        # Card shadow system
        for shadow in range(12, 0, -1):
            shadow_alpha = int(255 * shadow / 12 * 0.15)
            shadow_color = self._add_alpha_to_color(palette['dark'], shadow_alpha)
            
            shadow_coords = [card_x + shadow, card_y + shadow,
                            card_x + card_width + shadow, card_y + card_height + shadow]
            draw.rectangle(shadow_coords, fill=shadow_color)
        
        # Main card
        draw.rectangle([card_x, card_y, card_x + card_width, card_y + card_height],
                      fill=palette['light'], outline=palette['primary'], width=3)
        
        # Card header
        header_height = 80
        header_area = [card_x, card_y, card_x + card_width, card_y + header_height]
        draw.rectangle(header_area, fill=palette['primary'])
        
        # Subtelne linie w karcie
        line_y = card_y + header_height + 40
        draw.line([(card_x + 40, line_y), (card_x + card_width - 40, line_y)],
                 fill=palette['gray'] + '40', width=1)
        
        return img

    def _create_executive_presentation(self, img, palette):
        """Prezentacja executive - premium business level"""
        draw = ImageDraw.Draw(img)
        
        # Executive background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['light'])
        
        # Premium header
        header_height = 250
        
        # Multi-layer header
        for y in range(header_height):
            factor = y / header_height
            if y < header_height * 0.7:
                color = self._interpolate_color(palette['primary'], palette['secondary'], factor * 1.4)
            else:
                color = self._interpolate_color(palette['secondary'], palette['accent'], (factor - 0.7) * 3.3)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Executive content area
        content_start = header_height + 50
        content_area = [60, content_start, 1020, 950]
        
        # Professional shadow
        shadow_offset = 10
        shadow_area = [content_area[0] + shadow_offset, content_area[1] + shadow_offset,
                      content_area[2] + shadow_offset, content_area[3] + shadow_offset]
        draw.rectangle(shadow_area, fill=palette['dark'] + '20')
        
        # Main content
        draw.rectangle(content_area, fill=palette['light'], outline=palette['primary'], width=3)
        
        # Executive grid
        grid_spacing = 80
        for x in range(content_area[0], content_area[2], grid_spacing):
            draw.line([(x, content_start), (x, 950)], fill=palette['gray'] + '20', width=1)
        
        for y in range(content_start, 950, grid_spacing):
            draw.line([(60, y), (1020, y)], fill=palette['gray'] + '20', width=1)
        
        return img

    def _create_industry_standard(self, img, palette):
        """Standard branżowy - zgodny z normami przemysłowymi"""
        draw = ImageDraw.Draw(img)
        
        # Industry background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['background'])
        
        # Industry header
        header_height = 160
        
        # Solid industry header
        draw.rectangle([0, 0, 1080, header_height], fill=palette['primary'])
        
        # Industry pattern
        for i in range(0, 1080, 60):
            # Vertical industry lines
            draw.line([(i, 0), (i, header_height)], fill=palette['primary'] + '60', width=2)
        
        # Central industry focus
        center_x, center_y = 540, 540
        
        # Industry circle
        circle_radius = 300
        draw.ellipse([center_x - circle_radius, center_y - circle_radius,
                     center_x + circle_radius, center_y + circle_radius],
                    outline=palette['secondary'], width=4)
        
        # Industry grid
        grid_size = 100
        for x in range(center_x - circle_radius, center_x + circle_radius, grid_size):
            for y in range(center_y - circle_radius, center_y + circle_radius, grid_size):
                if (x - center_x)**2 + (y - center_y)**2 <= circle_radius**2:
                    draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=palette['accent'])
        
        return img

    def _create_modern_business(self, img, palette):
        """Nowoczesny biznes - contemporary design"""
        draw = ImageDraw.Draw(img)
        
        # Modern background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['light'])
        
        # Modern gradient header
        header_height = 220
        
        for y in range(header_height):
            factor = y / header_height
            # Modern gradient
            if factor < 0.5:
                color = self._interpolate_color(palette['primary'], palette['secondary'], factor * 2)
            else:
                color = self._interpolate_color(palette['secondary'], palette['accent'], (factor - 0.5) * 2)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Modern content layout
        # Left panel
        left_panel = [40, header_height + 40, 520, 900]
        draw.rectangle(left_panel, fill=palette['light'], outline=palette['primary'], width=2)
        
        # Right panel
        right_panel = [560, header_height + 40, 1040, 900]
        draw.rectangle(right_panel, fill=palette['light'], outline=palette['primary'], width=2)
        
        # Modern accent lines
        accent_y = header_height + 30
        draw.line([(0, accent_y), (1080, accent_y)], fill=palette['accent'], width=4)
        
        return img

    def _create_premium_corporate(self, img, palette):
        """Premium korporacyjny - luksusowy business design"""
        draw = ImageDraw.Draw(img)
        
        # Premium background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['background'])
        
        # Premium header with sophisticated design
        header_height = 280
        
        # Multi-layer premium header
        for y in range(header_height):
            factor = y / header_height
            
            # Sophisticated color progression
            if y < header_height * 0.4:
                color = self._interpolate_color(palette['primary'], palette['secondary'], factor * 2.5)
            elif y < header_height * 0.8:
                mid_factor = (y - header_height * 0.4) / (header_height * 0.4)
                color = self._interpolate_color(palette['secondary'], palette['accent'], mid_factor)
            else:
                bottom_factor = (y - header_height * 0.8) / (header_height * 0.2)
                color = self._interpolate_color(palette['accent'], palette['success'], bottom_factor)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Premium content area
        content_start = header_height + 60
        content_area = [80, content_start, 1000, 920]
        
        # Premium shadow system
        for shadow in range(15, 0, -1):
            shadow_alpha = int(255 * shadow / 15 * 0.12)
            shadow_color = self._add_alpha_to_color(palette['dark'], shadow_alpha)
            
            shadow_coords = [content_area[0] + shadow, content_area[1] + shadow,
                            content_area[2] + shadow, content_area[3] + shadow]
            draw.rectangle(shadow_coords, fill=shadow_color)
        
        # Main premium content
        draw.rectangle(content_area, fill=palette['light'], outline=palette['primary'], width=4)
        
        # Premium inner frame
        inner_margin = 40
        inner_rect = [content_area[0] + inner_margin, content_area[1] + inner_margin,
                     content_area[2] - inner_margin, content_area[3] - inner_margin]
        draw.rectangle(inner_rect, outline=palette['secondary'], width=2)
        
        return img

    def _create_expert_consultation(self, img, palette):
        """Konsultacja ekspercka - profesjonalny consulting design"""
        draw = ImageDraw.Draw(img)
        
        # Expert background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['light'])
        
        # Expert header
        header_height = 200
        
        # Professional header
        draw.rectangle([0, 0, 1080, header_height], fill=palette['primary'])
        
        # Expert accent elements
        # Top accent line
        draw.rectangle([0, 0, 1080, 8], fill=palette['accent'])
        
        # Side accents
        draw.rectangle([0, 0, 8, 1080], fill=palette['accent'])
        draw.rectangle([1072, 0, 1080, 1080], fill=palette['accent'])
        
        # Expert content area
        content_start = header_height + 40
        content_area = [60, content_start, 1020, 900]
        
        # Professional shadow
        shadow_offset = 8
        shadow_area = [content_area[0] + shadow_offset, content_area[1] + shadow_offset,
                      content_area[2] + shadow_offset, content_area[3] + shadow_offset]
        draw.rectangle(shadow_area, fill=palette['gray'] + '25')
        
        # Main expert content
        draw.rectangle(content_area, fill=palette['light'], outline=palette['primary'], width=3)
        
        # Expert consultation elements
        # Left consultation panel
        left_panel = [content_area[0] + 30, content_start + 30, content_area[0] + 450, 870]
        draw.rectangle(left_panel, fill=palette['background'], outline=palette['secondary'], width=2)
        
        # Right consultation panel
        right_panel = [content_area[0] + 480, content_start + 30, 990, 870]
        draw.rectangle(right_panel, fill=palette['background'], outline=palette['secondary'], width=2)
        
        return img

    def _add_professional_content(self, img, hook_text, main_stat, call_to_action, palette, layout):
        """Dodaj profesjonalny content z business typography"""
        draw = ImageDraw.Draw(img)
        
        # GŁÓWNA STATYSTYKA - business hero element
        if main_stat:
            # Extract number for professional display
            import re
            numbers = re.findall(r'\d+[\.,]?\d*', main_stat)
            if numbers:
                big_number = numbers[0]
                
                # Position based on layout
                if layout in ['corporate_clean', 'business_report']:
                    number_y = 120
                elif layout in ['executive_presentation', 'premium_corporate']:
                    number_y = 100
                else:
                    number_y = 140
                
                # Professional number display
                bbox = draw.textbbox((0, 0), big_number, font=self.fonts['accent'])
                text_width = bbox[2] - bbox[0]
                x = 540 - text_width // 2
                
                # Professional shadow
                draw.text((x + 3, number_y + 3), big_number, 
                         fill=palette['gray'], font=self.fonts['accent'])
                
                # Main number
                draw.text((x, number_y), big_number, fill=palette['primary'], font=self.fonts['accent'])
                
                # Professional unit/context
                unit_match = re.search(r'\d+[\.,]?\d*\s*([^0-9]+)', main_stat)
                if unit_match:
                    unit = unit_match.group(1).strip()
                    
                    unit_bbox = draw.textbbox((0, 0), unit, font=self.fonts['subtitle'])
                    unit_width = unit_bbox[2] - unit_bbox[0]
                    unit_x = 540 - unit_width // 2
                    unit_y = number_y + 120
                    
                    # Professional unit styling
                    draw.text((unit_x, unit_y), unit, fill=palette['secondary'], font=self.fonts['subtitle'])
        
        # HOOK TEXT - profesjonalny business message
        if hook_text:
            # Clean hook text
            clean_hook = self._clean_hook_text(hook_text)
            
            # Smart text positioning
            if layout in ['corporate_clean', 'business_report']:
                hook_y_start = 350
                max_width = 800
            elif layout in ['executive_presentation', 'premium_corporate']:
                hook_y_start = 320
                max_width = 850
            else:
                hook_y_start = 380
                max_width = 800
            
            # Professional text wrapping
            wrapped_lines = self._professional_wrap_text(clean_hook, self.fonts['body'], max_width)
            
            line_height = 60
            
            for i, line in enumerate(wrapped_lines[:4]):  # Max 4 lines
                bbox = draw.textbbox((0, 0), line, font=self.fonts['body'])
                text_width = bbox[2] - bbox[0]
                x = 540 - text_width // 2
                y = hook_y_start + i * line_height
                
                # Professional text with subtle shadow
                draw.text((x + 2, y + 2), line, fill=palette['gray'] + '40', font=self.fonts['body'])
                draw.text((x, y), line, fill=palette['dark'], font=self.fonts['body'])
        
        # CALL TO ACTION - profesjonalny business button
        if call_to_action:
            main_cta = call_to_action.split('\n')[0].strip()
            if main_cta.startswith('🚀 '):
                main_cta = main_cta[2:].strip()
            
            # CTA positioning
            cta_y = 800
            bbox = draw.textbbox((0, 0), main_cta, font=self.fonts['subtitle'])
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Professional button design
            button_padding_x = 40
            button_padding_y = 20
            button_width = text_width + 2 * button_padding_x
            button_height = text_height + 2 * button_padding_y
            
            button_x = 540 - button_width // 2
            button_y = cta_y - button_padding_y
            
            # Professional button shadow
            shadow_offset = 6
            draw.rectangle([button_x + shadow_offset, button_y + shadow_offset,
                           button_x + button_width + shadow_offset, 
                           button_y + button_height + shadow_offset],
                          fill=palette['gray'] + '30')
            
            # Main button
            draw.rectangle([button_x, button_y, button_x + button_width, button_y + button_height],
                          fill=palette['secondary'], outline=palette['primary'], width=3)
            
            # Button text
            text_x = button_x + button_padding_x
            text_y = button_y + button_padding_y
            draw.text((text_x, text_y), main_cta, fill=palette['light'], font=self.fonts['subtitle'])
        
        # Professional branding
        brand_text = "INŻYNIERIA BEZPIECZEŃSTWA"
        try:
            brand_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
        except:
            brand_font = self.fonts['body']
        
        bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
        brand_width = bbox[2] - bbox[0]
        brand_x = 1080 - brand_width - 40
        brand_y = 1080 - 50
        
        # Professional brand text
        draw.text((brand_x, brand_y), brand_text, fill=palette['gray'], font=brand_font)

    def _apply_professional_effects(self, img):
        """Profesjonalne post-processing dla business quality"""
        
        # 1. Subtle contrast enhancement
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.15)
        
        # 2. Professional color balance
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.05)
        
        # 3. Subtle sharpening
        img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))
        
        # 4. Professional brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.02)
        
        return img

    def _clean_hook_text(self, hook_text):
        """Clean hook text from emoji prefixes"""
        prefixes_to_remove = ['🚨 ', '📊 ', '⚠️ ', '💰 ', '🤖 ', '☁️ ', '📱 ', '🏦 ', '🔐 ', '🛡️ ', '🌐 ', '👥 ', '🇺🇸 ', '🇪🇺 ', '🌍 ', '💸 ', '⏱️ ']
        
        clean_text = hook_text
        for prefix in prefixes_to_remove:
            if clean_text.startswith(prefix):
                clean_text = clean_text[len(prefix):].strip()
                break
        
        return clean_text

    def _professional_wrap_text(self, text, font, max_width):
        """Professional text wrapping for business typography"""
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
                else:
                    lines.append(word)
                    current_line = ""
        
        if current_line:
            lines.append(current_line)
        
        return lines

    def _interpolate_color(self, color1, color2, factor):
        """Professional color interpolation"""
        factor = max(0, min(1, factor))
        
        try:
            if color1.startswith('#'):
                r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
            else:
                r1, g1, b1 = 128, 128, 128
                
            if color2.startswith('#'):
                r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
            else:
                r2, g2, b2 = 128, 128, 128
            
            r = int(r1 + (r2 - r1) * factor)
            g = int(g1 + (g2 - g1) * factor)
            b = int(b1 + (b2 - b1) * factor)
            
            return f'#{r:02x}{g:02x}{b:02x}'
        except:
            return '#666666'

    def _add_alpha_to_color(self, hex_color, alpha):
        """Add alpha channel to hex color"""
        try:
            r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
            return (r, g, b, alpha)
        except:
            return (128, 128, 128, alpha)

    def generate_image_base64(self, specialization, hook_text, main_stat, call_to_action="Skontaktuj się z nami!"):
        """Generate professional image and return as base64"""
        try:
            img = self.generate_professional_image(specialization, hook_text, main_stat, call_to_action)
            
            # Convert to base64 with professional quality
            img_io = io.BytesIO()
            img.save(img_io, 'PNG', quality=95, optimize=True)
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            
            return img_base64
            
        except Exception as e:
            print(f"Professional image generation error: {e}")
            return self._generate_professional_fallback()

    def _generate_professional_fallback(self):
        """Professional fallback image"""
        img = Image.new('RGB', (1080, 1080), '#F8F9FA')
        draw = ImageDraw.Draw(img)
        
        # Professional fallback design
        # Header
        draw.rectangle([0, 0, 1080, 200], fill='#2C3E50')
        
        # Content area
        content_area = [80, 240, 1000, 900]
        draw.rectangle(content_area, fill='#FFFFFF', outline='#2C3E50', width=3)
        
        # Professional text
        text = "Content Creator"
        subtitle = "Inżynieria Bezpieczeństwa"
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
            sub_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        except:
            title_font = self.fonts['title']
            sub_font = self.fonts['subtitle']
        
        # Title
        bbox = draw.textbbox((0, 0), text, font=title_font)
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 400
        
        draw.text((x, y), text, fill='#2C3E50', font=title_font)
        
        # Subtitle
        bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 520
        
        draw.text((x, y), subtitle, fill='#7F8C8D', font=sub_font)
        
        # Convert to base64
        img_io = io.BytesIO()
        img.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

# Create singleton instance
professional_instagram_graphics = ProfessionalInstagramGraphics()
