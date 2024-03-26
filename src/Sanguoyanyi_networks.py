import pandas as pd
from pyecharts.render import make_snapshot
from pyecharts.charts import Graph
from pyecharts import options as opts
import jieba
import jieba.posseg as pseg
from snapshot_selenium import snapshot



# 處理《紅樓夢》文本資料
def deal_data():
    
    # 打開文本、讀取所有的行，並將其存儲在清單 honglou 中。
    with open("Sanguoyanyi.txt", encoding='utf-8') as f:
        honglou = f.readlines()
    
    # 載入自訂字典 "renwu_forcut"，用於jieba分詞。
    jieba.load_userdict("Sanguoyanyi_renwu_forcut.txt")
    
    # 使用 pandas 庫的 read_csv 函數讀取 "renwu_forcut" 檔，其中 header=-1 表示沒有列名。
    renwu_data = pd.read_csv("Sanguoyanyi_renwu_forcut.txt", header=None)
    
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



# 構建人物之間的關係，並將結果保存到一個 CSV 檔，以便建立人物關係圖
    
    # 對於臨時人物列表中的每個子列表進行迴圈處理。
    for name in tmpNames:
        
        # 對於當前子列表中的每個人名進行迴圈處理。
        for name1 in name:
            
            # 對於當前子列表中的每個人名再次進行迴圈處理。
            for name2 in name:
                
                # 如果當前兩個人名相同，則繼續下一個迴圈，跳過重複計算。
                if name1 == name2:
                    continue
                
                # 如果名為 name1 的人物與名為 name2 的人物之間的關係尚未建立，則創建一個新的關係，初始權重為1。
                if relationships[name1].get(name2) is None:
                    relationships[name1][name2] = 1
                
                # 如果關係已存在，則將權重加1。
                else:
                    relationships[name1][name2] += 1
    
    # 輸出生成的人物關係字典。
    print(relationships)
    
    # 打開一個 CSV 檔 "relationship.csv"，以寫入模式打開，使用 UTF-8 編碼。
    with open("Sanguoyanyi_N_relationship.csv", "w", encoding='utf-8') as f:
        
        # 寫入 CSV 文件的表頭，即列名 "Source"（人物1）, "Target"（人物2）, "Weight"（關係權重）。
        f.write("Source,Target,Weight\n")
        
        # 對於人物關係字典中的每個鍵值對進行迴圈處理。
        for name, edges in relationships.items():
            
            # 對於每個人物的關係字典中的鍵值對進行迴圈處理，其中鍵是與當前人物有關係的另一個人物，值是兩者之間的關係權重。
            for v, w in edges.items():
                
                # 將人物關係以 CSV 格式寫入檔，每一行表示一個關係，格式為 "Source,Target,Weight"。
                f.write(name + "," + v + "," + str(w) + "\n")



# 定義了一個函數 deal_graph()，用於處理圖資料
# 讀取兩個 CSV 檔中的資料並將其轉換為列表形式，以便後續對圖資料進行處理。
def deal_graph():

    # 使用 pandas 庫的 read_csv 函數讀取名為 'relationship.csv' 的 CSV 檔，並將其存儲在 relationship_data 中。
    relationship_data = pd.read_csv('relationship.csv')

    # 使用 pandas 庫的 read_csv 函數讀取名為 'NameNode.csv' 的 CSV 檔，並將其存儲在 namenode_data 中。
    namenode_data = pd.read_csv('NameNode.csv')

    # 將 relationship_data 轉換為列表形式，其中每個子列表對應 CSV 檔中的一行資料。結果存儲在 relationship_data_list 中。
    relationship_data_list = relationship_data.values.tolist()

    # 將 namenode_data 轉換為列表形式，其中每個子列表對應 CSV 檔中的一行資料。結果存儲在 namenode_data_list 中。
    namenode_data_list = namenode_data.values.tolist()



if __name__ == '__main__':
    
    # 調用 deal_data() 函數，這個函數處理文本資料。
    deal_data()
