import time

def getTs()->str:
    t=time.time()
    timestamp=int(t)
    result=time.strftime("%Y%m%dT%H%M%S", time.localtime(timestamp))
    return result