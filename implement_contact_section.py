#!/usr/bin/env python3
"""
Implement the new Contact Us section across all pages
"""

import re
from pathlib import Path

# CSS for the contact section (to be added to styles.css)
CONTACT_CSS = """
/* Unified Contact Section */
.unified-contact-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
    position: relative;
    overflow: hidden;
}

.unified-contact-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background:
        linear-gradient(135deg, rgba(132, 204, 22, 0.03) 0%, transparent 50%),
        radial-gradient(circle at 20% 80%, rgba(132, 204, 22, 0.05) 0%, transparent 50%);
    pointer-events: none;
}

.unified-contact-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 40px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
    position: relative;
    z-index: 1;
}

/* Left Content */
.contact-left-content h2 {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 24px;
    color: #0f172a;
}

.contact-left-content p {
    font-size: 1.2rem;
    line-height: 1.7;
    color: #64748b;
    margin-bottom: 32px;
}

.contact-progress-dots {
    display: flex;
    gap: 6px;
    margin-bottom: 32px;
}

.contact-progress-dots .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #84CC16;
}

.contact-progress-dots .dot.empty {
    background: #e2e8f0;
}

.contact-learn-btn {
    display: inline-block;
    padding: 14px 32px;
    background: #0f172a;
    color: white;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    margin-bottom: 48px;
    transition: all 0.3s ease;
}

.contact-learn-btn:hover {
    background: #1e293b;
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.2);
}

/* Testimonials */
.contact-testimonials {
    display: flex;
    gap: 24px;
    margin-bottom: 48px;
}

.contact-testimonial {
    flex: 1;
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.testimonial-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}

.testimonial-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
}

.testimonial-badge {
    width: 24px;
    height: 24px;
    background: #84CC16;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: -8px;
    border: 2px solid white;
}

.contact-testimonial p {
    font-size: 0.95rem;
    font-style: italic;
    color: #475569;
    line-height: 1.6;
    margin: 0;
}

/* Feature Grid */
.contact-features {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
}

.contact-feature {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.contact-feature-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #84CC16 0%, #65a30d 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.contact-feature h4 {
    font-size: 1.1rem;
    font-weight: 700;
    color: #0f172a;
    margin: 0;
}

.contact-feature p {
    font-size: 0.95rem;
    color: #64748b;
    margin: 0;
    line-height: 1.5;
}

/* Right Form */
.contact-form-wrapper {
    background: white;
    padding: 48px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.1);
}

.contact-form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

.contact-form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.contact-form-group.full-width {
    grid-column: 1 / -1;
}

.contact-form-group label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #0f172a;
}

.contact-form-group input,
.contact-form-group select,
.contact-form-group textarea {
    padding: 14px 16px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease;
}

.contact-form-group input:focus,
.contact-form-group select:focus,
.contact-form-group textarea:focus {
    outline: none;
    border-color: #84CC16;
    box-shadow: 0 0 0 3px rgba(132, 204, 22, 0.1);
}

.contact-form-group textarea {
    min-height: 120px;
    resize: vertical;
}

.contact-submit-btn {
    width: 100%;
    padding: 16px;
    background: linear-gradient(135deg, #84CC16 0%, #65a30d 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 12px;
}

.contact-submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(132, 204, 22, 0.3);
}

/* Responsive */
@media (max-width: 1024px) {
    .unified-contact-container {
        grid-template-columns: 1fr;
        gap: 60px;
    }

    .contact-left-content h2 {
        font-size: 2.5rem;
    }

    .contact-features {
        grid-template-columns: 1fr;
    }

    .contact-testimonials {
        flex-direction: column;
    }
}

@media (max-width: 768px) {
    .unified-contact-section {
        padding: 60px 0;
    }

    .unified-contact-container {
        padding: 0 20px;
    }

    .contact-form-wrapper {
        padding: 32px 24px;
    }

    .contact-form-row {
        grid-template-columns: 1fr;
    }

    .contact-left-content h2 {
        font-size: 2rem;
    }
}
"""

# HTML for the contact section
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

    return f'''
    <!-- Unified Contact Section -->
    <section class="unified-contact-section">
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

def main():
    """Main function."""
    print("=" * 80)
    print("CONTACT SECTION IMPLEMENTATION PLAN")
    print("=" * 80)
    print()
    print("This script prepares the contact section component.")
    print()
    print("CSS has been generated - needs to be added to styles.css")
    print("HTML templates created for different contexts:")
    print("  - Homepage")
    print("  - Service pages")
    print("  - Industry pages")
    print("  - Blog posts")
    print()

    # Save CSS to a file
    css_file = Path("/Users/juandelossantos/Desktop/Skills Master/contact_section.css")
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(CONTACT_CSS)
    print(f"✓ CSS saved to: {css_file}")

    # Save HTML templates
    html_file = Path("/Users/juandelossantos/Desktop/Skills Master/contact_section_templates.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write("<!-- HOMEPAGE VERSION -->\n")
        f.write(generate_contact_html("homepage"))
        f.write("\n\n<!-- SERVICE PAGE VERSION -->\n")
        f.write(generate_contact_html("service"))
        f.write("\n\n<!-- INDUSTRY PAGE VERSION -->\n")
        f.write(generate_contact_html("industry"))
        f.write("\n\n<!-- BLOG POST VERSION -->\n")
        f.write(generate_contact_html("blog"))
    print(f"✓ HTML templates saved to: {html_file}")
    print()

if __name__ == "__main__":
    main()
