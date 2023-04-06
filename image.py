# 練習把圖案轉成黑白或灰階
from PIL import Image
import os


for file in os.listdir('orig'): # 在這個資料夾內的檔案
    if file.endswith('.jpg'): # 檢查()的檔案類別
        img2 = Image.open('orig/' + file) #file path
        img2 = img2.convert('L') # convert to L (Grayscale)
        img2.save('result/' + file[:-4] + '_2.png') #file path # [:-4] 原檔名只取到倒數第五個