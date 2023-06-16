import numbers

nums = []

for one in range(1,21):
    for two in range(1,21):
        if one > two:
            nums.append(one)
        else:
            nums.append(two)

'''
data = open('D&D/R&D/adv.txt', mode='at')
#data.write(nums)
length = len(nums)
for i in range(length):
    data.write(f'{str(nums[i])}\n')
data.close()
'''

length = len(nums)

count = []

d20 = []
for num in range(1,21):
    d20.append(num)
    count.append(0)

for index in range(length):
    x = nums[index]
    count[x-1] += 1


total = sum(count)
print(total)

percent = []

for x in range(20):
    val = count[x]
    p = val / total * 100
    p = round(p,2)
    percent.append(p)


cumulative = []
for x in range(0,20):
    sum = 0
    for i in range(x,20):
        sum += percent[i]
    cumulative.append(sum)

data = open('D&D/R&D/data.txt', mode='wt')
data.write('number,count,percent,cumulative\n')
for i in range (20):
    data.write(f'{i+1},{count[i]},{percent[i]},{cumulative[i]}\n')
data.close()