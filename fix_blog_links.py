#!/usr/bin/env python3
"""
Fix blog.html links to point to the correct relative path for blog case studies.
Blog.html is at /pages/blog.html, but links point to blog/case-studies/...
They should point to ../blog/case-studies/... to go up one level.
"""

import re
from pathlib import Path

def fix_blog_links(filepath):
    """Fix blog case study links to use correct relative paths."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace blog/case-studies/ with ../blog/case-studies/
    # This pattern matches href="blog/case-studies/...html"
    pattern = r'href="blog/case-studies/'
    replacement = r'href="../blog/case-studies/'

    # Count how many replacements will be made
    count = len(re.findall(pattern, content))

    if count == 0:
        return False, 0

    # Perform the replacement
    new_content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, count

def main():
    """Main function."""
    print("=" * 80)
    print("FIXING BLOG.HTML CASE STUDY LINKS")
    print("=" * 80)
    print()

    blog_file = Path("/Users/juandelossantos/Desktop/Skills Master/pages/blog.html")

    print(f"Processing: {blog_file.name}")
    print()
    print("Current path: blog/case-studies/")
    print("Corrected path: ../blog/case-studies/")
    print()

    success, count = fix_blog_links(blog_file)

    if success:
        print(f"✓ Updated {count} blog case study links")
        print()
        print("=" * 80)
        print("COMPLETE")
        print("=" * 80)
        print()
        print("Blog.html now correctly links to:")
        print("  ../blog/case-studies/*.html")
        print()
        print("All blog post links will now load the properly formatted")
        print("case study pages with the dark gradient header, green metrics,")
        print("and full blog styling on both desktop and mobile.")
        print()
    else:
        print("✗ No links found to update (links may already be correct)")
        print()

if __name__ == "__main__":
    main()
