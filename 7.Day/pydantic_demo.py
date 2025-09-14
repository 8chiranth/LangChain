from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    name : str = "kishan"
    #builtin 
    email : EmailStr 
    #constraints
    cgpa : float = Field(gt = 0, lt = 10)


name = { 'name' : 'chiranth', 'email': 'chiruc.9500@gmail.com'}

student = Student(**name)

print(student)  