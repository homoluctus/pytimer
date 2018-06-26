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
            'count',
            type=int,
            metavar='N',
            help='Notify in N minutes',
        )

    parser.add_argument(
            '-h',
            '--hour',
            nargs=1,
            metavar='H',
            dest='hour',
            help='Notify in H hours',
        )

    parser.add_argument(
            '-m',
            '--minute',
            nargs=1,
            metavar='M',
            dest='minute',
            help='Notify in M minutes',
        )

    parser.add_argument(
            '-s',
            '--second',
            nargs=1,
            metavar='S',
            dest='second',
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
    time.sleep(countdown['count']*60)
    os.system("aplay ~/src/python/hobby/timer/music/Far_Away_Sting.wav")

def main():
    countdown = parseArgs()
    alert(countdown)

if __name__ == '__main__':
    main()
