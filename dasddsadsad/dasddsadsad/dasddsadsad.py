total = 0
n=0

a=int(input("합을 알고십은 배수를 써주세요 :"))

for n in range(1, 100):
    if n % a == 0:
        total += n

print(a,"의 배수의 합은 =",total)