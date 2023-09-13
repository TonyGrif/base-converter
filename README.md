# Decimal to Base-X Converter 
A python script to convert decimal (base-10) integers and floats to their base-x equivalent.

## Requirements
* [Python 3.11](https://www.python.org/)

## Running Instructions
This program can be run with the following command: `./main.py [args]` in which args is a non-zero amount of real numbers.  

If this program is run without any arguments, the following usage error message will be outputted:
`usage: ./main.py [-h] args [args ...]`

Invalid input will not be checked and will result in undefined behavior.

## Sample Execution & Output
When this program is run with `./main.py 0.25 -0.142857 0.75`, the following output will be created:

```
|   Base 10   |    Base 2   | 
| ----------- | ----------- |
|     0.25    |     0.01    |
|  -0.142857  | -0.00100100 |
|     0.75    |     0.11    |
```
