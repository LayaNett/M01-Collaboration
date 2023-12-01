"""Layla Nettavong
Python M06 programming assignment
 15.1
"""
import datetime
import time
import random
import multiprocessing as mp

def second1():

    #This will select a random number between 0and1
    waitTime = random.random()

    #This makes the program wait to print the current time
    currentTime = time.sleep(waitTime)

    #This all prints the current time
    currentTime = datetime.datetime.now().time()
    print(currentTime)

    exit()
def second2():

    #This will select a random number between 0and1
    waitTime = random.random()

    #This makes the program wait to print the current time
    currentTime = time.sleep(waitTime)

    #This all prints the current time
    currentTime = datetime.datetime.now().time()
    print(currentTime)

    exit()
def second3():

    #This will select a random number between 0and1
    waitTime = random.random()

    #This makes the program wait to print the current time
    currentTime = time.sleep(waitTime)

    #This all prints the current time
    currentTime = datetime.datetime.now().time()
    print(currentTime)

    exit()

if __name__ == '__main__':

    p = mp.Process(target= second1,)
    p.start()
   

    p2 = mp.Process(target= second2,)
    p2.start()
    

    p3 = mp.Process(target= second3,)
    p3.start()
 