# Q1: Count the Digits That Divide a Number
'''
Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

'''
num = 121
counter = 0

list1 = list(str(num))
for i in range(len(list1)):
    if num % int(list1[i]) == 0:
        counter = counter + 1
print(counter)
# **************************Q1 : End *************************
