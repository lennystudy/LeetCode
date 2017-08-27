#哎呀 其实确实左移就好了 想的方向搞错了

def ip_to_int32(ip):
  # your code here
  ips = ip.split('.')
  str1 = ""
  for x in ips:
  	str1 = str1 + str(bin(int(x)))
  str1 = str1.replace('0b', '')

  ans = 0
  for x in range(0,len(str1)):
  	if str1[x] == "1":
  		ans = ans + 2 ** (len(str1) - x - 1) 
  return ans

# print(dir("22"))

print(type(ip_to_int32("112.35.25.35")))

print(ip_to_int32("128.32.10.1"))

dd = ip_to_int32("252.35.25.35")
#d = dd.replace("0b", "")
#print("dd" + dd)

print(int("0b11",2))

str3 = "234"
print(str3[::-1])



# print(len(ip_to_int32("112.35.25.35")))
