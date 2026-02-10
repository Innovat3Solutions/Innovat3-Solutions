#!/usr/bin/env python3
"""
Update all pages with the new unified contact section
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

                <!-- Testimonials -->
                <div class="contact-testimonials">
                    <div class="contact-testimonial">
                        <div class="testimonial-header">
                            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop" alt="Customer" class="testimonial-avatar">
                            <div class="testimonial-badge">
                                <i data-lucide="quote" size="14"></i>
                            </div>
                        </div>
                        <p>We've gained a 360-degree view of our customers. The unified profiles allow us to personalize interactions, resulting in higher customer satisfaction and increased loyalty.</p>
                    </div>

                    <div class="contact-testimonial">
                        <div class="testimonial-header">
                            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop" alt="Customer" class="testimonial-avatar">
                            <div class="testimonial-badge">
                                <i data-lucide="quote" size="14"></i>
                            </div>
                        </div>
                        <p>Now, we truly understand our customers. These unified profiles enable personalized interactions, boosting satisfaction and strengthening loyalty.</p>
                    </div>
                </div>

                <!-- Features -->
                <div class="contact-features">
                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="clock" size="24"></i>
                        </div>
                        <h4>Customer History</h4>
                        <p>Analyze customer behavior across product lines</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="trending-up" size="24"></i>
                        </div>
                        <h4>Actionable Insights</h4>
                        <p>Employ predictive analytics to optimize sales pipelines</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="grid-3x3" size="24"></i>
                        </div>
                        <h4>Identify Patterns</h4>
                        <p>Utilize live data to improve conversion rates</p>
                    </div>

                    <div class="contact-feature">
                        <div class="contact-feature-icon">
                            <i data-lucide="search" size="24"></i>
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

def update_homepage():
    """Update the homepage contact section."""
    homepage = Path("/Users/juandelossantos/Desktop/Skills Master/index.html")

    with open(homepage, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the current contact section
    # Look for the section with "Ready to turn chaos into calm?"
    pattern = r'<section[^>]*id="contact"[^>]*>.*?</section>'

    new_contact_html = generate_contact_html("homepage")

    # Replace the section
    content = re.sub(pattern, new_contact_html, content, flags=re.DOTALL)

    with open(homepage, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✓ Homepage updated")

def main():
    """Main function."""
    print("=" * 80)
    print("UPDATING CONTACT SECTIONS ACROSS ALL PAGES")
    print("=" * 80)
    print()

    # Step 1: Update homepage
    print("Step 1: Updating homepage...")
    update_homepage()
    print()

    print("=" * 80)
    print("HOMEPAGE COMPLETE")
    print("=" * 80)
    print()
    print("Next steps:")
    print("  - Service pages need to be updated")
    print("  - Industry pages need to be updated")
    print("  - Blog posts need to be updated")
    print()

if __name__ == "__main__":
    main()
