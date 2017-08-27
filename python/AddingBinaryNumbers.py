
a = "01"
b = "11"

c = bin(10) + bin(11)
print(type(bin(20)))
print(c)

print(int(b,2))


# def add(a,b):
#     ans = int(a,2) + int(b,2)
#     return (bin(ans)).replace("0b",'')

# print(add('111','10'))


def binary_string_to_int(string):
    return sum((d == '1') * 2**i for i, d in enumerate(string[::-1]))

def add(a, b):
    return '{:b}'.format(binary_string_to_int(a) + binary_string_to_int(b))

print(add('111','10'))
d = 22
print('{0} is {1:b}'.format(d,3))

str1 = "hello"
for k,v in enumerate(str1):
	print(k,v)