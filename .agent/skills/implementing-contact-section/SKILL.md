---
name: implementing-contact-section
description: Generates a high-converting, "Monotree" style Contact Us section with a 2-column layout (Value Prop + Form) and feature grid. Use when the user asks to add a contact section or "Contact Us" area to any page.
---

# Implementing Contact Section Standard

## When to use this skill
- User asks to add a "Contact Us" section.
- User wants to implement the standard lead capture form at the bottom of a page.
- User references the "Manage customers across the Lifetime" design.

## Workflow
- [ ] Verify `lucide` icons are available in the page (`<script src="https://unpkg.com/lucide@latest"></script>`).
- [ ] Insert the HTML structure before the footer.
- [ ] Add the CSS styling to the page's `<style>` block or a dedicated CSS file.
- [ ] Initialize Lucide icons if not already auto-initialized.

## HTML Structure

Insert this HTML block where the contact section should appear (typically before the footer):

```html
<!-- CONTACT & LEAD CAPTURE SECTION -->
<section class="section contact-section" id="contact">
    <div class="container">
        <div class="contact-grid">
            <!-- Left Column: Value Proposition -->
            <div class="contact-content">
                <div class="contact-decoration">
                    <span class="dots">❖❖❖❖❖❖❖❖</span>
                    <span class="diamonds">♢♢♢♢♢♢</span>
                </div>
                
                <h2 class="contact-headline">
                    Manage customers<br>
                    across the <span class="highlight-merriweather">Lifetime</span><br>
                    of the product cycle
                </h2>
                
                <p class="contact-sub">
                    Build rich, unified profiles with purchase history, preferences, support interactions, and more so you can personalize experiences and boost retention at every touchpoint.
                </p>

                <div class="contact-actions">
                    <a href="#learn-more" class="btn btn-secondary">Learn More</a>
                </div>

                <!-- Social Proof / Trust -->
                <div class="contact-proof">
                    <div class="proof-avatars">
                         <!-- Placeholder avatars - replace with specific assets if available -->
                        <img src="https://i.pravatar.cc/100?img=12" alt="User" class="avatar">
                        <img src="https://i.pravatar.cc/100?img=33" alt="User" class="avatar">
                    </div>
                    <div class="proof-text">
                        <p>
                            <em>"We've gained a 360-degree view of our customers. The unified profiles allow us to personalize interactions."</em>
                        </p>
                    </div>
                </div>
            </div>

            <!-- Right Column: Form -->
            <div class="contact-form-wrapper">
                <form class="contact-form" onsubmit="event.preventDefault();">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="fname">First Name</label>
                            <input type="text" id="fname" placeholder="James..." required>
                        </div>
                        <div class="form-group">
                            <label for="lname">Last Name</label>
                            <input type="text" id="lname" placeholder="Smith..." required>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" placeholder="name@company.com" required>
                        </div>
                        <div class="form-group">
                            <label for="country">Country</label>
                            <div class="select-wrapper">
                                <span class="flag-icon">🇺🇸</span>
                                <select id="country">
                                    <option>USA</option>
                                    <option>Canada</option>
                                    <option>UK</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="role">Your Role</label>
                        <select id="role">
                            <option value="">Select your role</option>
                            <option>Executive</option>
                            <option>Manager</option>
                            <option>Developer</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" rows="4" placeholder="Enter message..."></textarea>
                    </div>

                    <div class="form-submit">
                        <button type="submit" class="btn btn-primary shiny-button">Contact Us</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Bottom Feature Grid -->
        <div class="contact-features">
            <div class="feature-item">
                <div class="feature-icon"><i data-lucide="clock"></i></div>
                <h4>Customer History</h4>
                <p>Analyze customer behavior across product lines</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon"><i data-lucide="bar-chart-2"></i></div>
                <h4>Actionable Insights</h4>
                <p>Employ predictive analytics to optimize sales pipelines</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon"><i data-lucide="layout-grid"></i></div>
                <h4>Identify Patterns</h4>
                <p>Utilize live data to improve conversion rates</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon"><i data-lucide="search"></i></div>
                <h4>Predictive Analysis</h4>
                <p>Employ real-time data to refine marketing strategies</p>
            </div>
        </div>
    </div>
</section>
```

## CSS Styling

Copy these styles into `services-layout.css` or the page's local style block.

```css
/* CONTACT SECTION STYLES */
.contact-section {
    background-color: #f8fafc; /* Light gray background */
    padding: 100px 0;
}

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    background: #fff; /* White card background ? Or transparent on light gray page? */
    /* Design implies content is on a light gray page background, but form is distinct? 
       Actually, the screenshot shows the whole section on a white card or light gray background.
       Let's stick to transparent grid on section background. */
}

/* Left Column */
.contact-decoration {
    font-size: 14px;
    letter-spacing: 2px;
    color: #94a3b8;
    margin-bottom: 20px;
    font-family: monospace;
}

.contact-headline {
    font-size: 48px;
    line-height: 1.1;
    font-weight: 600; /* As per design, bold headers */
    color: #0f172a;
    margin-bottom: 24px;
    letter-spacing: -1px;
}

.contact-sub {
    font-size: 18px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 32px;
    max-width: 90%;
}

.contact-actions {
    margin-bottom: 40px;
}

.contact-proof {
    display: flex;
    gap: 20px;
    padding-top: 30px;
    border-top: 1px solid #e2e8f0;
    align-items: flex-start;
}

.proof-avatars {
    display: flex;
    flex-shrink: 0;
}

.avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    border: 3px solid #fff;
    margin-right: -15px;
    position: relative;
    z-index: 1;
}

.avatar:last-child {
    z-index: 2;
}

.proof-text {
    font-size: 14px;
    color: #475569;
    font-style: italic;
    line-height: 1.5;
}

/* Right Column - Form */
.contact-form-wrapper {
    background: transparent; /* Or white if needed */
    padding: 10px;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-group label {
    font-size: 14px;
    font-weight: 600;
    color: #0f172a;
}

.form-group input,
.form-group select,
.form-group textarea {
    padding: 12px 16px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 14px;
    color: #0f172a;
    background: #fff;
    transition: border 0.2s, box-shadow 0.2s;
    width: 100%;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #84CC16;
    box-shadow: 0 0 0 3px rgba(132, 204, 22, 0.1);
}

.select-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.select-wrapper .flag-icon {
    position: absolute;
    left: 12px;
    z-index: 2;
    font-size: 16px;
}

.select-wrapper select {
    padding-left: 40px;
}

.form-submit {
    display: flex;
    justify-content: flex-end;
}

/* Bottom Features */
.contact-features {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    margin-top: 80px;
    padding-top: 60px;
    border-top: 1px solid #e2e8f0;
}

.feature-item {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.feature-icon {
    color: #f97316; /* Orange accent from screenshot */
    margin-bottom: 8px;
}

.feature-icon i {
    width: 24px;
    height: 24px;
}

.feature-item h4 {
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
}

.feature-item p {
    font-size: 14px;
    color: #475569;
    line-height: 1.5;
}

/* Responsive */
@media (max-width: 900px) {
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    
    .contact-features {
        grid-template-columns: 1fr 1fr;
        gap: 40px;
    }
    
    .form-row {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 600px) {
    .contact-features {
        grid-template-columns: 1fr;
    }
}
```
