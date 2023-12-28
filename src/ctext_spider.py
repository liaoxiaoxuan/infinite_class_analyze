# 匯入Selenium套件
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 開啟瀏覽器（browser）google chrome，以及欲前往的網頁
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://ctext.org/wiki.pl?if=gb&chapter=774685")