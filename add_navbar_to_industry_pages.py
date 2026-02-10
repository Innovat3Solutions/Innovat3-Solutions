#!/usr/bin/env python3
"""
Add navigation bar with Blog link to all industry pages
"""

import re
from pathlib import Path

# Navigation HTML for industry pages (with correct relative paths)
NAVBAR_HTML = '''    <nav class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../images/Innovat3-logos/innovate-logo-black-transparent.png" alt="Innovate Solutions"
                    class="logo-full">
            </a>

            <div class="nav-links">
                <div class="nav-item dropdown">
                    <a href="#services" class="dropdown-trigger">Services <span
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
                        <a href="../services/web-development.html">Web Development</a>
                    </div>
                </div>
                <div class="nav-item dropdown">
                    <a href="#niches" class="dropdown-trigger">Industries <span
                            class="dropdown-arrow">▼</span></a>
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
                <a href="../blog.html">Blog</a>
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
    </nav>

'''

def add_navbar_to_industry_page(filepath):
    """Add navigation bar to an industry page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if navbar already exists
    if '<nav class="navbar"' in content:
        return False

    # Find the <body> tag and add navbar right after it
    pattern = r'(<body>)'

    if re.search(pattern, content):
        content = re.sub(
            pattern,
            r'\1\n' + NAVBAR_HTML,
            content,
            count=1
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING NAVIGATION BAR TO ALL INDUSTRY PAGES")
    print("=" * 80)
    print()

    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = []

    for industry_file in sorted(industry_dir.glob("*.html")):
        try:
            if add_navbar_to_industry_page(industry_file):
                updated.append(industry_file.name)
                print(f"  ✓ {industry_file.name}")
            else:
                print(f"  ⊙ {industry_file.name} (already has navbar)")
        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {len(updated)}")
    print()
    print("Navigation bar now includes:")
    print("  ✓ Services dropdown (all 9 services)")
    print("  ✓ Industries dropdown (all 25 industries)")
    print("  ✓ Blog link")
    print("  ✓ Process link")
    print("  ✓ About link")
    print("  ✓ Get Started button")
    print("  ✓ Mobile menu toggle")
    print()
    print("All industry pages now have consistent navigation with the rest of the site.")
    print()

if __name__ == "__main__":
    main()
