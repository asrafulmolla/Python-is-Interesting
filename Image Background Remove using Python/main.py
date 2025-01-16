from rembg import remove
from PIL import Image
import os

# Define file paths
input_path = "C:/Users/armda/OneDrive/Python is interesting/Image Background Remove using Python/1.jpg"
output_path = "C:/Users/armda/OneDrive/Python is interesting/Image Background Remove using Python/output.jpg"

try:
    # Check if the input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found. Please check the file path.")

    # Open the input image
    print("Opening the input image...")
    input_image = Image.open(input_path)

    # Remove the background
    print("Removing background...")
    output_image = remove(input_image)

    # Save the output image
    print(f"Saving the output image to '{output_path}'...")
    output_image.save(output_path)
    print("Background removal completed successfully!")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
