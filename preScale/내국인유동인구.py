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

allData = []
fileName = '내국인_유동인구.csv'
totalCnt = 0

for p in range(7985, 8478):
    projectKey = '4j__7b4__c4744eett7e0_4o4_jj9ett'
    apiKey = 'Daaa1t3at3tt8a8DD3t55538t35Dab1t'
    startDate = 20170101
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

# baseDate, city, emd, gender, ageGroup, resdPop, workPop, visitPop
    for i in info:
        baseDate.append(i['baseDate'])
        city.append(i['city'])
        emd.append(i['emd'])
        gender.append(i['gender'])
        ageGroup.append(i['ageGroup'])
        resdPop.append(i['resdPop'])
        workPop.append(i['workPop'])
        visitPop.append(i['visitPop'])
        totalCnt = totalCnt + 1
    df = pd.DataFrame([baseDate, city, emd, gender, ageGroup, resdPop, workPop, visitPop]).T
    df.columns = ['날짜', '시군구', '읍면동', '성별', '연령대', '거주인구', '근무인구', '방문자수']
    df = df.sort_values(by='날짜', ascending=True)
    allData.append(df)
    print('현재까지 데이터 개수: ', totalCnt)
dataCombine = pd.concat(allData, axis=0, ignore_index=True)
dataCombine.to_csv(fileName, encoding='utf-8-sig')
