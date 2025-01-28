import os
from PIL import Image

# Configuration
INPUT_FOLDER = 'static'  # Change this to the folder containing the images
EXCLUDE_EXTENSIONS = {'.gif', '.ico'}  # Add file extensions to exclude
EXCLUDE_FILES = {'Blue Chip Invest Logo.001.png'}  # Add file names to exclude
GRAY_SCALE_RATIO = 0.9


# Helper function to convert an image to 90% grayscale
def apply_partial_grayscale(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            # Convert image to grayscale
            grayscale_img = img.convert('L').convert('RGBA')
            original_img = img.convert('RGBA')

            # Blend original and grayscale images
            blended_img = Image.blend(original_img, grayscale_img, GRAY_SCALE_RATIO)

            # Save the resulting image
            blended_img.save(output_path)
            print(f"Processed: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")


# Main function to process the images
def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        base, ext = os.path.splitext(filename)

        # Skip non-image files, excluded extensions, or excluded files
        if ext.lower() in EXCLUDE_EXTENSIONS or filename in EXCLUDE_FILES or not ext.lower() in ['.png', '.jpg',
                                                                                                 '.jpeg', '.bmp',
                                                                                                 '.tiff', '.webp']:
            continue

        # Create the new file name with '-grayscale'
        new_filename = f"{base}-grayscale{ext}"
        output_path = os.path.join(folder_path, new_filename)

        if os.path.exists(output_path):
            print(f"Skipping existing file: {output_path}")
            continue

        # Apply partial grayscale
        apply_partial_grayscale(file_path, output_path)


if __name__ == '__main__':
    process_images_in_folder(INPUT_FOLDER)
