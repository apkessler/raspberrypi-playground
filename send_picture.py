import picamera
import send_email
from time import sleep
import getpass

def main():
    camera = picamera.PiCamera()
    this_user = raw_input('User?')
    this_pwd = getpass.getpass()
    while 1:
        c_in = raw_input('Press P to take picture and send.')
        if (c_in == 'p'):
            camera.capture('image.jpg')
            send_email.send_mail(this_user,this_pwd,[this_user],'A picture for you...','Sent fron Python.',files=['image.jpg'])
            


if __name__ == "__main__":
    main()
