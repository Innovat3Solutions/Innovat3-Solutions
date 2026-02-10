#!/usr/bin/env python3
"""
Update all hero headings to remove bold and add green italics to key phrases
"""

import re
from pathlib import Path

def update_voice_ai_page():
    """Update Voice AI service page headings."""
    filepath = Path("/Users/juandelossantos/Desktop/Skills Master/pages/services/voice-ai.html")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change h1 font-weight from 700 to 300
    content = re.sub(
        r'(<h1[^>]*font-weight:)\s*700',
        r'\1 300',
        content
    )

    # Change stats font-weight from 700 to 300
    content = re.sub(
        r'(font-weight:)\s*700',
        r'\1 300',
        content
    )

    # Update "Voice Agents" to be italicized and green
    content = re.sub(
        r'(<span style="position: relative; display: inline-block;">)\s*Voice Agents',
        r'\1<em style="color: #84CC16; font-style: italic;">Voice Agents</em>',
        content
    )

    # Update "Not Just An Answering Machine" - make "Answering" green and italic
    content = re.sub(
        r'Not Just An Answering Machine',
        r'Not Just An <em style="color: #84CC16; font-style: italic;">Answering</em> Machine',
        content
    )

    # Update "Stop Wasting Time" - make "Wasting Time" green and italic
    content = re.sub(
        r'Stop Wasting Time on Spam',
        r'Stop <em style="color: #84CC16; font-style: italic;">Wasting Time</em> on Spam',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def update_all_service_pages():
    """Update all service pages to remove bold from headings."""
    service_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/services")
    updated = []

    for service_file in service_dir.glob("*.html"):
        try:
            with open(service_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove bold (font-weight: 700) from all headings
            modified = False

            # Change font-weight: 700 to font-weight: 300 in all contexts
            if 'font-weight: 700' in content or 'font-weight:700' in content:
                content = re.sub(r'font-weight:\s*700', 'font-weight: 300', content)
                modified = True

            if modified:
                with open(service_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated.append(service_file.name)

        except Exception as e:
            print(f"  ✗ Error updating {service_file.name}: {str(e)}")

    return updated

def update_all_industry_pages():
    """Update all industry pages to remove bold from headings."""
    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = []

    for industry_file in industry_dir.glob("*.html"):
        try:
            with open(industry_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove bold (font-weight: 700) from all headings
            modified = False

            # Change font-weight: 700 to font-weight: 300 in all contexts
            if 'font-weight: 700' in content or 'font-weight:700' in content:
                content = re.sub(r'font-weight:\s*700', 'font-weight: 300', content)
                modified = True

            if modified:
                with open(industry_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated.append(industry_file.name)

        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    return updated

def main():
    """Main function."""
    print("=" * 80)
    print("UPDATING HERO HEADINGS - REMOVING BOLD & ADDING GREEN ITALICS")
    print("=" * 80)
    print()

    # Update Voice AI page specifically
    print("Updating Voice AI page with green italics...")
    if update_voice_ai_page():
        print("  ✓ voice-ai.html")
    print()

    # Update all service pages to remove bold
    print("Removing bold from all service pages...")
    service_updated = update_all_service_pages()
    for filename in service_updated:
        print(f"  ✓ {filename}")
    print(f"  → {len(service_updated)} service pages updated")
    print()

    # Update all industry pages to remove bold
    print("Removing bold from all industry pages...")
    industry_updated = update_all_industry_pages()
    for filename in industry_updated:
        print(f"  ✓ {filename}")
    print(f"  → {len(industry_updated)} industry pages updated")
    print()

    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print("Changes made:")
    print("  ✓ All font-weight: 700 changed to font-weight: 300")
    print("  ✓ Voice AI page: 'Voice Agents' is now green and italicized")
    print("  ✓ Voice AI page: 'Answering' is now green and italicized")
    print("  ✓ Voice AI page: 'Wasting Time' is now green and italicized")
    print()
    print("Note: Other service/industry pages need manual keyword identification")
    print("for green italic emphasis on their specific key phrases.")
    print()

if __name__ == "__main__":
    main()
