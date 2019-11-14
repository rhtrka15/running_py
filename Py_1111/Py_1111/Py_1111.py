#물건 값을 입력하고 낸 돈을 확인후 거스름 돈의 동전을 구분하는 프로그램

AB=int(input("물건 값을 입력하시오. :"))

t=int(input("1000원 지폐 개수 :"))

fh=int(input("500원 동전의 개수 :"))

h=int(input("100원 동전의 개수 :"))

_1000=t*1000

_500=fh*500

_100=h*100

rus=_1000+_500+_100

print("500원의 개수:"rus//500)

re=rus%500

print("100원의 개수"re//100)

bb=re%100

print("50원의 개수:"bb//50)#

#abcd의 연산후 a와 b의 크기를 구분하는 프로그램
a=10
b=20
c=30
d=40

a,b=b,a

a,b,c,d=d,c,b,a

print(a,b,c,d)

if(a>b):
    print("a가 b보다 큽니다.")
else:
    print("b가 a보다 큽니다.")

#import를 통해 tutle을 불러내어 조금한 게임을 구현하는 프로그램
import turtle
t=turtle,pen()

while True:
    direction=input("왼쪽=left, 오른쪽=right  :")
    if direction=="l":
        t.left(60)
        t.forward(50)
    if direction=="r":
        t.right(60)
        t.forward(50)

#while문을 이용한홀수와 짝수를 구별하는 프로그램
a=1
while a<10:
    b=int(input("정수를 입력해 주십시오 :"))
    c=b%2
    if c==1:
        print("홀수입니다.")
    else:
        print("짝수입니다.")
    a+=1

#구입 금액이 10만원 이상일때 할인이된 최종 가격을 말하고 이하면 그냥 가격을 출력하는 프로그램
A=int(input("구입 금액을 입력하시오 :"))

if A>100000:
    dis=A*0.05
    c=A-dis
print("할인 가격은"c"입니다.")


#학점과 평점을 계산하여 졸업의 유무를 구분하는 프로그램
to=int(input("이수한 학점수를 입력하십시오 :"))
pp=float(input("평점을 입력하십시오 :"))

if to>140 and pp>2.0:
    print("졸업이 가능합니다! ㅊㅊ")
else:
    print("졸업이 불가능 합니다..! ㅠㅠ")


#dateime 을 import 하여 현재의 시간 분 초를 나타내는 프로그램.
import datetime

now = datetime.datetime.now()

print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

#datetime 을 improt 하여 if문을 사용해 계절을 구분하는 프로그램
if 3<= now.month <=5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6<= now.month <=8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9<= now.month <=11:
     print("이번 달은 {}월로 가을입니다!".format(now.month))

if 12 or 1 <= now.month <=2:
     print("이번 달은 {}월로 겨울입니다!".format(now.month))

#from  random or import random                랜덤 사용법
#random=randint(1,100)   random.randint(0,2)  랜덤 사용법

