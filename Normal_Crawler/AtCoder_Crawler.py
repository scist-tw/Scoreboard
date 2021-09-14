import requests, json
from requests import ConnectionError
from logger import logger

legal_status = ['AC', 'WA', 'CE', 'TLE', 'MLE']

def AtCoder_Crawler(Username, ProblemID):

    logger.info(f'#Username: {Username} #ProblemID: {ProblemID}.')

    # ensure Username and ProblemID are string
    if(not isinstance(Username, str)):
        logger.error('Username should be string.')
        return 'NE'
    if(not isinstance(ProblemID, str)):
        logger.error('ProblemID should be string.')
        return 'NE'

    # Get Submission list
    URL = f'https://kenkoooo.com/atcoder/atcoder-api/results?user={Username}'
    try:
        logger.info('Fetching Submissions ...')
        Result = requests.get(URL)
    except ConnectionError:
        logger.error('Cannot Connect to AtCoder API.')
        return 'NE'
    logger.info(f'Successfully Get Submission list.')
    submissions = json.loads(Result.text)

    # Get specify submission list
    sub = []
    for i in submissions:
        if(i['problem_id'] == ProblemID):
            sub.append(i)
    sorted(sub, key=lambda s:s['id'])

    # Get Status
    if(len(sub) == 0):
        logger.info(f'Successfully Get Status. #AtCoder{ProblemID} #{Username} #NE.')
        return 'NE'

    Status = sub[0]['result']
    for i in range(len(sub)):
        if(sub[i]['result'] == 'AC'):
            Status = 'AC'

    if(Status not in legal_status):
        Status = 'OS'
    
    logger.info(f'Successfully Get Status #AtCoder{ProblemID} #{Username} #{Status}')
    return Status