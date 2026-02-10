#!/usr/bin/env python3
"""
Add custom images to all 75 blog posts with proper integration
"""

import os
import re
from pathlib import Path

# Image specifications for AI generation prompts
IMAGE_PROMPTS = {
    "voice-ai-hero": """
    Professional business photo showing:
    - Modern office phone system or smartphone with incoming call notification
    - Clean, professional environment
    - Blue and green color scheme matching the brand (#84CC16)
    - Bright, optimistic lighting
    - High quality, 1920x1080px
    - Style: Modern, corporate, trustworthy
    - No people visible (focus on technology)
    """,

    "voice-ai-dashboard": """
    Screenshot or mockup of:
    - AI voice analytics dashboard
    - Call volume graphs showing upward trend
    - Green success metrics and indicators
    - Clean, modern UI design
    - Charts showing 110% increase
    - Professional dashboard aesthetic
    - 1600x900px
    """,

    "automation-hero": """
    Professional illustration showing:
    - Workflow automation concept
    - Connected gears, arrows, or process flows
    - Digital/tech aesthetic
    - Green (#84CC16) and dark blue colors
    - Modern, clean design
    - Conveys efficiency and systemization
    - 1920x1080px
    """,

    "automation-dashboard": """
    Mockup or screenshot showing:
    - Business automation dashboard
    - Time saved metrics prominently displayed
    - Calendar integration visualization
    - Invoice automation interface
    - Green success indicators
    - Professional, modern UI
    - 1600x900px
    """,

    "review-management-hero": """
    Professional visual showing:
    - 5-star rating system
    - Google reviews interface
    - Multiple positive review cards
    - Upward trending graph
    - Green (#84CC16) color accents
    - Modern, clean design
    - Conveys growth and positivity
    - 1920x1080px
    """,

    "review-management-dashboard": """
    Screenshot or mockup of:
    - Review collection dashboard
    - Review count increasing over time
    - Star rating improvements
    - Customer feedback interface
    - SMS/email automation preview
    - Professional UI design
    - 1600x900px
    """
}

# Stock photo alternatives
STOCK_PHOTO_ALTERNATIVES = {
    "voice-ai": [
        "Search: 'business phone call professional'",
        "Search: 'customer service technology'",
        "Search: 'AI assistant business'",
        "Unsplash: phone, business, technology tags"
    ],
    "automation": [
        "Search: 'workflow automation'",
        "Search: 'business process technology'",
        "Search: 'efficiency productivity'",
        "Unsplash: automation, workflow, efficiency tags"
    ],
    "review-management": [
        "Search: '5 star review google'",
        "Search: 'customer testimonials'",
        "Search: 'online reputation'",
        "Unsplash: review, rating, feedback tags"
    ]
}

