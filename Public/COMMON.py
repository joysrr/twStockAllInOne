import requests
from datetime import datetime
import time

# 常數

__LISTEDCODE__ = 'sii'  # 上市代號
__OTCCODE__ = 'otc'  # 上櫃代號
__EMERGINGSCODE__ = 'rotc'  # 興櫃代號
__PUBLICCODE__ = 'pub'  # 公開發行代號

# 轉換值


def TryParse(parseType, val):
    defaultVal = val
    try:
        if parseType == 'int':
            defaultVal = 0
            nval = int(val)
        elif parseType == 'float':
            defaultVal = 0
            nval = float(val)
        else:
            raise ValueError('Parse Type not exists!')
        return nval, True
    except:
        return defaultVal, False


# 移除欄位中的雜訊


def col_clear(column):
    column = column.replace('&nbsp;', '').replace('\t', '').replace('<br>', '')
    remove_one = column.split('<')
    remove_two = remove_one[0].split('>')
    return remove_two[1].replace(",", "")

# 讀取url將頁面資料輸出


def crawl_data2text(url, formdata, encoding='utf-8', delay=1000):
    response = requests.post(url, formdata)
    response.encoding = encoding
    time.sleep(float(delay/1000))
    return response.text

# 西元年轉民國年


def year_CE2RC(year):
    if year > 1911:
        year = year-1911
    return year

def date_CE2RC(strdate):
    dateArray = strdate.split('/')
    if len(dateArray)>1:
        intYear, vaild = TryParse('int', dateArray[0])
        if vaild:
            nstrdate = str(year_CE2RC(intYear))
            for i in range(1,len(dateArray)):
                nstrdate = nstrdate + f'/{dateArray[i]}'
            return nstrdate
    return strdate

# 民國年轉西元年


def year_RC2CE(year):
    if year < 300:
        year = year+1911
    return year

def date_RC2CE(strdate):
    dateArray = strdate.split('/')
    if len(dateArray)>1:
        intYear, vaild = TryParse('int', dateArray[0])
        if vaild:
            nstrdate = str(year_RC2CE(intYear))
            for i in range(1,len(dateArray)):
                nstrdate = nstrdate + f'/{dateArray[i]}'
            return nstrdate
    return strdate


# 時間扣除月份
def minusMonth(oDate, format):
    year = oDate.year
    month = oDate.month-1
    if month == 0:
        year = year-1
        month = 12
    nDate = datetime(year, month, 1)

    return nDate, nDate.strftime(format)

    
        
  