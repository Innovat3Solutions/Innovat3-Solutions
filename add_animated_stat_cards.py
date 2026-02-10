#!/usr/bin/env python3
"""
Add animated stat cards with clock and trending chart to industry pages
"""

import re
from pathlib import Path

# HTML for animated stat cards
ANIMATED_STATS_HTML = '''
                <!-- RAPID LAUNCH with animated clock -->
                <div class="stats-bento-card">
                    <div class="bento-stat-visual">
                        <div class="stat-icon-circle" style="background: linear-gradient(135deg, #84CC16 0%, #65a30d 100%);">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" class="animated-clock">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14" class="clock-hand"></polyline>
                            </svg>
                        </div>
                    </div>
                    <div class="bento-stat-content">
                        <div class="stat-number" style="font-size: 1.2rem; font-weight: 600;">RAPID LAUNCH</div>
                        <h3>Live in &lt; 48 Hours</h3>
                        <p>Get your AI automation up and running in less than 2 days.</p>
                    </div>
                </div>

                <!-- AVG. ROI with animated trending chart -->
                <div class="stats-bento-card">
                    <div class="bento-stat-visual">
                        <div class="stat-icon-circle" style="background: linear-gradient(135deg, #84CC16 0%, #65a30d 100%);">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" class="animated-chart">
                                <polyline points="3,18 7,14 11,16 15,10 19,13 23,7" class="chart-line"></polyline>
                                <circle cx="23" cy="7" r="2" fill="#84CC16" class="chart-dot"></circle>
                            </svg>
                        </div>
                    </div>
                    <div class="bento-stat-content">
                        <div class="stat-number" style="color: #84CC16;"><span class="counter-anim" data-target="300">0</span>%</div>
                        <h3>AVG. ROI</h3>
                        <p>First 90 days average return on investment.</p>
                    </div>
                </div>
'''

# CSS for animations
ANIMATION_CSS = '''
/* Animated Clock */
.animated-clock {
    animation: rotate-clock 4s linear infinite;
}

.clock-hand {
    transform-origin: 50% 50%;
    animation: tick-hand 2s ease-in-out infinite;
}

@keyframes rotate-clock {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes tick-hand {
    0%, 100% { transform: rotate(0deg); }
    50% { transform: rotate(90deg); }
}

/* Animated Chart */
.animated-chart .chart-line {
    stroke-dasharray: 100;
    stroke-dashoffset: 100;
    animation: draw-line 3s ease-in-out infinite;
}

.animated-chart .chart-dot {
    animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes draw-line {
    0% {
        stroke-dashoffset: 100;
        opacity: 0.3;
    }
    50% {
        stroke-dashoffset: 0;
        opacity: 1;
    }
    100% {
        stroke-dashoffset: -100;
        opacity: 0.3;
    }
}

@keyframes pulse-dot {
    0%, 100% {
        r: 2;
        opacity: 1;
    }
    50% {
        r: 3;
        opacity: 0.7;
    }
}
'''

def add_stat_cards_to_industry_page(filepath):
    """Add animated stat cards to an industry page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the stats-bento-grid section and add the new cards at the beginning
    pattern = r'(<div class="stats-bento-grid">)'

    if re.search(pattern, content):
        # Add the new stat cards right after the opening div
        content = re.sub(
            pattern,
            r'\1' + ANIMATED_STATS_HTML,
            content,
            count=1
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    return False

def add_animation_css():
    """Add animation CSS to styles.css"""
    css_file = Path("/Users/juandelossantos/Desktop/Skills Master/css/styles.css")

    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write(ANIMATION_CSS)

    print("✓ Added animation CSS to styles.css")

def main():
    """Main function."""
    print("=" * 80)
    print("ADDING ANIMATED STAT CARDS TO INDUSTRY PAGES")
    print("=" * 80)
    print()

    # Add CSS animations
    add_animation_css()
    print()

    # Update all industry pages
    industry_dir = Path("/Users/juandelossantos/Desktop/Skills Master/pages/niches")
    updated = []

    for industry_file in industry_dir.glob("*.html"):
        try:
            if add_stat_cards_to_industry_page(industry_file):
                updated.append(industry_file.name)
                print(f"  ✓ {industry_file.name}")
        except Exception as e:
            print(f"  ✗ Error updating {industry_file.name}: {str(e)}")

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print(f"Total pages updated: {len(updated)}")
    print()
    print("New animated stat cards added:")
    print("  ✓ RAPID LAUNCH - Live in < 48 Hours (animated clock)")
    print("  ✓ 300% AVG. ROI - First 90 days (trending chart in green)")
    print()

if __name__ == "__main__":
    main()
