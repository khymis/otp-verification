import random
import smtplib

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_email(receiver_email, otp):
    sender_email = "khyatimisra94@gmail.com"
    sender_password = "khptwodssukleomq"

    message = f"Subject: OTP Verification\n\nYour OTP is: {otp}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login('khyatimisra94@gmail.com','khptwodssukleomq')
            server.sendmail('khyatimisra94@gmail.com',receiver_email, message)
        print("OTP email sent successfully.")
    except Exception as e:
        print("Error sending OTP email:", str(e))

receiver_email = input("Enter your email address: ")
otp = generate_otp()
send_otp_email(receiver_email, otp)
print("OTP email sent to", receiver_email)
