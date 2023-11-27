print ("媽!我在這!")
import time
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# 創建 ChromeOptions 物件
chrome_options = webdriver.ChromeOptions()

# 在這裡設置選項，例如：
# chrome_options.add_argument("--headless")  # 以無頭模式運行

# 提供完整的 Chrome 驅動程式路徑
chrome_driver_path = "C:\\Users\\User\\Desktop\\chromedriver-win32\\chromedriver.exe"

# 創建 Chrome WebDriver 實例
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://pitch-neon-130.notion.site/QA-5f38fe662c7b44fcbb7a3c63e62e663a")
time.sleep(5)
driver.close()
