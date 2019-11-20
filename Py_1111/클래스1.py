_str=input("문자열을 입력하시오 :")

alphas=0
digits=0
spaces=0

for c in _str:
   if c.isalpha(): #isalpha함수 사용해서 알파벳 개수 확인
      alphas=alphas+1
   if c.isdigit(): #isdigit함수 사용해서 숫자 개수 확인
      digits=digits+1
   if c.isspace(): #isspace함수 사용해서 공백 개수 확인
      spaces=spaces+1
print("알파벳 문자의 개수=",alphas)
print("숫자 문자의 개수=",digits)
print("스페이스의 개수=",spaces)