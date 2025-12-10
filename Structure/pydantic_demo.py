from typing import Optional

from pydantic import BaseModel , EmailStr , Field

class Student(BaseModel):
    first_name: str = 'ritesh '
    last_name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=5,description= 'A decimal cgpa value')


new_student = {'first_name':'Ritesh','last_name':'Sajwan','email':'asd@gmail.com','cgpa':1}

student = Student(**new_student)
student_dict   = dict(student)
student_json = student.model_dump_json()
print(student)
print(student_dict['first_name'])
print(student_json)