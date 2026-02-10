from PIL import Image, ImageDraw, ImageFont
import os

def create_stat_graphic(filename, stat_text, label_text, color_theme="#84CC16"):
    # Settings
    width, height = 800, 600
    bg_color = (248, 250, 252) # Slate-50 background
    primary = (13, 148, 136) # Teal default
    
    # Custom color logic if needed, or stick to nice defaults
    if color_theme == "green": primary = (132, 204, 22) # Lime
    elif color_theme == "blue": primary = (59, 130, 246)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Fonts (Fallbacks)
    try:
        font_stat = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Bold.ttc", 120, index=0)
        font_label = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 40, index=0)
    except:
        font_stat = ImageFont.load_default()
        font_label = ImageFont.load_default()

    # Draw Text Centered
    # Stat
    stat_bbox = draw.textbbox((0, 0), stat_text, font=font_stat)
    stat_w = stat_bbox[2] - stat_bbox[0]
    draw.text(((width - stat_w)/2, height/2 - 80), stat_text, font=font_stat, fill="#0f172a")

    # Label
    label_bbox = draw.textbbox((0, 0), label_text, font=font_label)
    label_w = label_bbox[2] - label_bbox[0]
    draw.text(((width - label_w)/2, height/2 + 60), label_text, font=font_label, fill="#64748b")
    
    # Decorative Circle
    x1, y1 = 600, 100
    x2, y2 = 700, 200
    draw.arc([x1, y1, x2, y2], 0, 360, fill=color_theme, width=10)
    
    output_path = f"images/stats/{filename}"
    img.save(output_path)
    print(f"Generated {output_path}")

niches = [
    # General Contractors
    {"file": "stat_general_contractors.png", "stat": "238%", "label": "Higher Win Rate Response"},
    # Window Installers
    {"file": "stat_window_installers.png", "stat": "30%", "label": "More Appointments Set"},
    # Plumbers
    {"file": "stat_plumbers.png", "stat": "5min", "label": "Response Time Target"},
    # Painters
    {"file": "stat_painters.png", "stat": "40%", "label": "Fewer No-Show Estimates"},
    # Electricians
    {"file": "stat_electricians.png", "stat": "15hr", "label": "Saved Per Week"},
    # Property Management
    {"file": "stat_property_management.png", "stat": "95%", "label": "Rent Collection Rate"},
    
    # Medical
    {"file": "stat_dentists.png", "stat": "3X", "label": "More Google Reviews"},
    {"file": "stat_family_practice.png", "stat": "20%", "label": "Reduced Admin Cost"},
    {"file": "stat_veterinarians.png", "stat": "24/7", "label": "Emergency Triage"},
    {"file": "stat_med_spas.png", "stat": "100%", "label": "Waitlist Utilization"},
    
    # Beauty
    {"file": "stat_hair_salons.png", "stat": "50%", "label": "Fewer Cancellations"},
    {"file": "stat_barbershops.png", "stat": "$5k", "label": "New Revenue / Month"},
    {"file": "stat_nail_salons.png", "stat": "2X", "label": "Client Retention"},
    {"file": "stat_pet_groomers.png", "stat": "90%", "label": "Rebooking Rate"},
    
    # Professional
    {"file": "stat_attorneys.png", "stat": "1 min", "label": "Lead Qualify Speed"},
    {"file": "stat_accountants.png", "stat": "60%", "label": "Faster Doc Collection"},
    {"file": "stat_financial_managers.png", "stat": "35%", "label": "Meeting Show Rate"},
    {"file": "stat_real_estate_brokers.png", "stat": "10X", "label": "Faster Follow-up"},
    
    # Auto
    {"file": "stat_auto_mechanics.png", "stat": "25%", "label": "Higher Ticket Value"},
    {"file": "stat_window_tinting.png", "stat": "60%", "label": "Upsell Conversion"},
    
    # Hospitality
    {"file": "stat_restaurants.png", "stat": "15%", "label": "More Table Turns"}
]

if __name__ == "__main__":
    if not os.path.exists("images/stats"):
        os.makedirs("images/stats")
        
    for n in niches:
        create_stat_graphic(n["file"], n["stat"], n["label"], "green")
