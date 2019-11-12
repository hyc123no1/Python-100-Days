from PIL import Image

im = Image.open('E:\Python\Python-100-Days\geek_for_python\LXF\\test.jpg')

w,h = im.size

print('original image size:{}x{}'.format(w,h))

im.thumbnail((w//2,h//2))
print('resize image to:{}x{}'.format(w//2,h//2))

im.save('thumbnail.jpg','jpeg')