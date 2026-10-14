email="test@example.com"
if "@" in email and "." in email and " " not in email and email.find("@")>0 and email.find(".")>email.find("@")+1 and email.rfind(".")<len(email)-1:
  print(True)
else:
  print(False)