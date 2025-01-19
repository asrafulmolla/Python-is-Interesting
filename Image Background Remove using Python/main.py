from rembg import remove
from PIL import Image

# Define file paths
input_path = "1.jpg"
output_path = "output.jpg"

inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
Image.open(output_path)