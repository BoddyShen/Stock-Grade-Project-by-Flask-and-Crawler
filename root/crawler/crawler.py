import requests
import pandas
from fake_useragent import UserAgent

user_agent = UserAgent()


def get_roe(stock_no='2330', quarter='20221'):
    '''Crawler the stock web to find sum of roe in recent quarters'''
    try:

        url = f'https://goodinfo.tw/tw/StockFinDetail.asp?STEP=DATA&STOCK_ID={stock_no}&RPT_CAT=XX_QUAR&QRY_TIME={quarter}'
        headers = {
            'origin': 'https://goodinfo.tw',
            'referer': f'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={stock_no}',
            'user-agent': user_agent.random
        }

        res = requests.post(url, headers=headers)
        res.encoding = "utf-8"

        dfs = pandas.read_html(res.text)
        name = dfs[0].iloc[0].values[0].split("\xa0")[1]
        df = dfs[1]
        roe_data = df[df['獲利能力'] ==
                      '股東權益報酬率\xa0(當季)'].iloc[0][1:5].astype(float)
        roe = sum(roe_data)
        return round(roe, 1), name

    except:
        return


def get_fcf(stock_no='2330', quarters='20221'):
    '''Crawler the stock web to find sum of free cash flow(fcf) in recent quarters'''
    try:
        url = f'https://goodinfo.tw/tw/StockFinDetail.asp?STEP=DATA&STOCK_ID={stock_no}&RPT_CAT=CF_QUAR&QRY_TIME={quarters}'
        headers = {
            'origin': 'https://goodinfo.tw',
            'referer': f'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={stock_no}',
            'user-agent': user_agent.random
        }

        res = requests.post(url, headers=headers)
        res.encoding = "utf-8"

        dfs = pandas.read_html(res.text)
        df = dfs[1]
        op_cashflow = df[df['營業活動'] ==
                         '營業活動之淨現金流入(出)'].iloc[0][1:5].astype(float)
        inv_cashflow = df[df['營業活動'] ==
                          '投資活動之淨現金流入(出)'].iloc[0][1:5].astype(float)
        fcf = sum(op_cashflow) + sum(inv_cashflow)
        return round(fcf, 1)

    except:
        return


if __name__ == '__main__':
    print(get_roe('2330', '20221'))
    print(get_roe('2330', '20211'))

    print(get_fcf('2330', '20221'))
    print(get_fcf('2330', '20211'))
