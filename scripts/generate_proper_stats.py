from PIL import Image, ImageDraw, ImageFont
import os
import math

# --- 1. CONFIGURATION ---
WIDTH = 800
HEIGHT = 600
BG_COLOR = (248, 250, 252) # Slate-50 background
PRIMARY_COLOR = (13, 148, 136) # Teal default
TEXT_MAIN = (15, 23, 42) # Slate-900
TEXT_MUTED = (100, 116, 139) # Slate-500
BORDER_COLOR = (226, 232, 240) # Slate-200

def get_fonts():
    # Attempt to load nice system fonts (MacOS specific mostly)
    try:
        font_stat = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Medium.ttc", 140, index=0)
        font_label = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 40, index=0)
        font_sub = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Light.ttc", 30, index=0)
    except:
        # Fallback
        font_stat = ImageFont.load_default()
        font_label = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    return font_stat, font_label, font_sub

# --- 2. DRAWING HELPERS ---

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    x, y, w, h = bbox
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill, outline=outline, width=width)

def draw_arrow_up(draw, x, y, size, color):
    # Draw a green upward arrow indicating growth
    points = [
        (x, y + size),        # Bottom stick
        (x, y + size/2),      # Stick top
        (x - size/2, y + size/2), # Left wing
        (x + size/2, y - size/2), # Top point
        (x + size * 1.5, y + size/2), # Right wing
        (x + size, y + size/2),   # Stick right side
        (x + size, y + size)      # Bottom stick right
    ]
    # Simplified Triangle
    draw.polygon([
        (x, y + size), 
        (x + size, y), 
        (x + size*2, y + size)
    ], fill=color)
    draw.rectangle([x + size*0.7, y + size, x + size*1.3, y + size*2.5], fill=color)

def draw_clock(draw, center_x, center_y, radius, color):
    # Draw clock face
    draw.ellipse([center_x-radius, center_y-radius, center_x+radius, center_y+radius], outline=color, width=8)
    # Hands
    draw.line([center_x, center_y, center_x, center_y - radius + 15], fill=color, width=6)
    draw.line([center_x, center_y, center_x + radius - 20, center_y], fill=color, width=6)

# --- 3. MAIN GENERATOR ---

def create_graphic(filename, stat_value, label_text, sub_text="", visual_type="growth"):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    font_stat, font_label, font_sub = get_fonts()
    
    # Draw Card Background (centered)
    card_w, card_h = 600, 400
    cx, cy = WIDTH//2, HEIGHT//2
    card_x, card_y = cx - card_w//2, cy - card_h//2
    
    # Shadow offset (simulated)
    draw_rounded_rect(draw, (card_x+10, card_y+15, card_w, card_h), 30, (230,230,240))
    # Main Card
    draw_rounded_rect(draw, (card_x, card_y, card_w, card_h), 30, (255,255,255), outline=BORDER_COLOR, width=2)
    
    # Visual Icon
    icon_color = (34, 197, 94) if visual_type == "growth" else (59, 130, 246)
    if visual_type == "time": icon_color = (245, 158, 11)
    
    # Draw Visual Decoration
    if visual_type == "growth":
        # Draw Arrow
        draw_arrow_up(draw, card_x + 60, card_y + 60, 40, icon_color)
    elif visual_type == "time":
        draw_clock(draw, card_x + 100, card_y + 100, 40, icon_color)
    elif visual_type == "money":
        # Draw $ Sign circle
        draw.ellipse([card_x+60, card_y+60, card_x+140, card_y+140], fill=(220, 252, 231))
        # Text $
        # Simple Draw $
        try:
            money_font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Bold.ttc", 60, index=0)
        except: money_font = font_label
        draw.text((card_x+82, card_y+65), "$", font=money_font, fill=(21, 128, 61))

    # Stat Value
    # Check text size to center it
    stat_bbox = draw.textbbox((0, 0), stat_value, font=font_stat)
    stat_w = stat_bbox[2] - stat_bbox[0]
    
    # Center position
    draw.text((cx - stat_w/2, card_y + 120), stat_value, font=font_stat, fill=TEXT_MAIN)
    
    # Label
    label_bbox = draw.textbbox((0, 0), label_text, font=font_label)
    label_w = label_bbox[2] - label_bbox[0]
    draw.text((cx - label_w/2, card_y + 280), label_text, font=font_label, fill=TEXT_MUTED)
    
    # Sub Label
    if sub_text:
        sub_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
        sub_w = sub_bbox[2] - sub_bbox[0]
        draw.text((cx - sub_w/2, card_y + 340), sub_text, font=font_sub, fill=(148, 163, 184))

    # Save
    output_path = f"images/stats/{filename}"
    img.save(output_path)
    print(f"Generated {output_path}")

