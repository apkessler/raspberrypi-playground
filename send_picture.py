import picamera
import send_email
from time import sleep


def main():
    camera = picamera.PiCamera()
    this_user = raw_input('User?')
    this_pwd = getpass.getpass()
    while 1:
        in = raw_input ('Press P to take picture and send.')
        if (in == 'p'):
            camera.capture('image.jpg')
            send_email.send_mail(this_user,this_pwd,[this_user],'A picture for you...','Sent fron Python.',files=['image.jpg'])
            


if __name__ == "__main__":
    main()
