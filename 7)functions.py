def area(b,h,shape_type='triangle'):
    if shape_type == 'triangle':
     area = 0.5*b*h
    elif shape_type =='rectangle':
     area = b*h
    return area

n=area(10,5)
print(n)


def pattern(n=5):
  n = int(input('Enter any number'))
  for i in range(n):
    print('*'*(i+1))


j=pattern()
print()