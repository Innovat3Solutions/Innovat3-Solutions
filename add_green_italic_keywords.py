#!/usr/bin/env python3
"""
Add green italic styling to specific keywords across service pages
"""

import re
from pathlib import Path

# Define the updates for each page
# Format: (filepath, [(pattern, replacement, description)])
UPDATES = {
    "custom-apps.html": [
        (r'\b(Custom)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "Custom in title/hero"),
        (r'\b([Bb]rand)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "brand in 'your brand, their pocket'"),
    ],
    "review-automation.html": [
        (r'\b([Aa]utomated)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "Automated"),
        (r'\b([Mm]arketers)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "marketers in 'turn happy customers into marketers'"),
    ],
    "private-ai-infra.html": [
        (r'Private AI', r'<em style="color: #84CC16; font-style: italic;">Private AI</em>', "Private AI"),
        (r'\b([Dd]ata)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "data in 'your data, your rules'"),
        (r'\b([Rr]ules)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "rules in 'your data, your rules'"),
    ],
    "lead-database.html": [
        (r'\b([Ii]nstant)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "instant"),
        (r'\b(Stop)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "Stop in 'stop buying dead lists'"),
    ],
    "data-intelligence.html": [
        (r'\b([Cc]ustomer)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "customer"),
        (r'\b([Ss]uperpower)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "superpower in 'Data is your superpower'"),
    ],
    "workflow-automation.html": [
        (r'Workflow Automation', r'<em style="color: #84CC16; font-style: italic;">Workflow Automation</em>', "Workflow Automation"),
        (r'\b([Ii]nvisible)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "invisible in 'the invisible workforce'"),
    ],
    "consulting.html": [
        (r'\b([Cc]onsulting)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "consulting"),
        (r'\b([Aa]rchitecture)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "architecture"),
        (r'\b([Cc]haos)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "chaos in 'from chaos to clockwork'"),
        (r'\b([Cc]lockwork)\b', r'<em style="color: #84CC16; font-style: italic;">\1</em>', "clockwork in 'from chaos to clockwork'"),
    ],
}

def add_green_italic_to_page(filepath, replacements):
    """Add green italic styling to specific words on a page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = []

    for pattern, replacement, description in replacements:
        # Check if the pattern exists and isn't already styled
        if re.search(pattern, content):
            # Skip if already has the em style wrapper
            check_pattern = pattern.replace(r'\b', '').replace('(', '').replace(')', '')
            if f'<em style="color: #84CC16; font-style: italic;">{check_pattern}</em>' not in content:
                # Apply the replacement
                new_content = re.sub(pattern, replacement, content, count=1)
                if new_content != content:
                    changes_made.append(description)
                    content = new_content

    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made

    return False, []

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING GREEN ITALIC STYLING TO SERVICE PAGE KEYWORDS")
    print("=" * 80)
    print()

    services_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/services")
    total_updated = 0

    for filename, replacements in UPDATES.items():
        filepath = services_dir / filename

        if not filepath.exists():
            print(f"  ✗ {filename} not found")
            continue

        try:
            updated, changes = add_green_italic_to_page(filepath, replacements)

            if updated:
                total_updated += 1
                print(f"  ✓ {filename}")
                for change in changes:
                    print(f"      • {change}")
            else:
                print(f"  ⊙ {filename} (no changes needed)")

        except Exception as e:
            print(f"  ✗ Error updating {filename}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {total_updated}")
    print()
    print("Styled keywords:")
    print("  ✓ Custom Apps: 'custom', 'brand'")
    print("  ✓ Review Management: 'automated', 'marketers'")
    print("  ✓ Private AI: 'Private AI', 'data', 'rules'")
    print("  ✓ Lead Capture: 'instant', 'Stop'")
    print("  ✓ Data Intelligence: 'customer', 'superpower'")
    print("  ✓ Workflow Automation: 'Workflow Automation', 'invisible'")
    print("  ✓ Growth Consulting: 'consulting', 'architecture', 'chaos', 'clockwork'")
    print()
    print("All keywords now appear in green (#84CC16) and italic styling.")
    print()

if __name__ == "__main__":
    main()
