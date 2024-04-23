import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime as dtime
import csv
from lxml import etree

# 변수 설정
QUERY = "오세훈"
search_QUERY = urlencode({'query' : QUERY}, encoding = 'utf-8')
URL = f"https://www.fmkorea.com/search.php?mid=home&act=IS&where=&sph_sort=&search_target=&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88#gsc.sort=date&gsc.tab=&gsc.q=%EC%98%A4%EC%84%B8%ED%9B%88&" 
URL2 = 'https://www.fmkorea.com/search.php?mid=home&act=IS&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88&where=document&page='
PATH = 'C:/Users/jm215/Documents/MEGA/Crawlers/IMDB/chromedriver.exe'

# 마지막 페이지까지 클릭 
def go_to_last_page(URL): 
# Set up Chrome options for headless mode
	chrome_options = Options()
	chrome_options.add_argument("--headless")  # Run in headless mode
	chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode

	# Specify the path to the chromedriver executable
	chromedriver_path = PATH


	service = webdriver.chrome.service.Service(executable_path= chromedriver_path)
	driver = webdriver.Chrome(service=service, options=chrome_options)
	'''
	#Linux
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
	'''
	# Set implicit wait time
	driver.implicitly_wait(1)

	# Navigate to the URL
	driver.get(URL)

	html = driver.page_source
	soup = BeautifulSoup(html, 'lxml')
	#driver.quit()
	return soup


# 마지막 페이지 번호 알아내기 
def get_last_page(URL): 
	soup = go_to_last_page(URL)
	#pagination = soup.find('div', {'class' : 'page'})
	pages = 999
	page_list = []
	#for page in pages[1 :]:
	#	page_list.append(int(page.get_text(strip=True)))
	max_page = 999
	print(f"총 {max_page} 개의 페이지가 있습니다.")
	return max_page


# 게시판 링크 모두 가져오기 
def get_boards(page_num):
    boards = []
    for index, page in enumerate(range(page_num)):
        if page == 0:
            continue
        if page >= 2 :
            break
        boards.append(URL2 + page)
        print(boards[-1])

    return boards

#max_page 원래는 page_num

# 게시글 링크 가져오기 
def get_posts(): 
    global QUERY
    global PAGES
    board_links = get_boards(PAGES)
    posts = []
    website = 'https://www.fmkorea.com'
    full_posts = []
    for board_link in board_links:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode

        # Specify the path to the chromedriver executable
        chromedriver_path = PATH


        service = webdriver.chrome.service.Service(executable_path= chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Set implicit wait time
        driver.implicitly_wait(1)
        try:
            driver.get(board_link)
            links = driver.find_element(By.CLASS_NAME, 'searchResult')
            alist = links.find_elements(By.TAG_NAME, 'li')
            
            for link in alist:
                atag = link.find_element(By.TAG_NAME, 'a')
                text = atag.get_attribute('href')
                print(text)
                posts.append(text)

        except Exception as e:
            print(f"Error processing {board_link}: {e}")

        finally:
            driver.quit()
    
    print(f"총 {len(posts)} 개의 글 링크를 찾았습니다.")

    # 게시글 링크 csv로 저장 
    post_file = open(f"FMKOREA_{QUERY}_{PAGES}pages_inner_links.csv", mode='w', encoding='utf-8')
    writer = csv.writer(post_file)
    for post in posts:
        writer.writerow([website + post])
    post_file.close()
    
    return posts


# 한 페이지에서 정보 가져오기 
def extract_info(URL, wait_time=1, delay_time=1): 
	try:
		# Set up Chrome options for headless mode
		chrome_options = Options()
		chrome_options.add_argument("--headless")  # Run in headless mode
		chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode

		chromedriver_path = PATH


		service = webdriver.chrome.service.Service(executable_path= chromedriver_path)
		driver = webdriver.Chrome(service=service, options=chrome_options)
		# Set implicit wait time
		driver.implicitly_wait(wait_time)

		# Navigate to the URL
		driver.get(URL)
		html = driver.page_source
		time.sleep(delay_time)

		soup = BeautifulSoup(html, 'lxml')
   
		title = soup.find('div', {'class' : 'top_area ngeb'}).find('h1', {'class' : 'np_18px'}).find('span', {'class' :'np_18px_span'}).get_text(strip=True)  #잘 찾아짐
		print('Title: ' , title)
		post_time = soup.find('div', {'class' : 'top_area ngeb'}).find('span', {'class' : 'date m_no'}).get_text(strip=True) #잘 찾아짐
		print('Time: ', post_time)
		post = soup.find('article').get_text(strip=True) 
		
		print('Post: ', post)

		reply_cnt = 1
		reply_content = ""
		replies = soup.find_all('div', {'class' : 'comment-content'})
		print(replies)
		
		for reply in replies:
			reply_content += reply.get_text(strip=True).replace('\n', '').replace('\r', '').replace('\t','') + "\n"
		print(reply_content)

		print(URL, "완료")

		return {'title' : title, 'post_time' :post_time, 'post' : post, 'reply_cnt' : reply_cnt, 'reply_content' : reply_content}
	except Exception as e:
		print(f"에러발생: {e}")
		print(URL, "에러")
		pass


def get_contents(): 
	global fmkorea_results
	post_links = get_posts()
	for post_link in post_links:
		content = extract_info(post_link)
		if content is not None:
			append_to_file(f"FMKOREA_{QUERY}_{PAGES} pages.csv", content)
		else:
			append_to_file(f"FMKOREA_{QUERY}_{PAGES} pages.csv", {'title' : '', 'post_time' : '', 'post' : '', 'replsy_count' : 0, 'reply_content' : ''})
	return print("모든 작업이 완료되었습니다.")


# 저장 파일 만드는 함수 
def save_to_file(): 
	global QUERY
	global PAGES
	file = open(f"fmkorea_{QUERY}_{PAGES} pages.csv", mode='w', encoding='utf-8')
	writer = csv.writer(file)
	#writer.writerow(['site', 'title', 'user_id', 'post_time', 'post', 'view_cnt', 'recomm_cnt', 'reply_cnt', 'reply_content'])
	writer.writerow(['title', 'post_time', 'post', 'reply_count','reply_content'])
	file.close()
	return file

# 파일 열어서 쓰는 함수 
def append_to_file(file_name, dictionary): 
	file = open(file_name, mode='a', encoding='utf-8') # 덮어 쓰기 
	writer = csv.writer(file)
	writer.writerow(list(dictionary.values()))
	file.close()
	return 


# 함수 실행 
PAGES = get_last_page(URL)
fmkorea_results = save_to_file()
get_contents()