import smtplib
from email.message import EmailMessage
from random import randint

verification_codes = {}

def send_verify_code(email):
    EMAIL_ADDRESS = "znzsndj@gmail.com"
    EMAIL_PASSWORD = ("wvzy zyek nvrp cfbr")
    VERIFY_CODE = randint(1111, 9999)

    msg = EmailMessage()
    msg['Subject'] = "인증번호가 도착하였습니다."
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content(f"인증번호는 {VERIFY_CODE}입니다.")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    verification_codes[email] = {
        'code': VERIFY_CODE
    }

def verify(email, code):
    data = verification_codes.get(email)

    if not data:
        return False, "인증 요청이 없습니다."
    if data == code:
        return True, "인증이 완료되었습니다."
    elif data['code'] != code:
        return False, "인증번호가 올바르지 않습니다."
    else:
        return False, "알 수 없는 오류"

if __name__ == "__main__":
    TARGET_EMAIL = input("이메일을 입력하세요: ")
    send_verify_code(TARGET_EMAIL)
    INPUT_CODE = int(input("인증번호를 입력하세요: "))
    success, message = verify(TARGET_EMAIL, INPUT_CODE)
    print(message)