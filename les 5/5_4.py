import re

def new_password(oldpassword, newpassword):
  return(oldpassword != newpassword and len(newpassword) >= 6 and re.search('\d', newpassword) != None)

print(new_password('wachtwoord', 'wachtwoord1')) # True want nieuw wachtwoord met een cijfer
print(new_password('wachtwoord', 'wachtwoordd')) # False want geen cijfer
print(new_password('wachtwoord', 'wachtwoord')) # False want zelfde wachtwoord
print(new_password('wacht', 'woord')) # False want geen cijfer en te kort
