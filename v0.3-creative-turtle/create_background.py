
from PIL import Image

# Create a black background
width = 1200
height = 900

background = Image.new("RGB", (width, height), "black")

# Save the background as a GIF
background.save("v0.3-creative-turtle/background.gif")

print("Black background created successfully!")
