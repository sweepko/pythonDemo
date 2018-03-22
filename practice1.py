# print(ord("a")) 转换为字符对应的acii码
# print(chr(45))转换为字符

# print('率为朋'.encode("utf-8"))
# print('hello,%s'% 'sweep') %占位符
# print('hello,{0},asas{1:.2f}'.format('sweep',1.343))
#
# a=10
# b=12
# a=a^b
# b=a^b
# a=a^b
# print(a,'|',b)
# birth=input('birth:')
# print(birth)
# d={'sweep':12,"swp":23,"shaui":45}
# print(d['sweep'])
# print('ll' in d) boolean
# print(d.pop('swp'))
# print(d)
#杨辉三角
# def triangles():
#     l=[1]
#     while True:
#         yield l
#         l.append(0)
#         l=[l[i-1]+l[i] for i in range(len(l))]
# n=0
# for t in triangles():
#     print(t)
#     n=n+1
#     if n==10:
#         break


def normalize(name):
   name=name[0].upper()+name[1:].lower()
   return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)




