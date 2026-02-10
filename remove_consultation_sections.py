#!/usr/bin/env python3
"""
Remove the "Ready to dominate your market?" consultation section from all industry pages
"""

import re
from pathlib import Path

def remove_consultation_section(filepath):
    """Remove the consultation section from an industry page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the entire consultation section
    # Starting with the comment and section tag, ending with the closing section tag
    pattern = r'<!-- 6\. FINAL CTA \(Consultation Section\) -->.*?<section[^>]*class="consultation-section"[^>]*>.*?</section>'

    # Check if pattern exists
    if re.search(pattern, content, flags=re.DOTALL):
        # Remove the section
        content = re.sub(pattern, '', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("REMOVING CONSULTATION SECTIONS FROM INDUSTRY PAGES")
    print("=" * 80)
    print()

    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    removed_count = 0

    for industry_file in industry_dir.glob("*.html"):
        try:
            if remove_consultation_section(industry_file):
                removed_count += 1
                print(f"  ✓ {industry_file.name}")
        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total sections removed: {removed_count}")
    print()
    print("Note: The unified contact section is still present on all pages.")
    print()

if __name__ == "__main__":
    main()
