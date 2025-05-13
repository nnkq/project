"""
File test_code_quality.py - Được thiết kế để kiểm tra các chỉ số:
- LOC (Lines of Code)
- Cyclomatic Complexity
- Code Duplication
- Cohesion
- Coupling
"""

import os
import sys
import json
from datetime import datetime
from collections import defaultdict, OrderedDict
import numpy as np
import pandas as pd  # Giả định thư viện này được cài đặt

# ===== Code trùng lặp có chủ đích =====
def duplicate_function_1():
    print("This is a duplicate function.")
    x = 5 + 10
    return x

def duplicate_function_2():
    print("This is a duplicate function.")
    y = 5 + 10
    return y

# ===== Lớp với cohesion thấp =====
class LowCohesionExample:
    def __init__(self):
        self.data = []
        self.config = {}
    
    def load_data(self, file_path):
        with open(file_path, 'r') as f:
            self.data = json.load(f)
    
    def save_data(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.data, f)
    
    def print_config(self):
        print(self.config)
    
    def connect_to_database(self):  # Phương thức không liên quan
        print("Connecting to DB...")
        return "db_connection"

# ===== Lớp với cohesion cao =====
class HighCohesionExample:
    def __init__(self):
        self.math_utils = MathUtils()
    
    def calculate_stats(self, numbers):
        return {
            'mean': self.math_utils.mean(numbers),
            'median': self.math_utils.median(numbers),
            'std_dev': self.math_utils.std_dev(numbers)
        }

# ===== Lớp tiện ích =====
class MathUtils:
    def mean(self, numbers):
        return sum(numbers) / len(numbers)
    
    def median(self, numbers):
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]
    
    def std_dev(self, numbers):
        avg = self.mean(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        return variance ** 0.5

# ===== Hàm với độ phức tạp cyclomatic cao =====
def complex_function(x, y, z):
    if x > 0:
        if y < 0:
            for i in range(10):
                if i % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
        elif y == 0:
            try:
                result = x / z
            except ZeroDivisionError:
                result = float('inf')
            return result
        else:
            while z > 0:
                z -= 1
                if z == 5:
                    break
    else:
        with open('temp.txt', 'w') as f:
            f.write(str(x))
    
    return None

# ===== Hàm dài với nhiều logic =====
def long_function():
    # Phần 1: Xử lý dữ liệu
    data = [random.randint(1, 100) for _ in range(100)]
    processed_data = []
    for num in data:
        if num % 2 == 0:
            processed_data.append(num * 2)
        else:
            processed_data.append(num ** 2)
    
    # Phần 2: Phân tích thống kê
    mean = sum(processed_data) / len(processed_data)
    variance = sum((x - mean) ** 2 for x in processed_data) / len(processed_data)
    
    # Phần 3: Xuất kết quả
    report = {
        'original_data': data,
        'processed_data': processed_data,
        'statistics': {
            'mean': mean,
            'variance': variance,
            'std_dev': variance ** 0.5
        }
    }
    
    # Phần 4: Ghi file (trùng lặp với phương thức trong LowCohesionExample)
    with open('report.json', 'w') as f:
        json.dump(report, f)
    
    return report

# ===== Code trùng lặp thêm =====
def another_duplicate():
    print("This is another duplicate.")
    x = 10 + 20
    return x

def yet_another_duplicate():
    print("This is another duplicate.")
    y = 10 + 20
    return y

# ===== Main execution =====
if __name__ == "__main__":
    # Tạo đối tượng để test cohesion/coupling
    low_cohesion = LowCohesionExample()
    high_cohesion = HighCohesionExample()
    
    # Test hàm phức tạp
    result = complex_function(10, -5, 3)
    print(f"Result of complex function: {result}")
    
    # Test hàm dài
    report = long_function()
    print(f"Report generated with {len(report['original_data'])} items")
    
    # Gọi các hàm trùng lặp
    duplicate_function_1()
    duplicate_function_2()
    another_duplicate()
    yet_another_duplicate()