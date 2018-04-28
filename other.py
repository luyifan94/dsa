#计算器
import re
s = '1+2*3*3+4'
n = 23

operators = re.findall("[\+\*]", s)
calc_list = list(map(int, re.split("[\+\*]", s)))

res = None
for index,i in enumerate(calc_list):
    if res:
        if operators[index-1] == "+":
            res += i
        elif operators[index-1] == "*":
            res *= i
    else:
        res = i

for index,i in enumerate(operators):
    if i == '*':
        temp = calc_list[index]*calc_list[index+1]
        calc_list[index]=0
        calc_list[index+1]=temp
res2 = 0
for i in calc_list:
    res2 += i

ans = None
if n == res and n == res2:
    ans = 'U'
elif n==res:
    ans = 'L'
elif n==res2:
    ans = 'M'
elif n == res and n == res2:
    ans = 'U'
else:
    ans = 'I'
print(ans)