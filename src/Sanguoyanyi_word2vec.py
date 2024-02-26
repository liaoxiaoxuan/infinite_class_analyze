import sys                      # 系統控制模組
import os.path                  # 系統功能模組
import numpy                    # 分析模組

import requests                 # 網路模組
from collections import Counter # 次數統計模組

from PIL import Image           # 圖片處理模組
import jieba                    # 分詞模組
import re                       # 正則表達式
import matplotlib.pyplot as plt # 視覺化模組
import matplotlib
from matplotlib.font_manager import FontProperties  # 導入 FontProperties 類別，用於設置字體相關屬性
import wordcloud                # 文字雲模組

import gensim                   # NLP 函式庫
from gensim.models import Word2Vec

from jiayan import load_lm      # 「甲言」分析工具
from jiayan import CharHMMTokenizer

import numpy as np              # 多維陣列或矩陣運算
from sklearn.decomposition import PCA  # 從 scikit-learn 庫（機器學習和數據分析的工具和算法）中，導入 PCA（主成分分析）類



# 在 jieba 分詞 module 中，增加字典
jieba.load_userdict("Sanguoyanyi_character.txt")  # 人名
jieba.load_userdict("Sanguoyanyi_place.txt")  # 地名



# 匯入 data，並用「取代」進行分句
f = open('Sanguoyanyi.txt', encoding='utf-8')
f = f.read().split("。")
# print(list(f))



