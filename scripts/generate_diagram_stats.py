from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Config
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

def get_fonts():
    try:
        font_header = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Bold.ttc", 48, index=0)
        font_text_bold = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Medium.ttc", 36, index=0)
        font_text = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 32, index=0)
        font_small = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue-Light.ttc", 24, index=0)
    except:
        font_header = ImageFont.load_default()
        font_text_bold = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_small = ImageFont.load_default()
    return font_header, font_text_bold, font_text, font_small

def draw_section(draw, x, y, w, h, bg, title, text, icon_type, fonts):
    fh, ftb, ft, fs = fonts
    
    # Background
    draw.rectangle([x, y, x+w, y+h], fill=bg)
    
    # Icon Circle
    cx = x + w//2
    cy = y + 80
    r = 40
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255,255,255))
    
    # Icon (Simple shapes)
    if icon_type == "pain":
        draw.line([cx-15, cy-15, cx+15, cy+15], fill=(239, 68, 68), width=5)
        draw.line([cx+15, cy-15, cx-15, cy+15], fill=(239, 68, 68), width=5)
    else: # gain
        draw.line([cx-15, cy, cx-5, cy+10], fill=(34, 197, 94), width=5)
        draw.line([cx-5, cy+10, cx+15, cy-15], fill=(34, 197, 94), width=5)

    # Title
    t_bbox = draw.textbbox((0,0), title, font=ftb)
    t_w = t_bbox[2] - t_bbox[0]
    draw.text((cx - t_w/2, cy + 60), title, font=ftb, fill=(30, 41, 59))
    
    # Text (Wrapped)
    lines = textwrap.wrap(text, width=20)
    curr_y = cy + 120
    for line in lines:
        l_bbox = draw.textbbox((0,0), line, font=ft)
        l_w = l_bbox[2] - l_bbox[0]
        draw.text((cx - l_w/2, curr_y), line, font=ft, fill=(71, 85, 105))
        curr_y += 40

def create_comparison_graphic(filename, niche_name, pain_title, pain_desc, gain_title, gain_desc):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    fh, ftb, ft, fs = fonts
    
    # Header
    draw.rectangle([0, 0, WIDTH, 100], fill=(15, 23, 42))
    h_bbox = draw.textbbox((0,0), niche_name, font=fh)
    h_w = h_bbox[2] - h_bbox[0]
    draw.text(((WIDTH - h_w)/2, 25), niche_name, font=fh, fill=(255, 255, 255))
    
    # Left Side (Pain) - Light Red
    draw_section(draw, 0, 100, WIDTH//2, HEIGHT-100, (254, 242, 242), pain_title, pain_desc, "pain", fonts)
    
    # Right Side (Gain) - Light Green
    draw_section(draw, WIDTH//2, 100, WIDTH//2, HEIGHT-100, (240, 253, 244), gain_title, gain_desc, "gain", fonts)
    
    # Divider Arrow
    cx, cy = WIDTH//2, HEIGHT//2 + 50
    draw.polygon([
        (cx-20, cy-40), (cx+20, cy), (cx-20, cy+40)
    ], fill=(15, 23, 42))
    
    output_path = f"images/stats/{filename}"
    img.save(output_path)
    print(f"Generated {output_path}")

data = [
    # 21 Niches
    ("stat_general_contractors.png", "Construction", "Shared Leads", "leads sold to 5 contractors at once = price war.", "Speed-to-Lead", "First to call wins 78% of the jobs."),
    ("stat_window_installers.png", "Window Installers", "Manual Quotes", "Driving out just to measure & getting ghosted.", "Virtual Estimates", "Pre-qualify sizing via photos before driving."),
    ("stat_plumbers.png", "Plumbing", "Missed Emergencies", "Voicemail during a burst pipe = lost job.", "24/7 AI Dispatch", "Instant routing to on-call techs."),
    ("stat_painters.png", "Painters", "No-Shows", "Clients forget estimates or touch-ups.", "Auto Reminders", "SMS confirmations reduce no-shows by 40%."),
    ("stat_electricians.png", "Electricians", "Unbilled Hours", "Paperwork lost in the truck.", "On-Site Invoicing", "Collect payment instantly via mobile app."),
    ("stat_property_management.png", "Property Mgmt", "Late Rent", "Chasing checks and manual ledgers.", "Tenant Portal", "95% auto-pay adoption & auto-late fees."),
    ("stat_dentists.png", "Dentistry", "Empty Chairs", "Last minute cancellations kill profits.", "Waitlist AI", "Auto-text waitlist fills gaps in minutes."),
    ("stat_family_practice.png", "Medical Practice", "Front Desk Chaos", "Phones ringing off the hook.", "AI Intake", "Patient self-scheduling & insurance check."),
    ("stat_veterinarians.png", "Veterinary", "Mid-Surgery Calls", "Stopping work to answer phones.", "AI Triage", "Intelligent routing based on urgency."),
    ("stat_med_spas.png", "Med Spas", "Empty Slots", "Perishable inventory (time) lost.", "Flash Sales", "SMS blast fills slow days instantly."),
    ("stat_hair_salons.png", "Hair Salons", "No-Shows", "Loss of 2 hours of revenue.", "Deposit Systems", "SMS deposits secure the booking."),
    ("stat_barbershops.png", "Barbershops", "Phone Tag", "Interrupting cuts to book appts.", "Self-Booking", "Clients book 24/7 without calls."),
    ("stat_nail_salons.png", "Nail Salons", "One-Offs", "Tourists who never return.", "Loyalty Club", "Rewards program drives 2x retention."),
    ("stat_pet_groomers.png", "Pet Groomers", "Forgotten Appts", "Owners forget it's been 6 weeks.", "Recurring SMS", "Auto-reminders based on breed schedule."),
    ("stat_attorneys.png", "Legal Firms", "Bad Leads", "Hours wasted on 'free advice'.", "AI Screening", "24/7 Qualification of high-value cases."),
    ("stat_accountants.png", "Accounting", "Chasing Docs", "Emailing clients for W2s repeatedly.", "Secure Portal", "Auto-follow up request system."),
    ("stat_financial_managers.png", "Financial Advisors", "Scheduling Tag", "Back-and-forth email chains.", "Instant Booking", "Syncs with Outlook/Cal instantly."),
    ("stat_real_estate_brokers.png", "Real Estate", "Slow Response", "Lead goes cold in 5 minutes.", "Instant Connect", "Web form triggers immediate phone call."),
    ("stat_auto_mechanics.png", "Auto Repair", "Low Tickets", "Just doing the oil change.", "Upsell SMS", "Text photos of dirty filters to approve work."),
    ("stat_window_tinting.png", "Auto Styling", "Price Shoppers", "Tire kickers asking 'how much'.", "Visual Quoter", "Show value via simulator before price."),
    ("stat_restaurants.png", "Restaurants", "Empty Tables", "Slow Tuesday nights.", "Reservation AI", "Waitlist management and VIP promos."),
]

if __name__ == "__main__":
    for item in data:
        create_comparison_graphic(*item)
