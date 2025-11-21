#!/usr/bin/env python3
"""
Create a favicon from the lightning bolt icon with white parts made transparent.
"""

from PIL import Image
import os

def make_white_transparent(image_path, output_path):
    """
    Make white parts of an image transparent while preserving the lightning bolt.
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get image data
    data = img.getdata()
    
    # Create new data with white parts made transparent
    new_data = []
    for item in data:
        r, g, b, a = item
        
        # Check if pixel is white or very light (high RGB values)
        # We'll make pixels transparent if they're close to white
        if r > 240 and g > 240 and b > 240:
            # Make white/very light pixels transparent
            new_data.append((r, g, b, 0))
        else:
            # Keep other pixels as they are
            new_data.append(item)
    
    # Update image data
    img.putdata(new_data)
    
    # Save the result
    img.save(output_path, 'PNG')
    print(f"Created transparent favicon: {output_path}")

def create_favicon_sizes(base_image_path, output_dir):
    """
    Create multiple favicon sizes from the base image.
    """
    # Standard favicon sizes
    sizes = [
        (16, 16, 'favicon-16x16.png'),
        (32, 32, 'favicon-32x32.png'),
        (48, 48, 'favicon-48x48.png'),
        (64, 64, 'favicon-64x64.png'),
        (96, 96, 'favicon-96x96.png'),
        (128, 128, 'favicon-128x128.png'),
        (192, 192, 'favicon-192x192.png'),
        (256, 256, 'favicon-256x256.png'),
        (512, 512, 'favicon-512x512.png')
    ]
    
    # Open the base image
    base_img = Image.open(base_image_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for width, height, filename in sizes:
        # Resize the image
        resized = base_img.resize((width, height), Image.Resampling.LANCZOS)
        
        # Save the resized image
        output_path = os.path.join(output_dir, filename)
        resized.save(output_path, 'PNG')
        print(f"Created {filename} ({width}x{height})")

def main():
    # Check if we have the lightning bolt image
    lightning_image = "lightning-bolt-icon.png"
    
    if not os.path.exists(lightning_image):
        print(f"Error: Lightning bolt image not found at {lightning_image}")
        print("Please make sure the image file exists in the current directory.")
        return
    
    # Create the main transparent favicon
    make_white_transparent(lightning_image, "lightning-favicon.png")
    
    # Create multiple sizes for the website
    create_favicon_sizes("lightning-favicon.png", "website/assets")
    
    # Create a simple favicon.ico for the Flutter app
    img = Image.open("lightning-favicon.png")
    img.save("app_flutter/web/favicon.png", "PNG")
    print("Created favicon.png for Flutter app")
    
    print("\nFavicon creation complete!")
    print("Files created:")
    print("- lightning-favicon.png (main transparent favicon)")
    print("- website/assets/favicon-*.png (multiple sizes)")
    print("- app_flutter/web/favicon.png (Flutter app favicon)")

if __name__ == "__main__":
    main()
