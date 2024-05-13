d = {
    1 : ['a', 'b'],
    2 : ['c', 'd']
}

print(''.join(i for j in list(d.values()) for i in j))
print(list(d.values()))
# print(map({print('test')},*d.values()))
# print(''.join(*d.values()))