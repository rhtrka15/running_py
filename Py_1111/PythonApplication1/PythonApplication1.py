#s_i=input("태어난 해를 입력해주세요 :")
#b_y=int(s_i)%12

#if b_y == 0:
#    print("원숭이띠 입니다!")
#elif b_y ==1:
#    print("닭띠 입니다!")
#elif b_y ==2:
#    print("개띠 입니다!")
#elif b_y ==3:
#    print("돼지띠 입니다!")
#elif b_y ==4:
#    print("쥐띠 입니다!")
#elif b_y ==5:
#    print("소띠 입니다!")
#elif b_y ==6:
#    print("범(호랑이)띠 입니다!")
#elif b_y ==7:
#    print("토끼띠 입니다!")
#elif b_y ==8:
#    print("용띠 입니다!")
#elif b_y ==9:
#    print("뱀띠 입니다!")
#elif b_y ==10:
#    print("말띠 입니다!")
#elif b_y ==11:
#    print("양띠 입니다!")

#st="hello"

#st.upper()
#print("A지점:",st)

#print("B지점:",st.upper())

f=int(input("첫 번째 정수:"))

s=int(input("두 번째 정수:"))

if f>s:
    print("큰수는 ",f)
else:
    print("큰수는 ",s)

str=input("문자열을 입력하시오 :")

if len(str) % 2:
    print(str[len(str)//2])
else:
    print(str[(len(str)//2 -1) : len(str)//2+1])

import random

r=random.randint(1,100)
print("숫자 게임에 오신 것을 환영합니다!")

f=int(input("숫자를 맞춰보세요!:"))

if f>r:
    print("숫자가 작습니다!")
elif f<r:
    print("숫자가 큽니다!")
elif f==r:
    print("****맞추셧 습니다! 축하드려요!****")



user = input("가위, 바위, 보 중 하나를 고르세요. ")

com = random.randint(1, 3)


if com==1:
    computer="가위"
elif com==2:
    computer="바위"
elif com==3:
    computer="보"

if (user=='가위' and com == 3 ) or (user=='바위' and com ==1) or (user== '보' and com ==2) :
    print("사용자:",user,"컴퓨터",computer)
    print("user가 승리하셨습니다!!")
elif (user=='가위' and com==1) or (user=='바위' and com==2) or (user=='보' and com==3) :
    print("사용자:",user,"컴퓨터",computer)
    print("비겼습니다!")
else :
    print("사용자:",user,",컴퓨터",computer)
    print("user가 졌습니다..")


s=int(input("도형을 선택하시오(사각형:1  삼각형:2  원:3"))

if s==1:
    h=int(input("세로: "))
    w=int(input("가로: "))
    print("면적 =", h*w)
elif s==2:
    h=int(input("세로: "))
    w=int(input("가로: "))
    print("면적 =",h*w/2)
elif s==3:
    h=int(input("반지름: "))
    print("면적 =",(h*2)*3.141592)
