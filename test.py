import smtplib
import os
from email.message import EmailMessage
from testnews import *

subList = []
chooseList = []


EMAIL_ADDRESS = 'azzzaokz@gmail.com'
EMAIL_PASSWORD = 'sam123max123!'

class Subscribers:
        def __init__(self, subEmail):
                self.subEmail = subEmail

        def addToList(self):
                subList.append(self.subEmail)


sub1 = Subscribers('azzzaokz@gmail.com')
sub2 = Subscribers('aaronokoroh@hotmail.com')

sub1.addToList()
sub2.addToList()

msg = EmailMessage()
indv = EmailMessage()
choose = EmailMessage()

def sendToAll(x, keyword):
        msg['Subject'] = 'Your Articles'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = subList
        msg.set_content("Your article is about " + keyword + ". Here is the link: " + x)


def sendIndv(email, y, keyword):
        indv['Subject'] = 'Your Articles'
        indv['From'] = EMAIL_ADDRESS
        indv['To'] = email
        indv.set_content("Your article is about " + keyword + ". Here is the link: " + y)

def sendToSelected(z, keyword):
        choose['Subject'] = 'Your Articles'
        choose['From'] = EMAIL_ADDRESS
        choose['To'] = chooseList
        choose.set_content("Your article is about " + keyword + ". Here is the link: " + z)



def selectEmail():
        stop = False
        while stop == False:
                print("All Subcribers: ", subList)
                print("Subscribers to recieve articles: ", chooseList)
                choice = int(input("Who would you like to send the articles to?: "))
                if choice > len(subList)-1 or choice < 0:
                        print("Invalid input")
                        selectEmail()
                chooseList.append(subList[choice])
                #checks to see if user is finished adding emails
                userStop = input("Are you finished adding emails? Enter Y or N: ")
                if userStop == "Y":
                        break
                elif userStop == "N":
                        os.system("cls")
                else:
                        print("Please enter Y or N")
                                
                
        stop = True
                



def sendMessage(user):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(user)


def addSubs(subName, email):
        subName = Subscribers(email)
        subName.addToList()
        print(subList)



def removeSubs(sub):
        subList.remove(sub)

def displayMenu():
        print("--------Manage Subscribers--------")
        print("[1] View Subscribers")
        print("[2] Enter the email you want to add")
        print("[3] Enter the email you want to delete")
        print("[4] Send Emails to all")
        print("[5] Send Email to individual")
        print("[6] Send Emails to selected subscribers")



while(True):
        displayMenu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
                os.system("cls")
                print("Subscribers: ", subList)
                go = input("Enter anything to continue: ")
                os.system("cls")
                

        if choice == 2:
                os.system("cls")
                subName = input("Input the sub name: ")
                email = input("Input the Email address: ")
                addSubs(subName, email)
                os.system("cls")

        if choice == 3:
                os.system("cls")
                print(subList)
                emailDelete = input("Enter the email you want to remove from the service: ")
                removeSubs(emailDelete)
                os.system("cls")

        if choice == 4:
                os.system("cls")
                keyword = input("Input the type of article you would like to send: ")
                x = addArticle(keyword)
                sendToAll(x, keyword)
                sendMessage(msg)
                os.system("cls")

        if choice == 5:
                os.system("cls")
                email = input("What email would you like to send an article to?: ")
                keyword = input("Input the type of article you would like to send: ")
                y = addArticle(keyword)
                sendIndv(email, y, keyword)
                sendMessage(indv)
                os.system("cls")

        if choice == 6:
                os.system("cls")
                selectEmail()
                keyword = input("Input the type of article you would like to send: ")
                z = addArticle(keyword)
                sendToSelected(z, keyword)
                sendMessage(choose)
                os.system("cls")

        



        
                
