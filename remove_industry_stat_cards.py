#!/usr/bin/env python3
"""
Remove the animated RAPID LAUNCH and AVG. ROI stat cards from industry pages
"""

import re
from pathlib import Path

def remove_animated_cards(filepath):
    """Remove the animated stat cards from an industry page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match both RAPID LAUNCH and AVG. ROI cards
    # They were added together, so remove both at once
    pattern = r'<!-- RAPID LAUNCH with animated clock -->.*?<!-- AVG\. ROI with animated trending chart -->.*?</div>\s*</div>\s*\n'

    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, '', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("REMOVING ANIMATED STAT CARDS FROM INDUSTRY PAGES")
    print("=" * 80)
    print()

    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    removed = []

    for industry_file in industry_dir.glob("*.html"):
        try:
            if remove_animated_cards(industry_file):
                removed.append(industry_file.name)
                print(f"  ✓ {industry_file.name}")
        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {len(removed)}")
    print()
    print("Removed cards:")
    print("  ✓ RAPID LAUNCH - Live in < 48 Hours")
    print("  ✓ 300% AVG. ROI - First 90 days")
    print()
    print("These cards now only appear on the homepage.")
    print()

if __name__ == "__main__":
    main()
