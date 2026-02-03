from PIL import Image
import os

images_dir = "images"
output_dir = "images"

# Target aspect ratio 16:9 (wider)
target_ratio = 16 / 9

for i in range(1, 9):
    filename = f"discord{i}.jpg"
    filepath = os.path.join(images_dir, filename)
    
    if os.path.exists(filepath):
        img = Image.open(filepath)
        width, height = img.size
        current_ratio = width / height
        
        print(f"{filename}: {width}x{height} (ratio: {current_ratio:.2f})")
        
        # Crop to 16:9 - take center portion
        if current_ratio < target_ratio:
            # Image is too tall, crop top and bottom
            new_height = int(width / target_ratio)
            top = (height - new_height) // 2
            crop_box = (0, top, width, top + new_height)
        else:
            # Image is too wide, crop left and right
            new_width = int(height * target_ratio)
            left = (width - new_width) // 2
            crop_box = (left, 0, left + new_width, height)
        
        cropped = img.crop(crop_box)
        
        # Save backup first
        backup_path = os.path.join(images_dir, f"discord{i}_original.jpg")
        if not os.path.exists(backup_path):
            img.save(backup_path, quality=95)
            print(f"  Backed up to {backup_path}")
        
        # Save cropped version
        cropped.save(filepath, quality=95)
        print(f"  Cropped to {cropped.size[0]}x{cropped.size[1]} (16:9)")
        
print("\nDone! All images cropped to 16:9 ratio.")
