import docx
import os
from PIL import Image
import datetime






def B27_img_extract(media_B27,ImageName,RPmtime_urltime,FiledocxPathName):
    doc = docx.Document(FiledocxPathName)
    ImgSavePathlist = []
    rIdlist = ['rId7']
    for i in rIdlist:
        imgSavePath = media_B27 + '\\' + ImageName + RPmtime_urltime + '_' + i + '.jpg'
        # imgSavePath.encode('utf-8')
        # print(imgSavePath)
        imgblob = doc.part.related_parts[i]
        img = open(imgSavePath, 'wb')
        img.write(imgblob.blob)
        img.close()
        box1 = (634, 462)
        im_m = Image.open(imgSavePath)
        out = im_m.resize(box1, Image.ANTIALIAS)
        out = out.convert('RGB')
        out.save(imgSavePath)
        ImgSavePathlist.append(imgSavePath)
    return ImgSavePathlist[0]

