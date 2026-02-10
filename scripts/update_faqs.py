import os
import re

# Target files (excluding custom-apps.html which is done, and web-development which has none)
TARGET_FILES = [
    "pages/services/voice-ai.html",
    "pages/services/review-automation.html",
    "pages/services/private-ai-infra.html",
    "pages/services/lead-database.html",
    "pages/services/data-intelligence.html",
    "pages/services/workflow-automation.html",
    "pages/services/consulting.html"
]

BASE_DIR = "/Users/juandelossantos/Desktop/Skills Master"

def update_file(rel_path):
    file_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(file_path):
        print(f"Skipping {rel_path}, file not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check if FAQ exists
    if "Frequently Asked Questions" not in content:
        print(f"Skipping {rel_path}, no FAQ section found.")
        return
    
    # 2. Extract Questions and Answers using Regex
    # Pattern to match <details>...</details> blocks
    # This is a simple regex stategy.
    
    qa_list = []
    
    # Find the FAQ section block first to avoid matching other details if any
    # Assumption: The FAQ section starts with <section class="section">...Frequently Asked Questions...
    # and ends with </section>.
    
    # Let's find the section via regex
    section_pattern = re.compile(r'(<section class="section">\s*<div class="container"[^>]*>\s*<h2[^>]*>Frequently Asked Questions</h2>.*?<\/section>)', re.DOTALL)
    match = section_pattern.search(content)
    
    if not match:
        print(f"Could not isolate FAQ section in {rel_path}")
        return

    old_section_html = match.group(1)
    
    # Parse QA pairs from the old HTML
    # <details ...> <summary ...> QUESTION <span ...>+</span> </summary> <p ...> ANSWER </p> </details>
    
    details_pattern = re.compile(r'<details[^>]*>(.*?)<\/details>', re.DOTALL)
    details_matches = details_pattern.findall(old_section_html)
    
    for details_html in details_matches:
        # Extract Question
        q_match = re.search(r'<summary[^>]*>\s*(.*?)\s*<span', details_html, re.DOTALL)
        if not q_match:
             # Try matching without span if span is missing
             q_match = re.search(r'<summary[^>]*>\s*(.*?)\s*<\/summary>', details_html, re.DOTALL)
             
        question = q_match.group(1).strip() if q_match else "Question"
        
        # Extract Answer
        a_match = re.search(r'<p[^>]*>(.*?)<\/p>', details_html, re.DOTALL)
        answer = a_match.group(1).strip() if a_match else "Answer"
        
        qa_list.append({'q': question, 'a': answer})

    print(f"Found {len(qa_list)} QAs in {rel_path}")
    
    # 3. Build New HTML
    new_cards_html = ""
    for qa in qa_list:
        card = f'''
                <div class="faq-card">
                    <h3 class="faq-question">{qa['q']}</h3>
                    <div class="faq-answer">
                        <p>{qa['a']}</p>
                    </div>
                </div>'''
        new_cards_html += card

    new_section_html = f'''    <!-- FAQ Carousel Section -->
    <section class="faq-carousel-section">
        <div class="faq-header-container">
            <div>
                <span class="subtitle">Support</span>
                <h2 style="font-weight: 300;">Frequently<br><span class="highlight-merriweather">Asked Questions</span></h2>
            </div>
            
            <div class="faq-nav-group">
                <button class="faq-nav-btn prev" aria-label="Previous">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
                </button>
                <button class="faq-nav-btn next" aria-label="Next">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
                </button>
            </div>
        </div>

        <div class="faq-carousel-wrapper">
            <div class="faq-track">
{new_cards_html}
            </div>
        </div>
    </section>'''

    # 4. Replace content
    new_content = content.replace(old_section_html, new_section_html)
    
    # 5. Add CSS Link
    # Find services-layout.css and append after it
    css_link = '<link rel="stylesheet" href="../../css/faq-carousel.css">'
    if css_link not in new_content:
        new_content = new_content.replace('<link rel="stylesheet" href="../../css/services-layout.css">', 
                                          '<link rel="stylesheet" href="../../css/services-layout.css">\n    <link rel="stylesheet" href="../../css/faq-carousel.css">')
    
    # 6. Add JS Link
    # Append before closing body
    js_script = '<script src="../../js/faq-carousel.js"></script>'
    if js_script not in new_content:
        # Try finding the split layout script or body end
        if '<!-- Interactive Script for Split Layout -->' in new_content:
             new_content = new_content.replace('<!-- Interactive Script for Split Layout -->', 
                                               f'{js_script}\n    <!-- Interactive Script for Split Layout -->')
        else:
             new_content = new_content.replace('</body>', f'{js_script}\n</body>')

    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {rel_path}")

# Run
for path in TARGET_FILES:
    update_file(path)
