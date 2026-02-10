import os
import re

# The standard navbar content with relative paths for pages/services/* and pages/niches/*
# Note: Using shiny-button to match the premium design requirement
NAVBAR_HTML = """    <!-- Nav -->
    <nav class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../images/Innovat3-logos/innovate-logo-black-transparent.png" alt="Innovate Solutions"
                    class="logo-full">
            </a>

            <div class="nav-links">
                <div class="nav-item dropdown">
                    <a href="../../index.html#services" class="dropdown-trigger">Services <span
                            class="dropdown-arrow">▼</span></a>
                    <div class="dropdown-menu">
                        <a href="../services/voice-ai.html">Voice AI Agents</a>
                        <a href="../services/custom-apps.html">Custom Apps</a>
                        <a href="../services/review-automation.html">Review Management</a>
                        <a href="../services/private-ai-infra.html">Private AI</a>
                        <a href="../services/lead-database.html">Lead Capture</a>
                        <a href="../services/data-intelligence.html">Data Intelligence</a>
                        <a href="../services/workflow-automation.html">Workflow Automations</a>
                        <a href="../services/consulting.html">Growth Consulting</a>
                    </div>
                </div>
                <div class="nav-item dropdown">
                    <a href="../../index.html#niches" class="dropdown-trigger">Industries <span class="dropdown-arrow">▼</span></a>
                    <div class="dropdown-menu niche-dropdown-menu">
                        <div class="niche-dropdown-grid">
                            <!-- Column 1: Home Services -->
                            <div class="niche-col">
                                <h4>Home & Property</h4>
                                <a href="../niches/pool-cleaners-and-maintenance.html">Pool Cleaners</a>
                                <a href="../niches/pool-contractors-and-construction.html">Pool Construction</a>
                                <a href="../niches/landscaping-and-lawn-care.html">Landscaping</a>
                                <a href="../niches/hvac-services.html">HVAC Services</a>
                                <a href="../niches/general-contractors.html">General Contractors</a>
                                <a href="../niches/window-installers.html">Window Installers</a>
                                <a href="../niches/plumbers.html">Plumbers</a>
                                <a href="../niches/painters.html">Painters</a>
                                <a href="../niches/electricians.html">Electricians</a>
                                <a href="../niches/property-management.html">Property Management</a>
                            </div>

                            <!-- Column 2: Health & Beauty -->
                            <div class="niche-col">
                                <h4>Health & Medical</h4>
                                <a href="../niches/dentists-and-orthodontists.html">Dentists</a>
                                <a href="../niches/family-practice-doctors.html">Family Practice</a>
                                <a href="../niches/veterinarians.html">Veterinarians</a>
                                <a href="../niches/med-spas-and-laser-facilities.html">Med Spas</a>

                                <h4 class="mt-sm">Beauty & Care</h4>
                                <a href="../niches/hair-salons-and-stylists.html">Hair Salons</a>
                                <a href="../niches/barbershops.html">Barbershops</a>
                                <a href="../niches/nail-salons.html">Nail Salons</a>
                                <a href="../niches/pet-groomers.html">Pet Groomers</a>
                            </div>

                            <!-- Column 3: Professional & Other -->
                            <div class="niche-col">
                                <h4>Professional Services</h4>
                                <a href="../niches/attorneys-and-law-firms.html">Attorneys</a>
                                <a href="../niches/accountants-and-cpas.html">Accountants & CPAs</a>
                                <a href="../niches/financial-managers-and-advisors.html">Financial Advisors</a>
                                <a href="../niches/real-estate-brokers.html">Real Estate Brokers</a>

                                <h4 class="mt-sm">Retail & Auto</h4>
                                <a href="../niches/auto-mechanics-and-repair-shops.html">Auto Mechanics</a>
                                <a href="../niches/window-tinting-and-auto-detail.html">Auto Detail/Tint</a>
                                <a href="../niches/restaurants.html">Restaurants</a>
                            </div>
                        </div>
                    </div>
                </div>
                <a href="../../index.html#process">Process</a>
                <a href="../../index.html#about">About</a>
            </div>

            <div class="nav-actions">
                <a href="../../index.html#contact" class="btn btn-primary shiny-button">Get Started</a>
            </div>

            <!-- Mobile Menu Toggle -->
            <button class="mobile-toggle" aria-label="Toggle Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>"""

def replace_navbar(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the nav block
        # It looks for <nav class="navbar"...> ... </nav>
        # Dotall to match across lines
        pattern = re.compile(r'(<!--\s*Nav\s*-->\s*)?<nav class="navbar".*?</nav>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(NAVBAR_HTML, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"Navbar not found in: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Update Template
    template_path = os.path.join(base_dir, 'templates', 'niche_template.html')
    replace_navbar(template_path)

    # 2. Update Service Pages
    services_dir = os.path.join(base_dir, 'pages', 'services')
    if os.path.exists(services_dir):
        for filename in os.listdir(services_dir):
            if filename.endswith(".html"):
                replace_navbar(os.path.join(services_dir, filename))
    
    print("Navbar standardization complete.")

if __name__ == "__main__":
    main()
