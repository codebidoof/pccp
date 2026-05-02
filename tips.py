# 파이썬 팁 모음집

# 리스트의 역순 탐색(인덱스 활용)
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, -1, -1): #시작, 끝, 증감폭
    print(arr[i], end = " ") # 5, 4, 3, 2, 1

#정렬 함수 sorted() -> sorted(iterable, key = 함수 : 정렬 기준, reverse 속성)
d = {'apple':3, 'banana':1, 'cherry':2}
d = sorted(d.items(), key=lambda x: x[1]) # 각 튜플에서 두번째 값을 기준으로 정렬
print(d) #[('banana', 1), ('cherry', 2), ('apple', 3)]

#split(구분자) : 문자열을 구분자 기준으로 나누어 리스트로 반환!!
s = "one two three four"
print(s.split(" ")) #결과 : ['one', 'two', 'three', 'four']

#조건 표현식 : <값1> if <조건> else <값2>
x = -5
result = x if x >= 0 else -x
print(result)  # 출력: 5

# math 모듈
# floor() - 내림
# ceil() - 올림
# sqrt() - 제곱근

# random 모듈
# random() - 0이상 1미만의 실수인 난수 생성
# randrange(시작 숫자, 끝 숫자) - 주어진 범위 안에서 정수인 난수 생성(끝 숫자 미포함)
# randint(시작 숫자, 끝 숫자) - 주어진 범위 안에서 정수인 난수 생성(끝 숫자 포함)
# shuffle(itrable) - 리스트의 요소를 무작위로 섞음. 반환값 x
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

#패킹 - 여러 개의 값을 하나의 변수에 튜플 형태로 묶는 것
solution = lambda *x : sum(x)
print(solution(1, 2, 3))        # 출력: 6
print(solution(10, 20, 30, 40)) # 출력: 100
print(solution())               # 출력: 0 (인자가 없으면 0)

def func(*args):
    return args
print(func(1, 2, 3), type(func(1, 2, 3))) # (1, 2, 3) <class 'tuple'>

a, b, c = 1, 2, 3
packed = a, b, c
print(type(packed)) #tuple

#sum(iterable, start) - start는 합계에 더해질 초깃값, 디폴트는 0

#startswith() - 문자열이 어떤 접두사로 시작하는지 확인하는 메서드(bool 반환)
a = "Hello world"
print(a.startswith("Hell")) #true

# 리스트.reverse() -> 뒤집기

# 리스트 컴프리헨션 정리
numbers = [x for x in range(5)]
print(numbers) # [0, 1, 2, 3, 4]

cartesian_product = [(x, y) for x in range(2) for y in range(3)]
print(cartesian_product) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

def square(x): 
    return x*x
squares = [square(x) for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]

even_numbers = [x for x in range(5) if x%2==0]
print(even_numbers) # [0, 2, 4]

squares = list(map(lambda x: x*x, range(5))) # map(함수, iterable 자료형) -> 원소에 함수를 하나씩 적용. 반환값이 map객체이므로 list()나 tuple()로 감싸야 함
print(squares) #[0, 1, 4, 9, 16]

numbers = [x if x%2==0 else -x for x in range(5)] #조건 표현식과 리스트 컴프리헨션의 조합
print(numbers) #[0, -1, 2, -3, 4]

# 행렬의 전치

#enumerate(iterable -> 반복문에서 인덱스와 값을 동시에 꺼낼 때!
def solution(wallpaper): #바탕화면 정리 문제
    x, y = [], [] 
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]