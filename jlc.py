from __future__ import print_function
from PIL import Image

im = Image.open("jlc.jpg")
char_list = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"")}]`"

for y in range(0,im.size[1]):
#for x in range(0,im.size[0]):
    for x in range(0,im.size[0]):
    #for y in range(0,im.size[1]):
        rgb_val = im.getpixel((x,y))
        avg_brightness= (rgb_val[0]+rgb_val[1]+rgb_val[2])//3
        char_index = avg_brightness //4
        print(char_list[char_index]*2, end="")
    print("")
