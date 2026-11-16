
from PIL import Image

image = Image.new("RGB", (400, 300), "blue")

image.save("v0.2-pillow/first_image.png")

print("Image created successfully!")
