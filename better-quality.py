from PIL import Image

f = open('final-better', 'w')

img = Image.open('eiffel.jpg')

img = img.resize((385, 700))
width, height = img.size
f.write("pu\n")

x = -385
y = 350
for i in range(height):
    f.write("setxy " + str(x) + " " + str(y) + "\n")
    f.write("seth 90\n")
    f.write("pd\n")
    for j in range(width):
        r, g, b = img.getpixel((j, i))
        f.write("setcolor [" + str(r) + " " + str(g) + " " + str(b) + "] fd 2\n")

    y -= 1
    f.write("pu\n")
