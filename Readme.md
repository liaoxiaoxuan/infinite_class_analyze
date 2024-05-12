# 用自然語言處理文言文中人物關係之研究

## 專案概述

這個專案是我第一個「資料視覺化與分析」相關的專案，旨在使用資料分析和自然語言處理技術，分析文言文的人物關係。  
會將分析材料鎖定於文言文，係由於我本身畢業於中國文學系所，除了文本的研讀與探究，研究所期間也有修習「數位人文」課程，對運用數位媒材協助議題的開展，甚感新鮮與有趣。因此，想藉由這次的程式操作，更進一步理解資料分析的城市開發，以及運用程式進行資料分析與傳統的研究方法，兩者的探究結果之異同。

### 分析資料

#### 1. 《詩話總龜》前集  
《詩話總龜》前集是宋人阮閱所編之宋代著名的詩話總集，蒐羅宋代詩話、隨筆等詩歌評論的書籍。期望可以藉由資料分析方法，得知書中引用內容和蒐羅資料的出處來源。

#### 2. 《紅樓夢》和《三國演義》  
這兩本是中國古代著名的章回小說。尤其是《紅樓夢》，更是最為著名且研究議題為古今中外討論度最高的，甚至將研究《紅樓夢》相關議題的學問，稱為「紅學」，其重要程度可見一斑。然而，也正因為《紅樓夢》‵備受高度關注，現有的資料分析，亦多如過江之鯽；因此，另外再加上也是為大眾所熟知的《三國演義》，以同樣方法進行分析、再次演練。

### 分析方法
+ 使用 [Jieba 分詞模組]() 進行文本分詞。
+ 使用詞頻分析模組進行詞頻統計。
+ 使用 matplotlib 技術生成文字雲和長條圖以視覺化詞頻分佈。
+ 使用 Word2Vec 模型進行詞向量表示和相似度計算。
+ 使用 networks 技術生成人際網絡圖。

## 安裝說明

1. Clone 這個專案到 local  
    ```bash
    git clone https://github.com/liaoxiaoxuan/infinite_class_analyze.git
    ```

2. 安裝相關資源
    ```
        pip install -r requirements.txt  
    ```

## 使用方式

### 1. 《詩話總龜》前集引用詩話分析

#### 1-1. 安裝相關模組：  
```
    pip install numpy
    pip install pillow
    pip install jieba
    pip install matplotlib
    pip install wordcloud
```

#### 1-2. 下載相關資源
+ 下載繁體中文詞庫檔案 dict.txt.big.txt
+ 下載中文字型檔案 NotoSerifTC-Regular.otf

#### 1-3. 執行程式碼
```
    python src/txt_author_jieba.py
```

### 2. 《紅樓夢》和《三國演義》詞向量表示和相似度計算

#### 2-1. 安裝相關模組：  
```
    pip install numpy
    pip install pillow
    pip install jieba
    pip install matplotlib
    pip install gensim
    pip install scikit-learns
```

#### 2-2. 下載相關資源
+ 下載繁體中文詞庫檔案 dict.txt.big.txt
+ 下載中文字型檔案 NotoSerifTC-Regular.otf
+ 下載文本檔案
    - 《紅樓夢》 Dream_of_the_Red_Chamber.txt  
    - 《三國演義》 Sanguoyanyi.txt
+ 下載人名和地名字典檔案
    - 《紅樓夢》 Hongxue_character.txt 和 Hongxue_place.txt
    - 《三國演義》 Sanguoyanyi_character.txt 和 Sanguoyanyi_place.txt

#### 2-3. 執行程式碼
+ 《紅樓夢》
    ```
        python src/Hongxue_word2vec.py
    ```
+ 《三國演義》
    ```
        python src/Sanguoyanyi_word2vec.py
    ```

### 3. 《紅樓夢》和《三國演義》人際網絡圖

#### 3-1. 安裝相關模組：  
```
    pip install pandas
    pip install pyecharts
    pip install jieba
    pip install snapshot-selenium
```

#### 3-2. 下載相關資源
+ 下載繁體中文詞庫檔案 dict.txt.big.txt
+ 下載中文字型檔案 NotoSerifTC-Regular.otf
+ 下載文本檔案
    - 《紅樓夢》 Dream_of_the_Red_Chamber.txt  
    - 《三國演義》 Sanguoyanyi.txt
+ 下載人名字典
    - 《紅樓夢》 Hongxue_renwu_forcut.txt
    - 《三國演義》 Sanguoyanyi_renwu_forcut.txt

#### 3-3. 執行程式碼
+ 《紅樓夢》
    ```
        python src/Hongxue_networks.py
    ```
+ 《三國演義》
    ```
        python src/Sanguoyanyi_networks.py
    ```

## 程式架構與結果呈現

1. 《詩話總龜》前集引用詩話分析  
    分析《詩話總龜》前集引用的詩話次數和頻率，生成文字雲和長條圖。  
    + 文字雲
    ![fig1](./src/book_wc.png)  
    
    + 長條圖  
    ![fig2](./src/book_plt.png)  