# --- 4. DATA ---

niches_data = [
    {"file": "stat_general_contractors.png", "stat": "238%", "label": "Higher Win Rate", "sub": "When responding first", "type": "growth"},
    
    {"file": "stat_dentists.png", "stat": "+$50k", "label": "Revenue Surge", "sub": "From 30-day reactivation", "type": "money"},
    
    {"file": "stat_attorneys.png", "stat": "15hrs", "label": "Billable Time Saved", "sub": "Per month via automation", "type": "time"},
    
    {"file": "stat_window_installers.png", "stat": "30%", "label": "More Appointments", "sub": "Through instant booking", "type": "growth"},
    
    {"file": "stat_plumbers.png", "stat": "<5min", "label": "Response Time", "sub": "Industry standard target", "type": "time"},
    
    {"file": "stat_painters.png", "stat": "40%", "label": "Fewer No-Shows", "sub": "With automated reminders", "type": "growth"},
    
    {"file": "stat_electricians.png", "stat": "15hrs", "label": "Hours Recovered", "sub": "Admin work automated", "type": "time"},
    
    {"file": "stat_property_management.png", "stat": "95%", "label": "On-Time Rent", "sub": "Via automated portals", "type": "money"},
    
    {"file": "stat_family_practice.png", "stat": "20%", "label": "Lower Admin Cost", "sub": "Efficiency gains", "type": "money"},
    
    {"file": "stat_veterinarians.png", "stat": "24/7", "label": "Triage Coverage", "sub": "Always-on AI routing", "type": "time"},
    
    {"file": "stat_med_spas.png", "stat": "100%", "label": "Waitlist Fill Rate", "sub": "Zero empty slots", "type": "growth"},
    
    {"file": "stat_hair_salons.png", "stat": "50%", "label": "Less Cancellations", "sub": "SMS deposit protection", "type": "growth"},
    
    {"file": "stat_barbershops.png", "stat": "$5k", "label": "New Monthly Rev", "sub": "From filled cancellations", "type": "money"},
    
    {"file": "stat_nail_salons.png", "stat": "2X", "label": "Retention Rate", "sub": "Loyalty automation", "type": "growth"},
    
    {"file": "stat_pet_groomers.png", "stat": "90%", "label": "Rebook Rate", "sub": "Automated regular reminders", "type": "growth"},
    
    {"file": "stat_accountants.png", "stat": "60%", "label": "Faster Docs", "sub": "Document collection speed", "type": "time"},
    
    {"file": "stat_financial_managers.png", "stat": "35%", "label": "Higher Show Rate", "sub": "For annual reviews", "type": "growth"},
    
    {"file": "stat_real_estate_brokers.png", "stat": "10X", "label": "Lead Response", "sub": "Instant vs Manual", "type": "time"},
    
    {"file": "stat_auto_mechanics.png", "stat": "25%", "label": "Higher Ticket", "sub": "Upsells via text", "type": "money"},
    
    {"file": "stat_window_tinting.png", "stat": "60%", "label": "Conversion Rate", "sub": "From inquiry to booking", "type": "growth"},
    
    {"file": "stat_restaurants.png", "stat": "15%", "label": "Table Turn Increase", "sub": "Efficient reservation mgmt", "type": "growth"},
]

if __name__ == "__main__":
    if not os.path.exists("images/stats"):
        os.makedirs("images/stats")
    
    for item in niches_data:
        create_graphic(item["file"], item["stat"], item["label"], item["sub"], item["type"])
