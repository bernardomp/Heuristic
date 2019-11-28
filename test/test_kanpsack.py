import pytest
import sys
from src.Knapsack import *


def test_hamming_distance_one():

    input = ['0', '1', '00','11','101','1101']
    result = [
        ['1'],
        ['0'],
        ['10','01'],
        ['01','10'],
        ['001','111','100'],
        ['0101','1001','1111','1100']
        ]

    
    
    for i in range(len(input)):
        knap = Knapsack(num_objects=len(input[i]))
        assert knap.hamming_distance_one(input[i]) == result[i]


def test_hamming_distance():

    tests = [
        ("111",2,set(['011','101','110','001','010','100']) ),
        ("0000",3, set(['1000','0100','0010','0001','1100','1010','1001','0110','0101','0011','1110','1101','1011','0111']))
    ]

   

    for test in tests:
        knap = Knapsack(num_objects=len(test[0]))
        assert knap.hamming_distance(test[0],test[1]) == test[2]
   
   
