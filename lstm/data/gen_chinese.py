# -*- coding: utf-8 -*-
import numpy as np
import freetype
import copy
import random
import cv2

import re
import xlrd

img =np.zeros([50,650,3])
color_ = (255,255,255) # Green
pos = (3, 6)
text_size = 20
class put_chinese_text(object):
    def __init__(self, ttf):
        self._face = freetype.Face(ttf)

    def draw_text(self, image, pos, text, text_size, text_color):
        '''
        draw chinese(or not) text with ttf
        :param image:     image(numpy.ndarray) to draw text
        :param pos:       where to draw text
        :param text:      the context, for chinese should be unicode type
        :param text_size: text size
        :param text_color:text color
        :return:          image
        '''
        self._face.set_char_size(text_size * 64)
        metrics = self._face.size
        ascender = metrics.ascender/64.0

        #descender = metrics.descender/64.0
        #height = metrics.height/64.0
        #linegap = height - ascender + descender
        ypos = int(ascender)

        if not isinstance(text, unicode):
            text = text.decode('utf-8')
        img = self.draw_string(image, pos[0], pos[1]+ypos, text, text_color)
        return img

    def draw_string(self, img, x_pos, y_pos, text, color):
        '''
        draw string
        :param x_pos: text x-postion on img
        :param y_pos: text y-postion on img
        :param text:  text (unicode)
        :param color: text color
        :return:      image
        '''
        prev_char = 0
        pen = freetype.Vector()
        pen.x = x_pos << 6   # div 64
        pen.y = y_pos << 6

        hscale = 1.0
        matrix = freetype.Matrix(int(hscale)*0x10000, int(0.2*0x10000),\
                                 int(0.0*0x10000), int(1.1*0x10000))
        cur_pen = freetype.Vector()
        pen_translate = freetype.Vector()

        image = copy.deepcopy(img)
        for cur_char in text:
            self._face.set_transform(matrix, pen_translate)

            self._face.load_char(cur_char)
            kerning = self._face.get_kerning(prev_char, cur_char)
            pen.x += kerning.x
            slot = self._face.glyph
            bitmap = slot.bitmap

            cur_pen.x = pen.x
            cur_pen.y = pen.y - slot.bitmap_top * 64
            self.draw_ft_bitmap(image, bitmap, cur_pen, color)

            pen.x += slot.advance.x
            prev_char = cur_char

        return image

    def draw_ft_bitmap(self, img, bitmap, pen, color):
        '''
        draw each char
        :param bitmap: bitmap
        :param pen:    pen
        :param color:  pen color e.g.(0,0,255) - red
        :return:       image
        '''
        x_pos = pen.x >> 6
        y_pos = pen.y >> 6
        cols = bitmap.width
        rows = bitmap.rows

        glyph_pixels = bitmap.buffer

        for row in range(rows):
            for col in range(cols):
                if glyph_pixels[row*cols + col] != 0:
                    img[y_pos + row][x_pos + col][0] = color[0]
                    img[y_pos + row][x_pos + col][1] = color[1]
                    img[y_pos + row][x_pos + col][2] = color[2]
ft = put_chinese_text('fonts/huawenxihei.ttf')


studentdata =xlrd.open_workbook('2011student.xlsx')
table =studentdata.sheets()[0] #通过索引顺序获取 
cols=table.col_values(2) #取出第2列
words=[]
generwords=[]
for col in cols[1:]:# 取出第一行
    col=col.replace('','')
    generwords.append(col)
    for word in col:
        words.append(word)
diffwords=list(set(words))

#print('chinesecount={}'.format(len(diffwords)))
#源码表
diffwords.sort()
#print('chinesecountsort={}'.format(len(diffwords)))

#汉字->位置
encode_maps = {}
#位置->汉字
decode_maps = {}
for i, char in enumerate(diffwords):
    encode_maps[char] = i
    decode_maps[i] = char

my=[1,10,688,700,40,100,800]
for x in my:
    print(decode_maps[x])
# count=len(generwords)
# train_count=700
# #test_count=count-train_count

# def chinesetoindex(sentence):
#     numbers=""
#     #print(sentence)
#     for s in sentence:
#         numbers+=str(encode_maps[s])
#         numbers+="-"
#     return numbers[:-1]

# 生成中文字符
img_dir='chinesedata/test/'
for x in range(train_count,count):
    line=generwords[x]
    img_name= '{:04d}'.format(x)+'_'+chinesetoindex(line)+'.png'
    print(img_name)
    ft = put_chinese_text('fonts/huawenxihei.ttf')
    image = ft.draw_text(img, pos, line, text_size, color_)
    cv2.imwrite(img_dir+img_name, image)

















#print(chinesetoindex(generwords[0]))
# for key in encode_maps:
#     print(key)
#     print(encode_maps[key])

#去重
#print(len(words))
#print(len(diffwords))
# j=0
# for diffword in diffwords:
#     if j%100!=0:
#         print(diffword),
#     else:
#         print(diffword)
#     j+=1




# line=cols[1].strip()
#   print(line)



# image = ft.draw_text(img, pos, line, text_size, color_)
# cv2.imshow('ss', image)
# cv2.imwrite('my.png', image)
# cv2.waitKey(0)







