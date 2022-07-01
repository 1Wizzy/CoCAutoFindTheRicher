# encoding: utf-8

from PIL import Image
import base64
from requests import post
"""
Function: Crop the Image to get Spoils info
InputParam: ImagePath, A tuple (x1,y1,x2,y2) to loacte the Spoils info
Return: Store The Image in Local
"""
def CropImage(ImagePath,SpoilsLoc):# Original Screenshot 
    img = Image.open(ImagePath)
    region = img.crop(SpoilsLoc)
    region.save("Spoils.png")

def LocalImageToBase64(ImagePath):# Processed Screenshot
    with open(ImagePath,'rb') as f:
        Base64Str = base64.b64encode(f.read())
    return Base64Str

def AnalyzeImage(AccessToken,Base64Str):# Processed Screenshot
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    request_url = request_url + "?access_token=" + AccessToken
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = post(request_url, data={"image":Base64Str}, headers=headers)  # 请求url     请求参数        请求头
    if response:
        ResDict = response.json()
    dic = {}
    SpoilsList = []
    for wd in ResDict["words_result"]:
        SpoilsList.append(wd["words"])
    dic.update({"GoldCoin":int(SpoilsList[0])})
    dic.update({"Exlixir":int(SpoilsList[1])})
    dic.update({"DarkElixirDrill":int(SpoilsList[2])})
    return dic

