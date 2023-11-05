contact_id = 1000


def contact_tuple():
    global contact_id
    contact_id += 1
    name = input("enter name: ")
    ph_num = input('enter phone number:')
    return contact_id, name, ph_num


