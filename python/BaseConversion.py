#任意进制转换的通法
def convert(input, source, target):
    """BEGIN"""
    source_len = len(source)
    target_len = len(target)
    input_len = len(input)
    temp_len = input_len
    oct_sum = 0
    #计算对应的十进制数值
    for x in range(0,input_len):
        index = source.index(input[x])
        temp_len = temp_len - 1
        oct_sum += index ** temp_len
    return temp_len

oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(oct.index('3'))

print(convert("2361",oct,oct))