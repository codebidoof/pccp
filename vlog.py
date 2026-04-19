
# my_list = [1, 2, 4]

# # 값 추가
# my_list.append(6) # 맨 뒤에 원소 추가
# print(my_list, my_list[2]) # [1, 2, 4, 6] 4

# #인덱싱으로 값 삭제
# del my_list[2] # del은 인덱스 위치에 있는 원소를 지우는 키워드
# print(my_list) # [1, 2, 6]

my_list = [1, 2, 3, 4, 5]

print(my_list[0:2]) # [1, 2]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[3:4]) # [4]
print(my_list[-4:-2]) # [2, 3]

numbers = [x for x in range(5)]
print(numbers) # [0, 1, 2, 3, 4]

def square(X):
    return X*X

squares = [square(x) for x in range(5)]
print(squares)

# 조건문이 있는 리스트 컴프리헨션
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers) # [0, 2, 4]

numbers = [x if x % 2 == 0 else -x for x in range(5)]
print(numbers) # [0, -1, 2, -3, 4]

# map() 함수와 람다식의 조합
squares = list(map(lambda x: x*x, range(5)))
print(squares) # [0, 1, 4, 9, 16]

# 빈 셋 생성
empty_set = set()
print(empty_set) # set()

# 리스트를 셋으로 반환
list_to_set = set([1, 2, 3, 3, 2])
print(list_to_set) # {1, 2, 3}

# 중괄호를 이용한 셋 생성
set_from_braces = {12, 14, 1, 7}
print(set_from_braces) # {1, 12, 14, 7}

# 문자열을 셋으로 변환(중복 문자 제거)
strings_to_set = set("hello")
print(strings_to_set) # {'l', 'h', 'e', 'o'}(순서는 다를 수 있음)

#튜플을 셋으로 변환(중복 문자 제거)
tuple_to_set = set((1, 2, 3, 3))
print(tuple_to_set) # {1, 2, 3}

# 셋 컴프리헨션을 이용한 초기화
comprehension_set = {x for x in range(5) if x % 2 == 0}
print(comprehension_set) # {0, 2, 4}

# add() 메서드로 하나의 원소 추가
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 4}

# update() 메서드로 여러 원소 추가
my_set.update([5, 6])
print(my_set) # {1, 2, 3, 4, 5, 6}

# remove() 메서드로 특정 원소 제거(제거 대상 원소 없으면 오류 발생)
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set) # {1, 3, 4}

# my_set.remove(5) # KeyError: 5 발생

# discard 메서드로 특정 원소 제거(제거 대상 원소 없어도 오류 없음)
my_set.discard(3)
print(my_set) # {1, 4}

my_set.discard(5) # 오류 발생하지 않음
print(my_set) # {1, 4}

# 모든 원소 제거
my_set.clear()
print(my_set) # set()

# union() 메서드를 이용한 합집합
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 4, 5}

# | 연산자를 사용한 합집합(set1에 set2의 원소를 추가)
set1 |= set2
print(set1) # {1, 2, 3, 4, 5}

# interection() 메서드를 이용한 교집합
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set) # {3}

# & 연산자를 사용한 교집합(set1에 set2와의 교집합을 저장)
set1 &= set2
print(set1) # {3}

# difference() 메서드를 이용한 차집합
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set) # {1, 2}

# - 연산자를 이용한 차집합(set1에 set2와의 차집합을 저장)
set1 = {1, 2, 3}
set1 -= set2
print(set1) # {1, 2}

my_dict = { }

# 딕셔너리 값 삽입
my_dict["apple"] = 1
my_dict["banana"] = 2
my_dict["orange"] = 3

# 딕셔너리 값 출력
print(my_dict)  # {'apple': 1, 'banana': 2, 'orange': 3}

key = "apple"
if key in my_dict:
    value = my_dict[key]
    print(f"{key}: {value}") # apple: 1
else:
    print(f"{key}는 딕셔너리에 존재하지 않습니다.")

my_dict["banana"] = 4
print(my_dict) # {'apple': 1, 'banana': 4, 'orange': 3}

del my_dict["orange"]
print(my_dict) # {'apple': 1, 'banana': 4}

# 딕셔너리 생성
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# my_dict 에 없는 key로 설정
key = "kiwi"

# 키가 딕셔너리에 있는지 확인
if key in my_dict:
    # 키가 딕셔너리에 있으면 해당 값 출력
    print(f"값: {my_dict[key]}")
else:
    # 키가 딕셔너리에 없으면 에러 메세지 출력
    print(f"'{key}' 키가 딕셔너리에 없습니다.")

my_tuple = (1, 2, 3)

# 인덱싱
print(my_tuple[0]) # 1
print(my_tuple[1]) # 2
print(my_tuple[2]) # 3

# 슬라이싱
print(my_tuple[1:]) # (2, 3)
print(my_tuple[:2]) # (1, 2)
print(my_tuple[1:2]) # (2,)

string = "Hello, World" # 큰따옴표 사용
string2 = 'Hello, World!' #작은따옴표 사용

string = "He"
string += "llo"
print(string) # Hello

# 문자열을 리스트에 담아두고 한 번에 결합
string_list = ["He", "llo"]
result = "".join(string_list)
print(result) # Hello

string = "Hello"
string = string.replace("l", "") # "l"을 모두 삭제
print(string) # Heo

def total_price(quantity, price):
    total = quantity * price
    if total > 100: # total이 100보다 크면
        # 다양한 작업들
        return total * 0.9 # 조기 반환
    return total

print(total_price(4, 50))

def calculate_average(numbers):
    if numbers is None: # 값이 없으면 종료(예외)
        return None
    if not isinstance(numbers, list): # numbers가 리스트가 아니면 종료(예외)
        return None
    if len(numbers) == 0: # numbers의 길이가 0이면 종료
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

def add_three(x):
    return x + 3

def square(x):
    return x*x

composed_function = lambda x: square(add_three(x))
print(composed_function(3)) # (3+3)^2 = 36

def func(*args):
    return args
print(func(1, 2, 3), type(func(1, 2, 3))) #tuple