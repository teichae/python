from selenium import webdriver
from bs4 import BeautifulSoup
import linecache
import sys

def getFinaceHtml ( code ):
    url = "https://finance.naver.com/item/main.nhn?code=" + str(code)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('/Users/teichae/python/venv/chromedriver',  chrome_options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    no_today = soup.find("dl", {"class": "blind"})
    arrSplit = no_today.text.split('\n')
    #print(arrSplit)

    result = {
        "종목명": "",
        "종목코드": "",
        "현재가": "",
        "전일가" : "",
        "시가" : "",
    }

    for row in arrSplit:
        arrRowSplit = row.split(" ")
    #    print(str(row))
        if arrRowSplit[0] == "종목명" :
            result["종목명"] = arrRowSplit[1]
        elif arrRowSplit[0] == "종목코드" :
            result["종목코드"] = arrRowSplit[1]
        elif arrRowSplit[0] == "현재가" :
            result["현재가"] = arrRowSplit[1]
        elif arrRowSplit[0] == "전일가" :
            result["전일가"] = arrRowSplit[1]
        elif arrRowSplit[0] == "시가" :
            result["시가"] = arrRowSplit[1]
    #   print("================")
    #print("================")
    #print("================")
    samSung = "48,800"
    macInfra = "11,450"
    hyundaiCar = "92,150"

    print(result)
    if result["종목명"] == "삼성전자":
        if result["현재가"] > samSung:
            print("개이득")
        elif result["현재가"] <= samSung:
            print("개손해")
    elif result["종목명"] == "맥쿼리인프라":
         if result["현재가"] > macInfra:
            print("개이득")
         elif result["현재가"] <= macInfra:
            print("개손해")
    elif result["종목명"] == "현대차":
        if result["현재가"] > hyundaiCar:
            print("개이득")
        elif result["현재가"] <= hyundaiCar:
            print("개손해")

    driver.quit()

codeList = [
    "005930",
    "005380",
    "088980"
             ]

for code in codeList:
    # sys.stdout = open('test.txt', 'w') #출력값 파일로 쓰기
    getFinaceHtml(code)
