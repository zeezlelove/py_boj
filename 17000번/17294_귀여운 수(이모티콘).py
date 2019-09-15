"""
문제
욱제는 귀여운 수~ε٩(๑> ₃ <)۶з를 좋아한다. 귀여운 수~ε٩(๑> ₃ <)۶з는 수를 이루는 각 자릿수가 등차수열[*]을 이루는 수이다. 당신은 욱제한테 귀여운 수~ε٩(๑> ₃ <)۶з 하나를 선물해주고 싶다. 수 하나가 주어졌을 때 이 수가 귀여운지 판단하는 프로그램을 짜 보자.



[*] 등차수열을 이루는 숫자들은, 왼쪽에서 오른쪽으로 가면서 일정한 크기(0일 수도 있음)만큼 커지거나 일정한 크기만큼 작아진다. 뭔지 모르겠으면 예제를 보고 알아보자. ㅋㅋ!

입력
정수 k(1≤k≤1018)가 주어진다. 입력은 0으로 시작하지 않는다.

출력
수가 귀여우면 "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"를, 귀엽지 않으면 "흥칫뿡!! <(￣ ﹌ ￣)>"를 따옴표 없이 출력한다.

예제 입력 1
630
예제 출력 1
◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!
예제 입력 2
631
예제 출력 2
흥칫뿡!! <(￣ ﹌ ￣)>
예제 입력 3
999999999999999999
예제 출력 3
◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!
예제 입력 4
1000000000000000000
예제 출력 4
흥칫뿡!! <(￣ ﹌ ￣)>
예제 입력 5
12
예제 출력 5
◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!
예제 입력 6
121
예제 출력 6
흥칫뿡!! <(￣ ﹌ ￣)>
예제 입력 7
7
예제 출력 7
◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!
예제 입력 8
13579
예제 출력 8
◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!
"""
def chk(a):
    a = [int(i) for i in a]
    li = []
    chk = False
    if len(a) <= 2:
        return True
    for i in range(len(a)):
        if i != len(a)-1:
            li.append(a[i+1]-a[i])
    for i in range(len(li)):
        if i != len(li)-1:
            if li[i] == li[i+1]:
                chk = True
            else:
                return False
    if chk == True:
        return True
if chk(list(input())) == True:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
