# FMKoreaCrawler
Crawler for the Korean Forum Website ['FMKorea'](https://www.fmkorea.com/)

### Required Libaries:
- beautifulsoup
- selenium

This crawler will gather all posts based on the search query, as well as its post comments.

It uses beautifulsoup in conjunction with selenium, please install if you have not done so already:

```
pip install beautifulsoup4
pip install -U selenium
```

There are a few lines you will need to manually enter, as FMKorea encodes its URL. The URL you will need to grab from FMKorea directly.

Here is where you will need to edit:
```
# 변수 설정
QUERY = "오세훈"
search_QUERY = urlencode({'query' : QUERY}, encoding = 'utf-8')
URL = f"https://www.fmkorea.com/search.php?mid=home&act=IS&where=&sph_sort=&search_target=&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88#gsc.sort=date&gsc.tab=&gsc.q=%EC%98%A4%EC%84%B8%ED%9B%88&" 
URL2 = 'https://www.fmkorea.com/search.php?mid=home&act=IS&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88&where=document&page='
PATH = 'C:/Users/jm215/Documents/MEGA/Crawlers/IMDB/chromedriver.exe'
```
URL is the URL of the page when you initially search your term. URL2, is when you go to the next page, but without the actual page number. The only changing part is the encoded string which is the search term '%EC%98%A4%EC%84%B8%ED%9B%88' in the above example code. You can technically just replace this portion only and it should work fine. 

QUERY of course is your search term and PATH is the PATH where your ChromeDriver is located.

The way FMKorea is configured, you can not view past page 999, even manually. You also cannot filter time.

### Using ChromeDriver: 
Make sure you have downloaded the latest ChromeDriver file, which you can find [here](https://chromedriver.chromium.org/getting-started), make sure to get the correct one for your OS and Chrome version. It may be necessary to update your Chrome as well.

```
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
```

This is to create a driver instance in **Linux**. You will have to change this line if your OS is NOT linux. 

For example, this would be what you would change it to in **Windows**:
```
# Specify the path to the ChromeDriver executable if not added to PATH
chrome_driver_path = 'path/to/chromedriver.exe'

# Create ChromeDriver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```

Initializing ChromeDriver is simple but may differ by your environment, so please correctly configure if my current setting does not work on your os.

# FMKoreaCrawler
한국 포럼 웹사이트 ['FMKorea'](https://www.fmkorea.com/)를 위한 크롤러

### 필요한 라이브러리:
- beautifulsoup
- selenium

이 크롤러는 검색어를 기반으로 모든 게시물과 해당 게시물의 댓글을 수집합니다.

이는 beautifulsoup과 selenium을 함께 사용하며, 아직 설치하지 않은 경우 다음 명령을 실행하여 설치하세요:
```
pip install beautifulsoup4
pip install -U selenium
```

FMKorea는 URL을 인코딩하므로 수동으로 몇 줄을 입력해야 합니다. URL은 FMKorea에서 직접 가져와야 합니다.

여기가 편집해야 할 곳입니다:
```
# 변수 설정
QUERY = "오세훈"
search_QUERY = urlencode({'query' : QUERY}, encoding = 'utf-8')
URL = f"https://www.fmkorea.com/search.php?mid=home&act=IS&where=&sph_sort=&search_target=&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88#gsc.sort=date&gsc.tab=&gsc.q=%EC%98%A4%EC%84%B8%ED%9B%88&" 
URL2 = 'https://www.fmkorea.com/search.php?mid=home&act=IS&is_keyword=%EC%98%A4%EC%84%B8%ED%9B%88&where=document&page='
PATH = 'C:/Users/jm215/Documents/MEGA/Crawlers/IMDB/chromedriver.exe'
```
URL은 검색어를 처음 검색할 때의 페이지 URL입니다. URL2는 다음 페이지로 이동할 때의 URL이며, 실제 페이지 번호는 포함되지 않습니다. 인코딩된 문자열인 검색어가 변경되는 부분인 '%EC%98%A4%EC%84%B8%ED%9B%88'은 위 예제 코드에서의 검색어입니다. 기술적으로 이 부분만 바꿔도 제대로 작동합니다.

QUERY는 검색어이고, PATH는 ChromeDriver가 위치한 경로입니다.

FMKorea의 구성 방식에 따라 수동으로도 페이지 999 이후를 볼 수 없습니다. 또한 시간을 필터링할 수 없습니다.

### ChromeDriver 사용전: 
최신 ChromeDriver 파일을 다운로드했는지 확인하세요. [여기](https://chromedriver.chromium.org/getting-started)에서 찾을 수 있습니다. 사용 중인 OS 및 Chrome 버전에 맞는 것을 가져오세요. Chrome을 업데이트해야 할 수도 있습니다.

리눅스로 드라이버 인스턴스 만들기: 
```
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
```

이것은 **리눅스**에서 드라이버 인스턴스를 만드는 것입니다. 사용 중인 OS가 리눅스가 아닌 경우 이 줄을 변경해야 합니다.

예를 들어, **윈도우**에서는 다음과 같이 변경해야 합니다:
```
# Specify the path to the ChromeDriver executable if not added to PATH
chrome_driver_path = 'path/to/chromedriver.exe'

# Create ChromeDriver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```

ChromeDriver를 초기화하는 것은 간단하지만 환경에 따라 다를 수 있으므로, 현재 설정이 작동하지 않는 경우 환경에 맞게 수정하세요.
