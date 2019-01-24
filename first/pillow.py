from PIL import Image
from PIL import ImageFilter
'''
img = Image.open("shakira.jpg")
area = (100,100, 375, 495)
cropped_img = img.crop(area)

print(img.size)
print(img.format)


img.show()
cropped_img.show()
'''
'''
shakira = Image.open("shakira.jpg")
kendall_jenner = Image.open("kendall_jenner.jpg")
area = (100, 100, 300, 300)
shakira.paste(kendall_jenner, area)

shakira.show()
'''

'''
shakira = Image.open("shakira.jpg")
print(shakira.mode)
r, g, b = shakira.split()
r.show()
g.show()
b.show()
'''

'''
shakira = Image.open("shakira.jpg")
kendall_jenner = Image.open("kendall_jenner.jpg")
print(shakira.mode)
r1, g1, b1 = shakira.split()
r2, g2, b2 = kendall_jenner.split()
new_Img = Image.merge("RGB", (b2, r1, g1))
new_Img.show()
'''

'''
kendall_jenner = Image.open("kendall_jenner.jpg")
square_kendall = kendall_jenner.resize((300, 300))
flip_kendall = kendall_jenner.transpose(Image.FLIP_LEFT_RIGHT)
spin_kendall = kendall_jenner.transpose(Image.ROTATE_90)

kendall_jenner.show()
square_kendall.show()
flip_kendall.show()
spin_kendall.show()
'''

'''
kendall_jenner = Image.open("kendall_jenner.jpg")
black_white = kendall_jenner.convert("L")
print(black_white.mode)
black_white.show()
'''

kendall_jenner = Image.open("kendall_jenner.jpg")
blur = kendall_jenner.filter(ImageFilter.BLUR)
detail = kendall_jenner.filter(ImageFilter.DETAIL)
edges = kendall_jenner.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()




