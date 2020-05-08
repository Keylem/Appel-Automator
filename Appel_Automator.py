#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:37:38 2020

@author: manjaro

Made by Kerem Eylem
"""
Appel_Sayisi = 8
Haftaici = ("Monday","Tuesday","Wednesday","Thursday","Friday")
gmail_user = '' #your mail
gmail_password = ''#your password
okulnumaran = ""

import datetime
import smtplib
from selenium import webdriver
import time
from pynput.mouse import Button, Controller

#Gün değerleri başlangıçta tanıtılır
current_day = datetime.datetime.now().strftime("%A")
print(current_day) #Gün adı
current_H = int(datetime.datetime.now().strftime("%H"))
print(current_H) #Saat
current_M = int(datetime.datetime.now().strftime("%M"))
print(current_M) #dakika

sent_from = gmail_user
to = [gmail_user]



#While döngüsü
while True:
    current_day = datetime.datetime.now().strftime("%A")
    current_H = int(datetime.datetime.now().strftime("%H"))
    current_M = int(datetime.datetime.now().strftime("%M"))
    
    #1. APPEL 8.20
    if current_H == 8 and current_M == 20 and Appel_Sayisi == 8 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 1
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
           
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 1
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)
            
            mouse = Controller()

            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")
        
        
    #2. APPEL    
    elif current_H == 9 and current_M == 0 and Appel_Sayisi == 1 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 2
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 2
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #3. APPEL    
    elif current_H == 9 and current_M == 40 and Appel_Sayisi == 2 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 3
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 3
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)

    
            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)
            
            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #4. APPEL    
    elif current_H == 10 and current_M == 20 and Appel_Sayisi == 3 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 4
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 4
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div').click()
                
                
            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)
            
            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
            
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #5. APPEL
    elif current_H == 11 and current_M == 45 and Appel_Sayisi == 4 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 5
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 5
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #6. APPEL    
    elif current_H == 12 and current_M == 25 and Appel_Sayisi == 5 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 6
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 6
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #7. APPEL    
    elif current_H == 13 and current_M == 5 and Appel_Sayisi == 6 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 7
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 4
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[7]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
            
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")        
        
        
    #8. APPEL    
    elif current_H == 13 and current_M == 45 and Appel_Sayisi == 7 and (current_day in Haftaici) == True:
        print("gotcha!")
        Appel_Sayisi = 8
        subject = 'Appel:{}'.format(Appel_Sayisi)
        body = 'Tu as envoye ton appelle pour le {}eme periode! \n\n Im a bot made by Dominateur-K!'.format(Appel_Sayisi)
        try:
            
            browser = webdriver.Chrome()
            browser.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSf3iVLdTZ-5BwQwoBQCvsuGPrNbuiNOWOCA_cHELlWQFiridg%2Fviewform&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(10)
            eposta = browser.find_element_by_name('identifier')
            eposta.send_keys(gmail_user)
            browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
            time.sleep(5)
            epostasifre = browser.find_element_by_name("password")
            epostasifre.send_keys(gmail_password)
            time.sleep(5)
            browser.find_element_by_id('passwordNext').click()
            time.sleep(15)
            for tekrar in range(3):
                #9C
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div').click()
                
                #Periode 8
                browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div').click()


            #
            browser.find_element_by_name('entry.1513188580').send_keys(okulnumaran)
            time.sleep(3)


            mouse = Controller()
            
            time.sleep(1)
            print(mouse.position)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(842,236)
            print(mouse.position)

            mouse.click(Button.left,1)
            mouse.scroll(0,-1000)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(171,846)
            mouse.click(Button.left,1)
            mouse.move(-10000,-10000)
            time.sleep(1)
            mouse.move(196,903)
            mouse.click(Button.left,2)
            time.sleep(5)
            browser.close()
    
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   
            server.ehlo()
            server.login(gmail_user, gmail_password)
            email_text = """\\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (sent_from, ", ".join(to), subject, body)
            server.sendmail(sent_from, to, email_text) 
            server.close() 
        
            print("{}.appel atıldı".format(Appel_Sayisi))
        
        except:
            print("bisisler yolunda gitmedi.... :/")
