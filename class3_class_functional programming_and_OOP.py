r"""°°°
# Recap
- 파이썬의 기본 자료구조
    - int, float
    - boolean
    - string
    - list, dictionary, tuple
        - iterable, indexing
    - for, while
        - list comprehension
    - if statement
°°°"""
# |%%--%%| <Ywuzq8154e|zsloHauYyW>
r"""°°°
# Class and Object
- 클래스 
    - 파이썬에서 가장 이해하기 어려운 지점
    - 객체를 만드는 최소단위임
    - 클래스를 만드는 것을 추상화라고 한다. 

- 클래스 선언하는 법
    - 클래스 이름
    - 메서드
        - 특별 메서드
            - `__init__`,`__repr__`,`__str__`
            - `__add__`, `__sub__`, `__mul__`
        - 메서드
            - def (self) 형태로 정의하면 됨
°°°"""
# |%%--%%| <zsloHauYyW|aGK8GHWtXO>

class Person:
    
    # 클래스가 기본적으로 갖고 있는 정보
    age = 16
    gender = 'male'
    
    def my_age_is(self):
        print("my age is",self.age)
    

# |%%--%%| <aGK8GHWtXO|orAk1aCPZb>

# Person class 객체로 some_guy라는 인스턴스 객체를 생성

some_guy = Person()
some_guy.my_age_is()

# |%%--%%| <orAk1aCPZb|TlYjTPTK6V>

# 해당 클래스의 인스턴스인지 확인

isinstance(some_guy, Person)

# |%%--%%| <TlYjTPTK6V|y3GOOu9p0B>

class Person:
    
    def __init__(self):
        self.age = 16
        self.gender = 'male'
    
    def my_age_is(self):
        print("my ag is",self.age)

# |%%--%%| <y3GOOu9p0B|a6NXDJktMj>

class Calculator:
    
    def add_(self, a, b):
        '''
        sum a and b
        '''
        assert (a and b) is not (float or int), "a and b should be numeric"
        return a + b
    
    def subtract_(self, a, b):
        assert (a and b) is not (float or int), "a and b should be numeric"
        return abs(a - b)

# |%%--%%| <a6NXDJktMj|EKm6GEqPcK>

mycal = Calculator()

# |%%--%%| <EKm6GEqPcK|yyffT0oxRR>

mycal.add_(1,2)

# |%%--%%| <yyffT0oxRR|D5GTVO4BXp>

mycal.subtract_(1,2)

# |%%--%%| <D5GTVO4BXp|DWAgGchuhW>
r"""°°°
## Class에서 정의해줘야 하는 것
- `__init__` : 기본 정의해야 할 요소들이 정의됨
- `__len__` : 클래스 요소의 구성요소의 갯수를 반환
°°°"""
# |%%--%%| <DWAgGchuhW|K1Gakiev6w>
r"""°°°
# 상속
- 다른 클래스의 기능을 그대로 물려 받는 것을 말함
°°°"""
# |%%--%%| <K1Gakiev6w|S4XuAxEHm9>

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_age_is(self):
        print("my age is",self.age)

# |%%--%%| <S4XuAxEHm9|0ciUZGKu6H>

class SoccerPlayer(Person):
    
    def __init__(self, name, age, team, position):
        super().__init__(name, age)
        self.team = team
        self.position = position
        self.steps = 0 
        self.ball = False
    
    def front(self, steps, ball=False):
        self.steps += steps
        self.ball = ball
    
    def back(self, steps, ball=False):
        self.steps -= steps
        self.ball = ball
    
    def pass_to(self, to_whom):
        if self.ball :
            return True
        else : 
            return False
    
    def kick(self):
        if self.ball :
            return "score!!"
        
        else :
            return "failed"

# |%%--%%| <0ciUZGKu6H|U1DXRfJSjg>

son = SoccerPlayer('Son', 32, 'totenham', 'midfielder')

# |%%--%%| <U1DXRfJSjg|quCTIeSght>

son.front(10, True)

# |%%--%%| <quCTIeSght|fZejbQ301w>

son.kick()

# |%%--%%| <fZejbQ301w|j2oYYvoUxQ>
r"""°°°
## 메서드 오버라이딩
- 상속받은 클래스를 조금 수정해서 사용하고 싶을 때 사용하는 법
°°°"""
# |%%--%%| <j2oYYvoUxQ|Ma9mZBev4i>

class Person1(Person):
    def print_name(self):
        print("my name is",self.name)

# |%%--%%| <Ma9mZBev4i|sti0Oc5bu7>

mike = Person1("mike", 20)

mike.print_name(), mike.my_age_is()

# |%%--%%| <sti0Oc5bu7|t1OCIjwuJ4>
r"""°°°
# Is a & Has a
- 클래스를 설계하는 개념
- A is a B
    - A 는 B이다. 상속을 이용해서 클래스를 만드는 방법
- A has B
    - A 는 B를 가진다. A가 B 객체 가지고 클래스를 만드는 방법
°°°"""
# |%%--%%| <t1OCIjwuJ4|CKXiUSLhEn>

# is a

class Person:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Person2(Person):
    def info(self):
        print(self.name, self.email)
        
p = Person2("peter", "peter@naver.com")
p.info()

# |%%--%%| <CKXiUSLhEn|0rHjlqvOr8>

# has a

class Name:
    def __init__(self, name):
        self.name_str = name
    
class Email:
    def __init__(self, email):
        self.email_str = email


class Person:
    
    def __init__(self, name_object, email_object):
        self.name = name_object
        self.email = email_object
    
    def info(self):
        print(self.name.name_str, self.email.email_str)
        
name1 = Name('peter')
email1 = Email('peter@naver.com')
p = Person(name1, email1)
p.info()

# |%%--%%| <0rHjlqvOr8|tmLvXzhw3h>
r"""°°°
# Modules and Libraries
- 모듈이란 여러개의 python 함수들이 들어있는 것을 말한다.
- 라이브러리란 여러개의 모듈을 모아 놓은 것
- API 라고 하는 것이 보통 모듈을 말한다.
°°°"""
# |%%--%%| <tmLvXzhw3h|dSSVaY7Ou1>

import myfunctions as myfunc

# |%%--%%| <dSSVaY7Ou1|J7xEGdgLlb>

path = '/home/wonseok'

myfunc.count_files(path)

# |%%--%%| <J7xEGdgLlb|yjeXBv3488>

from MyModule.functions import *

# |%%--%%| <yjeXBv3488|oQSYmlHXcO>

bingo = Animal('bingo')
