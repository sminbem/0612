user = {
    "name": "홍길동",
    "age": 25,
    "skills": ["Python", "Git"]
}
user["name"] = "김철수"
print(user["name"],"은 나이가", user["age"], "살입니다")

mart = {
    "apple": 1000,   # 키: "apple", 값: 1000
    "banana": 2500,  
    "orange": 1500
}
mart["apple"] = 5000
print("사과의 가격은", mart["apple"], "원입니다")

print(mart.keys()   )  # 키 목록 출력
print(mart.values() )  # 값 목록 출력
print(mart.items()  )  # 키-값 쌍(튜플) 목록 출력 
for fruit, price in mart.items():
    print(f"{fruit}의 가격은 {price}원입니다")

for key in mart.keys():
    print(f"mart 딕셔너리의 key값은 {key}가 있습니다")
mart2 = {"apple": 1000, "banana": 2500}

print("apple" in mart2)  # True
print("grape" in mart2)  # False

my_tuple = (1, 2, 3)
another_tuple = 10, 20, 30 # 튜플은 괄호 없이도 생성할 수 있습니다(수정 불가)


my_list = [1, 2, 3]
my_list[0] = 99  # 리스트는 변경 가능

# 리스트와 튜플의 차이점은 리스트는 변경 가능하지만 튜플은 변경 불가능하다는 것입니다.

numbers = (0, 1, 2, 3, 4, 5)
print(numbers[0])  # 0

a = (1, 2)
b = (3, 4)

print(a + b)  # (1, 2, 3, 4)
print(a * 3)  # (1, 2, 1, 2, 1, 2)

# 패킹
info = ("홍길동", 25, "서울")
# 언패킹
name, age, city = info
print(name)  # 홍길동
print(age)   # 25
print(city)  # 서울

x = 10
y = 20

#두 값을 서로 바꾸기 (튜플 언패킹 활용)
x, y = y, x

print(x)  # 20
print(y)  # 10

smaple = (1, 2, 3, 2, 4, 2)
print(smaple.count(2))
print(smaple.index(3))