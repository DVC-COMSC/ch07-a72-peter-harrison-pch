
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

SUBSET = True

for i in range(len(num2)):
    if num2[i] not in num1:
        SUBSET = False
        break

if SUBSET == True:
    statement = "is"
else:
    statement = 'is not'

message = f"num2 {statement} a subset of num1"
print(message)
print(str(SUBSET))

# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
