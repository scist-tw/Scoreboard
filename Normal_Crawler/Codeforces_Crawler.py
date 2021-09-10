import requests, json, hashlib, random, time
from requests import ConnectionError
from logger import logger

key = 'c26aa49d9515545ab7663b5ce4c69e9f5350d796'
secret = 'a710c2474ac88990799ac6e1c407c52727e7440d'

def Codeforces_Crawler(Handle, ProblemID):
    # ProblemID is combination of ContestID and index

    ProblemID = ProblemID.upper()
    
    # ensure Handle and ProblemID are string
    if(not isinstance(Handle, str)):
        logger.error('Handle should be string')
        return 'NE'
    if(not isinstance(ProblemID, str)):
        logger.error('ProblemID should be string')
        return 'NE'

    # Get Submission list
    rand = random.randint(100000, 999999)
    current_time = int(time.time())
    hashstr = hashlib.sha512(f"{rand}/user.status?apiKey={key}&handle={Handle}&time={current_time}#{secret}".encode()).hexdigest()
    URL = f'https://codeforces.com/api/user.status?apiKey={key}&handle={Handle}&time={current_time}&apiSig={rand}{hashstr}'

    try:
        Result = requests.get(URL)
    except ConnectionError:
        logger.error('Cannot Connect to Codeforces API.')
        return 'NE'
        # TODO: when connection failed, check at least three times.
    logger.info('Successfully Get Submissions.')
    Submissions = json.loads(Result.text)['result']

    # Get Status
    sub = []
    for i in Submissions:
        if(f"{i['problem']['contestId']}{i['problem']['index']}" == ProblemID):
            sub.append(i)

    sorted(sub, key=lambda s:s['id'])

    if(len(sub) == 0):
        logger.info(f'Successfully Get Status. #Codeforces{ProblemID} #{Handle} #NE.')
        return 'NE'

    StatusCode = sub[0]['verdict']
    for i in range(len(sub)):
        if(sub[i]['verdict'] == 'OK'):
            StatusCode = 'OK'
            break
    
    Status = 'OS'
    if(StatusCode == 'OK'):
        Status = 'AC'
    elif(StatusCode == 'COMPILATION_ERROR'):
        Status = 'CE'
    elif(StatusCode == 'RUNTIME_ERROR'):
        Status = 'RE'
    elif(StatusCode == 'WRONG_ANSWER'):
        Status = 'WA'
    elif(StatusCode == 'TIME_LIMIT_EXCEEDED'):
        Status = 'TLE'
    elif(StatusCode == 'MEMORY_LIMIT_EXCEEDED'):
        Status = 'MLE'
    
    logger.info(f'Successfully Get Status. #Codeforces{ProblemID} #{Handle} #{Status}.')
    return Status

if __name__ == '__main__':
    Codeforces_Crawler('Koios1143', '231C')