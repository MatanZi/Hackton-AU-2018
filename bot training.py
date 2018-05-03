# -*- coding: utf-8 -*-
from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
import sqlite3
from mysql.connector import errorcode
import mysql.connector
from time import sleep


chatbot = ChatBot("Yishay junior")
chatbot.set_trainer(ListTrainer)

teacherFNList = []

######################################################
######################################################
###########querry#####################################

'''
port = "4306"
hostname = "erlichsefi.mooo.com"	#127.0.0.1
username = 'remote'
password = 'remotetoor'
database = 'Hackatton'

myConnection = mysql.connector.connect(port=port ,host=hostname, user=username, passwd=password, db=database)

def query(query, numOfFields):
    curs = myConnection.cursor()
    qury = query
    table = []
    
    for i in range(numOfFields):
        cur = curs.execute(qury,params=None,multi=True)
        for (email) in cur:
            field = []
            for x in email:
                if(x):
                    field.append(x[i])
        table.append(field)
    curs.close()
    return table    
######################################################
######################################################
############ Mail Querries  Train############################
def trainMail(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append("מה המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("מה המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a +" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail1(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("מה המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail1(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail2(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail3(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
            
def trainMail2(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append(" תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail4(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail5(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail3(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail6(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail7(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail4(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail8(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail9(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail5(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conersation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail10(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conersation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
  
def trainMail11(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conersation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
############################################################################
############################################################################
###############lesson Querries Train########################################

def trainLesson(ListOfLesson):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה ומתי " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson1(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה ומתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson2(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson3(ListOfLesson, ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson4(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי ואיפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson5(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי והיכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson6(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("היכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson7(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson8(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson9(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה ואיפה" + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson10(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson11(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson12(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( "היכן"+lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson13(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( "היכן"+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson14(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( "היכן ומתי "+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
      #######################################remember ask about split(mavo)  
def trainLesson15(ListOfLesson ):
    for lesson in ListOfLesson:
        a,b=lesson.split(lesson)
        conersation = []
        conversation.append( "היכן ומתי "+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
        
def trainLesson(ListOfLesson):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה ומתי " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson1(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה ומתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
def trainLesson2(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
def trainLesson3(ListOfLesson, ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("איפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson4(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי ואיפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson5(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("מתי והיכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson6(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("היכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson7(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson8(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson9(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append("באיזה שעה ואיפה" + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson10(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson11(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson12(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( "היכן"+lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
        
def trainLesson13(ListOfLesson ):
    for lesson in ListOfLesson:
        conersation = []
        conversation.append( "היכן"+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)'''

###########################################################################################
###########################################################################################
###########################Conversation train##############################################
def trainConversation():
    conversation = [
            "שלום",
            "שלום גם לך",
            "מה נשמע",
            "הכל בסדר, מה בקשתך?",
            ]
    chatbot.train(conversation)
    conersation = [
            "תודה רבה",
            "בכיף המשך יום נעים",
            "תודה",
            "בכיף המשך יום נעים"
            ]
    chatbot.train(conversation)

def trainConversation1():
        conversation = []
        conversation.append( "מה המייל של אראל סגל?")
        conversation.append("erelsgl@gmail.com")
        chatbot.train(conversation)
def trainConversation2():
        conversation = []
        conversation.append( "מתי אוטומטיים?")
        conversation.append("יום רביעי בשעה 09:00, כתה 21.2.6")
        chatbot.train(conversation)


trainConversation1()
trainConversation()
trainConversation2()

s=input()

while s!="exit":
    response = chatbot.get_response(s)
    print(response)
    s=input()