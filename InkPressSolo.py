import sys
import os
from PIL import Image
from waveshare_epd import epd4in0e 

# --- SETTINGS ---
ICON_FOLDER = os.path.join(os.path.dirname(__file__), 'icons')
TEST_IMAGE_NAME = "test_image.png"

# The screen is 600 wide and 400 tall
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

def main():
    try:
        print("🕵️ Finding the screen...")
        epd = epd4in0e.EPD()
        epd.init()
        
        # 1. BUILD THE PATH
        full_path = os.path.join(ICON_FOLDER, TEST_IMAGE_NAME)

        if os.path.exists(full_path):
            print(f"✅ Found your image: {TEST_IMAGE_NAME}")
            
            # 2. OPEN THE IMAGE
            img = Image.open(full_path)
            print(f"📏 Original size: {img.size[0]}x{img.size[1]}")

            # 3. THE AUTO-RESIZER (The "Fixer")
            # If the image isn't 600x400, we force it to be!
            if img.size != (SCREEN_WIDTH, SCREEN_HEIGHT):
                print(f"✂️ Image is the wrong size! Resizing to {SCREEN_WIDTH}x{SCREEN_HEIGHT}...")
                img = img.resize((SCREEN_WIDTH, SCREEN_HEIGHT))

            # 4. ROTATE
            # Flip it 180 degrees so it's not upside down
            final_image = img.rotate(180)

            # 5. SHOW IT
            print("🚀 Sending to screen...")
            epd.display(epd.getbuffer(final_image))
            
            print("😴 Done! Screen is sleeping.")
            epd.sleep()

        else:
            print(f"❌ ERROR: File not found at {full_path}")

    except Exception as e:
        # This catches the 'image_temp' error or any other crashes
        print(f"⚠️ Something went wrong: {e}")

if __name__ == "__main__":
    main()