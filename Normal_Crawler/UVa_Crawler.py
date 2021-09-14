import requests, json
from requests import ConnectionError
from logger import logger

def UVa_Crawler(UserID, ProblemNum, WorkerNum):
    # We Usually user ProblemNum to identify a problem, but Uhunt API use ProblemID instead
    # Therefore, we receive ProblemNum, then transform it into ProblemID to search

    try:
        UserID = int(UserID)
    except:
        logger.error(f'[Worker {WorkerNum}] UserID Not Exists.')
        logger.info(f'[Worker {WorkerNum}] #UVa{ProblemNum} #{UserID} #NE')
        return 'NE'

    try:
        ProblemNum = int(ProblemNum)
    except:
        logger.error(f'[Worker {WorkerNum}] ProblemNum Not Exists.')
        logger.info(f'[Worker {WorkerNum}] #UVa{ProblemNum} #{UserID} #NE')
        return 'NE'

    # ensure UserID and ProblemNum are integer
    if(not isinstance(UserID, int)):
        logger.error(f'[Worker {WorkerNum}] UserID should be integer.')
        logger.info(f'[Worker {WorkerNum}] #UVa{ProblemNum} #{UserID} #NE')
        return 'NE'
    if(not isinstance(ProblemNum, int)):
        logger.error(f'[Worker {WorkerNum}] ProblemNum should be integer.')
        logger.info(f'[Worker {WorkerNum}] #UVa{ProblemNum} #{UserID} #NE')
        return 'NE'
        
    logger.info(f'[Worker {WorkerNum}] #UserID: {UserID} #ProblemNum: {ProblemNum}.')

    # Get ProblemID
    ProblemList_URL = f"https://uhunt.onlinejudge.org/api/p/num/{ProblemNum}"
    try:
        logger.info(f'[Worker {WorkerNum}] Fetching ProblemID ...')
        Result = requests.get(ProblemList_URL)
    except ConnectionError:
        logger.error(f'[Worker {WorkerNum}] Cannot Connect to uhunt API')
        logger.info(f'[Worker {WorkerNum}] #UVa{ProblemNum} #{UserID} #NE')
        return 'NE'

    try:
        ProblemID = json.loads(Result.text)['pid']
    except:
        logger.warning(f'[Worker {WorkerNum}] Invalid ProblemNum: {ProblemNum}.')
        return 'NE'
    
    logger.info(f'[Worker {WorkerNum}] Successfully Get ProblemNum {ProblemNum}\'s  ProblemID: {ProblemID}.')

    # Crawl Submissions
    URL = f"https://uhunt.onlinejudge.org/api/subs-pids/{UserID}/{ProblemID}/999999"
    try:
        logger.info(f'[Worker {WorkerNum}] Fetching Submissions ...')
        Result = requests.get(URL)
    except ConnectionError:
        logger.error(f'[Worker {WorkerNum}] Cannot Connect to uhunt API')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    logger.info(f'[Worker {WorkerNum}] Successfully Get Submissions.')
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
        logger.info(f'[Worker {WorkerNum}] Successfully Get Status. #UVa{ProblemNum} #{UserID} #NE.')
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

    logger.info(f'[Worker {WorkerNum}] Successfully Get Status. #UVa{ProblemNum} #{UserID} #{Status}.')

    return Status