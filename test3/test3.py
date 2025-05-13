import os
import sys

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, x):
        if x > 0:
            self.value += x
        else:
            self.value -= abs(x)
        return self.value
    
    def multiply(self, x):
        result = 1
        for i in range(x):
            result *= i
        return result

def example():
    try:
        with open('file.txt') as f:
            content = f.read()
    except:
        content = None
    return content