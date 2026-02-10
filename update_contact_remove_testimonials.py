#!/usr/bin/env python3
"""
Update contact sections - remove testimonials and add custom icons
"""

import re
from pathlib import Path

def generate_contact_html(context="homepage"):
    """Generate contact section HTML based on context."""

    if context == "homepage":
        title = "Manage customers across the Lifetime of the product cycle"
        description = "Build rich, unified profiles with purchase history, preferences, support interactions, and more so you can personalize experiences and boost retention at every touchpoint."
    elif context == "service":
        title = "Ready to transform your business?"
        description = "Let's discuss how our solutions can help you automate workflows, boost efficiency, and drive growth for your business."
    elif context == "industry":
        title = "See these results in your business"
        description = "Join hundreds of businesses who've transformed their operations with automation. Let's create a custom solution for your specific needs."
    elif context == "blog":
        title = "Want similar results?"
        description = "Let's discuss how we can implement these proven strategies for your business and help you achieve comparable growth."
    else:
        title = "Let's grow your business together"
        description = "Schedule a free consultation to discover how automation can transform your operations and drive real results."

    return f'''    <!-- Unified Contact Section -->
    <section class="unified-contact-section" id="contact">
        <div class="unified-contact-container">
            <!-- Left Content -->
            <div class="contact-left-content">
                <div class="contact-progress-dots">
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot empty"></span>
                    <span class="dot empty"></span>
                    <span class="dot empty"></span>
                </div>

                <h2>{title}</h2>
                <p>{description}</p>

                <a href="#" class="contact-learn-btn">Learn More</a>

                <!-- Features -->
                <div class="contact-features">
                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="history" size="24"></i>
                        </div>
                        <h4>Customer History</h4>
                        <p>Analyze customer behavior across product lines</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="bar-chart-3" size="24"></i>
                        </div>
                        <h4>Actionable Insights</h4>
                        <p>Employ predictive analytics to optimize sales pipelines</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="layers" size="24"></i>
                        </div>
                        <h4>Identify Patterns</h4>
                        <p>Utilize live data to improve conversion rates</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="target" size="24"></i>
                        </div>
                        <h4>Predictive Analysis</h4>
                        <p>Employ real-time data to refine marketing strategies</p>
                    </div>
                </div>
            </div>

            <!-- Right Form -->
            <div class="contact-form-wrapper">
                <form id="unified-contact-form" action="#" method="POST">
                    <div class="contact-form-row">
                        <div class="contact-form-group">
                            <label for="firstName">First Name</label>
                            <input type="text" id="firstName" name="firstName" placeholder="James..." required>
                        </div>

                        <div class="contact-form-group">
                            <label for="lastName">Last Name</label>
                            <input type="text" id="lastName" name="lastName" placeholder="Smith..." required>
                        </div>
                    </div>

                    <div class="contact-form-row">
                        <div class="contact-form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="robertapouros@gmail.com" required>
                        </div>

                        <div class="contact-form-group">
                            <label for="country">Country</label>
                            <select id="country" name="country" required>
                                <option value="USA">🇺🇸 USA</option>
                                <option value="Canada">🇨🇦 Canada</option>
                                <option value="UK">🇬🇧 United Kingdom</option>
                                <option value="Australia">🇦🇺 Australia</option>
                                <option value="Other">🌍 Other</option>
                            </select>
                        </div>
                    </div>

                    <div class="contact-form-group full-width">
                        <label for="role">Your Role</label>
                        <select id="role" name="role" required>
                            <option value="">Select your role</option>
                            <option value="Business Owner">Business Owner</option>
                            <option value="Manager">Manager</option>
                            <option value="Director">Director</option>
                            <option value="C-Level">C-Level Executive</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>

                    <div class="contact-form-group full-width">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" placeholder="Enter message..." required></textarea>
                    </div>

                    <button type="submit" class="contact-submit-btn">Contact Us</button>
                </form>
            </div>
        </div>
    </section>
'''

def update_page_contact_section(filepath, context):
    """Update a single page's contact section."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old contact section and replace with new one
    pattern = r'<section class="unified-contact-section"[^>]*>.*?</section>'

    new_contact_html = generate_contact_html(context)

    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_contact_html, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    return False

def update_homepage():
    """Update homepage."""
    homepage = Path("/Users/juandelossantos/Desktop/Skills Master/index.html")
    if update_page_contact_section(homepage, "homepage"):
        print("  ✓ Homepage")

def update_service_pages():
    """Update all service pages."""
    service_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/services")
    updated = 0

    for service_file in service_dir.glob("*.html"):
        if update_page_contact_section(service_file, "service"):
            updated += 1
            print(f"  ✓ {service_file.name}")

    return updated

def update_industry_pages():
    """Update all industry pages."""
    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = 0

    for industry_file in industry_dir.glob("*.html"):
        if update_page_contact_section(industry_file, "industry"):
            updated += 1
            print(f"  ✓ {industry_file.name}")

    return updated

def update_blog_posts():
    """Update all blog posts."""
    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = 0

    for blog_file in blog_dir.glob("*.html"):
        if blog_file.name.startswith("_"):
            continue

        if update_page_contact_section(blog_file, "blog"):
            updated += 1
            print(f"  ✓ {blog_file.name}")

    return updated

def main():
    """Main function."""
    print("=" * 80)
    print("UPDATING CONTACT SECTIONS - REMOVING TESTIMONIALS")
    print("=" * 80)
    print()

    print("Step 1: Updating homepage...")
    update_homepage()
    print()

    print("Step 2: Updating service pages...")
    service_count = update_service_pages()
    print(f"  → {service_count} service pages updated")
    print()

    print("Step 3: Updating industry pages...")
    industry_count = update_industry_pages()
    print(f"  → {industry_count} industry pages updated")
    print()

    print("Step 4: Updating blog posts...")
    blog_count = update_blog_posts()
    print(f"  → {blog_count} blog posts updated")
    print()

    print("=" * 80)
    print("UPDATE COMPLETE")
    print("=" * 80)
    print()
    print("Changes made:")
    print("  ✓ Removed testimonials section")
    print("  ✓ Updated icons: history, bar-chart-3, layers, target")
    print("  ✓ Cleaner layout with more space for features")
    print()

if __name__ == "__main__":
    main()
