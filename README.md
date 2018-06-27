# Pytimer
pytimer is timer application

# Usage
## Alert when it comes to a specific time

positional arguments:
  H                     Notify in H hours
  M                     Notify in M minutes
  S                     Notify in S seconds

optional arguments:
  -h, --help            show this help message and exit
  -t H M, --time H M
                        Specify local time and Notify when it comes to
                        specific time (H:M)

# Example

## Alert in 2 seconds

```
python pytimer.py 0 0 2
```

## Alert at 12:30

```
python pytimer.py -t 12 30
```
