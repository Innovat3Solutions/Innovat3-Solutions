#!/usr/bin/env python3
"""
Fix blog page designs - replace aggressive mobile CSS with proper responsive styling
"""

import re
from pathlib import Path

def fix_blog_design(filepath):
    """Replace the mobile CSS with proper responsive styling that preserves the blog theme."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the aggressive mobile CSS we added before
    old_mobile_css_pattern = r'\s*\/\* Mobile Responsive Styles \*\/.*?@media \(max-width: 767px\) \{.*?\}\s*'

    # Check if our mobile CSS exists
    if not re.search(old_mobile_css_pattern, content, re.DOTALL):
        return False

    # Remove old mobile CSS
    content = re.sub(old_mobile_css_pattern, '', content, flags=re.DOTALL)

    # Add proper responsive CSS that preserves the blog design
    proper_mobile_css = '''
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

    # Find the closing </style> tag and insert before it
    style_close_pattern = r'(</style>)'
    content = re.sub(style_close_pattern, proper_mobile_css + r'\n    \1', content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Main function."""
    print("=" * 80)
    print("FIXING BLOG PAGE DESIGNS - PRESERVING THEME")
    print("=" * 80)
    print()

    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = []
    skipped = []

    for blog_file in sorted(blog_dir.glob("*.html")):
        try:
            if fix_blog_design(blog_file):
                updated.append(blog_file.name)
                print(f"  ✓ {blog_file.name}")
            else:
                skipped.append(blog_file.name)
                print(f"  ⊙ {blog_file.name} (no changes needed)")
        except Exception as e:
            print(f"  ✗ Error fixing {blog_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total blog pages fixed: {len(updated)}")
    print(f"Total blog pages skipped: {len(skipped)}")
    print()
    print("Blog design preserved with:")
    print("  ✓ Dark gradient header maintained")
    print("  ✓ Green metric highlights preserved")
    print("  ✓ Styled content sections kept")
    print("  ✓ Professional layout on desktop")
    print("  ✓ Responsive layout on mobile")
    print("  ✓ Proper spacing and typography")
    print()

if __name__ == "__main__":
    main()
