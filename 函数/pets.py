def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a" + animal_type + ".")
    print("My " + animal_type + "'s name is" + pet_name.title() + ".")
    pass





import random

def v_code():

    code = ''
    for i in range(5):

        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])

    return code

print(v_code())