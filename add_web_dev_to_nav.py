#!/usr/bin/env python3
"""
Add Web Development to Services dropdown across all pages
"""

import re
from pathlib import Path

def add_web_dev_to_nav(filepath):
    """Add Web Development link to Services dropdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Web Development link already exists
    if 'web-development.html' in content:
        return False

    # Pattern: Find where to insert Web Development
    # Look for "Workflow Automations" followed by "Growth Consulting"
    # Different files may have different relative paths

    # Determine the correct path prefix based on file location
    if '/services/' in str(filepath):
        web_dev_link = '<a href="../services/web-development.html">Web Development</a>'
        workflow_pattern = r'(<a href="../services/workflow-automation\.html">Workflow Automations</a>)\s*(<a href="../services/consulting\.html">Growth Consulting</a>)'
    elif '/niches/' in str(filepath):
        web_dev_link = '<a href="../services/web-development.html">Web Development</a>'
        workflow_pattern = r'(<a href="../services/workflow-automation\.html">Workflow Automations</a>)\s*(<a href="../services/consulting\.html">Growth Consulting</a>)'
    else:  # index.html or root level
        web_dev_link = '<a href="pages/services/web-development.html">Web Development</a>'
        workflow_pattern = r'(<a href="pages/services/workflow-automation\.html">Workflow Automations</a>)\s*(<a href="pages/services/consulting\.html">Growth Consulting</a>)'

    if re.search(workflow_pattern, content):
        # Insert Web Development between Workflow Automations and Growth Consulting
        replacement = r'\1\n                        ' + web_dev_link + r'\n                        \2'
        content = re.sub(workflow_pattern, replacement, content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING WEB DEVELOPMENT TO SERVICES DROPDOWN")
    print("=" * 80)
    print()

    base_dir = Path("/Users/juandelossantos/Desktop/Skills Master")

    # Gather all HTML files that need updating
    files_to_update = []

    # Service pages
    service_files = list((base_dir / "pages" / "services").glob("*.html"))
    files_to_update.extend(service_files)

    # Industry pages
    niche_files = list((base_dir / "pages" / "niches").glob("*.html"))
    files_to_update.extend(niche_files)

    # Root index and blog
    if (base_dir / "index.html").exists():
        files_to_update.append(base_dir / "index.html")
    if (base_dir / "pages" / "blog.html").exists():
        files_to_update.append(base_dir / "pages" / "blog.html")

    updated = []
    skipped = []

    for filepath in sorted(files_to_update):
        try:
            if add_web_dev_to_nav(filepath):
                updated.append(filepath.name)
                print(f"  ✓ {filepath.name}")
            else:
                skipped.append(filepath.name)
                print(f"  ⊙ {filepath.name} (already has Web Development link)")
        except Exception as e:
            print(f"  ✗ Error updating {filepath.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {len(updated)}")
    print(f"Total pages skipped (already updated): {len(skipped)}")
    print()
    print("Services dropdown now includes:")
    print("  ✓ Voice AI Agents")
    print("  ✓ Custom Apps")
    print("  ✓ Review Management")
    print("  ✓ Private AI")
    print("  ✓ Lead Capture")
    print("  ✓ Data Intelligence")
    print("  ✓ Workflow Automations")
    print("  ✓ Web Development (NEWLY ADDED)")
    print("  ✓ Growth Consulting")
    print()

if __name__ == "__main__":
    main()
