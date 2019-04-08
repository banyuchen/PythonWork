def get_formatted_name(first_name, last_name, middle_name = ""):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name


# 这是一个无线循环！
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")

    f_name = str(input("First name:"))
    if f_name == 'q':
        break
    l_name = str(input("Last name:"))
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
