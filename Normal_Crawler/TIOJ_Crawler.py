import requests, json
from requests import ConnectionError
from logger import logger

legal_status = ['AC', 'WA', 'CE', 'TLE', 'MLE']

def TIOJ_Crawler(UserID, ProblemID, WorkerNum):

    try:
        ProblemID = int(ProblemID)
    except:
        logger.error(f'[Worker {WorkerNum}] ProblemNum Not Exists.')
        logger.info(f'[Worker {WorkerNum}] #TIOJ{ProblemID} #{UserID} #NE')
        return 'NE'

    # ensure UserID is string
    if(not isinstance(UserID, str)):
        logger.error(f'[Worker {WorkerNum}] UserID should be string')
        logger.info(f'[Worker {WorkerNum}] #TIOJ{ProblemID} #{UserID} #NE')
        return 'NE'
    # ensure ProblemID is integer
    if(not isinstance(ProblemID, int)):
        logger.error(f'[Worker {WorkerNum}] ProblemNum should be integer')
        logger.info(f'[Worker {WorkerNum}] #TIOJ{ProblemID} #{UserID} #NE')
        return 'NE'

    logger.info(f'[Worker {WorkerNum}] #UserID: {UserID} #ProblemID: {ProblemID}')

    # Crawl Submissions
    URL = f'https://tioj.ck.tp.edu.tw/submissions.json?filter_username={UserID}&filter_problem={ProblemID}'
    try:
        Result = requests.get(URL)
    except ConnectionError:
        logger.error(f'[Worker {WorkerNum}] Cannot Connect to TIOJ API')
        logger.info(f'[Worker {WorkerNum}] #TIOJ{ProblemID} #{UserID} #NE')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    logger.info(f'[Worker {WorkerNum}] Successfully Get Submissions.')
    Submissions = json.loads(Result.text)

    # Get Status
    if(len(Submissions) == 0):
        logger.info(f'[Worker {WorkerNum}] Successfully Get Status. #TIOJ{ProblemID} #{UserID} #NE.')
        return 'NE'
    
    Submissions = sorted(Submissions, key=lambda s:s['id'])
    Status = Submissions[0]['result']
    for i in range(len(Submissions)):
        if(Submissions[i]['result'] == 'AC'):
            Status = 'AC'
            break

    if(Status not in legal_status):
        Status = 'OS'

    logger.info(f'[Worker {WorkerNum}] Successfully Get Status. #TIOJ{ProblemID} #{UserID} #{Status}.')

    return Status