s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# utilizando os operadores + e *, crie as saídas:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod batbatcod'

print(s1 + ' ' + s2 + ' ' + s3)
print((s1 + ' ') * 10)
print(s1 + ' ' + (s2 + ' ') * 2 + (s3 + ' ')*3)
print((s1 + ' ' + s2 + ' ') * 7)
print(((s2 * 2 + s3)+ ' ') * 5)
