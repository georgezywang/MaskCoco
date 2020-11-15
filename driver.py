import MaskCoco
import os

def fileDic(path):
    imgList = []
    for i in range(501):
        mask = str(i).zfill(3) + "_gt.png"
        img = str(i).zfill(3) + "_rgb.png"
        maskPath = os.path.join(path, mask)
        if os.path.exists(maskPath):
            img = MaskCoco.ImageLabel(img, mask, 0, i)
            imgList.append(img)
    return imgList

catDic = {"wave": 0}
imgList = fileDic("images")
myParser = MaskCoco.MaskParser(catDic, imgList, inPath = "images",\
                               outPath="images/dat.json", useImgID = True)
myParser.saveJson()
