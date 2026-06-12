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