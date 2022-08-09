from dataclasses import dataclass
import random


@dataclass
class Stock:
    no: int
    name: str
    date: str
    roe: float
    fcf: float
    grade: str


def classify(roe: float, fcf: float):
    if (roe is None) or (fcf is None):
        return
    if roe >= 20:
        result = 'A1'
    elif 20 > roe >= 15:
        result = 'A2' if (fcf > 0) else 'B1'
    elif 15 > roe >= 10:
        result = 'B2' if (fcf > 0) else 'C'
    elif 10 > roe > 0:
        result = 'C1' if (fcf > 0) else 'C2'
    else:
        result = 'D'
    return result


def test_case():
    '''Input some stock cases'''
    cases = [
        {'no': '2330', 'name': '台積電', 'date': '2022-1',
            'roe': 31.4, 'fcf': 3763.0, 'grade': 'A1'},
        {'no': '2330', 'name': '台積電', 'date': '2021-4',
            'roe': 29.7, 'fcf': 2757.0, 'grade': 'A1'},
        {'no': '2330', 'name': '台積電', 'date': '2020-1',
            'roe': 24.8, 'fcf': 820.0, 'grade': 'A1'},
        {'no': '2308', 'name': '台達電', 'date': '2022-1',
            'roe': 15.4, 'fcf': -6.2, 'grade': 'B1'},
        {'no': '2308', 'name': '台達電', 'date': '2021-4',
            'roe': 15.8, 'fcf': 18.4, 'grade': 'A2'},
        {'no': '2618', 'name': '長榮航', 'date': '2022-1',
            'roe': 14.0, 'fcf': 303.1, 'grade': 'B2'},
        {'no': '2618', 'name': '長榮航', 'date': '2020-1',
            'roe': 2.2, 'fcf': -12.2, 'grade': 'C2'},
        {'no': '2603', 'name': '長榮', 'date': '2022-1',
            'roe': 118.0, 'fcf': 2199.6, 'grade': 'A1'},
        {'no': '2603', 'name': '長榮', 'date': '2021-1',
            'roe': 66.9, 'fcf': 497.6, 'grade': 'A1'},
        {'no': '2354', 'name': '鴻準', 'date': '2022-1',
            'roe': 3.7, 'fcf': -143.4, 'grade': 'C2'},
        {'no': '2354', 'name': '鴻準', 'date': '2021-1',
            'roe': 5.1, 'fcf': 385.6, 'grade': 'C1'},
        {'no': '2317', 'name': '鴻海', 'date': '2022-1',
            'roe': 10.0, 'fcf': -348.1, 'grade': 'C'},
        {'no': '2317', 'name': '鴻海', 'date': '2021-2',
            'roe': 10.6, 'fcf': 1976.4, 'grade': 'B2'},
        {'no': '2727', 'name': '王品', 'date': '2022-1',
            'roe': -5.7, 'fcf': 13.4, 'grade': 'D'},
        {'no': '2727', 'name': '王品', 'date': '2020-2',
            'roe': -1.0, 'fcf': 14.8, 'grade': 'D'},
        {'no': '1301', 'name': '台塑', 'date': '2022-1',
            'roe': 19.1, 'fcf': 446.8, 'grade': 'A2'},
        {'no': '2454', 'name': '聯發科', 'date': '2022-1',
         'roe': 28.9, 'fcf': 501.3, 'grade': 'A1'},
        {'no': '2453', 'name': '凌群', 'date': '2021-1',
         'roe': 10.1, 'fcf': 2.9, 'grade': 'B2'}
    ]
    return random.sample(cases, 5)
