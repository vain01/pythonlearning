from PIL import Image

TARGET_FILE = 'Jellyfish_s.jpg'
image = Image.open(TARGET_FILE)
print(image.width)
image.show()
