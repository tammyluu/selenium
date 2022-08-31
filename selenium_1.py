import time #  Sử dụng thư viện thời gian trong trường hợp cần đợi kết quả từ câu lệnh được thực thi
from selenium import webdriver # Sử dụng selenium để điều khiển trình duyệt web
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="C:/Users/luuta/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('https://trendoceans.com')
print('Title: %s' % browser.title) # print title of web
time.sleep(10)#Là thời gian để tải trang. Tùy thuộc vào tốc độ mạng để thiết lập thời gian.
browser.quit() # close chrôme