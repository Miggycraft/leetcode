s = "1211"
output = ""
ptr = s[0]
count = 0
for i in s:
    if ptr == i:
        #keep up
        count += 1
    else:
        # new pointer
        output += str(count) + ptr
        count = 1
        ptr = i
output += str(count) + ptr
#     # x[i] = x[i] + 1 if i in x else 1
# for j in x:
#     output += str(x[j])+j
print(output)