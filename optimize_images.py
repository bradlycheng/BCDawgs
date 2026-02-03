import os
from PIL import Image

def optimize_images(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    # Skip if already smallish (e.g. < 500KB) to avoid double compressing artifacts
                    # actually, let's just compress everything to ensure consistency, 
                    # but maybe keep a backup if needed? 
                    # The user has `_original` files for some, implying previous ops.
                    # I will overwrite the main files.
                    
                    # Resize if huge (e.g. > 1920px width)
                    if img.width > 2500:
                        ratio = 2500 / img.width
                        new_height = int(img.height * ratio)
                        img = img.resize((2500, new_height), Image.Resampling.LANCZOS)
                    
                    # Save with optimization
                    # If PNG, convert to RGB and save as JPG if it's opaque? 
                    # No, keep PNGs as PNGs but optimize? PNG optimization is hard with just PIL.
                    # Let's focus on JPGs mostly as they are the big photos.
                    
                    if filename.lower().endswith('.png'):
                        # Just optimize PNG
                        img.save(filepath, optimize=True)
                        print(f"Optimized PNG: {filename}")
                    else:
                        # JPG
                        # convert to RGB just in case (e.g. RGBA png saved as jpg error)
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                        
                        img.save(filepath, "JPEG", quality=75, optimize=True)
                        print(f"Optimized JPG: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    optimize_images("images")
