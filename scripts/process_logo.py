
from PIL import Image
import numpy as np
import os

def fix_logo():
    source_path = "images/innovate-logo.jpg"
    # Target naming based on what we saw in the file list and user request
    output_black = "images/innovate-logo-black-transparent.png"
    output_white = "images/innovate-logo-white-transparent.png"
    
    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found.")
        return

    print(f"Opening {source_path}...")
    img = Image.open(source_path).convert("RGBA")
    data = np.array(img)
    
    # 1. Create Black Version with Transparent Background
    # Assume background is white-ish.
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Mask: pixels brighter than 240.
    # Note: If the logo has anti-aliasing, simple threshold might leave white halos.
    # A better approach for simple B&W logos is to use the inverse of brightness as alpha.
    # But if the logo has colors (green), we need to be careful.
    
    # Let's check if it has colors other than grayscale.
    # If R, G, B are significantly different, it has color.
    # For now, let's stick to the threshold method as it's safer for preserving specific colors if they exist.
    
    # Improved masking: smooth transition for anti-aliasing?
    # For now, simple threshold to fix the "not transparent" issue.
    white_mask = (r > 240) & (g > 240) & (b > 240)
    
    data[white_mask, 3] = 0
    
    # Save Black/Original colored version
    black_img = Image.fromarray(data)
    black_img.save(output_black, "PNG")
    print(f"Saved {output_black}")
    
    # 2. Create White Version (for dark backgrounds)
    # We want to take the non-transparent pixels and make them white.
    # Using the transparent image data
    data_w = np.array(black_img)
    r, g, b, a = data_w[:,:,0], data_w[:,:,1], data_w[:,:,2], data_w[:,:,3]
    
    # Where alpha is > 0, set RGB to 255 (White)
    visible_mask = a > 0
    data_w[visible_mask, 0] = 255 # R
    data_w[visible_mask, 1] = 255 # G
    data_w[visible_mask, 2] = 255 # B
    
    white_img = Image.fromarray(data_w)
    white_img.save(output_white, "PNG")
    print(f"Saved {output_white}")

if __name__ == "__main__":
    fix_logo()
