email=input()
if '@gmail.com' in email[-10:]:
    first =email[0].lower()
    if first in "qerihfkmepigkugd":
        print("valid email")
