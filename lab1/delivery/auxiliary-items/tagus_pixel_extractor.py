from PIL import Image

im = Image.open("tagus.png")
pixels = im.load()
data = []

def is_in_triangle(x, y, max_coord):
    return x + y <= max_coord and x >= 0 and y >= 0

max_coord = 1033
for d in range(max_coord + 1):
    for y in range(d + 1):
        x = d - y
        if is_in_triangle(x, y, max_coord):
            data.append(pixels[x, y])
im7 = Image.new(im.mode, (1000,1000))
im7.putdata(data)
im7.save("./tagus_secret.png")
