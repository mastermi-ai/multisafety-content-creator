"""
ULTRA-PREMIUM GRAPHICS ENGINE - ŚWIATOWY POZIOM
Eliminuje WSZYSTKICH grafików - tworzy content na poziomie Nike, Apple, Tesla
Inspirowane najlepszymi kampaniami Instagram 2024/2025
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io
import base64
import os
import random
import math

class UltraPremiumGraphics:
    """Generator grafik na poziomie światowych marek"""
    
    def __init__(self):
        self.load_premium_fonts()
        
        # ULTRA-PREMIUM COLOR PALETTES - inspirowane luksusowymi markami
        self.ultra_palettes = {
            'bhp_ppoz': {
                'primary': '#FF6B35',           # Dynamic Orange
                'secondary': '#FFD700',        # Luxury Gold
                'accent1': '#FF4444',          # Power Red
                'accent2': '#00F5FF',          # Electric Blue
                'dark': '#0A0A0A',             # Deep Black
                'light': '#FFFFFF',           # Pure White
                'shadow': '#000000',          # True Black
                'gradient_start': '#FF6B35',
                'gradient_mid': '#FFD700',
                'gradient_end': '#FF4444'
            },
            'it_security': {
                'primary': '#00D4AA',          # Tech Cyan
                'secondary': '#667EEA',        # Neural Purple
                'accent1': '#FF0080',          # Neon Pink
                'accent2': '#00FF41',          # Matrix Green
                'dark': '#000814',             # Space Black
                'light': '#F8F9FA',           # Tech White
                'shadow': '#000000',
                'gradient_start': '#667EEA',
                'gradient_mid': '#00D4AA',
                'gradient_end': '#FF0080'
            },
            'ce_marking': {
                'primary': '#4ECDC4',          # EU Turquoise
                'secondary': '#FFE66D',        # Euro Gold
                'accent1': '#FF6B9D',          # EU Pink
                'accent2': '#95E1D3',          # Mint Green
                'dark': '#2C3E50',             # EU Navy
                'light': '#FFFFFF',
                'shadow': '#000000',
                'gradient_start': '#4ECDC4',
                'gradient_mid': '#FFE66D',
                'gradient_end': '#FF6B9D'
            },
            'equipment_supervision': {
                'primary': '#2ECC71',          # Safety Green
                'secondary': '#F39C12',        # Industrial Orange
                'accent1': '#E74C3C',          # Danger Red
                'accent2': '#3498DB',          # Industry Blue
                'dark': '#1B2631',             # Industrial Black
                'light': '#ECF0F1',           # Steel White
                'shadow': '#000000',
                'gradient_start': '#2ECC71',
                'gradient_mid': '#F39C12',
                'gradient_end': '#E74C3C'
            }
        }
        
        # ULTRA-PREMIUM DESIGN SYSTEMS
        self.design_systems = [
            'luxury_magazine',      # Vogue/GQ level
            'tech_keynote',        # Apple keynote style
            'social_viral',        # Instagram viral format
            'corporate_elite',     # Fortune 500 presentation
            'startup_unicorn',     # Silicon Valley startup
            'fashion_editorial',   # High-fashion magazine
            'automotive_premium',  # Tesla/Mercedes level
            'fintech_modern'       # Banking/crypto elite
        ]

    def load_premium_fonts(self):
        """Załaduj najbardziej premium fonts dostępne w systemie"""
        self.fonts = {}
        
        # macOS premium fonts - najwyższa jakość
        font_hierarchy = {
            'title_hero': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Futura.ttc", 
                "/Library/Fonts/Arial.ttf"
            ],
            'subtitle_bold': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/Avenir.ttc",
                "/Library/Fonts/Arial.ttf"
            ],
            'body_premium': [
                "/System/Library/Fonts/Helvetica.ttc",
                "/System/Library/Fonts/SFProDisplay.ttf",
                "/Library/Fonts/Arial.ttf"
            ],
            'accent_impact': [
                "/System/Library/Fonts/Impact.ttf",
                "/System/Library/Fonts/Futura.ttc",
                "/System/Library/Fonts/Helvetica.ttc"
            ]
        }
        
        # Load fonts with premium sizes
        for font_type, paths in font_hierarchy.items():
            for path in paths:
                if os.path.exists(path):
                    try:
                        if font_type == 'title_hero':
                            self.fonts[font_type] = ImageFont.truetype(path, 96)  # Massive title
                        elif font_type == 'subtitle_bold':
                            self.fonts[font_type] = ImageFont.truetype(path, 64)  # Strong subtitle
                        elif font_type == 'body_premium':
                            self.fonts[font_type] = ImageFont.truetype(path, 48)  # Premium body
                        elif font_type == 'accent_impact':
                            self.fonts[font_type] = ImageFont.truetype(path, 144) # Ultra impact
                        break
                    except:
                        continue
        
        # Fallback system
        for font_type in font_hierarchy.keys():
            if font_type not in self.fonts:
                self.fonts[font_type] = ImageFont.load_default()

    def generate_ultra_premium_image(self, specialization, hook_text, main_stat, call_to_action):
        """
        Generuje ultra-premium obraz na poziomie światowych marek
        """
        
        design_system = random.choice(self.design_systems)
        palette = self.ultra_palettes.get(specialization, self.ultra_palettes['bhp_ppoz'])
        
        # Utwórz ultra-premium canvas 1080x1080
        img = Image.new('RGB', (1080, 1080), palette['dark'])
        
        # Generuj background według wybranego systemu
        if design_system == 'luxury_magazine':
            img = self._create_luxury_magazine(img, palette)
        elif design_system == 'tech_keynote':
            img = self._create_tech_keynote(img, palette)
        elif design_system == 'social_viral':
            img = self._create_social_viral(img, palette)
        elif design_system == 'corporate_elite':
            img = self._create_corporate_elite(img, palette)
        elif design_system == 'startup_unicorn':
            img = self._create_startup_unicorn(img, palette)
        elif design_system == 'fashion_editorial':
            img = self._create_fashion_editorial(img, palette)
        elif design_system == 'automotive_premium':
            img = self._create_automotive_premium(img, palette)
        else:  # fintech_modern
            img = self._create_fintech_modern(img, palette)
        
        # Dodaj ultra-premium content
        self._add_ultra_premium_content(img, hook_text, main_stat, call_to_action, palette, design_system)
        
        # Ultra-premium post-processing
        img = self._apply_ultra_premium_effects(img)
        
        return img

    def _create_luxury_magazine(self, img, palette):
        """Luxury magazine cover - Vogue/GQ level"""
        draw = ImageDraw.Draw(img)
        
        # Ultra-sophisticated multi-layer gradient
        center_x, center_y = 540, 540
        
        # Create multiple radial gradients for depth
        for layer in range(3):
            for radius in range(600, 50, -8):
                factor = (600 - radius) / 550
                
                if layer == 0:  # Base layer
                    color = self._ultra_interpolate_color(palette['dark'], palette['primary'], factor * 0.4)
                elif layer == 1:  # Middle layer
                    if factor > 0.6:
                        color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], (factor - 0.6) * 2.5)
                    else:
                        continue
                else:  # Top layer
                    if factor > 0.8:
                        color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], (factor - 0.8) * 5)
                    else:
                        continue
                
                # Add subtle alpha blending
                alpha = int(255 * (0.3 + 0.7 * factor)) if layer > 0 else 255
                
                # Create circular gradient with soft edges
                offset_x = layer * 20 - 20
                offset_y = layer * 15 - 15
                
                draw.ellipse([center_x - radius + offset_x, center_y - radius + offset_y,
                             center_x + radius + offset_x, center_y + radius + offset_y], 
                            fill=color)
        
        # Add luxury frame elements
        # Golden ratio rectangles
        phi = 1.618
        frame_width = int(1080 / phi / phi)  # ~400px
        
        # Top luxury accent
        draw.rectangle([0, 0, 1080, 25], fill=palette['accent1'])
        draw.rectangle([0, 25, 1080, 35], fill=palette['secondary'])
        
        # Luxury side accents with golden ratio
        draw.rectangle([0, 0, 15, 1080], fill=palette['secondary'])
        draw.rectangle([1065, 0, 1080, 1080], fill=palette['secondary'])
        
        # Premium corner elements with glow effect
        corner_size = 120
        for corner in [(30, 30), (930, 30), (30, 930), (930, 930)]:
            x, y = corner
            
            # Create glow effect
            for glow_radius in range(20, 0, -2):
                glow_alpha = int(255 * (20 - glow_radius) / 20 * 0.3)
                glow_color = self._add_alpha_to_color(palette['accent2'], glow_alpha)
                
                draw.ellipse([x - glow_radius, y - glow_radius, 
                             x + corner_size + glow_radius, y + corner_size + glow_radius],
                            fill=glow_color)
            
            # Main corner element
            draw.ellipse([x, y, x + corner_size, y + corner_size], 
                        fill=palette['accent2'], outline=palette['light'], width=4)
            
            # Inner detail
            inner_size = corner_size - 40
            draw.ellipse([x + 20, y + 20, x + 20 + inner_size, y + 20 + inner_size],
                        outline=palette['secondary'], width=3)
        
        return img

    def _create_tech_keynote(self, img, palette):
        """Apple Keynote style - ultra clean with dramatic impact"""
        draw = ImageDraw.Draw(img)
        
        # Ultra-clean gradient background
        for y in range(1080):
            factor = y / 1080
            
            # Create smooth tri-color gradient
            if y < 360:  # Top third
                color = self._ultra_interpolate_color(palette['dark'], palette['primary'], factor * 1.5)
            elif y < 720:  # Middle third
                mid_factor = (y - 360) / 360
                color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], mid_factor)
            else:  # Bottom third
                bottom_factor = (y - 720) / 360
                color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], bottom_factor * 0.7)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Add geometric precision elements
        # Central focus area with perfect proportions
        center_rect = [200, 200, 880, 880]
        
        # Create depth with multiple shadows
        for shadow_offset in range(8, 0, -1):
            shadow_alpha = int(255 * shadow_offset / 8 * 0.4)
            shadow_color = self._add_alpha_to_color(palette['shadow'], shadow_alpha)
            
            shadow_rect = [center_rect[0] + shadow_offset, center_rect[1] + shadow_offset,
                          center_rect[2] + shadow_offset, center_rect[3] + shadow_offset]
            draw.rectangle(shadow_rect, fill=shadow_color)
        
        # Main content area with glass effect
        draw.rectangle(center_rect, fill=palette['light'] + '20', 
                      outline=palette['accent2'], width=3)
        
        # Add keynote-style accent lines
        line_positions = [100, 300, 500, 700, 900]
        for pos in line_positions:
            # Horizontal lines
            draw.line([(0, pos), (1080, pos)], fill=palette['accent2'] + '40', width=2)
            # Vertical lines
            draw.line([(pos, 0), (pos, 1080)], fill=palette['accent2'] + '40', width=2)
        
        # Central focus point
        focus_center = (540, 540)
        for radius in range(80, 20, -5):
            alpha = int(255 * (80 - radius) / 60 * 0.6)
            color = self._add_alpha_to_color(palette['accent1'], alpha)
            
            draw.ellipse([focus_center[0] - radius, focus_center[1] - radius,
                         focus_center[0] + radius, focus_center[1] + radius], fill=color)
        
        return img

    def _create_social_viral(self, img, palette):
        """Instagram viral format - optimized for engagement"""
        draw = ImageDraw.Draw(img)
        
        # Viral-optimized dynamic background
        # Create wave-like pattern that catches the eye
        for y in range(0, 1080, 4):
            for x in range(0, 1080, 4):
                # Complex wave mathematics for visual interest
                wave1 = math.sin(x * 0.008) * 60
                wave2 = math.cos(y * 0.006) * 40
                wave3 = math.sin((x + y) * 0.004) * 30
                
                distance = math.sqrt((x - 540)**2 + (y - 540)**2)
                factor = (distance + wave1 + wave2 + wave3) / 900
                factor = max(0, min(1, factor))
                
                # Multi-layer color blending
                if factor < 0.25:
                    color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], factor * 4)
                elif factor < 0.5:
                    color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], (factor - 0.25) * 4)
                elif factor < 0.75:
                    color = self._ultra_interpolate_color(palette['accent1'], palette['accent2'], (factor - 0.5) * 4)
                else:
                    color = self._ultra_interpolate_color(palette['accent2'], palette['dark'], (factor - 0.75) * 4)
                
                # Create texture
                draw.rectangle([x, y, x+4, y+4], fill=color)
        
        # Add viral elements - burst patterns
        center = (540, 540)
        
        # Energy burst rays
        for angle in range(0, 360, 12):
            rad = math.radians(angle)
            
            # Multiple ray lengths for depth
            for ray_length in [150, 250, 350]:
                start_dist = 80
                end_dist = ray_length
                
                # Calculate ray positions
                x1 = center[0] + start_dist * math.cos(rad)
                y1 = center[1] + start_dist * math.sin(rad)
                x2 = center[0] + end_dist * math.cos(rad)
                y2 = center[1] + end_dist * math.sin(rad)
                
                # Ray color based on length
                if ray_length == 150:
                    ray_color = palette['accent1']
                    width = 6
                elif ray_length == 250:
                    ray_color = palette['secondary']
                    width = 4
                else:
                    ray_color = palette['accent2']
                    width = 2
                
                draw.line([(x1, y1), (x2, y2)], fill=ray_color, width=width)
        
        # Central viral element
        for radius in range(100, 30, -5):
            alpha = int(255 * (100 - radius) / 70 * 0.8)
            color = self._add_alpha_to_color(palette['light'], alpha)
            
            draw.ellipse([center[0] - radius, center[1] - radius,
                         center[0] + radius, center[1] + radius], fill=color)
        
        return img

    def _create_corporate_elite(self, img, palette):
        """Fortune 500 presentation level"""
        draw = ImageDraw.Draw(img)
        
        # Elite corporate background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['dark'])
        
        # Premium header section
        header_height = 280
        
        # Multi-layer header gradient
        for y in range(header_height):
            factor = y / header_height
            if y < header_height * 0.6:
                color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], factor * 1.67)
            else:
                color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], (factor - 0.6) * 2.5)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Elite content sections with perfect spacing
        sections = [
            [60, header_height + 40, 520, 800],  # Left section
            [560, header_height + 40, 1020, 800]  # Right section
        ]
        
        for section in sections:
            # Professional shadow system
            for shadow in range(12, 0, -1):
                shadow_alpha = int(255 * shadow / 12 * 0.2)
                shadow_color = self._add_alpha_to_color(palette['shadow'], shadow_alpha)
                
                shadow_rect = [section[0] + shadow, section[1] + shadow,
                              section[2] + shadow, section[3] + shadow]
                draw.rectangle(shadow_rect, fill=shadow_color)
            
            # Main section with glass effect
            draw.rectangle(section, fill=palette['light'], 
                          outline=palette['accent2'], width=4)
            
            # Inner frame
            inner_margin = 20
            inner_rect = [section[0] + inner_margin, section[1] + inner_margin,
                         section[2] - inner_margin, section[3] - inner_margin]
            draw.rectangle(inner_rect, outline=palette['primary'], width=2)
        
        # Elite footer with branding space
        footer_y = 850
        draw.rectangle([0, footer_y, 1080, 1080], fill=palette['accent1'])
        
        # Professional grid overlay
        grid_spacing = 60
        for i in range(0, 1080, grid_spacing):
            # Vertical lines
            draw.line([(i, 0), (i, 1080)], fill=palette['accent2'] + '20', width=1)
            # Horizontal lines  
            draw.line([(0, i), (1080, i)], fill=palette['accent2'] + '20', width=1)
        
        return img

    def _create_startup_unicorn(self, img, palette):
        """Silicon Valley unicorn startup style"""
        draw = ImageDraw.Draw(img)
        
        # Ultra-modern gradient with tech feel
        # Create diagonal tech pattern
        for x in range(0, 1080, 8):
            for y in range(0, 1080, 8):
                # Tech pattern calculation
                pattern_value = (x + y) % 160
                tech_factor = pattern_value / 160
                
                # Distance from center for radial effect
                distance = math.sqrt((x - 540)**2 + (y - 540)**2)
                radial_factor = distance / 760
                
                # Combine factors
                combined_factor = (tech_factor + radial_factor) / 2
                combined_factor = max(0, min(1, combined_factor))
                
                # Tech color progression
                if combined_factor < 0.3:
                    color = self._ultra_interpolate_color(palette['dark'], palette['primary'], combined_factor * 3.33)
                elif combined_factor < 0.7:
                    color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], (combined_factor - 0.3) * 2.5)
                else:
                    color = self._ultra_interpolate_color(palette['secondary'], palette['accent2'], (combined_factor - 0.7) * 3.33)
                
                draw.rectangle([x, y, x+8, y+8], fill=color)
        
        # Add startup-style dynamic elements
        # Diagonal tech stripes
        stripe_width = 40
        for i in range(-200, 1280, stripe_width * 3):
            stripe_points = [
                (i, 0),
                (i + stripe_width, 0),
                (i + stripe_width + 200, 1080),
                (i + 200, 1080)
            ]
            
            # Alternating stripe colors with transparency
            if (i // (stripe_width * 3)) % 2 == 0:
                stripe_color = self._add_alpha_to_color(palette['accent1'], 60)
            else:
                stripe_color = self._add_alpha_to_color(palette['accent2'], 40)
            
            draw.polygon(stripe_points, fill=stripe_color)
        
        # Central innovation hub
        hub_center = (540, 540)
        hub_radius = 200
        
        # Multi-layer hub with glow
        for layer in range(5):
            layer_radius = hub_radius - layer * 30
            layer_alpha = int(255 * (5 - layer) / 5 * 0.4)
            
            if layer % 2 == 0:
                layer_color = self._add_alpha_to_color(palette['accent1'], layer_alpha)
            else:
                layer_color = self._add_alpha_to_color(palette['accent2'], layer_alpha)
            
            draw.ellipse([hub_center[0] - layer_radius, hub_center[1] - layer_radius,
                         hub_center[0] + layer_radius, hub_center[1] + layer_radius],
                        fill=layer_color)
        
        # Tech grid overlay
        grid_size = 45
        for x in range(0, 1080, grid_size):
            for y in range(0, 1080, grid_size):
                # Grid intersection points
                if x > 0 and y > 0:
                    intersection_size = 6
                    draw.ellipse([x - intersection_size//2, y - intersection_size//2,
                                 x + intersection_size//2, y + intersection_size//2],
                                fill=palette['light'] + '60')
        
        return img

    def _create_fashion_editorial(self, img, palette):
        """High-fashion magazine editorial style"""
        draw = ImageDraw.Draw(img)
        
        # Fashion-forward asymmetric design
        # Create artistic color blocks
        
        # Base sophisticated background
        draw.rectangle([0, 0, 1080, 1080], fill=palette['dark'])
        
        # Asymmetric color blocks - fashion magazine style
        blocks = [
            # Large primary block
            ([0, 0, 650, 400], palette['primary']),
            # Secondary accent block  
            ([650, 0, 1080, 250], palette['secondary']),
            # Small accent block
            ([650, 250, 1080, 400], palette['accent1']),
            # Bottom flowing block
            ([0, 400, 450, 1080], palette['accent2']),
            # Right column
            ([450, 400, 1080, 1080], palette['primary'])
        ]
        
        for block_coords, block_color in blocks:
            # Add gradient to each block
            x1, y1, x2, y2 = block_coords
            
            for y in range(y1, y2):
                factor = (y - y1) / (y2 - y1) if y2 > y1 else 0
                # Create subtle gradient within each block
                gradient_color = self._ultra_interpolate_color(block_color, palette['dark'], factor * 0.3)
                draw.line([(x1, y), (x2, y)], fill=gradient_color)
        
        # Add fashion-style geometric overlays
        # Diagonal cuts and overlays
        overlay_triangles = [
            # Top right triangle
            [(800, 0), (1080, 0), (1080, 180)],
            # Bottom left triangle  
            [(0, 900), (0, 1080), (280, 1080)],
            # Central accent triangle
            [(400, 300), (680, 400), (400, 500)]
        ]
        
        for i, triangle in enumerate(overlay_triangles):
            if i == 0:
                triangle_color = self._add_alpha_to_color(palette['accent1'], 180)
            elif i == 1:
                triangle_color = self._add_alpha_to_color(palette['accent2'], 160)
            else:
                triangle_color = self._add_alpha_to_color(palette['light'], 120)
            
            draw.polygon(triangle, fill=triangle_color)
        
        # Fashion-style line elements
        line_elements = [
            # Horizontal fashion lines
            [(100, 200), (500, 200)],
            [(600, 600), (980, 600)],
            # Vertical fashion lines
            [(200, 100), (200, 350)],
            [(800, 450), (800, 900)]
        ]
        
        for line in line_elements:
            draw.line(line, fill=palette['light'], width=8)
            # Add glow to lines
            draw.line(line, fill=palette['accent2'] + '80', width=12)
        
        return img

    def _create_automotive_premium(self, img, palette):
        """Tesla/Mercedes premium automotive style"""
        draw = ImageDraw.Draw(img)
        
        # Premium automotive gradient - sleek and powerful
        # Create metallic-like surface effect
        for y in range(1080):
            for x in range(0, 1080, 4):
                # Metallic reflection calculation
                surface_factor = math.sin(x * 0.01) * 0.1 + math.cos(y * 0.008) * 0.1
                distance_factor = math.sqrt((x - 540)**2 + (y - 540)**2) / 760
                
                combined_factor = (distance_factor + surface_factor + 0.5) / 2
                combined_factor = max(0, min(1, combined_factor))
                
                # Automotive color progression
                if combined_factor < 0.4:
                    color = self._ultra_interpolate_color(palette['dark'], palette['primary'], combined_factor * 2.5)
                elif combined_factor < 0.8:
                    color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], (combined_factor - 0.4) * 2.5)
                else:
                    color = self._ultra_interpolate_color(palette['secondary'], palette['light'], (combined_factor - 0.8) * 5)
                
                # Add metallic texture
                draw.line([(x, y), (x+4, y)], fill=color)
        
        # Add automotive design elements
        # Sleek curves and lines
        center_x, center_y = 540, 540
        
        # Central automotive design element
        curve_points = []
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            # Create automotive curve
            radius = 250 + 50 * math.sin(angle * 0.1)
            
            x = center_x + radius * math.cos(rad)
            y = center_y + radius * math.sin(rad)
            curve_points.append((x, y))
        
        # Draw smooth automotive curve
        for i in range(len(curve_points)):
            next_i = (i + 1) % len(curve_points)
            draw.line([curve_points[i], curve_points[next_i]], 
                     fill=palette['accent1'], width=6)
        
        # Add premium accent lines - automotive style
        accent_lines = [
            # Hood lines
            [(0, 300), (1080, 280)],
            [(0, 320), (1080, 300)],
            # Side character lines
            [(200, 0), (300, 1080)],
            [(780, 0), (880, 1080)]
        ]
        
        for line in accent_lines:
            # Main line
            draw.line(line, fill=palette['accent2'], width=4)
            # Glow effect
            draw.line(line, fill=palette['light'] + '60', width=8)
        
        # Premium corner elements - automotive inspired
        corner_elements = [(50, 50), (1030, 50), (50, 1030), (1030, 1030)]
        
        for corner in corner_elements:
            x, y = corner
            
            # Create automotive-style corner element
            corner_points = [
                (x, y),
                (x + 80, y + 20),
                (x + 60, y + 60),
                (x + 20, y + 80)
            ]
            
            draw.polygon(corner_points, fill=palette['accent1'], 
                        outline=palette['light'], width=3)
        
        return img

    def _create_fintech_modern(self, img, palette):
        """Modern fintech/banking elite style"""
        draw = ImageDraw.Draw(img)
        
        # Fintech gradient - trust and innovation
        # Create data visualization inspired background
        
        # Base financial gradient
        for y in range(1080):
            factor = y / 1080
            
            # Multi-stage financial gradient
            if y < 270:  # Top quarter
                color = self._ultra_interpolate_color(palette['dark'], palette['primary'], factor * 2)
            elif y < 540:  # Second quarter
                mid_factor = (y - 270) / 270
                color = self._ultra_interpolate_color(palette['primary'], palette['secondary'], mid_factor)
            elif y < 810:  # Third quarter
                mid_factor = (y - 540) / 270
                color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], mid_factor)
            else:  # Bottom quarter
                bottom_factor = (y - 810) / 270
                color = self._ultra_interpolate_color(palette['accent1'], palette['accent2'], bottom_factor)
            
            draw.line([(0, y), (1080, y)], fill=color)
        
        # Add fintech data visualization elements
        # Market chart inspired patterns
        data_points = []
        for x in range(0, 1080, 30):
            # Create market-like data pattern
            base_height = 540
            variation = 200 * math.sin(x * 0.02) + 100 * math.cos(x * 0.05)
            y = base_height + variation
            data_points.append((x, int(y)))
        
        # Draw market chart style lines
        for i in range(len(data_points) - 1):
            current_point = data_points[i]
            next_point = data_points[i + 1]
            
            # Market line with gradient
            draw.line([current_point, next_point], fill=palette['accent2'], width=6)
            
            # Add market volume bars
            bar_height = abs(current_point[1] - 540) // 3
            bar_bottom = max(current_point[1], 540)
            
            draw.rectangle([current_point[0] - 8, bar_bottom, 
                           current_point[0] + 8, bar_bottom + bar_height],
                          fill=palette['accent1'] + '80')
        
        # Add fintech grid system
        grid_spacing = 54  # Golden ratio derived
        
        for x in range(0, 1080, grid_spacing):
            # Vertical grid lines
            draw.line([(x, 0), (x, 1080)], fill=palette['light'] + '20', width=1)
            
        for y in range(0, 1080, grid_spacing):
            # Horizontal grid lines
            draw.line([(0, y), (1080, y)], fill=palette['light'] + '20', width=1)
            
            # Grid intersection highlights
            for x in range(0, 1080, grid_spacing):
                intersection_size = 4
                draw.ellipse([x - intersection_size//2, y - intersection_size//2,
                             x + intersection_size//2, y + intersection_size//2],
                            fill=palette['accent2'] + '60')
        
        # Central fintech focus element
        center = (540, 540)
        
        # Create layered hexagonal element (fintech/crypto inspired)
        hex_radius = 150
        
        for layer in range(3):
            layer_radius = hex_radius - layer * 40
            
            # Calculate hexagon points
            hex_points = []
            for i in range(6):
                angle = i * 60 + layer * 15  # Rotate each layer
                rad = math.radians(angle)
                x = center[0] + layer_radius * math.cos(rad)
                y = center[1] + layer_radius * math.sin(rad)
                hex_points.append((x, y))
            
            # Draw hexagon
            if layer == 0:
                hex_color = palette['accent1'] + '40'
            elif layer == 1:
                hex_color = palette['accent2'] + '60'
            else:
                hex_color = palette['light'] + '80'
            
            draw.polygon(hex_points, outline=hex_color, width=4)
        
        return img

    def _add_ultra_premium_content(self, img, hook_text, main_stat, call_to_action, palette, design_system):
        """Dodaj content z ultra-premium typography i layout"""
        draw = ImageDraw.Draw(img)
        
        # GŁÓWNA STATYSTYKA - hero element z maksymalnym impactem
        if main_stat:
            # Extract number for dramatic display
            import re
            numbers = re.findall(r'\d+[\.,]?\d*', main_stat)
            if numbers:
                big_number = numbers[0]
                
                # Position based on design system
                if design_system in ['luxury_magazine', 'fashion_editorial']:
                    number_x, number_y = 540, 150
                elif design_system in ['tech_keynote', 'corporate_elite']:
                    number_x, number_y = 540, 120
                elif design_system == 'social_viral':
                    number_x, number_y = 540, 180
                else:
                    number_x, number_y = 540, 140
                
                # Create ultra-dramatic number display with multiple effects
                
                # 1. Outer glow effect
                for glow_offset in range(12, 0, -1):
                    glow_alpha = int(255 * glow_offset / 12 * 0.3)
                    glow_color = self._add_alpha_to_color(palette['accent1'], glow_alpha)
                    
                    bbox = draw.textbbox((0, 0), big_number, font=self.fonts['accent_impact'])
                    text_width = bbox[2] - bbox[0]
                    x = number_x - text_width // 2
                    
                    draw.text((x + glow_offset, number_y + glow_offset), big_number, 
                             fill=glow_color, font=self.fonts['accent_impact'])
                
                # 2. Deep shadow for 3D effect
                for shadow_offset in range(8, 0, -1):
                    shadow_alpha = int(255 * shadow_offset / 8 * 0.6)
                    shadow_color = self._add_alpha_to_color(palette['shadow'], shadow_alpha)
                    
                    bbox = draw.textbbox((0, 0), big_number, font=self.fonts['accent_impact'])
                    text_width = bbox[2] - bbox[0]
                    x = number_x - text_width // 2
                    
                    draw.text((x + shadow_offset, number_y + shadow_offset), big_number,
                             fill=shadow_color, font=self.fonts['accent_impact'])
                
                # 3. Main number with gradient effect (simulated)
                bbox = draw.textbbox((0, 0), big_number, font=self.fonts['accent_impact'])
                text_width = bbox[2] - bbox[0]
                x = number_x - text_width // 2
                
                # Create gradient text effect by drawing multiple layers
                draw.text((x, number_y), big_number, fill=palette['secondary'], font=self.fonts['accent_impact'])
                draw.text((x, number_y - 2), big_number, fill=palette['accent2'], font=self.fonts['accent_impact'])
                
                # 4. Add unit/context below with premium styling
                unit_match = re.search(r'\d+[\.,]?\d*\s*([^0-9]+)', main_stat)
                if unit_match:
                    unit = unit_match.group(1).strip()
                    
                    # Unit background with glow
                    unit_bbox = draw.textbbox((0, 0), unit, font=self.fonts['subtitle_bold'])
                    unit_width = unit_bbox[2] - unit_bbox[0]
                    unit_height = unit_bbox[3] - unit_bbox[1]
                    unit_x = number_x - unit_width // 2
                    unit_y = number_y + 180
                    
                    # Unit background box with premium styling
                    padding = 20
                    box_coords = [unit_x - padding, unit_y - padding,
                                 unit_x + unit_width + padding, unit_y + unit_height + padding]
                    
                    # Box shadow
                    for shadow in range(6, 0, -1):
                        shadow_alpha = int(255 * shadow / 6 * 0.4)
                        shadow_color = self._add_alpha_to_color(palette['shadow'], shadow_alpha)
                        shadow_box = [box_coords[0] + shadow, box_coords[1] + shadow,
                                     box_coords[2] + shadow, box_coords[3] + shadow]
                        draw.rectangle(shadow_box, fill=shadow_color)
                    
                    # Main box
                    draw.rectangle(box_coords, fill=palette['accent1'], 
                                  outline=palette['light'], width=3)
                    
                    # Unit text
                    draw.text((unit_x, unit_y), unit, fill=palette['light'], font=self.fonts['subtitle_bold'])
        
        # HOOK TEXT - ultra-premium typography
        if hook_text:
            # Clean hook text
            clean_hook = self._clean_hook_text(hook_text)
            
            # Smart text positioning based on design system
            if design_system in ['social_viral', 'startup_unicorn']:
                hook_y_start = 400
                max_width = 800
            elif design_system in ['luxury_magazine', 'fashion_editorial']:
                hook_y_start = 450
                max_width = 900
            else:
                hook_y_start = 420
                max_width = 850
            
            # Ultra-premium text wrapping
            wrapped_lines = self._ultra_smart_wrap_text(clean_hook, self.fonts['body_premium'], max_width)
            
            line_height = 75
            
            for i, line in enumerate(wrapped_lines[:3]):  # Max 3 lines for impact
                bbox = draw.textbbox((0, 0), line, font=self.fonts['body_premium'])
                text_width = bbox[2] - bbox[0]
                x = 540 - text_width // 2
                y = hook_y_start + i * line_height
                
                # Multi-layer text effect for premium look
                # 1. Glow effect
                for glow in range(6, 0, -1):
                    glow_alpha = int(255 * glow / 6 * 0.2)
                    glow_color = self._add_alpha_to_color(palette['accent2'], glow_alpha)
                    draw.text((x + glow, y + glow), line, fill=glow_color, font=self.fonts['body_premium'])
                
                # 2. Shadow for depth
                draw.text((x + 3, y + 3), line, fill=palette['shadow'] + '60', font=self.fonts['body_premium'])
                
                # 3. Main text
                draw.text((x, y), line, fill=palette['light'], font=self.fonts['body_premium'])
        
        # CALL TO ACTION - ultra-premium button design
        if call_to_action:
            main_cta = call_to_action.split('\n')[0].strip()
            if main_cta.startswith('🚀 '):
                main_cta = main_cta[2:].strip()
            
            # CTA positioning
            cta_y = 800
            bbox = draw.textbbox((0, 0), main_cta, font=self.fonts['subtitle_bold'])
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Ultra-premium button design
            button_padding_x = 50
            button_padding_y = 25
            button_width = text_width + 2 * button_padding_x
            button_height = text_height + 2 * button_padding_y
            
            button_x = 540 - button_width // 2
            button_y = cta_y - button_padding_y
            
            # Multi-layer button shadow system
            for shadow_layer in range(15, 0, -1):
                shadow_alpha = int(255 * shadow_layer / 15 * 0.2)
                shadow_color = self._add_alpha_to_color(palette['shadow'], shadow_alpha)
                
                shadow_coords = [button_x + shadow_layer, button_y + shadow_layer,
                                button_x + button_width + shadow_layer, 
                                button_y + button_height + shadow_layer]
                draw.rectangle(shadow_coords, fill=shadow_color)
            
            # Button gradient background (simulated with layers)
            for layer in range(button_height):
                factor = layer / button_height
                layer_color = self._ultra_interpolate_color(palette['secondary'], palette['accent1'], factor)
                
                draw.line([(button_x, button_y + layer), 
                          (button_x + button_width, button_y + layer)], fill=layer_color)
            
            # Button border with glow
            draw.rectangle([button_x, button_y, button_x + button_width, button_y + button_height],
                          outline=palette['light'], width=4)
            
            # Inner border for premium effect
            inner_margin = 6
            draw.rectangle([button_x + inner_margin, button_y + inner_margin,
                           button_x + button_width - inner_margin, 
                           button_y + button_height - inner_margin],
                          outline=palette['accent2'], width=2)
            
            # CTA text with effects
            text_x = button_x + button_padding_x
            text_y = button_y + button_padding_y
            
            # Text shadow
            draw.text((text_x + 2, text_y + 2), main_cta, fill=palette['shadow'], font=self.fonts['subtitle_bold'])
            # Main text
            draw.text((text_x, text_y), main_cta, fill=palette['light'], font=self.fonts['subtitle_bold'])
        
        # Ultra-premium branding
        brand_text = "INŻYNIERIA BEZPIECZEŃSTWA"
        try:
            brand_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        except:
            brand_font = self.fonts['body_premium']
        
        bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
        brand_width = bbox[2] - bbox[0]
        brand_x = 1080 - brand_width - 40
        brand_y = 1080 - 50
        
        # Brand text with subtle glow
        for glow in range(4, 0, -1):
            glow_alpha = int(255 * glow / 4 * 0.3)
            glow_color = self._add_alpha_to_color(palette['secondary'], glow_alpha)
            draw.text((brand_x + glow, brand_y + glow), brand_text, fill=glow_color, font=brand_font)
        
        draw.text((brand_x, brand_y), brand_text, fill=palette['light'] + 'C0', font=brand_font)

    def _apply_ultra_premium_effects(self, img):
        """Ultra-premium post-processing dla maksymalnego impaktu"""
        
        # 1. Professional contrast enhancement
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.35)
        
        # 2. Color saturation boost for viral appeal
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.25)
        
        # 3. Professional sharpening
        img = img.filter(ImageFilter.UnsharpMask(radius=1.5, percent=150, threshold=3))
        
        # 4. Subtle brightness adjustment
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.08)
        
        # 5. Add subtle grain for premium texture (simulated)
        # This would require more advanced processing in a real implementation
        
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

    def _ultra_smart_wrap_text(self, text, font, max_width):
        """Ultra-intelligent text wrapping for premium typography"""
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
                    # Word too long, intelligent break
                    if len(word) > 20:
                        # Break long word intelligently
                        break_point = len(word) // 2
                        lines.append(word[:break_point] + "-")
                        current_line = word[break_point:]
                    else:
                        lines.append(word)
                        current_line = ""
        
        if current_line:
            lines.append(current_line)
        
        return lines

    def _ultra_interpolate_color(self, color1, color2, factor):
        """Ultra-smooth color interpolation with gamma correction"""
        factor = max(0, min(1, factor))
        
        # Apply gamma correction for smoother gradients
        gamma = 2.2
        factor_corrected = factor ** (1/gamma)
        
        try:
            if color1.startswith('#'):
                r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
            else:
                r1, g1, b1 = 128, 128, 128
                
            if color2.startswith('#'):
                r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
            else:
                r2, g2, b2 = 128, 128, 128
            
            # Gamma-corrected interpolation
            r = int(((r1/255)**gamma * (1-factor_corrected) + (r2/255)**gamma * factor_corrected)**(1/gamma) * 255)
            g = int(((g1/255)**gamma * (1-factor_corrected) + (g2/255)**gamma * factor_corrected)**(1/gamma) * 255)
            b = int(((b1/255)**gamma * (1-factor_corrected) + (b2/255)**gamma * factor_corrected)**(1/gamma) * 255)
            
            return f'#{r:02x}{g:02x}{b:02x}'
        except:
            return '#666666'

    def _add_alpha_to_color(self, hex_color, alpha):
        """Add alpha channel to hex color"""
        try:
            # Convert hex to RGB
            r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
            return (r, g, b, alpha)
        except:
            return (128, 128, 128, alpha)

    def generate_image_base64(self, specialization, hook_text, main_stat, call_to_action="Skontaktuj się z nami!"):
        """Generate ultra-premium image and return as base64"""
        try:
            img = self.generate_ultra_premium_image(specialization, hook_text, main_stat, call_to_action)
            
            # Convert to base64 with maximum quality
            img_io = io.BytesIO()
            img.save(img_io, 'PNG', quality=100, optimize=False)
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode()
            
            return img_base64
            
        except Exception as e:
            print(f"Ultra-premium image generation error: {e}")
            return self._generate_ultra_fallback()

    def _generate_ultra_fallback(self):
        """Ultra-premium fallback image"""
        img = Image.new('RGB', (1080, 1080), '#0A0A0A')
        draw = ImageDraw.Draw(img)
        
        # Premium fallback with gradient
        for y in range(1080):
            factor = y / 1080
            r = int(10 + (255 - 10) * factor * 0.4)
            g = int(10 + (107 - 10) * factor * 0.4)
            b = int(10 + (53 - 10) * factor * 0.4)
            draw.line([(0, y), (1080, y)], fill=f'#{r:02x}{g:02x}{b:02x}')
        
        # Ultra-premium text
        text = "ULTRA-PREMIUM"
        subtitle = "Content Creator"
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 84)
            sub_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        except:
            title_font = self.fonts['title_hero']
            sub_font = self.fonts['body_premium']
        
        # Title with effects
        bbox = draw.textbbox((0, 0), text, font=title_font)
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 400
        
        # Glow effect
        for glow in range(8, 0, -1):
            glow_alpha = int(255 * glow / 8 * 0.3)
            draw.text((x + glow, y + glow), text, fill=(255, 107, 53, glow_alpha), font=title_font)
        
        draw.text((x, y), text, fill='#FF6B35', font=title_font)
        
        # Subtitle
        bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
        text_width = bbox[2] - bbox[0]
        x = (1080 - text_width) // 2
        y = 520
        
        draw.text((x, y), subtitle, fill='#FFFFFF', font=sub_font)
        
        # Convert to base64
        img_io = io.BytesIO()
        img.save(img_io, 'PNG', quality=100)
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

# Create singleton instance
ultra_premium_graphics = UltraPremiumGraphics()
