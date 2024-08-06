import colorgram

# Provide the absolute path to the image
image_path = 'C:\\Users\\Lenovo\\Desktop\\01_HC_JOSHI\\Work\\100_DAYS_OF_PYTHON\\DAY_18\\hirst-painting-start\\image.jpg'

# Extract colors from the image
colors = colorgram.extract(image_path, 38)
# here 38 is no of color i want to extreted from the image

# List to hold the RGB values
rgb_colors = []

# Iterate over the extracted colors
for color in colors:
    # Access the RGB property
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Print the list of RGB colors
print(rgb_colors)
