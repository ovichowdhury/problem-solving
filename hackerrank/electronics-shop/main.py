# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for keyboard in keyboards:
        for drive in drives:
            total_cost = keyboard + drive
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost
    return max_spent

# Example usage:
keyboards = [40, 50, 60]
drives = [5, 8, 12]
b = 60
print(getMoneySpent(keyboards, drives, b))  # Output: 58