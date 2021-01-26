import datetime
import time
from day import peratio
from day import price
from month import revenue
from season import financial

def getLastPEData(max_error_times):
    error_times = 0
    hasped = False
    dataDate = datetime.date.today()
    while (hasped == False and error_times < max_error_times):
        try:
            time.sleep(10)
            dfped = peratio.peratio_date(dataDate)
            if (dfped.empty):
                raise ValueError('no data')
            else:
                hasped = True
                print('P/E Ratio: ', dataDate.strftime("%Y/%m/%d"), 'Success!')
        except BaseException:
            print('P/E Ratio: ', dataDate.strftime("%Y/%m/%d"), 'Failed!')
            error_times = error_times + 1
            dataDate = dataDate - datetime.timedelta(days=1)
            continue
    return dfped


def getLastPriceData(max_error_times):
    hasprd = False
    dataDate = datetime.date.today()
    error_times = 0
    while (hasprd == False and error_times < max_error_times):
        try:
            time.sleep(10)
            dfprd = price.price_date(dataDate)
            if (dfprd.empty):
                raise ValueError('no data')
            else:
                hasprd = True
                print('Price Ratio: ', dataDate.strftime("%Y/%m/%d"),
                      'Success!')
        except BaseException:
            print('Price Ratio: ', dataDate.strftime("%Y/%m/%d"), 'Failed!')
            error_times = error_times + 1
            dataDate = dataDate - datetime.timedelta(days=1)
            continue
    return dfprd


def getLastRevenueData(max_error_times):
    hasrevenue = False
    dataDate = datetime.date.today()
    error_times = 0
    while (hasrevenue == False and error_times < max_error_times):
        try:
            time.sleep(10)
            dfrevenue = revenue.revneue_statement_all(dataDate.year,
                                                      dataDate.month)
            if (dfrevenue.empty):
                raise ValueError('no data')
            else:
                hasrevenue = True
                print('Revenue: ', dataDate.strftime("%Y/%m"), 'Success!')
        except BaseException:
            print('Revenue: ', dataDate.strftime("%Y/%m"), 'Failed!')
            error_times = error_times + 1
            dataDate = datetime.datetime(
                dataDate.year - 1 if dataDate.month == 1 else dataDate.year,
                12 if dataDate.month == 1 else dataDate.month - 1, 1)
            continue
    return dfrevenue


def getLastFinancialData(max_error_times):
    hasfin = False
    dataDate = datetime.date.today()
    error_times = 0
    while (hasfin == False and error_times < max_error_times):
        try:
            time.sleep(10)
            dffin = financial.financial_statement_all(
                dataDate.year, int(round(dataDate.month / 4, 0) + 1))
            if (dffin.empty):
                raise ValueError('no data')
            else:
                hasfin = True
                print('Financial: ', dataDate.strftime("%Y/%m"), 'Success!')
        except BaseException:
            print('Financial: ', str(dataDate.year), '/',
                  str(int(round(dataDate.month / 4, 0) + 1)), 'Failed!')
            error_times = error_times + 1
            dataDate = datetime.datetime(
                dataDate.year - 1
                if 1 <= dataDate.month <= 3 else dataDate.year, 10 if
                1 <= dataDate.month <= 3 else 7 if 10 <= dataDate.month <= 12
                else 4 if 7 <= dataDate.month <= 9 else 1, 1)
            continue
    return dffin