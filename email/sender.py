import smtplib
from email.message import EmailMessage
from random import randint

EMAIL_ADDRESS = "znzsndj@gmail.com"
EMAIL_PASSWORD = ("
")

TARGET_EMAIL = input("이메일을 입력하세요: ")
VERIFY_CODE = randint(1111, 9999)

msg = EmailMessage()
msg['Subject'] = "인증번호가 도착하였습니다."
msg['From'] = EMAIL_ADDRESS
msg['To'] = TARGET_EMAIL
msg.set_content(f"인증번호는 {VERIFY_CODE}입니다.")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

INPUT_CODE = int(input("인증번호를 입력하세요: "))
if INPUT_CODE == VERIFY_CODE:
    print("회원가입이 완료되었다")
else:
    print("틀렸는데? 눈 없냐?")