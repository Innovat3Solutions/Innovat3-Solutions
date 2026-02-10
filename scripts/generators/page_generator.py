
import os
import re

# Source file for niches
SOURCE_FILE = "business_niches.md"
TEMPLATE_FILE = "pages/services/voice-ai.html"
OUTPUT_DIR = "pages/niches/"

# Base template variable
BASE_TEMPLATE = ""

def load_template():
    global BASE_TEMPLATE
    try:
        with open(TEMPLATE_FILE, "r") as f:
            BASE_TEMPLATE = f.read()
    except FileNotFoundError:
        print(f"Error: Template file {TEMPLATE_FILE} not found.")
        exit(1)

def parse_niches():
    try:
        with open(SOURCE_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Source file {SOURCE_FILE} not found.")
        exit(1)

    # Regex to find each niche section
    # Matches "### N. [Name]" -> stats/pain points
    niches = []
    
    # Simple state machine parser
    lines = content.split('\n')
    current_niche = {}
    
    for line in lines:
        line = line.strip()
        
        # Check for header "### N. Name"
        header_match = re.match(r'^### \d+\.\s+(.+)', line)
        if header_match:
            # Save previous if exists
            if current_niche:
                niches.append(current_niche)
            
            # Start new
            current_niche = {
                "name": header_match.group(1),
                "pain_point": "",
                "stat": "",
                "opportunity": ""
            }
            continue
            
        if not current_niche:
            continue
            
        # Parse content
        if line.startswith('*   **Pain Point:**'):
            current_niche["pain_point"] = line.replace('*   **Pain Point:**', '').strip()
        elif line.startswith('*   **Real Stat:**'):
            current_niche["stat"] = line.replace('*   **Real Stat:**', '').strip()
        elif line.startswith('*   **The Opportunity:**'):
            current_niche["opportunity"] = line.replace('*   **The Opportunity:**', '').strip()

    # Append last one
    if current_niche:
        niches.append(current_niche)
        
    return niches

def slugify(text):
    return text.lower().replace('&', 'and').replace(' ', '-').replace(',', '').replace('.', '')

def generate_pages(niches):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for niche in niches:
        slug = slugify(niche['name'])
        filename = f"{OUTPUT_DIR}{slug}.html"
        
        # Inject content into template
        # Note: This is a simple string replacement. A proper template engine like Jinja2 would be better,
        # but avoiding external dependencies for this quick script.
        
        page_html = BASE_TEMPLATE
        
        # Title
        page_html = page_html.replace("Voice AI Agents | Innovat3 Solutions", f"{niche['name']} Automation | Innovat3 Solutions")
        page_html = page_html.replace("Service Spotlight", "Industry Spotlight")
        page_html = page_html.replace("Voice AI Agents", niche['name'])
        
        # Values
        page_html = page_html.replace("The \"Missed Call\" Epidemic", f"The Challenges in {niche['name']}")
        page_html = page_html.replace("The Splash & Dash", "The Core Pain Point")
        page_html = page_html.replace("Pool techs and contractors in the field miss 30% of calls because their hands are full.", niche['pain_point'])
        
        page_html = page_html.replace("The 5-Minute Rule", "Industry Statistics")
        page_html = page_html.replace("Responding to a lead in 5 minutes increases conversion by 21x. After 30 minutes, it's dead.", niche['stat'])
        
        page_html = page_html.replace("The Seasonal Crush", "The Opportunity")
        page_html = page_html.replace("HVAC and Retail see call volume spikes they can't staff for, losing massive revenue.", niche['opportunity'])
        
        # Fix relative paths since we are going one level deeper (pages/niches/x.html vs pages/services/x.html)
        # Actually they are same depth: pages/services/ vs pages/niches/ so ../../ is correct.
        
        with open(filename, "w") as f:
            f.write(page_html)
            print(f"Generated: {filename}")

if __name__ == "__main__":
    load_template()
    niches = parse_niches()
    generate_pages(niches)
    print(f"Successfully generated {len(niches)} niche pages.")
