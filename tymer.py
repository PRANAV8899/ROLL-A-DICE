import time

second=input("Enter the time in seconds")

def countdown(second):
    mins=int(second / 60)
    secs=int(second % 60)

    timer=f'{mins}:{secs}'
    print(timer)
    second -= 1
    print('time up')

countdown(int(second))