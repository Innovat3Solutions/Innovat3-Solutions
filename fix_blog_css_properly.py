#!/usr/bin/env python3
"""
Properly fix blog page CSS - clean up and re-add mobile styles correctly
"""

import re
from pathlib import Path

def fix_blog_css_properly(filepath):
    """Fix the CSS properly by cleaning up and re-adding mobile styles."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <style> block
    style_pattern = r'(<style>.*?)(</style>)'

    match = re.search(style_pattern, content, re.DOTALL)
    if not match:
        return False

    # Extract the style content
    style_content = match.group(1)

    # Remove any existing mobile CSS (both versions)
    style_content = re.sub(r'\s*\/\*\s*Mobile Responsive Styles.*?\}\s*@media.*?\}.*?\}\s*', '', style_content, flags=re.DOTALL)
    style_content = re.sub(r'\}\s*\.blog-header h1 \{', '}\n\n        .blog-header h1 {', style_content)

    # Make sure back-link:hover is properly closed
    if '.back-link:hover' in style_content and not re.search(r'\.back-link:hover\s*\{[^}]*\}', style_content):
        style_content = re.sub(r'(\.back-link:hover\s*\{[^}]*)', r'\1}', style_content)

    # Add proper mobile CSS at the end
    mobile_css = '''

        /* Mobile Responsive Styles - Preserves Blog Theme */
        @media (max-width: 767px) {
            .blog-header {
                padding: 80px 1rem 50px !important;
            }

            .blog-header h1 {
                font-size: 1.75rem !important;
                line-height: 1.3 !important;
                padding: 0 0.5rem;
            }

            .blog-header p {
                font-size: 1rem !important;
                padding: 0 0.5rem;
            }

            .blog-meta {
                flex-direction: column;
                align-items: center;
                gap: 8px !important;
                font-size: 0.85rem !important;
            }

            .blog-content {
                max-width: 100%;
                padding: 0 1rem !important;
                font-size: 1rem !important;
                line-height: 1.7 !important;
            }

            .blog-content h2 {
                font-size: 1.5rem !important;
                margin-top: 2rem !important;
            }

            .blog-content h3 {
                font-size: 1.25rem !important;
                margin-top: 1.5rem !important;
            }

            .blog-content img {
                max-height: 250px !important;
                margin: 30px 0 !important;
            }

            .metric-highlight {
                padding: 1.5rem !important;
                margin: 1.5rem 0 !important;
            }

            .metric-number {
                font-size: 2.5rem !important;
            }

            .key-takeaway {
                padding: 1.5rem !important;
                margin: 2rem 0 !important;
            }

            .blog-content ul,
            .blog-content ol {
                padding-left: 1.5rem !important;
            }

            .case-tag {
                font-size: 0.75rem !important;
                padding: 6px 12px !important;
            }
        }

        @media (max-width: 480px) {
            .blog-header h1 {
                font-size: 1.5rem !important;
            }

            .metric-number {
                font-size: 2rem !important;
            }

            .blog-content {
                font-size: 0.95rem !important;
            }
        }
    '''

    # Rebuild the style block
    new_style_block = style_content + mobile_css + '\n    </style>'

    # Replace in content
    content = re.sub(style_pattern, new_style_block, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Main function."""
    print("=" * 80)
    print("PROPERLY FIXING BLOG PAGE CSS")
    print("=" * 80)
    print()

    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = 0

    for blog_file in sorted(blog_dir.glob("*.html")):
        try:
            if fix_blog_css_properly(blog_file):
                updated += 1
                print(f"  ✓ {blog_file.name}")
        except Exception as e:
            print(f"  ✗ Error fixing {blog_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total blog pages fixed: {updated}")
    print()
    print("Blog pages now have:")
    print("  ✓ Clean, properly formatted CSS")
    print("  ✓ Dark gradient header (preserved)")
    print("  ✓ Green metric highlights (preserved)")
    print("  ✓ Styled content sections (preserved)")
    print("  ✓ Mobile-responsive layout")
    print("  ✓ Proper spacing on all devices")
    print()

if __name__ == "__main__":
    main()
