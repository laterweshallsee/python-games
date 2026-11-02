import random

scorei = 0
scorek = 0

while True:
    print(input("press enter: "))
    i = random.randint(1, 6)
    k = random.randint(1, 6)
    if i > k:
        scorei = scorei + 1
        print('ti pobedil, ', i, k, 'score: tvoy ', scorei, 'moy', scorek)
    elif i < k:
        scorek = scorek + 1
        print('ti proebal, ', i, k, 'score: tvoy ', scorei, 'moy', scorek)
    else:
        print('nicya')
