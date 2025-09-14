from typing import TypedDict

class user(TypedDict):
    name: str
    age : int


new_user : user = {'name':'chiranth', 'age':20}

print(new_user)