from PIL import Image
import sys

# Open the image
img = Image.open('app_flutter/lib/images/bloodhound-detective-icon.png')
img = img.convert("RGBA")
datas = img.getdata()

# Target color to make transparent (RGB 250, 240, 228)
target_color = (250, 240, 228)
tolerance = 15

newData = []
for item in datas:
    # Check if the pixel color is close to the target color
    if (abs(item[0] - target_color[0]) <= tolerance and
        abs(item[1] - target_color[1]) <= tolerance and
        abs(item[2] - target_color[2]) <= tolerance):
        # Make it transparent
        newData.append((255, 255, 255, 0))
    else:
        # Keep original pixel
        newData.append(item)

img.putdata(newData)
img.save('app_flutter/lib/images/bloodhound-detective-icon.png', "PNG")
print("Image processed successfully! Background made transparent.")

