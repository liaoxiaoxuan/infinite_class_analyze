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



# 匯入 data
with open('spider_zonggui_previous.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    # print(data)
    # print('------------------')



# 定義繁體中文檔名
WORDS_PATH = 'dict.txt.big.txt' # 繁體中文詞庫檔名
TC_FONT_PATH = './NotoSerifTC-Regular.otf' # 繁體中文字型檔名

# 匯入圖表中文字體
font_path = "./NotoSerifTC-Regular.otf"  # 替換為實際的中文字體文件路徑
font_prop = FontProperties(fname=font_path)

# 設定中文字體
font_path = r"D:\PYTHON\infinite_class_analyze\src\NotoSerifSC-Regular.otf"  # 替換為實際的中文字體文件路徑
font_prop = FontProperties(fname=font_path)



# 排除範圍
    
def remove_brackets(data):
    return re.sub(r"\《(.+?)\》", '', data)



# 分詞

# 進行分詞
lm = load_lm('../static/jiayan_models/jiayan_models/jiayan.klm')
tokenizer = CharHMMTokenizer(lm)

# 顯示分詞結果

# # 整份文件
# tokenizing = list(tokenizer.tokenize(data))

# 排除範圍
tokenizing = list(tokenizer.tokenize(remove_brackets(data)))

# print(tokenizing)



# # 進行句法分析
# # 注意：Jiayan 主要提供分詞功能，句法分析可能不如其他工具包完善
# # 下面的示例僅為演示目的
# syntax_analysis = jiayan.seg(text)

# # 顯示句法分析結果
# print("句法分析結果:", syntax_analysis)



# 詞頻

# 總覽
counter = Counter(tokenizing)
# print(counter)



# # 前幾名
# most_counter_dict = Counter(tokenizing)  # 出來的結果會是 dict
# # most_counter_list = Counter(matches).most_common(100)  # 出來的結果會是 list
# # most_counter_dict = {_[0]:_[1] for _ in most_counter_list}  # 轉換成 dict
# # print(most_counter_dict)

STOP_WORDS = [' ', '，', '（', '）', '...', '。', '「', '」', '[', ']', '\n','《','》','〔','〕','：','、','？','！','『','』','；','●','［','］','■']
[counter.pop(x, None) for x in STOP_WORDS] # 從字典裡刪除停用詞
print(counter) # 把計算完的每個分詞出現次數顯示出來看看



# # 輸出結果 to txt

# # 結果是key
# with open("author_tokenizer_counter.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(counter))

# 結果是dict
with open("author_tokenizer_counter.txt", "w", encoding="utf-8") as file:
    file.write(str(counter))



# # 取前 N 個詞頻最高的詞
# N = 20
# top_words = dict(most_counter_dict.most_common(N))




