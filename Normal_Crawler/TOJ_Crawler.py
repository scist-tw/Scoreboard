import requests, json
from requests import ConnectionError
from logger import logger
from bs4 import BeautifulSoup
from lxml import etree

def TOJ_Crawler(UserID, ProblemID):
    
    #ensure UserID and ProblemID are integer
    if(not isinstance(UserID, int)):
        logger.error('UserID should be int.')
        return 'NE'
    if(not isinstance(ProblemID, int)):
        logger.error('ProblemID should be int')
        return 'NE'
    
    # check if has AC submission
    URL = 'https://toj.tfcis.org/oj/be/api'
    data = {
        'acct_id' : UserID,
        'reqtype' : 'AC'
    }
    
    try:
        AC_list = requests.post(URL, data=data)
    except ConnectionError:
        logger.error('Cannot Connect to TOJ API.')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    
    print(AC_list.text)
    AC_list = json.loads(AC_list.text)['ac']
    if(ProblemID in AC_list):
        logger.info(f'Successfully Get Status. #TOJ{ProblemID} #{UserID} #AC.')
        return 'AC'
    
    # get last submission
    URL = f'http://210.70.137.215/oj/be/chal?proid={ProblemID}&acctid={UserID}'
    try:
        result = requests.get(URL)
    except ConnectionError:
        logger.error('Cannot Connect to TOJ.')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    soup = BeautifulSoup(result.text, 'html.parser')
    dom = etree.HTML(str(soup))
    try:
        StatusCode = dom.xpath('//*[@id="challist"]/tbody/tr[2]/td[4]')[0].text
    except IndexError:
        logger.info(f'Successfully Get Status. #TOJ{ProblemID} #{UserID} #NE.')
        return 'NE'
    
    Status = 'OS'
    if(StatusCode == 'Wrong Answer'):
        Status = 'WA'
    elif(StatusCode == 'Runtime Error'):
        Status = 'RE'
    elif(StatusCode == 'Time Limit Exceed'):
        Status = 'TLE'
    elif(StatusCode == 'Memory Limit Exceed'):
        Status = 'MLE'
    elif(StatusCode == 'Compile Error'):
        Status = 'CE'
    
    logger.info(f'Successfully Get Status. #TOJ{ProblemID} #{UserID} #{Status}.')
    return Status