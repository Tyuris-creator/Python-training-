from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img.save("out.jpeg")
        img1 = img.filter(ImageFilter.BLUR)
        img1.save("out1.jpeg")
        
main()