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

#f=int(input("첫 번째 정수:"))

#s=int(input("두 번째 정수:"))

#if f>s:
#    print("큰수는 ",f)
#else:
#    print("큰수는 ",s)

str=input("문자열을 입력하시오 :")

if len(str) % 2:
    print(str[len(str)//2])
else:
    print(str[(len(str)//2 -1) : len(str)//2+1])


print("숫자 게임에 오신 것을 환영합니다!")

f=int(input("숫자를 맞춰보세요!:"))

