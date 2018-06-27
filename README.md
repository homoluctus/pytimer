# Pytimer
Pytimer is timer application\
Alert when it comes to a specific time

# Usage

```
python pytimer.py [-h] [-t H M] [H] [M] [S]
```

positional arguments:\
&emsp;H :&emsp;Notify in H hours\
&emsp;M :&emsp;Notify in M minutes\
&emsp;S :&emsp;Notify in S seconds\

optional arguments:\
&emsp;-h, --help :&emsp;&emsp;&emsp;&emsp;&emsp;Show this help message and exit\
&emsp;-t H M, --time H M :&emsp;Specify local time and Notify when it comes to specific time (H:M)

# Example

## Alert in 2 seconds

```
python pytimer.py 0 0 2
```

## Alert at 12:30

```
python pytimer.py -t 12 30
```
