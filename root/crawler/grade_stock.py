
from root.crawler.stock_info import Stock, classify
from root.crawler import crawler


def stock_grade(stock_no, quarter):  # 用來回應網站首頁的函式
    '''Use stock_no and quarters to grade the stock'''
    date = quarter[:4]+'-'+quarter[4]
    stock = Stock(stock_no, 'None', date, 0, 0, 'NG')
    roe_result = crawler.get_roe(stock.no, quarter)
    if roe_result != None:
        stock.roe, stock.name = roe_result
    stock.fcf = crawler.get_fcf(stock.no, quarter)
    print(stock.name, stock.roe, stock.fcf)

    stock.grade = classify(stock.roe, stock.fcf)
    print(stock.__dict__)
    return stock.__dict__
