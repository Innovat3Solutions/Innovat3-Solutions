#!/usr/bin/env python3
"""
Update homepage stat cards with animated clock and trending chart
"""

import re
from pathlib import Path

def update_homepage_stats():
    """Update the Rapid Launch and ROI cards on homepage."""
    filepath = Path("/Users/juandelossantos/Desktop/Skills Master/index.html")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Rapid Launch card (bars) with animated clock
    rapid_launch_old = r'<!-- Card 3: Rapid Launch \(Bars\) -->.*?</div>\s*</div>\s*<!-- Card 4: ROI'

    rapid_launch_new = '''<!-- Card 3: Rapid Launch (Animated Clock) -->
                <div class="stat-card">
                    <div class="stat-visual">
                        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#84CC16" stroke-width="2" class="animated-clock">
                            <circle cx="12" cy="12" r="10" stroke="#e2e8f0" fill="none"></circle>
                            <circle cx="12" cy="12" r="10" stroke="#84CC16" fill="none"></circle>
                            <polyline points="12 6 12 12 16 14" class="clock-hand" stroke="#84CC16" stroke-width="2.5" stroke-linecap="round"></polyline>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <h3>Rapid Launch</h3>
                        <p style="color: #64748b; font-size: 14px;">Live in &lt; 48 Hours</p>
                    </div>
                </div>

                <!-- Card 4: ROI'''

    content = re.sub(rapid_launch_old, rapid_launch_new, content, flags=re.DOTALL)

    # Replace ROI card (counter) with animated trending chart + counter
    roi_old = r'<!-- Card 4: ROI \(Counter\) -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>'

    roi_new = '''<!-- Card 4: ROI (Trending Chart) -->
                <div class="stat-card">
                    <div class="stat-visual">
                        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#84CC16" stroke-width="2.5" class="animated-chart">
                            <polyline points="3,18 7,14 11,16 15,10 19,13 23,7" class="chart-line" stroke="#84CC16"></polyline>
                            <circle cx="23" cy="7" r="2" fill="#84CC16" class="chart-dot"></circle>
                            <text x="12" y="22" text-anchor="middle" fill="#84CC16" font-size="8" font-weight="600">
                                <tspan class="counter-anim" data-target="300">300</tspan>%
                            </text>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <h3>Avg. ROI</h3>
                        <p style="color: #64748b; font-size: 14px;">First 90 days</p>
                    </div>
                </div>

            </div>
        </div>
    </section>'''

    content = re.sub(roi_old, roi_new, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✓ Updated homepage stat cards")

def main():
    """Main function."""
    print("=" * 80)
    print("UPDATING HOMEPAGE STAT CARDS")
    print("=" * 80)
    print()

    update_homepage_stats()

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print("Updated homepage stat cards:")
    print("  ✓ Rapid Launch - Now has animated rotating clock")
    print("  ✓ AVG. ROI - Now has animated upward trending chart in green")
    print()
    print("Animations:")
    print("  - Clock rotates continuously with ticking hands")
    print("  - Chart line draws and redraws with pulsing dot")
    print("  - All in brand green (#84CC16)")
    print()

if __name__ == "__main__":
    main()
