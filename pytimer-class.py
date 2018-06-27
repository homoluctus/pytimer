import sys
import time
import argparse
import subprocess
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

class Pytimer():
    def __init__(self, count):
        if count['time'] is None:
            self.hour   = count['hour']
            self.min    = count['minute']
            self.sec    = count['second']
        else:
            self.hour   = count['time'][0]
            self.min    = count['time'][1]
            self.sec    = 61

    def setTime(self):
        current_hour    = int(strftime("%H", localtime()))
        current_min     = int(strftime("%M", localtime()))
        current_sec     = int(strftime("%S", localtime()))

        rest_hour   = self.hour - current_hour
        rest_min    = self.min - current_min - 1
        rest_sec    = self.sec - current_sec

        if rest_hour < 0 or rest_min < 0:
            sys.exit("Error : Invalid time")

    def alert(self):
        # set the unit to seconds
        count = self.hour * 360 + self.min * 60 + self.sec
        time.sleep(count)
        # play music on background
        subprocess.run("aplay ~/src/python/hobby/timer/music/Far_Away_Sting.wav &", shell=True)

if __name__ == '__main__':
    count   = parseArgs()
    pytimer = Pytimer(count)
    if count['time'] is not None:
        pytimer.setTime()
    pytimer.alert()
