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



    # 過濾掉所有的標點符號
    for i in temp:
        i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》「」〔〕『』；［］■●...〈〉【】]+|[+——！，。？、~@#￥%……&*（）：]+", "", i)
        if len(i) > 0:
            words.append(i)
    if len(words) > 0:
        lines.append(words)
# print(lines)



# 輸入 Word2Vec 模型
model = Word2Vec(lines, window = 2 , min_count = 0)  # 在文本中查找的每個詞彙的左右各2個詞的上下文，並不容忽略任何詞彙
renwu = model.wv.most_similar('寶玉', topn = 50)  # 找到與「寶玉」最相關的20個詞，並將結果存儲在 renwu 中
print(renwu)

# 將詞向量轉換為二維空間中的向量，以便進行視覺化或其他分析
rawWordVec = []  # 建立一個空的列表 rawWordVec，用於存儲原始的詞向量
word2ind = {}  # 建立一個空的字典 word2ind，用於存儲詞到索引的映射
for i, w in enumerate(model.wv.index_to_key):  # 遍歷模型中的所有詞彙
    rawWordVec.append(model.wv.get_vector(w))  # 將每個詞的詞向量添加到 rawWordVec 中
    word2ind[w] = i  # 將詞與其在 rawWordVec 中的索引建立映射
rawWordVec = np.array(rawWordVec)  # 將 rawWordVec 轉換為NumPy陣列，以便後續的數學運算
X_reduced = PCA(n_components=2).fit_transform(rawWordVec)  # 利用主成分分析（PCA）將原始的詞向量降維到二維空間



# 繪製所有單詞向量的二維空間投影
fig = plt.figure(figsize = (15, 10))  # 創建了一個圖形物件 fig，並設置了該圖形的大小為（15, 10）  # plt = Matplotlib
ax = fig.gca()  # 創建了一個 Axes 物件 ax，並將它設置為剛剛創建的 Matplotlib 圖形物件 fig 的軸
ax.set_facecolor('black')  # 設置背景顏色為黑色
# 將散點圖繪製到軸上
# 在當前軸上繪製一個二維散點圖，散點圖的 X 座標和 Y 座標由 X_reduced 提供，點的樣式為點，大小為 1，透明度為 0.3，顏色為白色
ax.plot(X_reduced[:, 0], X_reduced[:, 1], '.', markersize = 1, alpha = 0.3, color = 'white')



# 繪製幾個特殊單詞的向量
words = ['賈寶玉', '林黛玉' , '薛寶釵' , '賈元春' , '賈探春' , '史湘雲' , '妙玉' , '賈迎春' , '賈惜春' , '王熙鳳' , '巧姐' , '李紈' , '秦可卿']



# 設置中文字體，否則無法在圖形上顯示中文
zhfont1 = matplotlib.font_manager.FontProperties(fname=r'..\Noto_Serif_TC\NotoSerifTC-Light.otf', size=16)
for w in words:
    if w in word2ind:
        ind = word2ind[w]
        xy = X_reduced[ind]
        plt.plot(xy[0], xy[1], '.', alpha =1, color = 'red')
        plt.text(xy[0], xy[1], w, fontproperties = zhfont1, alpha = 1, color = 'yellow')
plt.show()



# 計算向量歐式距離

# 定義函數計算兩個人物之間的距離
def calculate_distance(person1, person2):
    if person1 in word2ind and person2 in word2ind:
        # 獲取兩個人物的索引
        ind1 = word2ind[person1]
        ind2 = word2ind[person2]

        # 獲取兩個人物的向量
        vec1 = rawWordVec[ind1]
        vec2 = rawWordVec[ind2]

        # 計算兩個向量之間的歐式距離
        distance = np.linalg.norm(vec1 - vec2)
        return distance
    else:
        print(f"詞彙 '{person1}' 或 '{person2}' 不存在於詞彙中。")


# 遍歷所有人物組合，並計算距離
for i in range(len(words)):
    for j in range(i+1, len(words)):
        person1 = words[i]
        person2 = words[j]
        distance = calculate_distance(person1, person2)
        if distance is not None:
            print(f"{person1} 和 {person2} 之間的距離為: {distance}")
print("----------------------------------------------------------------")


# 將人物距離結果由低至高排序

# 創建一個空的列表，用於存儲所有人物之間的距離
distances = []

# 遍歷所有人物組合，並計算距離
for i in range(len(words)):
    for j in range(i+1, len(words)):
        person1 = words[i]
        person2 = words[j]
        distance = calculate_distance(person1, person2)
        if distance is not None:
            # 將距離和對應的人物組合添加到 distances 列表中
            distances.append((person1, person2, distance))

# 將 distances 列表按照距離由低至高排序
sorted_distances = sorted(distances, key=lambda x: x[2])

# 輸出排序後的結果
for distance_info in sorted_distances:
    print(f"{distance_info[0]} 和 {distance_info[1]} 之間的距離為: {distance_info[2]}")            



# # 輸出結果 to txt

# # 結果是key
# with open("Hongxue_jieba_counter.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(counter))

# # 結果是dict
# with open("Hongxue_word2vec_jieba_lcut.txt", "w", encoding="utf-8") as file:
#     file.write(str(lines))
