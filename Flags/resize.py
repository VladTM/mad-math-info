import os
from PIL import Image

def resize_images(input_directory, output_directory, seed_image_path):
    seed_image = Image.open(seed_image_path)
    target_width, target_height = seed_image.size

    for filename in os.listdir(input_directory):
        if filename.endswith(".png") and filename != "Paris.png":
            input_image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(output_directory, filename.replace(".png", "_resized.png"))

            original_image = Image.open(input_image_path)
            width_ratio = target_width / original_image.width
            height_ratio = target_height / original_image.height
            new_width = int(original_image.width * width_ratio)
            new_height = int(original_image.height * height_ratio)

            resized_image = original_image.resize((new_width, new_height))
            resized_image.save(output_image_path)

# Usage example
input_directory = "./"
output_directory = "./Resized/"
seed_image_path = os.path.join(input_directory, "Paris.png")

resize_images(input_directory, output_directory, seed_image_path)
