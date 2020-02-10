from  send_message import Send_Message
import sys

def main():
    fromaddress = '@gmail.com'
    toaddress = '@gmail.com'
    password = ''
    content =""

    try:
        mail = Send_Message(fromaddress, toaddress, password)
        mail.send(content)
        print("success")
    except:
        print("error")

if __name__ == "__main__":
    main()