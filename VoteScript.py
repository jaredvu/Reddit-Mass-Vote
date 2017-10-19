# -------------------------------------------------------------#
# Reddit Mass Voting Tool                                      #
# Disclaimer:                                                  #
# This is a proof of concept and not recommended for use as it #
# violates the terms and services of Reddit.com                #
#--------------------------------------------------------------#

import praw
from secret import acc
    # acc is a list of accounts
    # [username,password,clientID,clientSecret]
from random import *
import time

#Parameters---------------------------------------#
#number of accounts voting
NUM = 20
#vote up or down
VOTE = 'up'
#id
IDnum = ''
#comment or submission
SUB = 'submission'
#-------------------------------------------------#

def createUA(n):
    platform = ['android','ios','windows','osx','linux']
    appID = 'com.example.myredditapp'
    a = randint(0,10)
    version ='v1.'+str(a)
    name='(by /u/'+acc[n][0]+')'
    b = randint(0,5)
    return '%s:%s:%s %s'%(platform[b],appID,version,name)

def massVote():
    for i in range(NUM):
        r = praw.Reddit(client_id=acc[i][2],
                        client_secret=acc[i][3],
                        user_agent=createUA(i),
                        username=acc[i][0],
                        password=acc[i][1])
        if SUB == 'submission':
            submission = r.submission(id=IDnum)
        elif SUB == 'comment':
            submission = r.comment(id=IDnum)
        if VOTE == 'up':
            submission.upvote()
        elif VOTE == 'down':
            submission.downvote()
        time.sleep(randint(3,10))

if __name__ == '__main__':
    massVote()