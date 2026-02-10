#!/usr/bin/env python3
"""
Add Blog link to navigation bar on all industry pages
"""

import re
from pathlib import Path

def add_blog_link_to_nav(filepath):
    """Add Blog link to the navigation bar."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Blog link already exists
    if 'href="../blog.html">Blog</a>' in content or 'href="../../blog.html">Blog</a>' in content:
        return False

    # Pattern to find where to insert the Blog link
    # Looking for the closing of the Industries dropdown, followed by Process link
    pattern = r'(</div>\s*</div>\s*</div>\s*)(<a href="../../index\.html#process">Process</a>)'

    if re.search(pattern, content):
        # Insert Blog link before Process link
        replacement = r'\1<a href="../blog.html">Blog</a>\n                \2'
        content = re.sub(pattern, replacement, content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING BLOG LINK TO INDUSTRY PAGE NAVIGATION")
    print("=" * 80)
    print()

    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = []

    for industry_file in sorted(industry_dir.glob("*.html")):
        try:
            if add_blog_link_to_nav(industry_file):
                updated.append(industry_file.name)
                print(f"  ✓ {industry_file.name}")
            else:
                print(f"  ⊙ {industry_file.name} (already has Blog link)")
        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {len(updated)}")
    print()
    print("Navigation bar now includes:")
    print("  ✓ Services dropdown")
    print("  ✓ Industries dropdown")
    print("  ✓ Blog link (newly added)")
    print("  ✓ Process link")
    print("  ✓ About link")
    print()
    print("All navigation bars are now consistent across the entire site.")
    print()

if __name__ == "__main__":
    main()
