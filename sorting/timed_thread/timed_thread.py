



def startTimer():
    global timerStart
    timerStart = start_time = time.time()

def setTimeElapsed():
    global timeElapsed
    global timerStart
    timeElapsed = time.time() - timerStart

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
