res=0
for num in range(1,101):
    res+=num

print(res)

response=int(input("ingrese un numero"))

for num in range(1,11):
    print(f"{num} x {response} = {num*response}")