from PIL import Image
import os

def make_transparent(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            print(f"Error: Input file {input_path} does not exist.")
            return

        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # Change white (and near-white) pixels to transparent
            # Adjust tolerance if needed (e.g. > 200 or > 240)
            if item[0] > 230 and item[1] > 230 and item[2] > 230:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Successfully saved transparent logo to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    make_transparent("images/bcdawgs-logo.png", "images/bcdawgs-logo-transparent.png")
