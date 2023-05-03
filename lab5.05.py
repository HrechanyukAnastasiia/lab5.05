def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s1 = input('Введіть рядок англ.мовою:')
print('Кількість голосних літерів:', count_vowels(s1))
