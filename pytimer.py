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

def countdown(hour, min, sec):
    # set the unit to seconds
    count = hour*360 + min*60 + sec
    time.sleep(count)

def timer(hour, min):
    current_hour = int(strftime("%H", localtime()))
    current_min = int(strftime("%M", localtime()))
    current_sec = int(strftime("%S", localtime()))

    rest_hour = hour - current_hour
    rest_min = min - current_min - 1
    rest_sec = 61 - current_sec

    if rest_hour < 0 or rest_min < 0:
        sys.exit("Error : Invalid time")

    countdown(rest_hour, rest_min, rest_sec)

def alert():
    # play music on background
    subprocess.run("aplay ~/src/python/hobby/timer/music/Far_Away_Sting.wav &", shell=True)

def main():
    count = parseArgs()
    if count['time'] is None:
        countdown(count['hour'], count['minute'], count['second'])
        alert()
    else:
        timer(count['time'][0], count['time'][1])
        alert()

if __name__ == '__main__':
    main()
