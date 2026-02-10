#!/usr/bin/env python3
"""
Remove Contact Us section and Referenced Resources links from all blog posts
Keep the note but remove source links
"""

import re
from pathlib import Path

def remove_sections_from_blog(filepath):
    """Remove Contact Us section and source links from a blog post."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # 1. Remove the entire Unified Contact Section
    # Pattern: From "<!-- Unified Contact Section -->" to the closing </section>
    contact_pattern = r'<!-- Unified Contact Section -->.*?</section>\s*'
    if re.search(contact_pattern, content, flags=re.DOTALL):
        content = re.sub(contact_pattern, '', content, flags=re.DOTALL)
        changes.append("Removed Contact Us section")

    # 2. Remove the Referenced Sources list but keep the note
    # Pattern: From "Referenced Sources:" heading to just before the Note
    sources_pattern = r'(<div style="background: #f8fafc;[^>]*>)\s*<h3[^>]*>Referenced Sources:</h3>\s*<ul[^>]*>.*?</ul>\s*(<div style="margin-top: 25px;[^>]*>\s*<strong[^>]*>Note:</strong>.*?</div>\s*</div>)'

    if re.search(sources_pattern, content, flags=re.DOTALL):
        # Keep only the opening div and the note section
        content = re.sub(
            sources_pattern,
            r'\1\2',
            content,
            flags=re.DOTALL
        )
        changes.append("Removed source links, kept note")

    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes

    return False, []

def main():
    """Main function."""
    print("=" * 80)
    print("REMOVING CONTACT US & SOURCE LINKS FROM BLOG POSTS")
    print("=" * 80)
    print()

    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = []

    for blog_file in sorted(blog_dir.glob("*.html")):
        try:
            modified, changes = remove_sections_from_blog(blog_file)

            if modified:
                updated.append(blog_file.name)
                print(f"  ✓ {blog_file.name}")
                for change in changes:
                    print(f"      • {change}")
            else:
                print(f"  ⊙ {blog_file.name} (no changes)")

        except Exception as e:
            print(f"  ✗ Error updating {blog_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total blog posts updated: {len(updated)}")
    print()
    print("Changes made:")
    print("  ✓ Removed Contact Us section from all blog posts")
    print("  ✓ Removed Referenced Sources links")
    print("  ✓ Kept the privacy note at the bottom")
    print()

if __name__ == "__main__":
    main()
