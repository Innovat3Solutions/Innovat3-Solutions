---
name: creating-service-graphics
description: Generates high-quality, isometric, 3D tech-focused graphics for service pages using the generate_image tool. Use when the user asks for "niche graphics", "hero images", or "service illustrations".
---

# Creating Service Graphics

## Purpose
This skill defines the standard prompt engineering and aesthetic guidelines for generating **Service Graphics** for the Innovat3 Solutions website. These graphics are used in the Hero sections (Immersive, Monotree, marketive, etc.) and represent the "Future of [Industry]" concept.

## Aesthetic Standard: "The Monotree/Immersive Look"
All generated images must adhere to the following visual language:
- **Style**: 3D Isometric, Tech-Minimalist, High-Fidelity.
- **Composition**: A central "floating island" or "device cluster" showing UI elements, floating widgets, and glass-like panels.
- **Lighting**: Soft, studio lighting with subtle ambient occlusion. No harsh shadows.
- **Color Palette**: 
    - **Primary**: White/Light Grey (Clean base).
    - **Accents**: Specific to the niche (e.g., Teal for Medical, Blue for Pools, Lime for Default).
    - **Materials**: Matte plastic, frosted glass (glassmorphism), brushed metal.
- **Vibe**: Futuristic, Automated, Organized, Premium.

## When to Use
- When the user asks to "generate images for [Niche]".
- When a key service page is missing its `niche_graphic`.
- When the user wants to "refresh" the visuals.

## Workflow

### 1. Identify the Niche & Context
Determine the industry (e.g., "Plumbers") and the core value proposition (e.g., "Emergency dispatch", "Leaking pipes").

### 2. Construct the Prompt
Use the following strict template for `generate_image`:

```text
isometric 3d illustration of a [NICHE_SPECIFIC_OBJECT] connected to a modern digital interface, 
[NICHE_ACCENT_COLOR] color theme, 
floating UI widgets showing [RELEVANT_DATA_METRICS], 
glassmorphism style, 
white background, 
soft shadows, 
high quality, 
render, 
blender 3d, 
minimalist tech aesthetic, 
clean lines, 
no text
```

#### Example Prompts
**For Plumbers:**
> "isometric 3d illustration of a stylized modern piping system and water faucet connected to a digital dashboard, blue and white color theme, floating UI widgets showing water pressure and scheduling data, glassmorphism style, white background, soft shadows, high quality, render, blender 3d, minimalist tech aesthetic, clean lines"

**For Restaurants:**
> "isometric 3d illustration of a gourmet burger and smartphone app interface, orange and slate color theme, floating UI widgets showing order lists and delivery tracking, glassmorphism style, white background, soft shadows, high quality, render, blender 3d, minimalist tech aesthetic, clean lines"

### 3. Generate & Save
1.  Call `generate_image`.
2.  Save the file to `assets/images/niche_graphics/[slug].png`.
3.  **IMPORTANT**: The website CSS expects specific dimensions or aspect ratios. Ensure the image is roughly **4:3 or 16:9** depending on the container, but standardizing on **800x600** or **1024x1024** (if square) is safe. The images should have a **white or transparent** background to blend with the container.

### 4. Verify Integration
- Ensure the image file name matches the `slug` in `generate_niche_pages.py`.
- Check that the image looks good on both the "white" background (Monotree/Beyond) and "dark" background (Immersive - note: Immersive might need a separate 'dark mode' variant or a universally compatible image). *Current decision: Use clean white/transparent BG images that pop on dark and blend on white.*

## Checklist
- [ ] Graphic is clearly identifiable as the niche (e.g., a tooth for dentist, a pipe for plumber).
- [ ] Graphic contains "Tech" elements (UI panels, graphs, connection lines).
- [ ] Graphic uses the correct accent color.
- [ ] Background is clean (white or transparent).
- [ ] File size is optimized (under 500KB if possible, though generation tool handles raw output).
