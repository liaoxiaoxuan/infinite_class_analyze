import sys                      # 系統控制模組
import os.path                  # 系統功能模組
import numpy                    # 分析模組

import requests                 # 網路模組
from collections import Counter # 次數統計模組

from PIL import Image           # 圖片處理模組
import jieba                    # 分詞模組
import re                       # 正則表達示
import matplotlib.pyplot as plt # 視覺化模組
from matplotlib.font_manager import FontProperties  # 導入 FontProperties 類別，用於設置字體相關屬性
import wordcloud                # 文字雲模組

from jiayan import load_lm      # 「甲言」分析工具
from jiayan import CharHMMTokenizer



# 在 jieba 分詞 module 中，增加字典
jieba.load_userdict("Hongxue_character.txt")  # 人名
jieba.load_userdict("Hongxue_place.txt")  # 地名



# 匯入 data
with open('Dream_of_the_Red_Chamber.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    # print(type(data))  # 字串，非list
    # print('------------------')
# sys.exit(0)  # 正常離開程式

# 定義繁體中文檔名
WORDS_PATH = 'dict.txt.big.txt' # 繁體中文詞庫檔名
TC_FONT_PATH = './NotoSerifTC-Regular.otf' # 繁體中文字型檔名

# 匯入圖表中文字體
font_path = "./NotoSerifTC-Regular.otf"  # 替換為實際的中文字體文件路徑
font_prop = FontProperties(fname=font_path)

# 設定中文字體
font_path = r"D:/PYTHON/infinite_class_analyze/src/NotoSerifSC-Regular.otf"  # 替換為實際的中文字體文件路徑
font_prop = FontProperties(fname=font_path)

