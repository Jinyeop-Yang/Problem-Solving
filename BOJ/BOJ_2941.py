"""
크로아티아 알파벳
"""
string = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for i in string:
    alpha = alpha.replace(i, '!')
print(len(alpha))
