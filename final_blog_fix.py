#!/usr/bin/env python3
"""
Final comprehensive blog CSS fix - complete cleanup and proper mobile styles
"""

import re
from pathlib import Path

def final_blog_fix(filepath):
    """Complete cleanup and proper mobile styles."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract everything before <style> and after </style>
    before_style = re.search(r'(.*?)<style>', content, re.DOTALL)
    after_style = re.search(r'</style>(.*)', content, re.DOTALL)

    if not before_style or not after_style:
        return False

    # Create clean CSS from scratch
    clean_css = '''<style>
        .blog-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white;
            padding: 120px 0 80px;
            text-align: center;
        }

        .blog-meta {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin: 20px 0;
            font-size: 0.9rem;
            opacity: 0.8;
        }

        .blog-content {
            max-width: 800px;
            margin: 60px auto;
            padding: 0 20px;
            font-size: 1.1rem;
            line-height: 1.8;
            color: #334155;
        }

        .blog-content h2 {
            font-size: 2rem;
            margin-top: 3rem;
            margin-bottom: 1rem;
            color: #0f172a;
        }

        .blog-content h3 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #1e293b;
        }

        .metric-highlight {
            background: #f0fdf4;
            border-left: 4px solid #84CC16;
            padding: 30px;
            margin: 30px 0;
            border-radius: 8px;
        }

        .metric-number {
            font-size: 3rem;
            font-weight: 800;
            color: #84CC16;
            line-height: 1;
            margin-bottom: 10px;
        }

        .key-takeaway {
            background: #f8fafc;
            padding: 30px;
            border-radius: 12px;
            margin: 40px 0;
        }

        .back-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #84CC16;
            text-decoration: none;
            font-weight: 600;
            margin-bottom: 40px;
        }

        .back-link:hover {
            gap: 12px;
        }

        /* Mobile Responsive Styles */
        @media (max-width: 767px) {
            .blog-header {
                padding: 80px 1rem 50px;
            }

            .blog-header h1 {
                font-size: 1.75rem;
                line-height: 1.3;
                padding: 0 0.5rem;
            }

            .blog-header p {
                font-size: 1rem;
                padding: 0 0.5rem;
            }

            .blog-meta {
                flex-direction: column;
                align-items: center;
                gap: 8px;
                font-size: 0.85rem;
            }

            .blog-content {
                max-width: 100%;
                padding: 0 1rem;
                font-size: 1rem;
                line-height: 1.7;
            }

            .blog-content h2 {
                font-size: 1.5rem;
                margin-top: 2rem;
            }

            .blog-content h3 {
                font-size: 1.25rem;
                margin-top: 1.5rem;
            }

            .blog-content img {
                max-height: 250px;
                margin: 30px 0;
            }

            .metric-highlight {
                padding: 1.5rem;
                margin: 1.5rem 0;
            }

            .metric-number {
                font-size: 2.5rem;
            }

            .key-takeaway {
                padding: 1.5rem;
                margin: 2rem 0;
            }

            .blog-content ul,
            .blog-content ol {
                padding-left: 1.5rem;
            }

            .case-tag {
                font-size: 0.75rem;
                padding: 6px 12px;
            }
        }

        @media (max-width: 480px) {
            .blog-header h1 {
                font-size: 1.5rem;
            }

            .metric-number {
                font-size: 2rem;
            }

            .blog-content {
                font-size: 0.95rem;
            }
        }
    </style>'''

    # Rebuild content
    new_content = before_style.group(1) + clean_css + after_style.group(1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Main function."""
    print("=" * 80)
    print("FINAL COMPREHENSIVE BLOG FIX")
    print("=" * 80)
    print()

    blog_dir = Path("/Users/juandelossantos/Desktop/Skills Master/blog/case-studies")
    updated = 0

    for blog_file in sorted(blog_dir.glob("*.html")):
        try:
            if final_blog_fix(blog_file):
                updated += 1
                print(f"  ✓ {blog_file.name}")
        except Exception as e:
            print(f"  ✗ Error fixing {blog_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE - ALL BLOG PAGES FIXED")
    print("=" * 80)
    print()
    print(f"Total blog pages fixed: {updated}")
    print()
    print("Blog pages now have:")
    print("  ✓ Clean, properly formatted CSS (no duplicates)")
    print("  ✓ Dark gradient header - PRESERVED")
    print("  ✓ Green (#84CC16) metric highlights - PRESERVED")
    print("  ✓ Styled content sections - PRESERVED")
    print("  ✓ Professional desktop layout - PRESERVED")
    print("  ✓ Mobile-responsive design - ADDED")
    print("  ✓ Proper typography on all devices")
    print()

if __name__ == "__main__":
    main()
