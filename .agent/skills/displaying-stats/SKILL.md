---
name: displaying-stats
description: Implements the "Arc Fan" statistics display pattern. Use when the user wants to show stats in a curved, fanned-out card layout similar to the "Framer" reference.
---

# Arc Fan Stats Display

This skill implements a specific design pattern where statistic cards are arranged in an upward-facing arc or "fan" shape.

## When to use this skill
- Implementing the "Stats" section on a page.
- "Make the stats look like the Framer reference."
- "Fan out the cards" or "Arc layout".

## Core Design Principles

1.  **Card Style**:
    -   Square/Vertical Aspect Ratio.
    -   White Background with subtle shadow.
    -   Large Bold Number (Top).
    -   Small Descriptor Text (Bottom).

2.  **The Arc Layout**:
    -   Cards are positioned relative to a center point.
    -   Uses `transform: rotate(Ndeg) translateY(Ypx)` to create the arch.
    -   Outer cards are rotated more; inner cards are rotated less.
    -   **Animation**: Cards can optionally float or slide up on scroll.

## Component Blueprint

### HTML Structure
```html
<section class="section-stats-arc">
    <div class="container relative flex justify-center items-end h-[400px]"> <!-- Height needed for arc -->
        
        <!-- Card 1 (Far Left) - Rotated -15deg -->
        <div class="stat-card arc-1">
            <h3 class="text-4xl font-bold text-slate-900 mb-2">2 Hours</h3>
            <p class="text-sm text-slate-500">Used by millions if teams and professionals</p>
        </div>

        <!-- Card 2 (Mid Left) - Rotated -5deg -->
        <div class="stat-card arc-2">
            <h3 class="text-4xl font-bold text-slate-900 mb-2">500+</h3>
            <p class="text-sm text-slate-500">Used by millions if teams and professionals</p>
        </div>

        <!-- Card 3 (Mid Right) - Rotated 5deg -->
        <div class="stat-card arc-3">
            <h3 class="text-4xl font-bold text-slate-900 mb-2">120+</h3>
            <p class="text-sm text-slate-500">Used by millions if teams and professionals</p>
        </div>

        <!-- Card 4 (Far Right) - Rotated 15deg -->
        <div class="stat-card arc-4">
            <h3 class="text-4xl font-bold text-slate-900 mb-2">15,000+</h3>
            <p class="text-sm text-slate-500">Used by millions if teams and professionals</p>
        </div>

    </div>
    
    <!-- Bottom Content -->
    <div class="text-center mt-12">
        <span class="text-purple-600 font-semibold mb-4 block">What We Offer &rarr;</span>
        <h2 class="text-4xl font-bold max-w-2xl mx-auto mb-8">We committed to delivering innovative & strategic design solutions</h2>
        <a href="#contact" class="btn btn-primary shiny-button">Get Started Now</a>
    </div>
</section>
```

### CSS (Standard)
```css
.section-stats-arc {
    padding: 100px 0;
    overflow: hidden; /* Hide potential overflow from rotation */
}

.stat-card {
    background: white;
    padding: 30px;
    width: 240px;
    height: 260px;
    border-radius: 4px; /* Slight round, mostly sharp per ref */
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    position: absolute;
    bottom: 0;
    transform-origin: 50% 150%; /* Pivot from way below to assist arc */
    transition: transform 0.4s ease;
}

.stat-card:hover {
    z-index: 10;
    box-shadow: 0 30px 60px rgba(0,0,0,0.1);
}

/* Arc Positioning (Manual Tweak for perfect Framer look) */
.arc-1 {
    transform: translateX(-340px) translateY(40px) rotate(-12deg);
}

.arc-2 {
    transform: translateX(-120px) translateY(-10px) rotate(-4deg);
}

.arc-3 {
    transform: translateX(120px) translateY(-10px) rotate(4deg);
}

.arc-4 {
    transform: translateX(340px) translateY(40px) rotate(12deg);
}
```

### Tailwind Variant
If using Tailwind, use arbitrary values or add style tags for specific transforms as they are unique to this layout.

## Workflow Checklist
- [ ] **Container Height**: Ensure the container has enough height (`min-h-[400px]`) to accommodate the arch.
- [ ] **Origin**: Pivot point (`transform-origin`) is key. If manual positioning is too hard, use `transform-origin` with a large Y value.
- [ ] **Mobile**: **COLLAPSE THE ARC**. On mobile, stack them vertically or horizontally with scroll. `transform: none` on mobile breakpoint.
- [ ] **Shadows**: Keep shadows soft to create the "floating" card effect.
