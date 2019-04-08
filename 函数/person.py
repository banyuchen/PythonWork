def build_person(fist_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first":fist_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', "4")
print(musician)