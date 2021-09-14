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
            problem_id = data['problem_id']
            username = data['username']
            userID = data['userID']
            if(judge == 'uva'):
                res = UVa_Crawler(userID, problem_id, self.num)
            elif(judge == 'tioj'):
                res = TIOJ_Crawler(userID, problem_id, self.num)
            elif(judge == 'toj'):
                res = TOJ_Crawler(userID, problem_id, self.num)
            elif(judge == 'atcoder'):
                res = AtCoder_Crawler(userID, problem_id, self.num)
            elif(judge == 'codeforces'):
                res = Codeforces_Crawler(userID, problem_id, self.num)
            else:
                res = 'NE'
            
            self.lock.acquire()
            logger.info(f'[Worker {self.num}] Lock acquired by Worker {self.num}.')

            for problem in self.result['result'][scoreboard]:
                if(problem['problem_id'] == problem_id and problem['judge_name'] == judge):
                    for user in problem['users']:
                        if(user['username'] == username):
                            user['status'] = res
                            logger.info(f'[Worker {self.num}] Set result. Username: {username}, judge: {judge}, problem: {problem_id}, result: {res}')
                            break
                    break

            self.lock.release()
            logger.info(f'[Worker {self.num}] Lock released by Worker {self.num}.')

# run function receive two arguments: scoreboards and users
# scoreboards and users are both json type(or using dictionary type)
# in scoreboards, it accept multiple scoreboard requests
# in users, it contains all users config on website
def run(scoreboards, users, ThreadNum=10):
    Work_Queue = queue.Queue()
    result = {
        "result": {}
    }
    for scoreboard in scoreboards:
        result['result'][scoreboard] = []
        for problem in scoreboards[scoreboard]['problems']:
            judge = problem['judge_name']
            problem_id = problem['problem_id']
            result['result'][scoreboard].append({
                "problem_id": problem_id,
                "judge_name": judge,
                "users": [

                ]
            })
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
                result['result'][scoreboard][-1]['users'].append({
                    "username": user,
                    "status": "NE"
                })
                
    lock = threading.Lock()
    Workers = []
    
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
