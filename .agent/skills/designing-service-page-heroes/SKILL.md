---
name: designing-service-page-heroes
description: Designs service page hero sections based on the "Monotree" aesthetic (Clean, Isometric, Trust-Focused). Use when the user asks to design, implement, or update a service page hero section to match the specific Monotree reference.
---

# Monotree Service Hero Design Standard

This skill encapsulates the design principles extracted from the "Monotree" reference image. It focuses on a clean, white-space dominant aesthetic with high-contrast typography, isometric 3D visuals, and integrated email capture forms.

## When to use this skill
- Designing the hero section for a service page.
- Applying the "Monotree" or "Service Hero" look.
- "Making the hero look like the reference image."

## Core Design Principles (The "Monotree Standard")

1.  **Split Layout (Text Left / Visual Right)**
    -   **Left Column (50%)**: Focused on the Value Proposition and Conversion.
    -   **Right Column (50%)**: Dedicated to "Isometric Illustration". Contains white/clean vector-style isometric line art (dashboards, phones, UI elements).
    -   **Background**: Pure White (`#ffffff`) or very subtle off-white (`#fcfcfc`).

2.  **Typography**:
    -   **Headline**: Large, Bold, Sans-Serif (Inter/Manrope). Key feature: **Underline/Scribble** accent under a keyword (e.g., "people").
        -   Size: ~3.5rem - 4.5rem.
        -   Weight: 700/800.
        -   Color: Black (`#000000` or `#0f172a`).
    -   **Subheadline**: Clean, legible, high contrast.
        -   Size: ~1.125rem (18px).
        -   Color: Dark Grey (`#334155`).
        -   Line-height: 1.6.

3.  **Conversion Element (Email Capture)**:
    -   Instead of just buttons, use an **Input Group**.
    -   **Input**: "Enter work email" placeholder. Light border, rounded corners.
    -   **Button**: Bright Lime Green (`#84CC16`) background. "Book a demo" text. Black or Dark Green text.
    -   **Layout**: Side-by-side (Input + Button) inside a wrapper.

4.  **Trust & Stats (The "Data Row")**:
    -   Located below the CTA.
    -   **Layout**: Two columns of stats + a star rating.
    -   **Stat Style**: Big Bold Number ("75.2%") + Small Label ("Average daily activity").
    -   **Star Rating**: "4.5 Average user rating" with 5 solid stars.

## Component Blueprints

### 1. Headline with Scribble
```html
<h1 class="text-6xl font-bold tracking-tight text-slate-900 mb-6 font-primary">
    Put <span class="relative inline-block">
        people
        <!-- SVG Scribble Underline -->
        <svg class="absolute w-full h-3 -bottom-1 left-0 text-slate-900" viewBox="0 0 100 10" preserveAspectRatio="none">
            <path d="M0 5 Q 50 10 100 5" stroke="currentColor" stroke-width="3" fill="none" />
        </svg>
    </span> first
</h1>
```

### 2. Email Capture CTA
```html
<div class="flex items-center gap-2 max-w-md mb-12">
    <input type="email" placeholder="Enter work email" 
        class="flex-1 px-4 py-3 rounded-lg border border-slate-200 focus:outline-none focus:border-lime-500 bg-slate-50 text-slate-900 placeholder-slate-400">
    <button class="px-6 py-3 rounded-lg bg-lime-500 hover:bg-lime-600 text-white font-semibold transition-colors shadow-sm whitespace-nowrap">
        Book a demo
    </button>
</div>
```

### 3. Stat Row
```html
<div class="flex items-center gap-12 border-t border-slate-100 pt-8 mt-8">
    <!-- Stat 1 -->
    <div>
        <div class="text-3xl font-bold text-slate-900 mb-1">75.2%</div>
        <div class="text-sm text-slate-500 font-medium">Average daily activity</div>
    </div>
    <!-- Stat 2 -->
    <div class="border-l border-slate-200 pl-12">
        <div class="text-3xl font-bold text-slate-900 mb-1">~20k</div>
        <div class="text-sm text-slate-500 font-medium">Average daily users</div>
    </div>
</div>
<!-- Star Rating -->
<div class="flex items-center gap-2 mt-6">
    <div class="flex text-black">
        <!-- 5 Stars SVGs -->
        <i data-lucide="star" class="fill-black w-4 h-4"></i>
        <!-- ... -->
    </div>
    <span class="text-sm font-bold text-slate-900">4.5</span>
    <span class="text-sm text-slate-500">Average user rating</span>
</div>
```

### 4. Right Side Visual (Isometric Placeholder)
To achieve the look without custom assets, use a combination of CSS shapes or a placeholder image:
```html
<div class="relative w-full h-full min-h-[500px] flex items-center justify-center">
    <!-- Main Device Mockup -->
    <img src="assets/niche_images/isometric-dashboard-placeholder.png" alt="Dashboard" class="w-full max-w-lg drop-shadow-2xl transform hover:-translate-y-2 transition-transform duration-500">
</div>
```

## Workflow Checklist

- [ ] **Split Layout**: Ensure 50/50 split on desktop, stack on mobile.
- [ ] **Font Weight**: Ensure H1 is BOLD (weight 700/800).
- [ ] **Accent**: Add the "Scribble" or Underline to a key word.
- [ ] **Input Group**: Implement the Email + Button inline form.
- [ ] **Stats**: Add the two-column stat block with separation line.
- [ ] **Visuals**: Check that the right side image feels "floating" and "clean" (use drop shadows).
