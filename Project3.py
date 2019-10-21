# Система распознования пароля, введеного пользователем
password=int(input())
s = 0
while s < password:
    s = s + 1
a = [password, s]
for i in a:
    print(i)
if s == password:
    print('Пароль подобран верно')
else:
    print('Пароль подобран не верно, система ошиблась!')