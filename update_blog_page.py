#!/usr/bin/env python3
"""
Update the blog page with all 75 case study posts organized by industry
"""

import re
from pathlib import Path

# Industry to category mapping
INDUSTRY_CATEGORIES = {
    'pool-cleaners-and-maintenance': 'home-services',
    'pool-contractors-and-construction': 'home-services',
    'landscaping-and-lawn-care': 'home-services',
    'hvac-services': 'home-services',
    'general-contractors': 'home-services',
    'window-installers': 'home-services',
    'plumbers': 'home-services',
    'painters': 'home-services',
    'electricians': 'home-services',
    'property-management': 'home-services',
    'dentists-and-orthodontists': 'health',
    'family-practice-doctors': 'health',
    'veterinarians': 'health',
    'med-spas-and-laser-facilities': 'health',
    'hair-salons-and-stylists': 'health',
    'barbershops': 'health',
    'nail-salons': 'health',
    'pet-groomers': 'health',
    'attorneys-and-law-firms': 'professional',
    'accountants-and-cpas': 'professional',
    'financial-managers-and-advisors': 'professional',
    'real-estate-brokers': 'professional',
    'auto-mechanics-and-repair-shops': 'retail',
    'window-tinting-and-auto-detail': 'retail',
    'restaurants': 'retail',
}

# Display names for industries
INDUSTRY_NAMES = {
    'pool-cleaners-and-maintenance': 'Pool Cleaners',
    'pool-contractors-and-construction': 'Pool Construction',
    'landscaping-and-lawn-care': 'Landscaping',
    'hvac-services': 'HVAC Services',
    'general-contractors': 'General Contractors',
    'window-installers': 'Window Installers',
    'plumbers': 'Plumbers',
    'painters': 'Painters',
    'electricians': 'Electricians',
    'property-management': 'Property Management',
    'dentists-and-orthodontists': 'Dentists',
    'family-practice-doctors': 'Family Practice',
    'veterinarians': 'Veterinarians',
    'med-spas-and-laser-facilities': 'Med Spas',
    'hair-salons-and-stylists': 'Hair Salons',
    'barbershops': 'Barbershops',
    'nail-salons': 'Nail Salons',
    'pet-groomers': 'Pet Groomers',
    'attorneys-and-law-firms': 'Attorneys',
    'accountants-and-cpas': 'Accountants',
    'financial-managers-and-advisors': 'Financial Advisors',
    'real-estate-brokers': 'Real Estate',
    'auto-mechanics-and-repair-shops': 'Auto Mechanics',
    'window-tinting-and-auto-detail': 'Auto Detail',
    'restaurants': 'Restaurants',
}

# Blog type info
BLOG_TYPES = {
    'voice-ai-case-study': {
        'tag': 'Voice AI',
        'tag_class': 'tag-tech',
        'title_suffix': 'Doubles Bookings with Voice AI',
        'excerpt': 'How 24/7 AI voice agents eliminated missed calls and increased customer bookings.'
    },
    'automation-success': {
        'tag': 'Automation',
        'tag_class': 'tag-industry',
        'title_suffix': 'Saves Time with Automation',
        'excerpt': 'Automated workflows streamline operations and free up staff for high-value work.'
    },
    'review-management': {
        'tag': 'Reviews',
        'tag_class': 'tag-growth',
        'title_suffix': 'Grows Reviews by 300%',
        'excerpt': 'Automated review collection drives more customer feedback and improves online reputation.'
    },
}

def generate_blog_cards():
    """Generate HTML for all blog cards."""
    cards_html = []

    # Get all blog posts sorted by industry
    for industry_slug, category in INDUSTRY_CATEGORIES.items():
        industry_name = INDUSTRY_NAMES[industry_slug]

        # Generate 3 cards per industry (voice-ai, automation, review-management)
        for blog_type, type_info in BLOG_TYPES.items():
            blog_filename = f"{industry_slug}-{blog_type}.html"
            blog_path = f"../blog/case-studies/{blog_filename}"

            card_html = f'''
        <!-- {industry_name} - {type_info['tag']} -->
        <a href="{blog_path}" class="blog-card" data-category="{category}">
            <div class="card-image-wrapper">
                <img src="../assets/niche_images/{industry_slug.replace('-and-', '_').replace('-', '_')}.png"
                     alt="{industry_name}" class="card-image"
                     onerror="this.src='https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=800&auto=format&fit=crop'">
            </div>
            <div class="card-content">
                <div class="card-meta">
                    <span class="card-tag {type_info['tag_class']}">{type_info['tag']}</span>
                    <span class="card-date">Feb 03, 2026</span>
                </div>
                <h3 class="card-title">{industry_name} {type_info['title_suffix']}</h3>
                <p class="card-excerpt">{type_info['excerpt']}</p>
                <div class="card-footer">
                    <span class="author-name">Innovat3 Team</span>
                    <i data-lucide="arrow-right" class="card-arrow"></i>
                </div>
            </div>
        </a>'''

            cards_html.append(card_html)

    return '\n'.join(cards_html)

def update_blog_page():
    """Update blog.html with all case study cards."""
    blog_file = Path("/Users/juandelossantos/Desktop/Skills Master/pages/blog.html")

    with open(blog_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate all blog cards
    all_cards = generate_blog_cards()

    # Replace the existing blog cards section
    # Find the bento grid and replace everything between the opening and closing div
    pattern = r'(<div class="blog-bento-grid">)(.*?)(</div>\s*<!-- Expanded Footer)'

    replacement = f'''\\1

{all_cards}

    \\3'''

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(blog_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated blog.html with {len(INDUSTRY_CATEGORIES) * len(BLOG_TYPES)} case study cards")
    print(f"\nCards organized by category:")
    print(f"  - Home Services: {len([c for c in INDUSTRY_CATEGORIES.values() if c == 'home-services']) * 3} cards")
    print(f"  - Health & Medical: {len([c for c in INDUSTRY_CATEGORIES.values() if c == 'health']) * 3} cards")
    print(f"  - Professional: {len([c for c in INDUSTRY_CATEGORIES.values() if c == 'professional']) * 3} cards")
    print(f"  - Retail & Auto: {len([c for c in INDUSTRY_CATEGORIES.values() if c == 'retail']) * 3} cards")

if __name__ == "__main__":
    update_blog_page()
