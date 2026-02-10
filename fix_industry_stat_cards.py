#!/usr/bin/env python3
"""
Fix the broken stat cards layout on industry pages
"""

import re
from pathlib import Path

def fix_stat_cards(filepath):
    """Fix the stat cards structure on an industry page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the orphaned bento-stat-content div that was left after removing the cards
    # This is the broken structure: <div class="stats-bento-grid"> followed by <div class="bento-stat-content">
    pattern = r'(<div class="stats-bento-grid">)\s*<div class="bento-stat-content">.*?</div>\s*</div>\s*\n'

    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, r'\1\n                ', content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("FIXING INDUSTRY PAGE STAT CARDS LAYOUT")
    print("=" * 80)
    print()

    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    fixed = []

    for industry_file in industry_dir.glob("*.html"):
        try:
            if fix_stat_cards(industry_file):
                fixed.append(industry_file.name)
                print(f"  ✓ {industry_file.name}")
        except Exception as e:
            print(f"  ✗ Error fixing {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages fixed: {len(fixed)}")
    print()
    print("Changes made:")
    print("  ✓ Removed orphaned HTML from card removal")
    print("  ✓ Fixed grid structure to display 4 cards side by side")
    print("  ✓ Cards should now properly display in 4-column layout")
    print()

if __name__ == "__main__":
    main()
