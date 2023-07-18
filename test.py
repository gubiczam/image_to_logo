from PIL import Image

# Open an image file

f = open('final', 'w')

f.write("pu\nto negyzet :sz\nfilled :sz [\nrepeat 4 [\nfd 5 rt 90\n]\n]\nend\n");

img = Image.open('eiffel.jpg')

# Get the size of the image
img = img.resize((154, 140))
width, height = img.size
img.save("newimg.jpeg")
print(width, height)

# Loop over the image pixel by pixel
x = -385
y = 350
for i in range(height):
    f.write("setxy " + str(x) + " " + str(y) + "\n");
    f.write("seth 90\n");
    for j in range(width):
        r, g, b = img.getpixel((j, i))
        f.write("negyzet [ " + str(r) + " " + str(g) + " " + str(b) + " ] fd 5\n");

    y -= 5
