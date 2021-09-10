import requests, json
from requests import ConnectionError
from logger import logger

legal_status = ['AC', 'WA', 'CE', 'TLE', 'MLE']

def TIOJ_Crawler(UserID, ProblemID):

    # ensure UserID is string
    if(not isinstance(UserID, str)):
        logger.error('UserID should be string')
        return 'NE'
    # ensure ProblemID is integer
    if(not isinstance(ProblemID, int)):
        logger.error('ProblemNum should be integer')
        return 'NE'

    logger.info(f'#UserID: {UserID} #ProblemID: {ProblemID}')

    # Crawl Submissions
    URL = f'https://tioj.ck.tp.edu.tw/submissions.json?filter_username={UserID}&filter_problem={ProblemID}'
    try:
        Result = requests.get(URL)
    except ConnectionError:
        logger.error('Cannot Connect to TIOJ API')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    logger.info('Successfully Get Submissions.')
    Submissions = json.loads(Result.text)

    # Get Status
    if(len(Submissions) == 0):
        logger.info(f'Successfully Get Status. #TIOJ{ProblemID} #{UserID} #NE.')
        return 'NE'
    
    Submissions = sorted(Submissions, key=lambda s:s['id'])
    Status = Submissions[0]['result']
    for i in range(len(Submissions)):
        if(Submissions[i]['result'] == 'AC'):
            Status = 'AC'
            break

    if(Status not in legal_status):
        Status = 'OS'

    logger.info(f'Successfully Get Status. #TIOJ{ProblemID} #{UserID} #{Status}.')

    return Status