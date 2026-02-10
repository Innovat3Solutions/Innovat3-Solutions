#!/usr/bin/env python3
"""
Standardize all major headings across the website to use consistent styling
"""

import re
from pathlib import Path

# CSS to add for consistent heading styling
HEADING_CSS = """
/* Consistent Heading Styling Across Website */
.section h2,
.section-header h2,
.niches h2,
.contact-left-content h2,
.unified-contact-section h2 {
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    color: #0f172a;
    margin-bottom: 1.5rem;
}

/* Responsive heading sizes */
@media (max-width: 1024px) {
    .section h2,
    .section-header h2,
    .niches h2,
    .contact-left-content h2,
    .unified-contact-section h2 {
        font-size: 2.5rem;
    }
}

@media (max-width: 768px) {
    .section h2,
    .section-header h2,
    .niches h2,
    .contact-left-content h2,
    .unified-contact-section h2 {
        font-size: 2rem;
    }
}
"""

def add_heading_css():
    """Add consistent heading CSS to styles.css"""
    css_file = Path("/Users/juandelossantos/Desktop/Skills Master/css/styles.css")

    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write(HEADING_CSS)

    print("✓ Added consistent heading CSS to styles.css")

def main():
    """Main function."""
    print("=" * 80)
    print("STANDARDIZING HEADING STYLES ACROSS WEBSITE")
    print("=" * 80)
    print()

    add_heading_css()

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print("All major section headings now use:")
    print("  - Font size: 3.5rem (desktop), 2.5rem (tablet), 2rem (mobile)")
    print("  - Font weight: 700 (bold)")
    print("  - Letter spacing: -0.02em")
    print("  - Color: #0f172a (dark slate)")
    print()
    print("Affected sections:")
    print("  ✓ Specialized for Your Industry")
    print("  ✓ Contact form headings")
    print("  ✓ All service page headings")
    print("  ✓ All industry page headings")
    print()

if __name__ == "__main__":
    main()