def update_blog_post_with_images(filepath, blog_type):
    """Update a blog post to include image references."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define image paths based on blog type
    hero_image = f"../images/{blog_type}/hero-{blog_type}.jpg"
    dashboard_image = f"../images/{blog_type}/dashboard-{blog_type}.jpg"

    # Add hero image right after the back-link
    hero_img_html = f'''
        <img src="{hero_image}" alt="Success story visualization" style="width: 100%; max-width: 800px; height: 400px; object-fit: cover; border-radius: 12px; margin: 40px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
'''

    # Add dashboard image in the results section
    dashboard_img_html = f'''
        <img src="{dashboard_image}" alt="Results dashboard" style="width: 100%; max-width: 800px; height: auto; border-radius: 12px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
'''

    # Insert hero image after back link
    pattern1 = re.compile(r'(</a>\s*\n)')
    if pattern1.search(content):
        content = pattern1.sub(f'</a>\n{hero_img_html}\n', content, 1)

    # Insert dashboard image after first h2 (The Results section)
    pattern2 = re.compile(r'(<h2>The Results:.*?</h2>\s*)')
    if pattern2.search(content):
        content = pattern2.sub(f'\\1{dashboard_img_html}\n', content, 1)

    return content

def main():
    """Main function to add images to all blog posts."""
    print("=" * 80)
    print("ADDING CUSTOM IMAGES TO BLOG POSTS")
    print("=" * 80)
    print()

    base_dir = Path("/Users/juandelossantos/Desktop/Skills Master")
    blog_dir = base_dir / "blog" / "case-studies"

    # Categorize blog posts by type
    blog_types = {
        'voice-ai': [],
        'automation': [],
        'review-management': []
    }

    # Scan all blog posts
    for blog_file in blog_dir.glob("*.html"):
        if blog_file.name.startswith("_"):
            continue

        filename = blog_file.name
        if 'voice-ai-case-study' in filename:
            blog_types['voice-ai'].append(blog_file)
        elif 'automation-success' in filename:
            blog_types['automation'].append(blog_file)
        elif 'review-management' in filename:
            blog_types['review-management'].append(blog_file)

    # Update all blog posts
    total_updated = 0

    for blog_type, files in blog_types.items():
        print(f"\nUpdating {blog_type} blog posts...")
        print("-" * 80)

        for filepath in files:
            try:
                updated_content = update_blog_post_with_images(filepath, blog_type)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                total_updated += 1
                print(f"  ✓ {filepath.name}")

            except Exception as e:
                print(f"  ✗ Error updating {filepath.name}: {str(e)}")

    print()
    print("=" * 80)
    print(f"COMPLETE: {total_updated} blog posts updated with image placeholders")
    print("=" * 80)
    print()

    # Generate image specification document
    spec_file = base_dir / "blog" / "IMAGE_SPECIFICATIONS.md"

    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write("# Blog Post Image Specifications\n\n")
        f.write("This document provides detailed specifications for creating images for all blog posts.\n\n")

        f.write("## Required Images (6 total)\n\n")

        f.write("### 1. Voice AI Hero Image\n")
        f.write(f"**Filename:** `blog/images/voice-ai/hero-voice-ai.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['voice-ai-hero']}\n\n")
        f.write("**Stock Photo Alternative:**\n")
        for alt in STOCK_PHOTO_ALTERNATIVES['voice-ai']:
            f.write(f"- {alt}\n")
        f.write("\n---\n\n")

        f.write("### 2. Voice AI Dashboard Image\n")
        f.write(f"**Filename:** `blog/images/voice-ai/dashboard-voice-ai.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['voice-ai-dashboard']}\n\n")
        f.write("**Alternative:** Create a mockup dashboard using Figma or Canva\n")
        f.write("\n---\n\n")

        f.write("### 3. Automation Hero Image\n")
        f.write(f"**Filename:** `blog/images/automation/hero-automation.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['automation-hero']}\n\n")
        f.write("**Stock Photo Alternative:**\n")
        for alt in STOCK_PHOTO_ALTERNATIVES['automation']:
            f.write(f"- {alt}\n")
        f.write("\n---\n\n")

        f.write("### 4. Automation Dashboard Image\n")
        f.write(f"**Filename:** `blog/images/automation/dashboard-automation.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['automation-dashboard']}\n\n")
        f.write("**Alternative:** Screenshot from actual automation tools (Zapier, Make.com)\n")
        f.write("\n---\n\n")

        f.write("### 5. Review Management Hero Image\n")
        f.write(f"**Filename:** `blog/images/review-management/hero-review-management.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['review-management-hero']}\n\n")
        f.write("**Stock Photo Alternative:**\n")
        for alt in STOCK_PHOTO_ALTERNATIVES['review-management']:
            f.write(f"- {alt}\n")
        f.write("\n---\n\n")

        f.write("### 6. Review Management Dashboard Image\n")
        f.write(f"**Filename:** `blog/images/review-management/dashboard-review-management.jpg`\n")
        f.write(f"**AI Generation Prompt:**{IMAGE_PROMPTS['review-management-dashboard']}\n\n")
        f.write("**Alternative:** Screenshot from Google My Business or review platform\n")
        f.write("\n---\n\n")

        f.write("## Image Generation Tools\n\n")
        f.write("### AI Image Generators (Recommended)\n")
        f.write("1. **DALL-E 3** (via ChatGPT Plus) - Best for business/professional imagery\n")
        f.write("2. **Midjourney** - High quality, artistic results\n")
        f.write("3. **Leonardo.ai** - Good for dashboard mockups\n")
        f.write("4. **Ideogram** - Excellent for text-in-image generation\n\n")

        f.write("### Stock Photo Sources (Free)\n")
        f.write("1. **Unsplash** - https://unsplash.com\n")
        f.write("2. **Pexels** - https://pexels.com\n")
        f.write("3. **Pixabay** - https://pixabay.com\n\n")

        f.write("### Design Tools (For Dashboards)\n")
        f.write("1. **Figma** - Professional UI mockups\n")
        f.write("2. **Canva** - Quick dashboard designs\n")
        f.write("3. **Sketch** - Mac-only design tool\n\n")

        f.write("## Quick Start Guide\n\n")
        f.write("### Option 1: AI Generation (Fastest)\n")
        f.write("1. Use ChatGPT Plus (has DALL-E 3 access)\n")
        f.write("2. Copy the AI generation prompt for each image\n")
        f.write("3. Generate the image\n")
        f.write("4. Download and save to the specified filename\n\n")

        f.write("### Option 2: Stock Photos (Free)\n")
        f.write("1. Go to Unsplash.com\n")
        f.write("2. Search using the suggested search terms\n")
        f.write("3. Download high-resolution version\n")
        f.write("4. Rename and save to specified location\n\n")

        f.write("### Option 3: Hybrid Approach (Best Quality)\n")
        f.write("1. Use stock photos for hero images\n")
        f.write("2. Create dashboard mockups in Figma/Canva\n")
        f.write("3. Export as JPG at specified dimensions\n\n")

        f.write("## Technical Requirements\n\n")
        f.write("- **Format:** JPG (optimized for web)\n")
        f.write("- **Hero Images:** 1920x1080px minimum\n")
        f.write("- **Dashboard Images:** 1600x900px minimum\n")
        f.write("- **File Size:** Under 500KB each (use compression)\n")
        f.write("- **Quality:** High (80-90% JPG quality)\n")
        f.write("- **Color Profile:** sRGB\n\n")

        f.write("## Image Optimization\n\n")
        f.write("After creating images, compress them using:\n")
        f.write("- **TinyPNG** - https://tinypng.com\n")
        f.write("- **ImageOptim** (Mac) - Free compression tool\n")
        f.write("- **Squoosh** - https://squoosh.app (web-based)\n\n")

        f.write("## Notes\n\n")
        f.write("- All 75 blog posts now reference these 6 images\n")
        f.write("- Each blog type (voice-ai, automation, review-management) shares the same 2 images\n")
        f.write("- This keeps file count manageable while providing visual enhancement\n")
        f.write("- Images are referenced with relative paths from blog posts\n")
        f.write("- Once images are added, no code changes needed - they'll display automatically\n")

    print(f"Image specifications saved to: {spec_file}")
    print()
    print("Next Steps:")
    print("1. Review IMAGE_SPECIFICATIONS.md for detailed instructions")
    print("2. Generate or download the 6 required images")
    print("3. Place images in blog/images/ subdirectories")
    print("4. Images will automatically appear in all 75 blog posts")
    print()

if __name__ == "__main__":
    main()
