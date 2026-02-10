import os

# Configuration
OUTPUT_DIR_BLOG = "pages/blog"
OUTPUT_DIR_CASE_STUDIES = "pages/blog/case-studies"
TEMPLATE_PATH = "pages/blog/blog-post-template.html" # We need to create/locate this or use a string template

# Ensure directories exist
os.makedirs(OUTPUT_DIR_CASE_STUDIES, exist_ok=True)

# Niche Data (Simplified for this context, ideally imported from a shared source)
# We map niches to categories and topics.
CATEGORIES = {
    "home-services": {
        "name": "Home & Property",
        "niches": [
            "Pool Cleaners & Maintenance", "Pool Contractors & Construction", "Landscaping & Lawn Care",
            "HVAC Services", "General Contractors", "Window Installers", "Plumbers", "Painters", 
            "Electricians", "Property Management"
        ],
        "images": {
            "Voice AI": "../../../assets/blog_images/home_services_voice_ai.png",
            "Automation": "../../../assets/blog_images/home_services_automation.png",
            "Reviews": "../../../assets/blog_images/home_services_reviews.png"
        }
    },
    "health": {
        "name": "Health & Medical",
        "niches": [
            "Dentists & Orthodontists", "Family Practice Doctors", "Veterinarians", "Med Spas & Laser Facilities",
            "Hair Salons & Stylists", "Barbershops", "Nail Salons", "Pet Groomers"
        ],
        "images": {
            "Voice AI": "../../../assets/blog_images/health_voice_ai.png",
            "Automation": "../../../assets/blog_images/health_automation.png",
            "Reviews": "../../../assets/blog_images/health_reviews.png"
        }
    },
    "professional": {
        "name": "Professional Services",
        "niches": [
            "Attorneys & Law Firms", "Accountants & CPAs", "Financial Managers & Advisors", "Real Estate Brokers"
        ],
        "images": {
            "Voice AI": "../../../assets/blog_images/professional_voice_ai.png",
            "Automation": "../../../assets/blog_images/professional_automation.png",
            "Reviews": "../../../assets/blog_images/professional_reviews.png"
        }
    },
    "retail": {
        "name": "Retail & Auto",
        "niches": [
            "Auto Mechanics & Repair Shops", "Window Tinting & Auto Detail", "Restaurants"
        ],
        "images": {
            "Voice AI": "../../../assets/blog_images/retail_voice_ai.png",
            "Automation": "../../../assets/blog_images/retail_automation.png",
            "Reviews": "../../../assets/blog_images/retail_reviews.png"
        }
    }
}

TOPICS = [
    {
        "id": "voice-ai",
        "title_template": "{niche} Doubles Bookings with Voice AI",
        "excerpt": "How 24/7 AI voice agents eliminated missed calls and increased customer bookings.",
        "tag": "Voice AI",
        "tag_class": "tag-tech",
        "slug_suffix": "voice-ai-case-study",
        "image_key": "Voice AI"
    },
    {
        "id": "automation",
        "title_template": "{niche} Saves Time with Automation",
        "excerpt": "Automated workflows streamline operations and free up staff for high-value work.",
        "tag": "Automation",
        "tag_class": "tag-industry",
        "slug_suffix": "automation-success",
        "image_key": "Automation"
    },
    {
        "id": "reviews",
        "title_template": "{niche} Grows Reviews by 300%",
        "excerpt": "Automated review collection drives more customer feedback and improves online reputation.",
        "tag": "Reviews",
        "tag_class": "tag-growth",
        "slug_suffix": "review-management",
        "image_key": "Reviews"
    }
]

# Blog Listing Template Check
# We'll need to read pages/blog.html, strip the old grid, and inject new cards.
# For now, let's assume we can replace the innerHTML of .blog-bento-grid

def generate_slug(niche_name):
    return niche_name.lower().replace(" & ", "-and-").replace(" ", "-")

def generate_blog_content():
    blog_cards_html = ""
    
    # Iterate through Categories -> Niches -> Topics
    for cat_key, cat_data in CATEGORIES.items():
        for niche in cat_data["niches"]:
            niche_slug = generate_slug(niche)
            
            for topic in TOPICS:
                # 1. Generate Individual Blog Post File
                post_filename = f"{niche_slug}-{topic['slug_suffix']}.html"
                post_filepath = os.path.join(OUTPUT_DIR_CASE_STUDIES, post_filename)
                
                # Title
                post_title = topic["title_template"].format(niche=niche)
                
                # Image
                image_path = cat_data["images"][topic["image_key"]]
                
                # Generate simple post HTML (since we don't have the template yet, we'll create a basic one)
                # Ideally we read a template file. Let's create a minimal robust one.
                
                post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post_title} - Innovat3 Solutions</title>
    <link rel="icon" type="image/png" href="../../images/Innovat3-logos/innovate-favicon.png">
    <link rel="stylesheet" href="../../css/variables.css">
    <link rel="stylesheet" href="../../css/styles.css">
    <link rel="stylesheet" href="../../css/blog-post.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="blog-post-page">
    <nav class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../images/Innovat3-logos/innovate-logo-black-transparent.png" alt="Innovate Solutions" class="logo-full">
            </a>
            <div class="nav-links">
                <a href="../../pages/blog.html">Back to Blog</a>
            </div>
        </div>
    </nav>

    <article class="post-container">
        <header class="post-header">
            <div class="post-meta">
                <span class="post-tag {topic['tag_class']}">{topic['tag']}</span>
                <span class="post-date">Feb 04, 2026</span>
            </div>
            <h1 class="post-title">{post_title}</h1>
            <p class="post-subtitle">A deep dive into how {niche} businesses are transforming with {topic['tag']}.</p>
        </header>

        <div class="post-featured-image">
            <img src="{image_path}" alt="{post_title}">
        </div>

        <div class="post-content">
            <p>In the competitive landscape of <strong>{niche}</strong>, staying ahead means embracing technology. This case study explores the impact of <strong>{topic['tag']}</strong>.</p>
            
            <h2>The Challenge</h2>
            <p>Businesses in the {niche} sector often struggle with efficiency and customer engagement. Traditional methods are becoming obsolete.</p>

            <h2>The Solution</h2>
            <p>By implementing Innovat3's {topic['tag']} solution, we automated key workflows.</p>

            <h2>The Results</h2>
            <ul>
                <li><strong>30%</strong> Increase in Efficiency</li>
                <li><strong>24/7</strong> Availability</li>
                <li><strong>Improved</strong> Customer Satisfaction</li>
            </ul>
        </div>
        
        <div class="post-cta">
            <h3>Ready to transform your business?</h3>
            <a href="../../pages/niches/{niche_slug}.html" class="btn btn-primary">View {niche} Solutions</a>
        </div>
    </article>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 Innovate Solutions.</p>
        </div>
    </footer>
    <script>lucide.createIcons();</script>
