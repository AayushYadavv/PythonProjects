import cv2
import os
import smtplib
import imghdr
from  email.message import EmailMessage
import csv

path = 'certi.jpg'
savepath = './GeneratedCerti'


 
window_name = 'Image'

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font1 =cv2.FONT_HERSHEY_SIMPLEX

org1 = (1033, 1940)
org2 = (1630, 2445)




fontScale = 4
color = (0 ,0, 0)
thickness = 7

def mailsender(file,name):
	email = EmailMessage()
	email['from'] = 'Team INSIGHT 2020'
	email['to'] = Email
	email['subject'] = 'Insight Certificate'
	con = f'Hi,{ name}. Greetings from Team Insight. \nHere is your Insight Certificate.\n - Aayush Yadav'
	email.set_content(con)

	with open(file, 'rb') as fp:
	    img_data = fp.read()
	email.add_attachment(img_data, maintype='image',subtype=imghdr.what(None, img_data))
	
	with smtplib.SMTP('smtp.gmail.com',port = 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login('email','password')
		smtp.send_message(email)

with open('CulCdetails.csv',mode = 'r') as exfile:
	for line in exfile:
		image = cv2.imread(path)
		Full_name, Gender ,Event ,Position , Email ,Escape = line.split(',')
		if(Full_name=='Full name' or Gender =='Gender' or Event == 'Event' ):
			continue
		if Gender == 'M' or Gender == 'm':
			org4 = (1930 , 2165)
		elif Gender == 'F' or Gender =='f':
			org4 = (1772 , 2165)
		else:
			print('Gender Not Provided well')

		if Position == '1st' or Position == '2nd'or Position == '3nd':
			org3 = (1500, 2985)
		else:
			 org3 = (1350, 2945)
		
		
		print(Full_name, Gender ,Event ,Position)
		cv2.putText(image, Full_name, org1, font,
		                    fontScale, color, thickness, cv2.LINE_AA)
		cv2.putText(image, Event, org2, font,
		                    fontScale, color, thickness, cv2.LINE_AA)
		cv2.putText(image, Position, org3, font,
		                   3, color, thickness, cv2.LINE_AA)
		cv2.putText(image, '/', org4, font,
		                    fontScale, color, thickness, cv2.LINE_AA)

		# Displaying the image 
		# cv2.namedWindow(window_name	, cv2.WINDOW_NORMAL)
		# cv2.imshow(window_name, image)
		# cv2.resizeWindow(window_name,1000,1000)
		# cv2.waitKey(0) 
		# cv2.destroyAllWindows()
		cv2.imwrite(os.path.join(savepath,Full_name+'.jpg'),image)
		mailsender(os.path.join(savepath,Full_name+'.jpg'),Full_name)
		with open('EmailSentList.csv',newline ='',mode='a') as sentfile:
			csv01 = csv.writer(sentfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			csv01.writerow([Full_name,Event,Position])

