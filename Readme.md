# 用自然語言處理文言文中人物關係之研究

## 專案概述

這個專案是我第一個「資料視覺化與分析」相關的專案，旨在使用資料分析和自然語言處理技術，分析文言文的人物關係。  
會將分析材料鎖定於文言文，係由於我本身畢業於中國文學系所，除了文本的研讀與探究，研究所期間也有修習「數位人文」課程，對運用數位媒材協助議題的開展，甚感新鮮與有趣。因此，想藉由這次的程式操作，更進一步理解運用程式進行資料分析，與傳統的研究方法與學識認知的異同。

### 分析資料

#### 1. 《詩話總龜》前集  
是宋人阮閱所編之宋代著名的詩話總集，蒐羅宋代詩話、隨筆等詩歌評論的書籍。期望可以藉由資料分析方法，得知書中引用內容和蒐羅資料的出處來源。

#### 2. 《紅樓夢》和《三國演義》  
這兩本是中國古代著名的章回小說。尤其是《紅樓夢》，更是是最為著名且研究議題為古今中外討論度最高的，甚至將研究《紅樓夢》相關議題的學問，稱為「紅學」，其重要程度可見一斑。然而，也正因為《紅樓夢》的備受關注，現有的資料分析，亦多如過江之鯽；因此，另外再加上也是為大眾所熟知的《三國演義》，以同樣方法進行分析、再次演練。

### 分析方法
+ 使用 Jieba 分詞模組進行文本分詞。
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

2. 《紅樓夢》和《三國演義》詞向量表示和相似度計算  
    分析《詩話總龜》前集引用的詩話次數和頻率，生成文字雲和長條圖。  
    + 文字雲
    ![fig1](./src/book_wc.png)  
    + 長條圖  
    ![fig2](./src/book_plt.png)  