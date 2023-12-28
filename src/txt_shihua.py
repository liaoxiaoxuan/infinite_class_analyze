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



# 匯入 data
file_path = 'spider_zonggui_previous.txt'
with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()
    # print(data)
    # print('------------------')



# 定義繁體中文檔名
WORDS_PATH = 'dict.txt.big.txt' # 繁體中文詞庫檔名
TC_FONT_PATH = './NotoSerifTC-Regular.otf' # 繁體中文字型檔名

# 匯入圖表中文字體
font_path = "./NotoSerifTC-Regular.otf"  # 替換為實際的中文字體文件路徑
font_prop = FontProperties(fname=font_path)

# # 設定中文字體
# font_path = r"D:\PYTHON\infinite_class_spider\src\NotoSerifSC-Regular.otf"  # 替換為實際的中文字體文件路徑
# font_prop = FontProperties(fname=font_path)



# # 切換 jieba 繁體中文詞庫

# jieba.set_dictionary(WORDS_PATH)



# jieba 斷詞

# 精確模式
# for sentence in data:
seg_list = jieba.lcut(data)
# print('/'.join(seg_list))

print('---------------')

# # 全模式
# for sentence in data:
#     seg_list = jieba.cut(sentence, cut_all=True)
#     print('/'.join(seg_list))

# print('---------------')

# # 搜索引擎模式
# for sentence in data:
#     seg_list = jieba.cut_for_search(sentence)
#     print('/'.join(seg_list))



# 使用正則表示式提取資訊（書名）
pattern = r"\《(.*?)\》"
matches = re.findall(pattern, data)

# 輸出提取到的資訊
# print("提取到的括號內的資訊：", matches)



# 詞頻

# # 總覽
# counter = Counter(matches)
# print(counter)

# 前幾名
most_counter_dict = Counter(matches)  # 出來的結果會是 dict
# most_counter_list = Counter(matches).most_common(100)  # 出來的結果會是 list
# most_counter_dict = {_[0]:_[1] for _ in most_counter_list}  # 轉換成 dict
print(most_counter_dict)

STOP_WORDS = [' ', '，', '（', '）', '...', '。', '「', '」', '[', ']', '\n','《','》','〔','〕']
[most_counter_dict.pop(x, None) for x in STOP_WORDS] # 從字典裡刪除停用詞
print(most_counter_dict) # 把計算完的每個分詞出現次數顯示出來看看

# 取前 N 個詞頻最高的詞
N = 20
top_words = dict(most_counter_dict.most_common(N))



# # 文字雲

# # 文字雲格式設定
# wc = wordcloud.WordCloud(background_color='white',
#                         margin=2, # 文字間距
#                         font_path=TC_FONT_PATH, # 設定字體
#                         max_words=200, # 取多少文字在裡面
#                         width=1280, height=720) # 解析度
# # wc = wordcloud.WordCloud()
                         
# # 生成文字雲
# wc.generate_from_frequencies(most_counter_dict) # 吃入次數字典資料

# # 產生圖檔
# wc.to_file('./book_wc.png')

# # 顯示文字雲圖片
# plt.imshow(wc)



# 圖表

# 設定 Matplotlib 使用的默認字體，注意替換為支援中文的字體路徑
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文黑體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 長條圖
plt.bar(top_words.keys(), top_words.values())

# 在每個 bar 頂部添加頻率次數
for x, y in zip(top_words.keys(), top_words.values()):
    plt.text(x, y + 0.05, str(y), ha='center', va='bottom', fontproperties=font_prop)

# # 添加標題和標籤
# plt.title('Top {} Words in the Text'.format(N))
# plt.xlabel('Words')
# plt.ylabel('Frequency')

# 添加中文標題和標籤
# plt.bar(data.keys(), data.values())
plt.title('前 20 名詩話來源', fontproperties=font_prop)  # 使用中文字體
plt.xlabel('詩話', fontproperties=font_prop)  # 使用中文字體
plt.ylabel('頻率', fontproperties=font_prop)  # 使用中文字體

# 產生圖檔
plt.savefig('./book_plt.png', format='png')

# 顯示圖表
plt.show()
