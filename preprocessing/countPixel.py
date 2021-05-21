# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:51:41 2020

@author: src-by-hannah

# https://stackoverflow.com/questions/28576203/how-to-count-the-number-of-pixels-of-a-certain-color-in-python
# https://stackoverflow.com/questions/50545192/count-different-colour-pixels-python/50545224
"""

"""
# 회색(#a0a0a0 / 160, 160, 160)
# 하늘색(#87cefa / 135, 206, 250)
# 초록색(#81c147 / 129, 193, 71)
"""

from PIL import Image
import csv

filename = '301관 바라봄.jpg'
im = Image.open(filename)
imrgb = im.convert("RGB") # (r, g, b 순서임)

f = open('result.csv', 'a', newline='')
wr = csv.writer(f)

gray = 0
blue = 0
green = 0
other = 0
 
for pixel in imrgb.getdata():
    if (150<pixel[0]<170) and (150<pixel[1]<170) and (150<pixel[2]<170): 
        gray += 1
    
    elif (125<pixel[0]<145) and (196<pixel[1]<216) and (240<pixel[2]<260): 
        blue += 1
        
    elif (119<pixel[0]<139) and (183<pixel[1]<203) and (61<pixel[2]<81): 
        green += 1
    
    else:
        other += 1

print('gray=' + str(gray)+', blue='+str(blue)+', green='+str(green)+', other='+str(other))

# 비율 계산
total = gray+blue+green+other
gray_per = gray / total *100
blue_per = blue /total *100
green_per = green /total *100
other_per = other/total *100

print('gray=' + str("%0.1f" % gray_per)+', blue='+str("%0.1f" % blue_per)+', green='+str("%0.1f" % green_per)+', other='+str("%0.1f" % other_per))

wr.writerow([filename,
    str(gray), str(blue), str(green), str(other),
    str("%0.1f" % gray_per), str("%0.1f" % blue_per), str("%0.1f" % green_per), str("%0.1f" % other_per)])
f.close()
