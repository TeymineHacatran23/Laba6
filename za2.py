email="test@example.com"
if "@" in email and "." in email and " " not in email and "@"!=email[0] and "."!=email[-1]:
  for i in range(len(email)):
    if email[i]=="@":
      s=i
  for i in range(s+1, len(email)):
    if email[i]==".":
      t=i
      break
  if s>0 and t>s+1:
    print(True)
  else:
    print(False)
else:
  print(False)