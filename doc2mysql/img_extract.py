import docx
import os
from PIL import Image
import datetime
from docx.parts.image import ImagePart





def B27_img_extract(media_B27,ImageName,RPmtime_urltime,FiledocxPathName):
    doc = docx.Document(FiledocxPathName)
    ImgSavePathlist = []
    rIdlist = []
    docpic = doc.part.related_parts
    for i in docpic:
        # 判断docpic[i]是Imagepart 类，首先导入 Imagepart 类，一次类推，以后判断类型，不光可以判断int ,str dict， list ，也可判断自定义类
        if isinstance(docpic[i], ImagePart):
            rIdlist.append(i)
        else:
            pass
    print(rIdlist)
    rIdlist.sort()
    print(rIdlist)
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

