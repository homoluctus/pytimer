import os
import sys
import time
import argparse
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
            nargs=1,
            metavar='H:M',
            dest='time',
            help='Specify local time and Notify when it comes to specific time',
        )

    return vars(parser.parse_args())

def alert(countdown):
    count = countdown['hour']*360 + countdown['minute']*60 + countdown['second']
    time.sleep(count)
    os.system("aplay ~/src/python/hobby/timer/music/Far_Away_Sting.wav &")

def main():
    countdown = parseArgs()
    alert(countdown)

if __name__ == '__main__':
    main()
