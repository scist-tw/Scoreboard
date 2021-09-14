import threading, queue
from threading import Thread
from AtCoder_Crawler import AtCoder_Crawler
from Codeforces_Crawler import Codeforces_Crawler
from TIOJ_Crawler import TIOJ_Crawler
from TOJ_Crawler import TOJ_Crawler
from UVa_Crawler import UVa_Crawler
from logger import logger

class Crawler(Thread):
    def __init__(self, queue, num, lock, result):
        Thread.__init__(self)
        self.queue = queue
        self.num = num
        self.lock = lock
        self.result = result
    

    def run(self):
        while self.queue.qsize() > 0:
            data = self.queue.get()
            scoreboard = data['scoreboard']
            judge = data['judge']
            problem = data['problem_id']
            username = data['username']
            userID = data['userID']
            if(judge == 'uva'):
                res = UVa_Crawler(userID, problem)
            elif(judge == 'tioj'):
                res = TIOJ_Crawler(userID, problem)
            elif(judge == 'toj'):
                res = TOJ_Crawler(userID, problem)
            elif(judge == 'atcoder'):
                res = AtCoder_Crawler(userID, problem)
            elif(judge == 'codeforces'):
                res = Codeforces_Crawler(userID, problem)
            else:
                res = 'NE'
            
            self.lock.acquire()
            logger.info(f'Lock acquired by Worker {self.num}.')

            try:
                self.result[scoreboard]
            except:
                self.result[scoreboard] = {}

            try:
                self.result[scoreboard][username]
            except:
                self.result[scoreboard][username] = {}

            self.result[scoreboard][username][f'[{judge}]{problem}'] = res
            logger.info(f'Set result. Username: {username}, judge: {judge}, problem: {problem}, result: {res}')

            self.lock.release()
            logger.info(f'Lock released by Worker {self.num}.')

# run function receive two arguments: scoreboards and users
# scoreboards and users are both json type(or using dictionary type)
# in scoreboards, it accept multiple scoreboard requests
# in users, it contains all users config on website
def run(scoreboards, users, ThreadNum=10):
    Work_Queue = queue.Queue()
    for scoreboard in scoreboards:
        for problem in scoreboards[scoreboard]['problems']:
            judge = problem['judge_name']
            problem_id = problem['problem_id']
            for user in scoreboards[scoreboard]['users']:
                try:
                    UserID = users[user][judge]
                except:
                    UserID = None
                Work_Queue.put({
                    'scoreboard': scoreboard,
                    'judge': judge,
                    'problem_id': problem_id,
                    'username': user,
                    'userID': UserID
                })
    lock = threading.Lock()
    Workers = []
    result = {}
    
    for i in range(ThreadNum):
        Workers.append(Crawler(Work_Queue, i, lock, result))
    
    for i in range(ThreadNum):
        logger.info(f'Start Worker {i}')
        Workers[i].start()
    
    for i in range(ThreadNum):
        Workers[i].join()
        logger.info(f'Worker {i} Done.')
    
    logger.info('All Workers Done.')

    return result

if __name__ == '__main__':
    import json
    scoreboards = json.loads(open('data/scoreboards.json').read().encode())
    users = json.loads(open('data/users.json').read().encode())
    print(run(scoreboards, users, 15))
