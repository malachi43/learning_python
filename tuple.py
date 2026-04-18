tup = 23,45,67,98,78
tup_2 = (45,65,77,55,37)
tupA = (2, "malachi",0.5)
tupB = (34,"uko",[5,4,3,2,1])
num1, name, decimalNum = tupA
var1,var2,var3 = tupB
testTup = (50,70,90)
x = testTup[0]
y = testTup[2]
print("x + y = ", x + y)
print(var1 in tupB, var1)
print(var2 in tupB, var2)
print(var3 in tupB,var3)

tupB[2][3] = 7
print("var3: ", var3)
print(type(tup))
print("tup: ", tup)
print("tup_2: ", tup_2)
print("min: ", min(tup))
print("max: ", max(tup))
print("sum - tup: ", sum(tup))
print("sum - tup_2: ", sum(tup_2))
print("len - tup: ", len(tup),"\nlen - tup_2: ", len(tup_2))
print("num1: ", num1)
print("name: ", name)
print("decimalNum: ", decimalNum)
