oldpassword = input('wat is uw oude pw?: ')
newpassword = input('wat is uw nieuwe pw?: ')

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return True
    else:
        return False
print(new_password(oldpassword, newpassword))