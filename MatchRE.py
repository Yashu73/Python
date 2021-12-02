import re
print("Using pattern for name")
pattern = '^Y.......i$'
test_string = 'Yashashri'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")


print("using pattern for group name")



list = ["Yashashri Chafekar" , "Pune" , "ZealClg"]
for element in list:
  z=re.match("(Y\w+)\W(C\w+)" , element)
  if z:
      print((z.groups()))
