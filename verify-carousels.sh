#!/bin/bash

# Carousel Verification Script
# This script checks that all industry pages have the required carousel elements

echo "=========================================="
echo "Carousel Structure Verification"
echo "=========================================="
echo ""

PAGES_DIR="/Users/juandelossantos/Desktop/Skills Master/pages/niches"
TOTAL_PAGES=0
PAGES_WITH_SERVICES=0
PAGES_WITH_PILLARS=0
PAGES_WITH_MOBILE_CSS=0

for file in "$PAGES_DIR"/*.html; do
    TOTAL_PAGES=$((TOTAL_PAGES + 1))
    BASENAME=$(basename "$file")

    echo "Checking: $BASENAME"

    # Check for mobile-optimizations.css
    if grep -q "mobile-optimizations.css" "$file"; then
        echo "  ✓ Mobile CSS linked"
        PAGES_WITH_MOBILE_CSS=$((PAGES_WITH_MOBILE_CSS + 1))
    else
        echo "  ✗ Mobile CSS NOT linked"
    fi

    # Check for services-grid
    if grep -q 'class="services-grid"' "$file"; then
        echo "  ✓ services-grid found"
        PAGES_WITH_SERVICES=$((PAGES_WITH_SERVICES + 1))
    else
        echo "  ✗ services-grid NOT found"
    fi

    # Check for pillars-grid
    if grep -q 'class="pillars-grid"' "$file"; then
        echo "  ✓ pillars-grid found"
        PAGES_WITH_PILLARS=$((PAGES_WITH_PILLARS + 1))
    else
        echo "  ✗ pillars-grid NOT found"
    fi

    echo ""
done

echo "=========================================="
echo "Summary"
echo "=========================================="
echo "Total pages checked: $TOTAL_PAGES"
echo "Pages with mobile-optimizations.css: $PAGES_WITH_MOBILE_CSS / $TOTAL_PAGES"
echo "Pages with services-grid: $PAGES_WITH_SERVICES / $TOTAL_PAGES"
echo "Pages with pillars-grid: $PAGES_WITH_PILLARS / $TOTAL_PAGES"
echo ""

if [ $PAGES_WITH_MOBILE_CSS -eq $TOTAL_PAGES ] && [ $PAGES_WITH_SERVICES -eq $TOTAL_PAGES ] && [ $PAGES_WITH_PILLARS -eq $TOTAL_PAGES ]; then
    echo "✅ All pages are properly configured!"
else
    echo "⚠️  Some pages may need attention"
fi

echo ""
echo "=========================================="
echo "Mobile-Optimizations.css Status"
echo "=========================================="

CSS_FILE="/Users/juandelossantos/Desktop/Skills Master/css/mobile-optimizations.css"

if [ -f "$CSS_FILE" ]; then
    echo "✓ File exists"

    # Check for services-grid carousel styles
    if grep -q ".services-section .services-grid" "$CSS_FILE"; then
        echo "✓ Services carousel styles present"
    else
        echo "✗ Services carousel styles missing"
    fi

    # Check for pillars-grid carousel styles
    if grep -q ".pillars-section .pillars-grid" "$CSS_FILE"; then
        echo "✓ Pillars carousel styles present"
    else
        echo "✗ Pillars carousel styles missing"
    fi

    # Check for flex display
    if grep -q "display: flex !important" "$CSS_FILE"; then
        echo "✓ Flex display rules present"
    else
        echo "✗ Flex display rules missing"
    fi

    # Check for scroll-snap
    if grep -q "scroll-snap-type: x mandatory" "$CSS_FILE"; then
        echo "✓ Scroll snap rules present"
    else
        echo "✗ Scroll snap rules missing"
    fi
else
    echo "✗ mobile-optimizations.css file not found!"
fi

echo ""
echo "=========================================="
echo "Testing Instructions"
echo "=========================================="
echo "1. Open any industry page in Chrome/Firefox"
echo "2. Press F12 to open DevTools"
echo "3. Toggle device toolbar (Ctrl+Shift+M or Cmd+Shift+M)"
echo "4. Select mobile device or set width < 767px"
echo "5. Verify these sections scroll horizontally:"
echo "   - Our Capabilities (services-grid)"
echo "   - Blueprint to Market Dominance (pillars-grid)"
echo ""
echo "Test file available at:"
echo "file:///Users/juandelossantos/Desktop/Skills%20Master/test-carousel.html"
echo ""
