def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print('-------------------------------')

print_params(3, 'котик', False)
print_params(5)
print_params(b=7, c='гонка')
print_params()
print('-------------------------------')

print_params(b=25)
print_params(c=[1, 2, 3])
print('-------------------------------')

values_list = ['яблоко', False, 5]
values_dict = {'a' : True, 'b' : 18, 'c' : 'апельсин'}

print_params(*values_list)
print_params(**values_dict)
print('-------------------------------')

values_list2 = [55, 'море']
print_params(*values_list2, 42)