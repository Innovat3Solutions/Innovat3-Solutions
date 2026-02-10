import os
import re

# The Standard Footer Template (Child Version - relative paths for pages/*/*.html)
# Note: Paths are ../../ for root assets and ../x for sibling directories
FOOTER_TEMPLATE = """<footer class="footer">
    <div class="container">
        <div class="footer-grid">
            <!-- Column 1: Brand -->
            <div class="footer-col" style="flex: 2;">
                <a href="../../index.html" class="footer-logo">
                    <img src="../../images/Innovat3-logos/innovate-logo-white-transparent.png" alt="Innovate Solutions" class="logo-full" style="height: 30px;">
                </a>
                <p>Modernizing Miami one automated workflow at a time.</p>
            </div>

            <!-- Column 2: Services -->
            <div class="footer-col">
                <h4>Services</h4>
                <a href="../services/voice-ai.html">Voice AI Agents</a>
                <a href="../services/custom-apps.html">Custom Apps</a>
                <a href="../services/review-automation.html">Review Management</a>
                <a href="../services/private-ai-infra.html">Private AI</a>
                <a href="../services/lead-database.html">Lead Capture</a>
                <a href="../services/data-intelligence.html">Data Intelligence</a>
                <a href="../services/workflow-automation.html">Workflow Automation</a>
                <a href="../services/consulting.html">Growth Consulting</a>
            </div>

            <!-- Column 3: Industries -->
            <div class="footer-col">
                <h4>Industries</h4>
                <a href="../niches/general-contractors.html">Home Services</a>
                <a href="../niches/family-practice-doctors.html">Medical & Health</a>
                <a href="../niches/attorneys-and-law-firms.html">Legal & Prof.</a>
                <a href="../niches/hair-salons-and-stylists.html">Beauty & Wellness</a>
                <a href="../niches/restaurants.html">Retail & Hospitality</a>
                <a href="../niches/auto-mechanics-and-repair-shops.html">Automotive</a>
                <a href="../niches/real-estate-brokers.html">Real Estate</a>
                <a href="../../index.html#niches" style="color: var(--primary-color); font-weight: 600; margin-top: 8px;">View All Industries &rarr;</a>
            </div>

            <!-- Column 4: Resources -->
            <div class="footer-col">
                <h4>Company</h4>
                <a href="../../index.html#process">Process</a>
                <a href="../../index.html#about">About</a>
                <a href="../../index.html#contact">Contact</a>
                <a href="mailto:hello@innovat3solutions.com">hello@innovat3solutions.com</a>
                <p style="margin-top: 10px; opacity: 0.6;">Miami, FL</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Innovate Solutions. All rights reserved.</p>
        </div>
    </div>
</footer>"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICES_DIR = os.path.join(BASE_DIR, "pages", "services")
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "niche_template.html")

def update_footer(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find footer. Handles various attributes and newlines.
        # We look for <footer class="footer"... > ... </footer>
        pattern = re.compile(r'<footer class="footer".*?</footer>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(FOOTER_TEMPLATE, content)
            
            # Write only if changed
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {os.path.basename(filepath)}")
            else:
                print(f"No changes needed: {os.path.basename(filepath)}")
        else:
            print(f"Warning: No footer found in {os.path.basename(filepath)}")

    except Exception as e:
        print(f"Error updating {filepath}: {e}")

def main():
    # Update Service Pages
    if os.path.exists(SERVICES_DIR):
        for filename in os.listdir(SERVICES_DIR):
            if filename.endswith(".html"):
                update_footer(os.path.join(SERVICES_DIR, filename))
    
    # Update Niche Template
    if os.path.exists(TEMPLATE_PATH):
        update_footer(TEMPLATE_PATH)

if __name__ == "__main__":
    main()
