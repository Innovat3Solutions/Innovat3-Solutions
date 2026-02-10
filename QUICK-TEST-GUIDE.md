# Quick Test Guide - Mobile Carousels

## 🎯 Quick Test (2 Minutes)

### Option 1: Chrome DevTools
1. Open any industry page: `pages/niches/accountants-and-cpas.html`
2. Press `F12` (Windows) or `Cmd+Option+I` (Mac)
3. Press `Ctrl+Shift+M` (Windows) or `Cmd+Shift+M` (Mac)
4. Select "iPhone 12 Pro" or set width to `375px`
5. Scroll to "Our Capabilities" section
6. ✅ Should scroll horizontally with snap behavior

### Option 2: Test Page
1. Open `file:///Users/juandelossantos/Desktop/Skills%20Master/test-carousel.html`
2. Resize browser window to < 767px width
3. ✅ Both grids should be horizontal carousels

### Option 3: Real Device
1. Open any industry page on actual iPhone/Android
2. Scroll to carousel sections
3. ✅ Swipe horizontally through cards

---

## 📱 What to Look For

### ✅ WORKING (Expected Behavior):
- Horizontal scrolling (left/right swipe)
- Cards are ~85-90% of screen width
- Can see edge of next card (peek effect)
- Smooth snap-to-card behavior
- No scrollbar visible
- Touch scrolling feels smooth

### ❌ BROKEN (If Still Not Working):
- Cards stacked vertically
- Grid layout on mobile
- Can't scroll horizontally
- Cards too small/overlapping
- Visible scrollbar
- Janky scrolling

---

## 🔧 If Carousels Still Don't Work

### Check 1: Browser Cache
```bash
# Clear cache and hard reload
Ctrl+Shift+R (Windows)
Cmd+Shift+R (Mac)
```

### Check 2: File Linked
Look in HTML `<head>` for:
```html
<link rel="stylesheet" href="../../css/mobile-optimizations.css">
```

### Check 3: Media Query Active
1. Open DevTools (F12)
2. Go to "Elements" tab
3. Find `.services-grid` element
4. Check computed styles
5. Should show `display: flex` on mobile

### Check 4: Run Verification
```bash
cd "/Users/juandelossantos/Desktop/Skills Master"
bash verify-carousels.sh
```

---

## 🎨 Visual Test Checklist

### "Our Capabilities" Section (services-grid):
- [ ] 4 columns on desktop (> 767px)
- [ ] Horizontal carousel on mobile (< 767px)
- [ ] Cards at 85% viewport width on mobile
- [ ] Peek effect showing next card
- [ ] Snap behavior when releasing

### "Blueprint to Market Dominance" Section (pillars-grid):
- [ ] 3 columns on desktop (> 767px)
- [ ] Horizontal carousel on mobile (< 767px)
- [ ] Cards at 90% viewport width on mobile
- [ ] Peek effect showing next card
- [ ] Snap behavior when releasing
- [ ] Connecting line hidden on mobile

---

## 📊 Quick Verification Commands

### Check all pages have CSS linked:
```bash
for file in "/Users/juandelossantos/Desktop/Skills Master/pages/niches/"*.html; do
    grep -q "mobile-optimizations.css" "$file" && echo "✓ $(basename "$file")" || echo "✗ $(basename "$file")";
done
```

### Check CSS file exists:
```bash
ls -lh "/Users/juandelossantos/Desktop/Skills Master/css/mobile-optimizations.css"
```

### Test specific page:
```bash
open "/Users/juandelossantos/Desktop/Skills Master/pages/niches/accountants-and-cpas.html"
```

---

## 🌐 Test URLs (Local)

Replace `YOUR_SERVER` with your local server URL:

```
http://YOUR_SERVER/pages/niches/accountants-and-cpas.html
http://YOUR_SERVER/pages/niches/dentists-and-orthodontists.html
http://YOUR_SERVER/pages/niches/general-contractors.html
http://YOUR_SERVER/test-carousel.html
```

---

## 📱 Recommended Test Devices

### Real Devices (Best):
- iPhone 12/13/14 (Safari)
- Samsung Galaxy S21/S22 (Chrome)
- Google Pixel 5/6 (Chrome)

### DevTools Emulation (Good):
- iPhone 12 Pro (375 x 812)
- iPhone SE (375 x 667)
- Pixel 5 (393 x 851)
- Galaxy S20 (360 x 800)

### Custom Width (Quick):
- 375px - iPhone standard
- 390px - iPhone 12 Pro Max
- 360px - Android standard

---

## 🐛 Common Issues & Fixes

### Issue: Carousel not scrolling
**Fix:** Hard refresh (Ctrl+Shift+R)

### Issue: Cards too small
**Fix:** Check viewport meta tag in HTML

### Issue: Vertical scroll instead of horizontal
**Fix:** Verify CSS loaded (check DevTools Network tab)

### Issue: Grid still showing on mobile
**Fix:** Clear browser cache completely

### Issue: Scrollbar visible
**Fix:** Check `::-webkit-scrollbar` styles applied

---

## ✅ Success Criteria

All of these should be true:

- [x] 25/25 industry pages have mobile-optimizations.css
- [x] 25/25 pages have .services-grid element
- [x] 25/25 pages have .pillars-grid element
- [x] CSS overrides inline grid styles
- [x] Flex display on mobile (< 767px)
- [x] Grid display on desktop (> 767px)
- [x] Horizontal scroll works
- [x] Snap behavior works
- [x] Scrollbar hidden
- [x] Touch optimized

**Current Status: ALL PASSING ✅**

---

## 📞 Quick Support

If issues persist:
1. Check `CAROUSEL-FIX-SUMMARY.md` for detailed info
2. Check `BEFORE-AFTER-COMPARISON.md` for visual comparison
3. Run `verify-carousels.sh` for automated check

**Last Updated:** February 4, 2026
**Fix Status:** ✅ Complete and Verified
