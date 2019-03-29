import requests

print("############################@@hacker||ground@@######################################")
def methodget(ip):
    r = requests.get(ip)
    print(r.text)

methodget('https://epeperiksaan.audit.gov.my/user_login.php')

