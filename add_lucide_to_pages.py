#!/usr/bin/env python3
"""
Add Lucide script to all pages that need icons
"""

import re
from pathlib import Path

def add_lucide_script(filepath):
    """Add Lucide script if not already present."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Lucide is already loaded
    if 'unpkg.com/lucide' in content or 'lucide@latest' in content:
        return False

    # Add Lucide script in the head section
    lucide_script = '    <script src="https://unpkg.com/lucide@latest"></script>'

    # Find the closing </head> tag and add script before it
    pattern = r'(</head>)'
    if re.search(pattern, content):
        content = re.sub(
            pattern,
            f'{lucide_script}\n\\1',
            content,
            count=1
        )

        # Now add lucide.createIcons() at the end of the body scripts
        # Find the last script tag before </body>
        init_script = '''
        lucide.createIcons();
    '''

        # Add initialization before closing body tag
        pattern2 = r'(</body>)'
        if re.search(pattern2, content):
            content = re.sub(
                pattern2,
                f'    <script>{init_script}</script>\n\\1',
                content,
                count=1
            )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def process_homepage():
    """Process homepage."""
    homepage = Path("/Users/juandelossantos/Desktop/Skills Master/index.html")
    if add_lucide_script(homepage):
        print("  ✓ Homepage")
        return 1
    else:
        print("  - Homepage (already has Lucide)")
        return 0

def process_service_pages():
    """Process all service pages."""
    service_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/services")
    updated = 0

    for service_file in service_dir.glob("*.html"):
        if add_lucide_script(service_file):
            updated += 1
            print(f"  ✓ {service_file.name}")

    return updated

def process_industry_pages():
    """Process all industry pages."""
    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = 0

    for industry_file in industry_dir.glob("*.html"):
        if add_lucide_script(industry_file):
            updated += 1
            print(f"  ✓ {industry_file.name}")

    return updated

def process_blog_posts():
    """Process all blog posts."""
    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = 0

    for blog_file in blog_dir.glob("*.html"):
        if blog_file.name.startswith("_"):
            continue

        if add_lucide_script(blog_file):
            updated += 1
            print(f"  ✓ {blog_file.name}")

    return updated

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING LUCIDE ICON LIBRARY TO ALL PAGES")
    print("=" * 80)
    print()

    print("Step 1: Adding to homepage...")
    home_count = process_homepage()
    print()

    print("Step 2: Adding to service pages...")
    service_count = process_service_pages()
    print(f"  → {service_count} service pages updated")
    print()

    print("Step 3: Adding to industry pages...")
    industry_count = process_industry_pages()
    print(f"  → {industry_count} industry pages updated")
    print()

    print("Step 4: Adding to blog posts...")
    blog_count = process_blog_posts()
    print(f"  → {blog_count} blog posts updated")
    print()

    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {home_count + service_count + industry_count + blog_count}")
    print()
    print("Changes made:")
    print("  ✓ Added Lucide CDN script to <head>")
    print("  ✓ Added lucide.createIcons() initialization")
    print("  ✓ Icons will now display in contact section")
    print()

if __name__ == "__main__":
    main()
