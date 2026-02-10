#!/bin/bash

echo "======================================================================"
echo "CAROUSEL FUNCTIONALITY VERIFICATION SCRIPT"
echo "======================================================================"
echo ""

NICHES_DIR="/Users/juandelossantos/Desktop/Skills Master/pages/niches"
CSS_FILE="/Users/juandelossantos/Desktop/Skills Master/css/mobile-optimizations.css"

# Check if mobile-optimizations.css exists
if [ ! -f "$CSS_FILE" ]; then
    echo "❌ ERROR: mobile-optimizations.css not found!"
    exit 1
fi

echo "✅ mobile-optimizations.css found"
echo ""

# Check if CSS contains the carousel rules
echo "Checking CSS file for carousel rules..."
echo ""

if grep -q "\.services-grid" "$CSS_FILE"; then
    echo "✅ .services-grid rules found"
else
    echo "❌ .services-grid rules NOT found"
fi

if grep -q "\.pillars-grid" "$CSS_FILE"; then
    echo "✅ .pillars-grid rules found"
else
    echo "❌ .pillars-grid rules NOT found"
fi

if grep -q "grid-template-columns: none" "$CSS_FILE"; then
    echo "✅ grid-template-columns: none override found"
else
    echo "❌ grid-template-columns: none override NOT found"
fi

if grep -q "scroll-snap-type: x mandatory" "$CSS_FILE"; then
    echo "✅ scroll-snap-type configuration found"
else
    echo "❌ scroll-snap-type configuration NOT found"
fi

echo ""
echo "----------------------------------------------------------------------"
echo "Checking industry pages for CSS link..."
echo "----------------------------------------------------------------------"
echo ""

TOTAL_PAGES=$(ls "$NICHES_DIR"/*.html 2>/dev/null | wc -l | tr -d ' ')
LINKED_PAGES=$(grep -l "mobile-optimizations.css" "$NICHES_DIR"/*.html 2>/dev/null | wc -l | tr -d ' ')

echo "Total industry pages: $TOTAL_PAGES"
echo "Pages with mobile-optimizations.css: $LINKED_PAGES"
echo ""

if [ "$TOTAL_PAGES" -eq "$LINKED_PAGES" ]; then
    echo "✅ All industry pages have mobile-optimizations.css linked"
else
    echo "⚠️  Some pages missing mobile-optimizations.css link"
    echo "Missing pages:"
    for page in "$NICHES_DIR"/*.html; do
        if ! grep -q "mobile-optimizations.css" "$page"; then
            echo "  - $(basename "$page")"
        fi
    done
fi

echo ""
echo "----------------------------------------------------------------------"
echo "Checking specific carousel CSS properties..."
echo "----------------------------------------------------------------------"
echo ""

# Extract and verify specific CSS rules
echo "Services Grid Carousel Rules:"
grep -A 10 "\.services-grid" "$CSS_FILE" | grep -E "(display:|flex-direction:|overflow-x:|scroll-snap-type:|grid-template-columns:)" | head -5
echo ""

echo "Pillars Grid Carousel Rules:"
grep -A 10 "\.pillars-grid" "$CSS_FILE" | grep -E "(display:|flex-direction:|overflow-x:|scroll-snap-type:|grid-template-columns:)" | head -5
echo ""

echo "----------------------------------------------------------------------"
echo "Sample Page Check: nail-salons.html"
echo "----------------------------------------------------------------------"
echo ""

SAMPLE_PAGE="$NICHES_DIR/nail-salons.html"

if [ -f "$SAMPLE_PAGE" ]; then
    if grep -q "mobile-optimizations.css" "$SAMPLE_PAGE"; then
        echo "✅ nail-salons.html has CSS linked"
    else
        echo "❌ nail-salons.html missing CSS link"
    fi

    if grep -q "services-grid" "$SAMPLE_PAGE"; then
        echo "✅ nail-salons.html has .services-grid section"
    else
        echo "❌ nail-salons.html missing .services-grid section"
    fi

    if grep -q "pillars-grid" "$SAMPLE_PAGE"; then
        echo "✅ nail-salons.html has .pillars-grid section"
    else
        echo "❌ nail-salons.html missing .pillars-grid section"
    fi
else
    echo "❌ nail-salons.html not found"
fi

echo ""
echo "======================================================================"
echo "VERIFICATION COMPLETE"
echo "======================================================================"
echo ""
echo "Next Steps:"
echo "  1. Open test_carousel_mobile.html in a browser"
echo "  2. Resize to < 767px width"
echo "  3. Verify horizontal scrolling works"
echo "  4. Test on actual industry page (e.g., nail-salons.html)"
echo ""
echo "Documentation:"
echo "  - CAROUSEL_VERIFICATION.md - Detailed verification checklist"
echo "  - CAROUSEL_FIX_SUMMARY.md - Complete implementation summary"
echo "  - test_carousel_mobile.html - Standalone test file"
echo ""
