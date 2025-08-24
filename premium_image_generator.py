"""
PREMIUM IMAGE GENERATOR - AGENCY-LEVEL GRAPHICS
Eliminuje potrzebę grafików - tworzy content na poziomie najlepszych agencji
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io
import base64
import os
import random
import math
import textwrap

class PremiumImageGenerator:
    """Generator obrazów na poziomie premium agency"""
    
    def __init__(self):
        self.load_fonts()
        
        # PREMIUM DESIGN SYSTEMS - inspirowane najlepszymi brandami
        self.design_systems = {
            'bhp_ppoz': {
                'primary': '#FF6B35',      # Energetyczny pomarańcz
                'secondary': '#FFD700',    # Złoty akcent  
                'dark': '#1A1A1A',        # Głęboki czarny
                'light': '#FFFFFF',       # Czysta biel
                'gradient_start': '#FF6B35',
                'gradient_end': '#FFD700',
                'accent': '#E74C3C',      # Czerwony alarm
                'text_primary': '#FFFFFF',
                'text_secondary': '#1A1A1A'
            },
            'it_security': {
                'primary': '#00D4AA',      # Cyjan tech
                'secondary': '#667EEA',    # Fioletowy gradient
                'dark': '#0F1419',        # Tech dark
                'light': '#FFFFFF',
                'gradient_start': '#667EEA',
                'gradient_end': '#00D4AA',
                'accent': '#E91E63',      # Różowy alert
                'text_primary': '#FFFFFF',
                'text_secondary': '#0F1419'
            },
            'ce_marking': {
                'primary': '#4ECDC4',      # EU blue-green
                'secondary': '#F39C12',    # Pomarańczowy akcent
                'dark': '#2C3E50',        # Elegancki granat
                'light': '#FFFFFF',
                'gradient_start': '#4ECDC4',
                'gradient_end': '#F39C12',
                'accent': '#E74C3C',      # Czerwony
                'text_primary': '#FFFFFF',
                'text_secondary': '#2C3E50'
            },
            'equipment_supervision': {
                'primary': '#2ECC71',      # Zielony bezpieczeństwo
                'secondary': '#F1C40F',    # Żółty przemysł
                'dark': '#1C2833',        # Przemysłowy granat
                'light': '#FFFFFF',
                'gradient_start': '#2ECC71',
                'gradient_end': '#F1C40F',
                'accent': '#E74C3C',      # Czerwony danger
                'text_primary': '#FFFFFF',
                'text_secondary': '#1C2833'
            }
        }
        
        # PREMIUM LAYOUT TEMPLATES
        self.premium_layouts = [
            'magazine_cover',          # Jak okładka magazynu
            'corporate_presentation',  # Prezentacja korporacyjna
            'tech_startup',           # Nowoczesny startup
            'luxury_brand',           # Luksusowy brand
            'modern_minimalist',      # Minimalistyczny design
            'dynamic_energy',         # Dynamiczne energy
            'professional_report'     # Profesjonalny raport
        ]

    def load_fonts(self):
        """Załaduj premium fonts"""
        self.fonts = {}
        
        # macOS premium fonts
        font_paths = {
            'title': ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Arial.ttf"],
            'subtitle': ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Arial.ttf"],
            'body': ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Arial.ttf"],
            'accent': ["/System/Library/Fonts/Impact.ttf", "/System/Library/Fonts/Futura.ttc"]
        }
        
        for font_type, paths in font_paths.items():
            for path in paths:
                if os.path.exists(path):
                    try:
                        if font_type == 'title':
                            self.fonts[font_type] = ImageFont.truetype(path, 84)
                        elif font_type == 'subtitle':
                            self.fonts[font_type] = ImageFont.truetype(path, 56)
                        elif font_type == 'body':
                            self.fonts[font_type] = ImageFont.truetype(path, 42)
                        elif font_type == 'accent':
                            self.fonts[font_type] = ImageFont.truetype(path, 128)
                        break
                    except:
                        continue
        
        # Fallback fonts
        for font_type in ['title', 'subtitle', 'body', 'accent']:
            if font_type not in self.fonts:
                self.fonts[font_type] = ImageFont.load_default()

    def generate_premium_image(self, specialization, hook_text, main_stat, call_to_action):
        """
        Generuje premium-level obraz eliminujący potrzebę grafika
        """
        
        layout = random.choice(self.premium_layouts)
        colors = self.design_systems.get(specialization, self.design_systems['bhp_ppoz'])
        
        # Utwórz canvas 1080x1080
        img = Image.new('RGB', (1080, 1080), colors['dark'])
        
        # Generuj premium background
        if layout == 'magazine_cover':
            img = self._create_magazine_cover(img, colors)
        elif layout == 'corporate_presentation':
            img = self._create_corporate_presentation(img, colors)
        elif layout == 'tech_startup':
            img = self._create_tech_startup(img, colors)
        elif layout == 'luxury_brand':
            img = self._create_luxury_brand(img, colors)
        elif layout == 'modern_minimalist':
            img = self._create_modern_minimalist(img, colors)
        elif layout == 'dynamic_energy':
            img = self._create_dynamic_energy(img, colors)
        else:  # professional_report
            img = self._create_professional_report(img, colors)
        
        # Dodaj content z premium typography
        self._add_premium_content(img, hook_text, main_stat, call_to_action, colors, layout)
        
        # Premium post-processing
        img = self._apply_premium_effects(img)
        
        return img

    def _create_magazine_cover(self, img, colors):
        """Premium magazine cover design"""
        draw = ImageDraw.Draw(img)
        
        # Sophisticated gradient background
        for y in range(1080):
            factor = y / 1080
            # Create smooth gradient with multiple points
            if y < 300:
                # Top section - darker to lighter
                color = self._interpolate_color(colors['dark'], colors['primary'], factor * 2)
            elif y < 600:
                # Middle section - primary color
                mid_factor = (y - 300) / 300
                color = self._interpolate_color(colors['primary'], colors['secondary'], mid_factor)
            else:
                # Bottom section - lighter gradient
                bottom_factor = (y - 600) / 480
                color = self._interpolate_color(colors['secondary'], colors['light'], bottom_factor * 0.3)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Add premium geometric elements
        # Top accent bar
        draw.rectangle([0, 0, 1080, 20], fill=colors['accent'])
        
        # Side accent lines
        draw.rectangle([0, 0, 8, 1080], fill=colors['accent'])
        draw.rectangle([1072, 0, 1080, 1080], fill=colors['accent'])
        
        # Premium corner elements
        corner_size = 60
        for corner in [(0, 0), (1020, 0), (0, 1020), (1020, 1020)]:
            x, y = corner
            draw.rectangle([x, y, x + corner_size, y + corner_size], 
                          fill=colors['accent'], outline=colors['light'], width=3)
        
        return img

    def _create_corporate_presentation(self, img, colors):
        """Professional corporate design"""
        draw = ImageDraw.Draw(img)
        
        # Clean corporate background
        draw.rectangle([0, 0, 1080, 1080], fill=colors['dark'])
        
        # Header section with gradient
        for y in range(250):
            factor = y / 250
            color = self._interpolate_color(colors['primary'], colors['secondary'], factor)
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Premium content area with subtle shadow
        content_area = [60, 280, 1020, 820]
        # Shadow
        shadow_area = [65, 285, 1025, 825]
        draw.rectangle(shadow_area, fill='#00000040')
        # Main area
        draw.rectangle(content_area, fill=colors['light'], outline=colors['primary'], width=4)
        
        # Bottom accent bar
        draw.rectangle([0, 1060, 1080, 1080], fill=colors['accent'])
        
        return img

    def _create_tech_startup(self, img, colors):
        """Modern tech startup aesthetic"""
        draw = ImageDraw.Draw(img)
        
        # Dark tech background
        draw.rectangle([0, 0, 1080, 1080], fill=colors['dark'])
        
        # Diagonal tech elements
        for i in range(0, 1080, 120):
            # Create diagonal lines pattern
            start_x = i
            start_y = 0
            end_x = i + 60
            end_y = 1080
            
            # Create polygon for diagonal stripe
            points = [
                (start_x, start_y),
                (end_x, start_y),
                (end_x + 30, end_y),
                (start_x + 30, end_y)
            ]
            
            opacity = 0.1 if i % 240 == 0 else 0.05
            color_with_alpha = colors['primary'] + f"{int(opacity * 255):02x}"
            
            # Draw stripe
            stripe_img = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
            stripe_draw = ImageDraw.Draw(stripe_img)
            stripe_draw.polygon(points, fill=self._hex_to_rgba(colors['primary'], int(opacity * 255)))
            
            img = Image.alpha_composite(img.convert('RGBA'), stripe_img).convert('RGB')
        
        # Tech grid overlay
        grid_spacing = 40
        for x in range(0, 1080, grid_spacing):
            draw.line([(x, 0), (x, 1080)], fill=colors['primary'] + '20', width=1)
        for y in range(0, 1080, grid_spacing):
            draw.line([(0, y), (1080, y)], fill=colors['primary'] + '20', width=1)
        
        return img

    def _create_luxury_brand(self, img, colors):
        """Luxury brand aesthetic"""
        draw = ImageDraw.Draw(img)
        
        # Elegant gradient
        center_x, center_y = 540, 540
        max_radius = 600
        
        for radius in range(max_radius, 0, -5):
            factor = (max_radius - radius) / max_radius
            if factor < 0.3:
                color = self._interpolate_color(colors['dark'], colors['primary'], factor * 3)
            else:
                color = self._interpolate_color(colors['primary'], colors['secondary'], (factor - 0.3) * 1.4)
            
            draw.ellipse([center_x - radius, center_y - radius,
                         center_x + radius, center_y + radius], fill=color)
        
        # Luxury frame
        frame_width = 25
        draw.rectangle([0, 0, 1080, frame_width], fill=colors['accent'])
        draw.rectangle([0, 1080-frame_width, 1080, 1080], fill=colors['accent'])
        draw.rectangle([0, 0, frame_width, 1080], fill=colors['accent'])
        draw.rectangle([1080-frame_width, 0, 1080, 1080], fill=colors['accent'])
        
        # Corner decorations
        corner_size = 100
        for corner in [(frame_width, frame_width), (1080-frame_width-corner_size, frame_width), 
                      (frame_width, 1080-frame_width-corner_size), (1080-frame_width-corner_size, 1080-frame_width-corner_size)]:
            x, y = corner
            # Create ornate corner
            draw.line([(x, y), (x + corner_size, y)], fill=colors['secondary'], width=3)
            draw.line([(x, y), (x, y + corner_size)], fill=colors['secondary'], width=3)
            draw.line([(x + 20, y + 20), (x + corner_size - 20, y + 20)], fill=colors['light'], width=2)
            draw.line([(x + 20, y + 20), (x + 20, y + corner_size - 20)], fill=colors['light'], width=2)
        
        return img

    def _create_modern_minimalist(self, img, colors):
        """Clean minimalist design"""
        draw = ImageDraw.Draw(img)
        
        # Clean background
        draw.rectangle([0, 0, 1080, 1080], fill=colors['light'])
        
        # Minimalist accent elements
        # Top accent
        draw.rectangle([0, 0, 1080, 8], fill=colors['primary'])
        
        # Side accent
        draw.rectangle([0, 0, 8, 1080], fill=colors['primary'])
        
        # Central focus area with subtle shadow
        focus_area = [150, 200, 930, 880]
        # Subtle shadow
        shadow_area = [155, 205, 935, 885]
        draw.rectangle(shadow_area, fill='#00000010')
        
        # Clean geometric shapes
        # Circle element
        circle_center = (200, 200)
        circle_radius = 80
        draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                     circle_center[0] + circle_radius, circle_center[1] + circle_radius],
                    fill=colors['primary'], outline=colors['secondary'], width=4)
        
        # Rectangle element
        rect_area = [850, 850, 1000, 1000]
        draw.rectangle(rect_area, fill=colors['secondary'], outline=colors['accent'], width=3)
        
        return img

    def _create_dynamic_energy(self, img, colors):
        """Dynamic energy design"""
        draw = ImageDraw.Draw(img)
        
        # Dynamic gradient background
        for y in range(1080):
            for x in range(1080):
                # Create wave pattern
                wave1 = math.sin(x * 0.01) * 50
                wave2 = math.cos(y * 0.008) * 30
                
                distance_from_center = math.sqrt((x - 540)**2 + (y - 540)**2)
                factor = (distance_from_center + wave1 + wave2) / 800
                factor = max(0, min(1, factor))
                
                if factor < 0.3:
                    color = self._interpolate_color(colors['primary'], colors['secondary'], factor * 3)
                elif factor < 0.7:
                    color = self._interpolate_color(colors['secondary'], colors['accent'], (factor - 0.3) * 2.5)
                else:
                    color = self._interpolate_color(colors['accent'], colors['dark'], (factor - 0.7) * 3)
                
                # Only draw every 4th pixel for performance
                if x % 4 == 0 and y % 4 == 0:
                    draw.rectangle([x, y, x+4, y+4], fill=color)
        
        # Energy burst lines
        center = (540, 540)
        for angle in range(0, 360, 15):
            rad = math.radians(angle)
            start_dist = 100
            end_dist = 400
            
            x1 = center[0] + start_dist * math.cos(rad)
            y1 = center[1] + start_dist * math.sin(rad)
            x2 = center[0] + end_dist * math.cos(rad)
            y2 = center[1] + end_dist * math.sin(rad)
            
            draw.line([(x1, y1), (x2, y2)], fill=colors['light'], width=3)
        
        return img

    def _create_professional_report(self, img, colors):
        """Professional report design"""
        draw = ImageDraw.Draw(img)
        
        # Professional background
        draw.rectangle([0, 0, 1080, 1080], fill=colors['light'])
        
        # Header section
        header_height = 200
        draw.rectangle([0, 0, 1080, header_height], fill=colors['primary'])
        
        # Content area with grid
        content_start = header_height + 40
        content_area = [40, content_start, 1040, 1040]
        draw.rectangle(content_area, fill=colors['light'], outline=colors['dark'], width=2)
        
        # Professional grid
        grid_spacing = 60
        for i, x in enumerate(range(40, 1040, grid_spacing)):
            alpha = 0.3 if i % 2 == 0 else 0.1
            line_color = self._hex_to_rgba(colors['dark'], int(alpha * 255))
            
            # Convert to PIL-compatible format
            if x < 1040:
                draw.line([(x, content_start), (x, 1040)], fill=colors['dark'] + '30', width=1)
        
        for i, y in enumerate(range(content_start, 1040, grid_spacing)):
            alpha = 0.3 if i % 2 == 0 else 0.1
            
            if y < 1040:
                draw.line([(40, y), (1040, y)], fill=colors['dark'] + '30', width=1)
        
        # Footer accent
        draw.rectangle([0, 1060, 1080, 1080], fill=colors['secondary'])
        
        return img

    def _add_premium_content(self, img, hook_text, main_stat, call_to_action, colors, layout):
        """Dodaj content z premium typography"""
        draw = ImageDraw.Draw(img)
        
        # GŁÓWNA STATYSTYKA - hero element
        if main_stat:
            # Extract number for dramatic display
            import re
            numbers = re.findall(r'\d+[\.,]?\d*', main_stat)
            if numbers:
                big_number = numbers[0]
                
                # Position based on layout
                if layout in ['magazine_cover', 'luxury_brand']:
                    number_y = 120
                elif layout in ['corporate_presentation', 'professional_report']:
                    number_y = 80
                else:
                    number_y = 100
                
                # Create dramatic number display
                bbox = draw.textbbox((0, 0), big_number, font=self.fonts['accent'])
                text_width = bbox[2] - bbox[0]
                x = (1080 - text_width) // 2
                
                # Shadow effect for depth
                shadow_offset = 6
                draw.text((x + shadow_offset, number_y + shadow_offset), big_number, 
                         fill='#00000060', font=self.fonts['accent'])
                
                # Main number in accent color
                draw.text((x, number_y), big_number, fill=colors['accent'], font=self.fonts['accent'])
                
                # Add unit/context below number if exists
                unit_match = re.search(r'\d+[\.,]?\d*\s*([^0-9]+)', main_stat)
                if unit_match:
                    unit = unit_match.group(1).strip()
                    unit_bbox = draw.textbbox((0, 0), unit, font=self.fonts['subtitle'])
                    unit_width = unit_bbox[2] - unit_bbox[0]
                    unit_x = (1080 - unit_width) // 2
                    
                    draw.text((unit_x, number_y + 140), unit, fill=colors['text_primary'], font=self.fonts['subtitle'])
        
        # HOOK TEXT - main message
        if hook_text:
            # Clean and wrap text
            clean_hook = hook_text.replace('🚨 ', '').replace('📊 ', '').replace('⚠️ ', '').replace('💰 ', '')
            
            # Smart text wrapping
            wrapped_lines = self._smart_wrap_text(clean_hook, self.fonts['body'], 900)
            
            # Position based on layout
            if layout in ['magazine_cover', 'luxury_brand']:
                hook_y_start = 350
            elif layout in ['corporate_presentation']:
                hook_y_start = 320
            elif layout in ['professional_report']:
                hook_y_start = 300
            else:
                hook_y_start = 380
            
            line_height = 65
            
            for i, line in enumerate(wrapped_lines[:4]):  # Max 4 lines
                bbox = draw.textbbox((0, 0), line, font=self.fonts['body'])
                text_width = bbox[2] - bbox[0]
                x = (1080 - text_width) // 2
                y = hook_y_start + i * line_height
                
                # Text with subtle shadow for readability
                draw.text((x + 2, y + 2), line, fill='#00000040', font=self.fonts['body'])
                draw.text((x, y), line, fill=colors['text_primary'], font=self.fonts['body'])
        
        # CALL TO ACTION - premium button design
        if call_to_action:
            # Extract main CTA
            main_cta = call_to_action.split('\n')[0].strip()
            if main_cta.startswith('🚀 '):
                main_cta = main_cta[2:].strip()
            
            # Position CTA
            cta_y = 850
            bbox = draw.textbbox((0, 0), main_cta, font=self.fonts['subtitle'])
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Button dimensions
            button_padding_x = 40
            button_padding_y = 20
            button_width = text_width + 2 * button_padding_x
            button_height = text_height + 2 * button_padding_y
            
            button_x = (1080 - button_width) // 2
            button_y = cta_y - button_padding_y
            
            # Button shadow
            shadow_offset = 4
            draw.rectangle([button_x + shadow_offset, button_y + shadow_offset, 
                           button_x + button_width + shadow_offset, button_y + button_height + shadow_offset],
                          fill='#00000030')
            
            # Button background
            draw.rectangle([button_x, button_y, button_x + button_width, button_y + button_height],
                          fill=colors['secondary'], outline=colors['accent'], width=3)
            
            # Button text
            text_x = button_x + button_padding_x
            text_y = button_y + button_padding_y
            draw.text((text_x, text_y), main_cta, fill=colors['text_secondary'], font=self.fonts['subtitle'])
        
        # Add subtle branding
        brand_text = "INŻYNIERIA BEZPIECZEŃSTWA"
        brand_font_size = 28
        try:
            brand_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", brand_font_size)
        except:
            brand_font = self.fonts['body']
        
        bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
        brand_width = bbox[2] - bbox[0]
        brand_x = 1080 - brand_width - 30
        brand_y = 1080 - 40
        
        draw.text((brand_x, brand_y), brand_text, fill=colors['text_primary'] + '80', font=brand_font)

    def _apply_premium_effects(self, img):
        """Premium post-processing effects"""
        
        # Professional contrast enhancement
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2)
        
        # Color saturation boost
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.15)
        
        # Subtle sharpening
        img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
        
        # Professional brightness adjustment
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.05)
        
        return img

    def _smart_wrap_text(self, text, font, max_width):
        """Intelligent text wrapping for premium typography"""
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
                    # Word too long, force break
                    lines.append(word)
                    current_line = ""
        
        if current_line:
            lines.append(current_line)
        
        return lines

    def _interpolate_color(self, color1, color2, factor):
        """Smooth color interpolation"""
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

    def _hex_to_rgba(self, hex_color, alpha):
        """Convert hex to RGBA"""
        try:
            r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
            return (r, g, b, alpha)
        except:
            return (128, 128, 128, alpha)

    def generate_image_base64(self, specialization, hook_text, main_stat, call_to_action="Skontaktuj się z nami!"):
        """Generate premium image and return as base64"""
        try:
            img = self.generate_premium_image(specialization, hook_text, main_stat, call_to_action)
            
            # Convert to base64
            img_io = io.BytesIO()
            img.save(img_io, 'PNG', quality=98, optimize=True)
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            
            return img_base64
            
        except Exception as e:
            print(f"Premium image generation error: {e}")
            return self._generate_fallback_image()

    def _generate_fallback_image(self):
        """Premium fallback image"""
        img = Image.new('RGB', (1080, 1080), '#1A1A1A')
        draw = ImageDraw.Draw(img)
        
        # Premium fallback design
        # Gradient background
        for y in range(1080):
            factor = y / 1080
            r = int(26 + (255 - 26) * factor * 0.3)
            g = int(26 + (107 - 26) * factor * 0.3)
            b = int(26 + (53 - 26) * factor * 0.3)
            draw.line([(0, y), (1080, y)], fill=f'#{r:02x}{g:02x}{b:02x}')
        
        # Professional text
        text = "Content Creator"
        subtitle = "Inżynieria Bezpieczeństwa"
        
        # Title
        bbox = draw.textbbox((0, 0), text, font=self.fonts['title'])
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 400
        
        draw.text((x + 3, y + 3), text, fill='#00000080', font=self.fonts['title'])
        draw.text((x, y), text, fill='#FF6B35', font=self.fonts['title'])
        
        # Subtitle
        bbox = draw.textbbox((0, 0), subtitle, font=self.fonts['subtitle'])
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 520
        
        draw.text((x, y), subtitle, fill='#FFFFFF', font=self.fonts['subtitle'])
        
        # Convert to base64
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

# Create singleton instance
premium_image_generator = PremiumImageGenerator()
