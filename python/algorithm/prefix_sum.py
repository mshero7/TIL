a = [10,20,30,40,50];

sum = 0;
prefix_sum = [0];

for item in a :
    sum += item
    prefix_sum.append(sum)

print(prefix_sum)

left = 3
right = 4
print(prefix_sum[4] - prefix_sum[2]);