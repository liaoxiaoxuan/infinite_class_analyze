import sys                      # 系統控制模組
import os.path                  # 系統功能模組
import numpy                    # 分析模組

import requests                 # 網路模組
from collections import Counter # 次數統計模組

from PIL import Image           # 圖片處理模組
import jieba                    # 分詞模組
import re                       # 正則表達式
import matplotlib.pyplot as plt # 視覺化模組
from matplotlib.font_manager import FontProperties  # 導入 FontProperties 類別，用於設置字體相關屬性
import wordcloud                # 文字雲模組

from jiayan import load_lm      # 「甲言」分析工具
from jiayan import CharHMMTokenizer



# 在 jieba 分詞 module 中，增加字典
jieba.load_userdict("Hongxue_character.txt")  # 人名
jieba.load_userdict("Hongxue_place.txt")  # 地名



# 匯入 data，並用「取代」進行分句
f = open('Dream_of_the_Red_Chamber.txt', encoding='utf-8')
f = f.read().split("。")
# print(list(f))

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



# jieba 斷詞

# # 精確模式
# for sentence in data:
#     seg_list = jieba.lcut(data)
#     print('/'.join(seg_list))
    
#     print('---------------')

# # 全模式
# for sentence in data:
#     seg_list = jieba.cut(sentence, cut_all=True)
#     print('/'.join(seg_list))

# print('---------------')

# # 搜索引擎模式
# for sentence in data:
#     seg_list = jieba.cut_for_search(sentence)
#     print('/'.join(seg_list))

# jieba.lcut () 模式
lines = []
for line in f:
    temp = jieba.lcut(line)
    words = []



# # 過濾掉所有的標點符號

# for i in seg_list:
#     # 將 seg_list 中的每個元素 i 中的特定字符（例如標點符號和特殊字元）替換為空字串
#     # i = re.sub("尋找字符", "取代字符", i)
#     i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》「」〔〕『』；［］■●...〈〉【】]+|[+——！，。？、~@#￥%……&*（）：]+", "", i)
#     if len(i) > 0:
#         words.append(i)
# # print(len(words))
# # print(words)

# # # 建立 trigrams 的列表
# # # Trigrams 是一種 NLP 中常用的技術，用於建立文本的模型，特別是在語言生成或預測下一個詞語時
# # # 建立一個包含文本中所有可能的 trigram 的列表，輸出前三個 trigrams，以供檢視
# # trigrams = [([words[i], words[i + 1]], words[i + 2]) for i in range(len(words) - 2)]
# # print(trigrams[:3])



# # 輸出結果 to txt

# # 結果是key
# with open("Hongxue_jieba_counter.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(counter))

# 結果是dict
# with open("Hongxue_word2vec_split.txt", "w", encoding="utf-8") as file:
#     file.write(str(list(f)))
