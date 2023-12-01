# -*- coding: utf-8 -*-
import time
import random
import unittest
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class practicetest(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    #print("開始單元測試")
    cls.options = webdriver.ChromeOptions()
    #彈出視窗問題
    cls.prefs = {  
        'profile.default_content_setting_values' :  {  
            'notifications' : 2  
        }  
    }
    cls.options.add_experimental_option('prefs', cls.prefs)

    cls.options.add_argument('--no-sandbox')
    cls.options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(options=cls.options)

    cls.driver.maximize_window()#全螢幕
    cls.driver.implicitly_wait(10)

    
 

  def test1_search(self):
    self.driver.get('https://24h.pchome.com.tw/')
    wait = WebDriverWait(self.driver, 3)
    time.sleep(3)
    x_offset = random.randint(1, 500)
    y_offset = random.randint(1, 500)

    # 使用 ActionChains 進行移動和點擊操作
    actions = ActionChains(self.driver)
    actions.move_by_offset(x_offset, y_offset).click()

    #搜尋框輸入
    wait = WebDriverWait(self.driver, 3)
    self.input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'l-header__siteSearchInput')))
    self.input.send_keys(' Whoscall')
    self.input.send_keys(Keys.ENTER)

  def test2_click(self):
    wait = WebDriverWait(self.driver, 5)
    self.input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'prod_name'))).click()
    
    # 切換到新分頁
    wait.until(lambda driver: len(driver.window_handles) == 2)
    # 切換到新分頁
    self.driver.switch_to.window(self.driver.window_handles[1])

  def test3_check(self):
    wait = WebDriverWait(self.driver, 5)
    price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="o-prodPrice__price"]')))
    
    #獲取元素的文字內容
    actual_price = price.text
    
    #預期的價格
    expected_price = "$999"

    # 斷言檢查
    self.assertEqual(actual_price, expected_price)
    

  def test4_scroll(self):
    time.sleep(1)
    wait = WebDriverWait(self.driver, 5)
    
    actions = ActionChains(self.driver)
    for _ in range(133):  # 模擬捲動
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(0.01)#捲動間隔時間

  def test5_screenshot(self):
    time.sleep(1)
    screenshot_filename = 'cropped_screenshot.png'
    screenshot = self.driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))

     # 根據提供的座標和大小裁剪圖片
    cropped_image = image.crop((500, 100, 1666, 800))
        
    # 儲存裁剪後的圖片
    cropped_image.save(screenshot_filename)

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

if __name__=='__main__':
     unittest.main()

