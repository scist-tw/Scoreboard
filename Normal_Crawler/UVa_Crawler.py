import requests, json
from requests import ConnectionError
from logger import logger

def UVa_Crawler(UserID, ProblemNum):
    # We Usually user ProblemNum to identify a problem, but Uhunt API use ProblemID instead
    # Therefore, we receive ProblemNum, then transform it into ProblemID to search

    try:
        UserID = int(UserID)
    except:
        logger.error('UserID Not Exists.')
        return 'NE'

    try:
        ProblemNum = int(ProblemNum)
    except:
        logger.error('ProblemNum Not Exists.')
        return 'NE'

    # ensure UserID and ProblemNum are integer
    if(not isinstance(UserID, int)):
        logger.error('UserID should be integer.')
        return 'NE'
    if(not isinstance(ProblemNum, int)):
        logger.error('ProblemNum should be integer.')
        return 'NE'
        
    logger.info(f'#UserID: {UserID} #ProblemNum: {ProblemNum}.')

    # Get ProblemID
    ProblemList_URL = f"https://uhunt.onlinejudge.org/api/p/num/{ProblemNum}"
    try:
        logger.info('Fetching ProblemID ...')
        Result = requests.get(ProblemList_URL)
    except ConnectionError:
        logger.error('Cannot Connect to uhunt API')
        return 'NE'

    try:
        ProblemID = json.loads(Result.text)['pid']
    except:
        logger.warning(f'Invalid ProblemNum: {ProblemNum}.')
        return 'NE'
    
    logger.info(f'Successfully Get ProblemNum {ProblemNum}\'s  ProblemID: {ProblemID}.')

    # Crawl Submissions
    URL = f"https://uhunt.onlinejudge.org/api/subs-pids/{UserID}/{ProblemID}/999999"
    try:
        logger.info('Fetching Submissions ...')
        Result = requests.get(URL)
    except ConnectionError:
        logger.error('Cannot Connect to uhunt API')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    logger.info('Successfully Get Submissions.')
    Submissions = json.loads(Result.text)[str(UserID)]['subs']

    '''
    | --------------------- Submission Mean --------------------- |
    | 0. Submission ID                                            |
    | 1. Problem ID                                               |
    | 2. Verdict ID                                               |
    | 3. Runtime                                                  |
    | 4. Submission Time (unix timestamp)                         |
    | 5. Language ID (1=ANSI C, 2=Java, 3=C++, 4=Pascal, 5=C++11) |
    | 6. Submission Rank                                          |
    '''

    # Get Status

    if(len(Submissions) == 0):
        logger.info(f'Successfully Get Status. #UVa{ProblemNum} #{UserID} #NE.')
        return "NE"
    
    Submissions = sorted(Submissions, key=lambda s:s[4])
    StatusCode = Submissions[0][2]
    for i in range(len(Submissions)):
        if(Submissions[i][2] == 90):
            StatusCode = 90
            break

    Status = 'OS'
    if(StatusCode == 90):
        Status = 'AC'
    elif(StatusCode == 70):
        Status = 'WA'
    elif(StatusCode == 30):
        Status = 'CE'
    elif(StatusCode == 40):
        Status = 'RE'
    elif(StatusCode == 50):
        Status = 'TLE'
    elif(StatusCode == 60):
        Status = 'MLE'

    logger.info(f'Successfully Get Status. #UVa{ProblemNum} #{UserID} #{Status}.')

    return Status