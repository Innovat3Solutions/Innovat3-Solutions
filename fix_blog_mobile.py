#!/usr/bin/env python3
"""
Add mobile-responsive CSS to all blog pages
"""

import re
from pathlib import Path

def add_mobile_css_to_blog(filepath):
    """Add mobile-responsive CSS to blog page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if mobile styles already exist
    if '@media (max-width: 767px)' in content:
        return False

    # Find the closing </style> tag in the head
    style_pattern = r'(</style>)'

    mobile_css = '''
        /* Mobile Responsive Styles */
        @media (max-width: 767px) {
            .blog-header {
                padding: 100px 0 60px !important;
            }

            .blog-header h1 {
                font-size: 1.75rem !important;
                line-height: 1.3 !important;
            }

            .blog-header p {
                font-size: 1rem !important;
            }

            .blog-meta {
                flex-direction: column;
                gap: 10px !important;
                font-size: 0.85rem !important;
            }

            .blog-content {
                padding: 0 1rem !important;
                font-size: 1rem !important;
                line-height: 1.7 !important;
            }

            .blog-content h2 {
                font-size: 1.5rem !important;
            }

            .blog-content h3 {
                font-size: 1.25rem !important;
            }

            .metric-highlight {
                padding: 20px !important;
            }

            .metric-number {
                font-size: 2rem !important;
            }

            .key-takeaway {
                padding: 20px !important;
            }

            .blog-content img {
                height: auto !important;
                max-height: 250px !important;
            }
        }
    '''

    if re.search(style_pattern, content):
        # Insert mobile CSS before closing </style>
        content = re.sub(style_pattern, mobile_css + r'\n    \1', content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING MOBILE RESPONSIVE CSS TO ALL BLOG PAGES")
    print("=" * 80)
    print()

    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = []

    for blog_file in sorted(blog_dir.glob("*.html")):
        try:
            if add_mobile_css_to_blog(blog_file):
                updated.append(blog_file.name)
                print(f"  ✓ {blog_file.name}")
            else:
                print(f"  ⊙ {blog_file.name} (already has mobile CSS)")
        except Exception as e:
            print(f"  ✗ Error updating {blog_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total blog pages updated: {len(updated)}")
    print()
    print("Mobile responsive features added:")
    print("  ✓ Header padding reduced for mobile")
    print("  ✓ Title size adjusted (1.75rem)")
    print("  ✓ Content padding optimized")
    print("  ✓ Images auto-height on mobile")
    print("  ✓ Meta info stacked vertically")
    print("  ✓ Proper text sizing for readability")
    print()

if __name__ == "__main__":
    main()
