#!/usr/bin/env python3
"""
Fix homepage stat cards - make them crisp and uniform in color
"""

import re
from pathlib import Path

def fix_homepage_stats():
    """Fix the stat cards on homepage for consistency and clarity."""
    filepath = Path("/Users/juandelossantos/Desktop/Skills Master/index.html")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Rapid Launch card with cleaner version
    rapid_launch_pattern = r'<!-- Card 3: Rapid Launch \(Animated Clock\) -->.*?</div>\s*</div>\s*<!-- Card 4: ROI'

    rapid_launch_new = '''<!-- Card 3: Rapid Launch (Animated Clock) -->
                <div class="stat-card">
                    <div class="stat-visual">
                        <svg width="80" height="80" viewBox="0 0 80 80" fill="none" class="animated-clock" style="shape-rendering: geometricPrecision;">
                            <circle cx="40" cy="40" r="32" stroke="#e2e8f0" stroke-width="3" fill="none"></circle>
                            <circle cx="40" cy="40" r="32" stroke="#84CC16" stroke-width="3" fill="none"></circle>
                            <polyline points="40 20 40 40 52 46" class="clock-hand" stroke="#84CC16" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></polyline>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <h3>Rapid Launch</h3>
                        <p style="color: #64748b; font-size: 14px;">Live in &lt; 48 Hours</p>
                    </div>
                </div>

                <!-- Card 4: ROI'''

    content = re.sub(rapid_launch_pattern, rapid_launch_new, content, flags=re.DOTALL)

    # Replace ROI card with crisp trending chart
    roi_pattern = r'<!-- Card 4: ROI \(Trending Chart\) -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>'

    roi_new = '''<!-- Card 4: ROI (Trending Chart) -->
                <div class="stat-card">
                    <div class="stat-visual">
                        <svg width="80" height="80" viewBox="0 0 80 80" fill="none" class="animated-chart" style="shape-rendering: geometricPrecision;">
                            <!-- Trending line -->
                            <polyline points="10,60 22,48 34,52 46,36 58,42 70,24"
                                class="chart-line"
                                stroke="#84CC16"
                                stroke-width="3.5"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                fill="none"></polyline>
                            <!-- End dot -->
                            <circle cx="70" cy="24" r="4" fill="#84CC16" class="chart-dot"></circle>
                            <!-- 300% text -->
                            <text x="40" y="72" text-anchor="middle" fill="#84CC16" font-size="14" font-weight="700" font-family="Inter, sans-serif">
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

    content = re.sub(roi_pattern, roi_new, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✓ Fixed homepage stat cards")

def main():
    """Main function."""
    print("=" * 80)
    print("FIXING HOMEPAGE STAT CARDS - CRISP & UNIFORM")
    print("=" * 80)
    print()

    fix_homepage_stats()

    print()
    print("=" * 80)
    print("COMPLETE")
    print("=" * 80)
    print()
    print("Fixes applied:")
    print("  ✓ Changed viewBox to match width/height (80x80) for crisp rendering")
    print("  ✓ Added shape-rendering: geometricPrecision for sharp edges")
    print("  ✓ All colors now use uniform green (#84CC16)")
    print("  ✓ Increased stroke widths for better visibility")
    print("  ✓ Improved chart line smoothness and clarity")
    print("  ✓ Better text rendering in AVG. ROI card")
    print()

if __name__ == "__main__":
    main()
