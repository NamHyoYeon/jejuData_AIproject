import json
import urllib
from urllib.parse import urlencode, unquote, quote_plus

import pandas as pd
import requests

# title
# startDate - endDate
# apiKey
# totalCnt
# pageNumber
# resultField

# 내국인 유동인구
# 20170101 - 20191231
# Daaa1t3at3tt8a8DD3t55538t35Dab1t
# 847530
# 8477
# baseDate, city, emd, gender, ageGroup, resdPop, workPop, visitPop

# 외국인장기체류
# 20171101 - 20191231
# 1aabbD515b0t9ataDD055551D5b0t1t1
# 645910
# 6460
# baseDate, nationality, city, emd, resdPop, workPop, visitPop

# 외국인단기체류
# 20180101 - 20191231
# t18b1bttt8abaDt51b8aat85ttaa8t5b
# 248205
# 2483
# baseDate, nationality, city, emd, visitPop

allData = []
fileName = '외국인_단기체류.csv'
totalCnt = 0

for p in range(2483, 2484):
    projectKey = '511b1pjjpjpe1t9tp59jp_1pet_15cjr'
    apiKey = 't18b1bttt8abaDt51b8aat85ttaa8t5b'
    startDate = 20180101
    endDate = 20191231
    pageNumber = p
    limit = 100
    url = f'https://open.jejudatahub.net/api/proxy/{apiKey}/{projectKey}?'

    queryParams = urlencode({quote_plus('startDate'): startDate,
                             quote_plus('endDate'): endDate,
                             quote_plus('limit'): limit,
                             quote_plus('number'): pageNumber,
                             })

    url2 = url + queryParams
    response = requests.get(url2)
    data = response.json()

    print(data)
    # data 정보
    info = data['data']

    baseDate = []
    city = []
    emd = []
    gender = []
    ageGroup = []
    resdPop = []
    workPop = []
    visitPop = []
    nationality = []

# baseDate, nationality, city, emd, visitPop
    for i in info:
        baseDate.append(i['baseDate'])
        city.append(i['city'])
        emd.append(i['emd'])
        nationality.append(i['nationality'])
        visitPop.append(i['visitPop'])
        totalCnt = totalCnt + 1
    df = pd.DataFrame([baseDate, nationality, city, emd, visitPop]).T
    df.columns = ['날짜', '국가', '시군구', '읍면동', '방문자수']
    df = df.sort_values(by='날짜', ascending=True)
    allData.append(df)
    print('현재까지 데이터 개수: ', totalCnt)
dataCombine = pd.concat(allData, axis=0, ignore_index=True)
dataCombine.to_csv(fileName, encoding='utf-8-sig')
