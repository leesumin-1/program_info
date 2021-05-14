import time
import selenium
from selenium import webdriver

print("편성정보가 궁금한 티비 프로그램 4개를 입력하시오(,로 구분)")
print("ex : 나혼자 산다, 놀라운 토요일, 런닝맨, 놀면 뭐하니")
program_list_string=input(">> : ")
program_list=program_list_string.split(",")

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
driver = webdriver.Chrome(executable_path='./chromedriver.exe')#, options=options)
driver.get(url=URL)

for tv_program in program_list:
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(tv_program)

    search_btn=driver.find_element_by_class_name("bt_search")
    search_btn.click()

    title= driver.find_element_by_class_name("title").text
    start_and_when = driver.find_element_by_class_name("info_group").text

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()

time.sleep(3)

driver.close()