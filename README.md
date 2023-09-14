# Decimal to Base-X Converter 
A python script to convert decimal (base-10) integers and floats to their base-x equivalent.

## Requirements
* [Python 3.11](https://www.python.org/)

## Running Instructions
This program can be run with the following command: `./main.py [args]` in which args is a non-zero base number and a non-zero amount of real numbers. The real-numbers input is limited to -1 (exclusive) to 1 (exclusive). 

If this program is run without any arguments, the following usage error message will be outputted:
`usage: ./main.py [-h] base numbers [numbers ...]`

Invalid input will not be checked for and will result in undefined behavior.

## Sample Execution & Output
When this program is run with `./main.py 2 0.25 -0.142857 0.75 0.8`, the following output will be created:

```
|   Base 10   |    Base 2   | 
| ----------- | ----------- |
|     0.25    |     0.01    |
|  -0.142857  | -0.00100100 |
|     0.75    |     0.11    |
|     0.8     |  0.11001100 |
```

When this program is run with `./main.py 60 0.25 -0.142857 0.75 0.8`, the following output will be created:

```
|   Base 10   |   Base 60   | 
| ----------- | ----------- |
|     0.25    |     0.15    |
|  -0.142857  |   -0.83417  |
|     .75     |     0.45    |
|     0.8     |     0.48    |
```
