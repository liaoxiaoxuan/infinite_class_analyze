import pandas as pd
from pyecharts.charts import Graph
from pyecharts import options as opts
import jieba
import jieba.posseg as pseg



# 處理《紅樓夢》文本資料
def deal_data():
    
    # 打開文本、讀取所有的行，並將其存儲在清單 honglou 中。
    with open("Dream_of_the_Red_Chamber.txt", encoding='utf-8') as f:
        honglou = f.readlines()
    
    # 載入自訂字典 "renwu_forcut"，用於jieba分詞。
    jieba.load_userdict("Hongxue_renwu_forcut")
    
    # 使用 pandas 庫的 read_csv 函數讀取 "renwu_forcut" 檔，其中 header=-1 表示沒有列名。
    renwu_data = pd.read_csv("Hongxue_renwu_forcut", header=-1)
    
    # 將讀取到的資料轉換為清單，並提取每個元素的第一個字串，然後存儲在 mylist 中。
    mylist = [k[0].split(" ")[0] for k in renwu_data.values.tolist()]
    
    # 創建一個空列表 tmpNames。
    tmpNames = []
    
    # 創建一個空字典 names，用於存儲人物名稱及出現次數。
    names = {}
    
    # 創建一個空字典 relationships，用於存儲人物關係。
    relationships = {}

    # 對於文字檔中的每一行進行迴圈處理。
    for h in honglou:
        # h.replace("贾妃", "元春")
        # h.replace("李宫裁", "李纨")
        
        # 使用 jieba 分詞工具對當前行進行分詞，將結果存儲在 poss 中。
        poss = pseg.cut(h)
        
        # 將一個空列表添加到 tmpNames 列表中。
        tmpNames.append([])

        # 對於每一個分詞結果進行迴圈處理。
        for w in poss:

            # 檢查當前分詞是否為人名、是否長度為2、是否在自訂字典中。
            if w.flag != 'nr' or len(w.word) != 2 or w.word not in mylist:
                continue

            # 將符合條件的詞添加到 tmpNames 列表中的最後一個子列表中。
            tmpNames[-1].append(w.word)

            # 檢查 names 字典中是否已存在當前人名，如果不存在則創建一個空字典。
            if names.get(w.word) is None:
                names[w.word] = 0

            # 為當前人名創建一個空字典，用於存儲其關係。
            relationships[w.word] = {}

            # 更新當前人名出現的次數。
            names[w.word] += 1
    
    # 輸出人物關係字典。
    print(relationships)
    
    # 輸出臨時人物列表。
    print(tmpNames)

    # 對於 names 字典中的每個鍵值對進行迴圈。
    for name, times in names.items():

        # 輸出人物名稱及出現次數。
        print(name, times)



