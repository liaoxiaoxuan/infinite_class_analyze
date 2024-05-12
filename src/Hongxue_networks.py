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
    with open("hongloumeng.txt", encoding='utf-8') as f:
        honglou = f.readlines()
    
    # 載入自訂字典 "renwu_forcut"，用於jieba分詞。
    jieba.load_userdict("Hongxue_renwu_forcut.txt")
    
    # 使用 pandas 庫的 read_csv 函數讀取 "renwu_forcut" 檔，其中 header=-1 表示沒有列名。
    renwu_data = pd.read_csv("Hongxue_renwu_forcut.txt", header=None)
    
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
    with open("relationship.csv", "w", encoding='utf-8') as f:
        
        # 寫入 CSV 文件的表頭，即列名 "Source"（人物1）, "Target"（人物2）, "Weight"（關係權重）。
        f.write("Source,Target,Weight\n")
        
        # 對於人物關係字典中的每個鍵值對進行迴圈處理。
        for name, edges in relationships.items():
            
            # 對於每個人物的關係字典中的鍵值對進行迴圈處理，其中鍵是與當前人物有關係的另一個人物，值是兩者之間的關係權重。
            for v, w in edges.items():
                
                # 將人物關係以 CSV 格式寫入檔，每一行表示一個關係，格式為 "Source,Target,Weight"。
                f.write(name + "," + v + "," + str(w) + "\n")



# 將人物名稱及其出現次數寫入到一個名為 "NameNode.csv" 的 CSV 文件中
    
    # 以寫入模式打開一個名為 "NameNode.csv" 的檔，並指定編碼為'utf-8'，檔物件賦值給 f。
    with open("NameNode.csv", "w", encoding='utf-8') as f:
        
        # 將檔的第一行寫入標題，這裡是 "ID（人物ID）,Label（人物名稱）,Weight（關係權重）"，用逗號分隔，表示列名。
        f.write("ID,Label,Weight\n")
        
        # 對於 names 字典中的每個鍵值對進行迴圈，其中鍵是人物名稱，值是該人物出現的次數。
        for name, times in names.items():
            
            # 將人物名稱、人物名稱和出現次數以逗號分隔的形式寫入檔。str(times)將出現次數轉換為字串。每次迴圈後換行。
            f.write(name + "," + name + "," + str(times) + "\n")



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



# 處理讀取的節點和關係資料，以準備構建視覺化圖
# 生成一個包含節點和邊的列表，以便後續使用這些資料來構建圖形視覺化

    # 創建一個空清單 nodes，用於存儲節點資料。
    nodes = []

    # 對於讀取的名為 'NameNode.csv' 的節點資料清單中的每個節點進行迴圈處理。
    for node in namenode_data_list:

        # 檢查當前節點的名稱是否為 "寶玉"。
        if node[0] == "寶玉":

            # 如果當前節點的名稱為 "寶玉"，則將其權重值除以3。
            node[2] = node[2]/3
        
        # 將節點的名稱和權重信息（經過處理後）以字典的形式添加到 nodes 列表中，其中 "name" 鍵對應節點名稱，"symbolSize" 鍵對應節點的大小。
        nodes.append({"name": node[0], "symbolSize": node[2]/30})
    
    # 創建一個空清單 links，用於存儲關係資料。
    links = []

    # 對於讀取的名為 'relationship.csv' 的關係資料清單中的每個關係進行迴圈處理。
    for link in relationship_data_list:

        # 將關係的源節點、目標節點以及關係權重以字典的形式添加到 links 列表中。
        # "Source"：人物1, "Target"：人物2, "Weight"：關係權重
        links.append({"source": link[0], "target": link[1], "value": link[2]})



    # 使用 pyecharts 庫創建一個圖形物件，並將之前處理得到的節點和邊資料添加到圖形中，以構建一個關係圖。
    
    # 定義一個名為 g 的變數，用於存儲圖形物件。
    g = (
        
        # 創建一個空白的關係圖物件。
        Graph()
        
        # 向關係圖中添加節點和邊
        # nodes：節點資料；links：邊資料；repulsion=8000：指定節點之間的斥力大小，使得節點之間的間距適當。
        .add("", nodes, links, repulsion=8000)
        
        # 設置全域選項，包括標題選項，這裡將標題設置為 "紅樓人物關係"。
        .set_global_opts(title_opts=opts.TitleOpts(title="紅樓人物關係"))
    )

    # 返回構建好的關係圖物件 g。
    return g



if __name__ == '__main__':
    
    # 調用 deal_data() 函數，這個函數處理文本資料。
    deal_data()

    # 調用 deal_graph() 函數，處理圖形資料，並將返回的圖形物件賦值給變數 g。
    g = deal_graph()

    # 將圖形物件 g 渲染成檔或顯示在螢幕上。
    # 具體的操作取決於 render() 方法的實現。
    # 通常情況下，它會將圖形保存到檔中，並根據檔案格式的尾碼進行選擇，比如 .html、.png 等。
    g.render()
    make_snapshot(snapshot,g.render(),'honglou_relationship.png')



deal_data()