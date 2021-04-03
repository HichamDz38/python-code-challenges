from playsound import playsound
import time


def play(timing, file, message):
    """my solution without seeing the instructor solution"""
    time.sleep(timing)
    playsound(file)
    print(message)
    input("enter any key to exit")
    return True


# test
print(play.__doc__)
play(1, 'simple.wav', "work_time")
