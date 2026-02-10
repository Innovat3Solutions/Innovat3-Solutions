#!/usr/bin/env python3
"""
Script to update blog post images based on industry category mapping
"""

import os
import shutil
from pathlib import Path

# Define the base directories
ASSETS_DIR = Path("/Users/juandelossantos/Desktop/Skills Master/assets/blog_images")
BLOG_IMAGES_DIR = Path("/Users/juandelossantos/Desktop/Skills Master/blog/images")
CASE_STUDIES_DIR = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")

# Industry category mapping
INDUSTRY_MAPPING = {
    # HOME SERVICES
    "pool-cleaners-and-maintenance": "home_services",
    "pool-contractors-and-construction": "home_services",
    "hvac-services": "home_services",
    "plumbers": "home_services",
    "electricians": "home_services",
    "painters": "home_services",
    "general-contractors": "home_services",
    "landscaping-and-lawn-care": "home_services",
    "window-installers": "home_services",

    # HEALTH
    "dentists-and-orthodontists": "health",
    "family-practice-doctors": "health",
    "med-spas-and-laser-facilities": "health",
    "veterinarians": "health",

    # PROFESSIONAL
    "accountants-and-cpas": "professional",
    "attorneys-and-law-firms": "professional",
    "financial-managers-and-advisors": "professional",
    "real-estate-brokers": "professional",
    "property-management": "professional",

    # RETAIL
    "restaurants": "retail",
    "barbershops": "retail",
    "hair-salons-and-stylists": "retail",
    "nail-salons": "retail",
    "auto-mechanics-and-repair-shops": "retail",
    "window-tinting-and-auto-detail": "retail",
    "pet-groomers": "retail",
}

# Blog types
BLOG_TYPES = ["voice-ai", "automation", "review-management"]

def copy_images_to_directories():
    """Copy the appropriate images to each blog subdirectory based on category"""
    print("Copying images to blog subdirectories...")

    for blog_type in BLOG_TYPES:
        blog_dir = BLOG_IMAGES_DIR / blog_type
        blog_dir.mkdir(parents=True, exist_ok=True)

        # Copy images for each category
        for category in ["home_services", "health", "professional", "retail"]:
            # Determine which image to use based on blog type
            if blog_type == "voice-ai":
                source_image = ASSETS_DIR / f"{category}_voice_ai.png"
            elif blog_type == "automation":
                source_image = ASSETS_DIR / f"{category}_automation.png"
            elif blog_type == "review-management":
                source_image = ASSETS_DIR / f"{category}_reviews.png"

            # Copy to hero and dashboard locations
            hero_dest = blog_dir / f"hero-{blog_type}-{category}.png"
            dashboard_dest = blog_dir / f"dashboard-{blog_type}-{category}.png"

            if source_image.exists():
                shutil.copy2(source_image, hero_dest)
                shutil.copy2(source_image, dashboard_dest)
                print(f"  Copied {source_image.name} -> {hero_dest.name}")
            else:
                print(f"  WARNING: Source image not found: {source_image}")

def update_blog_post(file_path, industry_key, blog_type):
    """Update a single blog post's image references"""
    category = INDUSTRY_MAPPING.get(industry_key)
    if not category:
        print(f"  WARNING: No category mapping for {industry_key}")
        return False

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update image paths - change .jpg to .png and update paths
    old_hero_path = f'../images/{blog_type}/hero-{blog_type}.jpg'
    new_hero_path = f'../images/{blog_type}/hero-{blog_type}-{category}.png'

    old_dashboard_path = f'../images/{blog_type}/dashboard-{blog_type}.jpg'
    new_dashboard_path = f'../images/{blog_type}/dashboard-{blog_type}-{category}.png'

    # Replace the paths
    updated_content = content.replace(old_hero_path, new_hero_path)
    updated_content = updated_content.replace(old_dashboard_path, new_dashboard_path)

    # Check if any changes were made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True

    return False

def update_all_blog_posts():
    """Update all blog posts with correct image paths"""
    print("\nUpdating blog post image references...")

    updated_count = 0
    not_found_count = 0

    # Get all HTML files in case-studies directory
    html_files = list(CASE_STUDIES_DIR.glob("*.html"))

    for html_file in html_files:
        filename = html_file.stem

        # Skip the generation report
        if filename.startswith("_generation"):
            continue

        # Determine industry key and blog type from filename
        blog_type = None
        industry_key = None

        if filename.endswith("-voice-ai-case-study"):
            blog_type = "voice-ai"
            industry_key = filename.replace("-voice-ai-case-study", "")
        elif filename.endswith("-automation-success"):
            blog_type = "automation"
            industry_key = filename.replace("-automation-success", "")
        elif filename.endswith("-review-management"):
            blog_type = "review-management"
            industry_key = filename.replace("-review-management", "")
        else:
            # Special case for pool-service-doubles-bookings-voice-ai
            if "pool-service" in filename and "voice-ai" in filename:
                blog_type = "voice-ai"
                industry_key = "pool-cleaners-and-maintenance"

        if blog_type and industry_key:
            if update_blog_post(html_file, industry_key, blog_type):
                updated_count += 1
                print(f"  ✓ Updated: {filename} ({industry_key} -> {INDUSTRY_MAPPING.get(industry_key)})")
            else:
                print(f"  - No changes: {filename}")
        else:
            not_found_count += 1
            print(f"  ? Could not parse: {filename}")

    print(f"\nSummary:")
    print(f"  Updated: {updated_count} files")
    print(f"  Could not parse: {not_found_count} files")

def main():
    print("=" * 60)
    print("Blog Image Update Script")
    print("=" * 60)

    # Step 1: Copy images to subdirectories
    copy_images_to_directories()

    # Step 2: Update all blog posts
    update_all_blog_posts()

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