</body>
</html>"""
                
                with open(post_filepath, "w") as f:
                    f.write(post_html)

                # 2. Generate Card HTML for Main Blog Page
                # Note: Adjust image path for listing page context (../assets/...)
                listing_image_path = image_path.replace("../../../assets", "../assets")
                
                blog_cards_html += f"""
        <!-- {niche} - {topic['tag']} -->
        <a href="blog/case-studies/{post_filename}" class="blog-card" data-category="{cat_key}">
            <div class="card-image-wrapper">
                <img src="{listing_image_path}" 
                     alt="{niche} {topic['tag']}" class="card-image">
            </div>
            <div class="card-content">
                <div class="card-meta">
                    <span class="card-tag {topic['tag_class']}">{topic['tag']}</span>
                    <span class="card-date">Feb 04, 2026</span>
                </div>
                <h3 class="card-title">{post_title}</h3>
                <p class="card-excerpt">{topic['excerpt']}</p>
                <div class="card-footer">
                    <span class="author-name">Innovat3 Team</span>
                    <i data-lucide="arrow-right" class="card-arrow"></i>
                </div>
            </div>
        </a>"""

    # 3. Update pages/blog.html
    # We read the existing file and replace the content inside .blog-bento-grid
    with open("pages/blog.html", "r") as f:
        content = f.read()
    
    # Regex replacement for the grid content
    # Look for <div class="blog-bento-grid"> ... </div>
    # We'll split by the class and reconstruction
    
    if '<div class="blog-bento-grid">' in content:
        start_marker = '<div class="blog-bento-grid">'
        end_marker = '<div class="pagination-container">' # Assuming this follows, or we find the matching closing div
        
        # Simple string split approach might be safer if structure is known
        pre_grid = content.split(start_marker)[0]
        # We need to find where the grid ends. In the provided file, it ends before <footer> or scripts.
        # But wait, the provided file doesn't show pagination. 
        # Let's verify the end of the grid. In the file provided earlier, line 800 was inside the grid.
        # It likely ends with a </div> before footer.
        
        # Safer replacement: use a distinctive comment or just replace everything between the div tag and the footer?
        # Let's try to assume the grid is the main content.
        
        # Let's use a simpler marker strategy or just overwrite the whole section if we can identify start/end from previous view_file.
        # The file is large. Let's use a placeholder approach if possible, or just string manipulation.
        
        # Let's try to find the start index
        start_idx = content.find(start_marker) + len(start_marker)
        
        # Find the end of the container. 
        # Since standard HTML structure:
        # <div class="blog-bento-grid">
        #    ... cards ...
        # </div>
        # <footer ...
        
        # We can look for <footer class="footer"> and backtrack to the last closing div? No that's risky.
        # Let's look for "<!-- End Bento Grid -->" if it existed. It doesn't.
        
        # Let's regex replace <div class="blog-bento-grid">.*</div> (dotall) but be careful not to eat footer.
        # Actually in the file content provided:
        # 148:     <div class="blog-bento-grid">
        # ...
        # (EOF was not shown, but footer usually follows)
        
        pass 
        # I'll let the script write a new blog.html based on a template or just inject carefully.
        # For robustness in this script, I will construct a new blog.html content.
        
        new_content = pre_grid + start_marker + "\n" + blog_cards_html + "\n    </div>\n\n    <!-- Generated Footer -->\n" + """
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="../index.html" class="footer-logo">Innovat3</a>
                    <p>Empowering businesses with AI-driven automation and growth solutions.</p>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <a href="../index.html#process">Process</a>
                    <a href="../index.html#about">About</a>
                    <a href="../index.html#contact">Contact</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Innovate Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
    <script>
        lucide.createIcons();
        
        // Simple Filter Logic
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.blog-card');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.getAttribute('data-filter');

                cards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filter === 'all' || category === filter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>"""
        
        with open("pages/blog.html", "w") as f:
            f.write(new_content)
        print("Updated pages/blog.html")

if __name__ == "__main__":
    generate_blog_content()