2. 《紅樓夢》和《三國演義》詞向量表示和相似度計算：**Word2Vec**  應用  

    **2-1. 《紅樓夢》**  
        匯入人名和地名字典之後，將《紅樓夢》進行斷詞，接著繪製 Word2Vec 二維空間投影，並計算書中賈寶玉和十二金釵等主要人物之間的距離相似度。  
    
    + 二維空間投影
    ![fig3](./src/Hongxue_word2vec.jpeg)

    + 詞向量表示  
        ```
        賈惜春 和 秦可卿 之間的距離為: 0.09717483818531036
        賈元春 和 賈迎春 之間的距離為: 0.12379106134176254
        賈元春 和 秦可卿 之間的距離為: 0.1463087499141693
        賈迎春 和 秦可卿 之間的距離為: 0.15767629444599152
        賈元春 和 賈惜春 之間的距離為: 0.17363978922367096
        賈迎春 和 賈惜春 之間的距離為: 0.1937878131866455
        賈寶玉 和 王熙鳳 之間的距離為: 0.31754785776138306
        賈寶玉 和 薛寶釵 之間的距離為: 0.32167917490005493
        薛寶釵 和 王熙鳳 之間的距離為: 0.4114401638507843
        史湘雲 和 巧姐 之間的距離為: 0.6686884760856628
        ```
    
    + 餘弦相似度  
        ```
        林黛玉 和 賈惜春 之間的 cosine similarity 為: 0.6387871503829956
        史湘雲 和 賈惜春 之間的 cosine similarity 為: 0.6321501731872559
        妙玉 和 賈惜春 之間的 cosine similarity 為: 0.6299555897712708
        賈惜春 和 巧姐 之間的 cosine similarity 為: 0.5755219459533691
        賈元春 和 賈惜春 之間的 cosine similarity 為: 0.5324227213859558
        賈寶玉 和 賈惜春 之間的 cosine similarity 為: 0.5182535648345947
        薛寶釵 和 賈惜春 之間的 cosine similarity 為: 0.49956437945365906
        賈惜春 和 王熙鳳 之間的 cosine similarity 為: 0.47346630692481995
        賈惜春 和 秦可卿 之間的 cosine similarity 為: 0.46621453762054443
        賈迎春 和 賈惜春 之間的 cosine similarity 為: 0.3522908091545105
        ```  

    **2-2. 《三國演義》**  
        匯入人名和地名字典之後，將《三國演義》進行斷詞，接著繪製 Word2Vec 二維空間投影，並計算書中諸葛亮和三國主要人物之間的距離相似度。  
    
    + 二維空間投影
    ![fig4](./src/Sanguoyanyi_word2vec.jpeg)
    
    + 詞向量表示  
        ```
        孫權 和 司馬懿 之間的距離為: 0.2548621892929077  
        張飛 和 司馬懿 之間的距離為: 0.27175915241241455  
        張飛 和 孫權 之間的距離為: 0.3394671082496643  
        趙雲 和 司馬懿 之間的距離為: 0.4629286527633667  
        張飛 和 趙雲 之間的距離為: 0.47713392972946167  
        關羽 和 劉禪 之間的距離為: 0.5029202699661255  
        劉備 和 張飛 之間的距離為: 0.5201414823532104  
        孫權 和 趙雲 之間的距離為: 0.5865809321403503  
        劉備 和 司馬懿 之間的距離為: 0.6148875951766968  
        劉備 和 孫權 之間的距離為: 0.6972569823265076
        ```  
    
    + 餘弦相似度  
        ```
        諸葛亮 和 關羽 之間的 cosine similarity 為: 0.9739437103271484
        關羽 和 趙雲 之間的 cosine similarity 為: 0.9715537428855896
        劉備 和 關羽 之間的 cosine similarity 為: 0.9709815382957458
        關羽 和 張飛 之間的 cosine similarity 為: 0.9692081809043884
        關羽 和 司馬昭 之間的 cosine similarity 為: 0.9681985378265381
        關羽 和 司馬懿 之間的 cosine similarity 為: 0.9670453071594238
        關羽 和 劉禪 之間的 cosine similarity 為: 0.966686487197876
        關羽 和 孫權 之間的 cosine similarity 為: 0.9662905335426331
        關羽 和 周瑜 之間的 cosine similarity 為: 0.9635964035987854
        關羽 和 曹操 之間的 cosine similarity 為: 0.955909252166748
        ```  

3. 《紅樓夢》和《三國演義》人際網絡圖：**networks** 應用  

    **3-1. 《紅樓夢》**  
        匯入人名和地名字典之後，將《紅樓夢》進行斷詞，並生成書中賈寶玉和十二金釵等主要人物之間的人際網絡圖。  
          
     ![fig5](./src/hongxue_networks.png)
    
    **2-2. 《三國演義》**  
        匯入人名和地名字典之後，將《三國演義》進行斷詞，並生成書中諸葛亮和三國主要人物之間的人際網絡圖。  
        
      ![fig6](./src/Sanguoyanyi_networks.png)
