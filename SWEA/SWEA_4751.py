"""
다솔이의 다이아몬드 장식
"""
T = int(input())

for tc in range(T):
    string = input()
    l = len(string)
    a = ['..#.'*l + '.', '.#.#'*l+'.', list('#.!.'*l+'#'), '.#.#'*l+'.', '..#.'*l+'.']
    idx = 0
    
    for i in range(2, l*4, 4):
        a[2][i] = string[idx]
        idx += 1

    for i in range(5):
        print(''.join(a[i]))