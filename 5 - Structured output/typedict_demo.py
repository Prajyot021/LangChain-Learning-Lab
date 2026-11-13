from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

result:person={'name':'Ram', 'age':34}

print(result)