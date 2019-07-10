from ch11_name_func import get_formatted_name

print("enter 'q' to quit")
while True:
    f_name = input("enter your first name: ")
    if f_name == 'q':
        break
    l_name = input("enter your last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)
