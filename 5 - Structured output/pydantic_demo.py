from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str
    name:str = "Raj" # we can pass default value like this and we wont have to give any value inside the dictionary if we dont want to in new_statement.

    age:Optional[int] = None # again we can send optional value here.
    email:EmailStr
    cgpa:float = Field(gt=0, lt=10, default=5, description="Just a description parameter check")

new_student ={"name":"Prajyot",
              "age":43,
              "email":"abs@gmail.com",
              "cgpa":8
              }
# one smart thing it can do is that if we give a number as a string and it needs int type in class then pydantic does automatic type conversion since it can recognsises that.
 
# new_student={} # to show for default values.

student = Student(**new_student) # its a pydantic object
# but we can convert it into dict object

student_dict = dict(student)

# print(student)

student_json = student.model_dump_json
print(student_dict["cgpa"]) # we can specifically call values like this using their key name.

print(student_json)