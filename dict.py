

phonbook = {
    "치킨집":"02-000-0000",
    "피자집":"062-123-4567"
}

# print(phonbook["치킨집"])



btob = { 
    "서은광":29,
    "이민혁":29,
    "이창섭":28,
    "임현식":27,
    "프니엘":26,
    "정일훈":25,
    "육성재":24,
    }
    
bts = {
    "랩몬":25,
    "슈가":24,
    "진":25,
    "제이홉":23,
    "지민":22,
    "뷔":25,
    "정국":27,
}    

idol ={
    "btob":btob,
    "bts":bts
}

# print(idol)
# print(idol["bts"]["진"])

score ={
    "수학":50,
    "국어":70,
    "영어":100,
}
for key, value in score.items():
    pass
    # print(key)
    # print(value)
    
    
for key in score.keys():
    pass
    #  print(key)
     
for value in score.values():
    pass
    # print(value)    
    
score_sum = 0
for value in score.values():
    score_sum = score_sum + value
    pass
# print(score_sum/3)    


ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}


print(len(ssafy ["location"]))
#keys()
#values()
#items()<-선생님이 알려주시거
if "requests" in ssafy ["language"]["python"]["python standard library"]:
    print("true")
else:
    print("false")


print(ssafy ["classes"] ["gj1"] ["class president"])

print("language")

