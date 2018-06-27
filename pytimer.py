import sys
import time
import argparse
import subprocess
from random import randint
from time import localtime, strftime
from pydub import AudioSegment

def parseArgs():
    parser = argparse.ArgumentParser(
        prog='pytimer',
        conflict_handler='resolve',
        description='Alert when it comes to a specific time',
    )

    parser.add_argument(
        'hour',
        type=int,
        nargs='?',
        metavar='H',
        help='Notify in H hours',
    )

    parser.add_argument(
        'minute',
        type=int,
        nargs='?',
        metavar='M',
        help='Notify in M minutes',
    )

    parser.add_argument(
        'second',
        type=int,
        nargs='?',
        metavar='S',
        help='Notify in S seconds',
    )

    parser.add_argument(
        '-t',
        '--time',
        type=int,
        nargs=2,
        metavar='H M',
        dest='time',
        help='Specify local time and Notify when it comes to specific time',
    )

    return vars(parser.parse_args())

class Pytimer:
    def __init__(self, count):
        if count['time'] is None:
            self.hour   = count['hour']
            self.min    = count['minute']
            self.sec    = count['second']
        else:
            self.hour   = count['time'][0]
            self.min    = count['time'][1]

    def setTime(self):
        current_hour    = int(strftime("%H", localtime()))
        current_min     = int(strftime("%M", localtime()))
        current_sec     = int(strftime("%S", localtime()))

        if self.hour < current_hour:
            self.hour = 24 - (current_hour - self.hour)
        else:
            self.hour -= current_hour

        if self.min < current_min:
            self.min = 60 - (current_min - self.min)
        elif self.min == current_min:
            self.min = 0
        else:
            self.min -= current_min + 1

        self.sec = 60 - current_sec
        print(self.hour, self.min, self.sec)

    def countdown(self):
        # set the unit to seconds
        count = self.hour * 360 + self.min * 60 + self.sec
        time.sleep(count)

    def alert(self):
        # play music on background
        sounds = [
            "Far_Away_Sting.wav",
            "Eyes_on_You_Sting.wav",
            "A_Long_Cold_Sting.wav",
        ]

        key = randint(0, len(sounds)-1)
        cmd = "aplay ~/src/python/hobby/timer/music/{} &".format(sounds[key])

        subprocess.run(cmd, shell=True)

if __name__ == '__main__':
    count   = parseArgs()
    pytimer = Pytimer(count)
    if count['time'] is not None:
        pytimer.setTime()
    pytimer.countdown()
    pytimer.alert()
