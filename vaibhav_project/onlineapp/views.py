from tkinter import EXCEPTION
from django.shortcuts import render, HttpResponse, redirect
import pymysql as mq
import random
import cv2
import numpy as np
import face_recognition
import os


# Create your views here.
# view for login page 
def login(request):
    conn = mq.connect(host='127.0.0.1',user='root',password='',database="onlinevotingapp")
    cursor = conn.cursor()
    if cursor:
        print("Connection Establish")
    else:
        print("Connection Failed")

    try:
        if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('pass')
            cursor.execute("SELECT email, pass FROM user_registration WHERE email = %s", [email])
            row = cursor.fetchone()
            request.session['user'] = email
            if row:
                if email == row[0] and password == row[1]:
                    return render(request, 'index.html')
            else:
                return redirect('signup')
    except Exception as e:
        print("Error While login", e)   
    return render(request, 'loader.html')

# view for registration page page 
def register(request):
    voter_id=random.randint(100000, 999999)
    conn = mq.connect(host='127.0.0.1',user='root',password='',database="onlinevotingapp")
    cursor = conn.cursor()
    if cursor:
        print("Connection Establish")
    else:
        print("Connection Failed")

    try:
        if request.method =="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            query="select name from user_registration where email = %s"
            sql=cursor.execute(query,email)
            if sql:
                return redirect('login')
            phone=request.POST.get('phone')
            age=request.POST.get('age')
            password=request.POST.get('pass')
            cpassword=request.POST.get('c_pass')
            vid=voter_id
            cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) #code for capture images 
            cv2.namedWindow("test")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
                    
                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = name+"{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    path = "C:/Users/DELL/3D Objects/vaibhav_project/vaibhav_project/onlineapp/static/images/images"
                    cv2.imwrite(os.path.join(path , img_name),frame)
                    print("{} written!".format(img_name))
                    
            cam.release()
            cv2.destroyAllWindows()
            if name and email and phone and age and password and cpassword and vid:
                query = "insert into user_registration(name, email, phone, age, pass,voter_id, c_pass) values(%s,%s,%s,%s,%s,%s,%s)"
                sql = cursor.execute(query,[name, email, phone, age, password,vid, cpassword])
                conn.commit()
                if sql:
                    return redirect('login')
                else:
                    return redirect('signup')
                    
    except Exception as e:
        print("eroor", e)
    return render(request, 'registration.html')

# view for home page 
def index(request):
    if request.session['user']:
        return render(request, 'index.html')
    else:
        return redirect('/')

# view for voting  page 
def voting(request):
    conn = mq.connect(host='127.0.0.1',user='root',password='',database="onlinevotingapp")
    cursor = conn.cursor()
    if cursor:
        print("Connection Establish")
    else:
        print("Connection Failed")
    try:
        if request.session['user']:
            if request.method == "POST":
                cd1 = request.POST.get('first-candidate')
                cd2 = request.POST.get('second-candidate')
                cd3 = request.POST.get('third-candidate')
                user1=request.session['user']
                query="SELECT `flag` FROM `user_registration` WHERE `email`=%s"
                cursor.execute(query,user1)
                fv = cursor.fetchone()
                if fv[0] == 0:
                    if cd1=="1":
                        query="UPDATE `candidates` SET `cd_votes`=`cd_votes`+1 WHERE cd_id = 1"
                        sql=cursor.execute(query)
                        if sql :
                            query="UPDATE `user_registration` SET `flag`='1' WHERE `email`=%s"
                            cursor.execute(query,user1)
                            conn.commit()
                        conn.commit()
                    if cd2=="2":
                        query="UPDATE `candidates` SET `cd_votes`=`cd_votes`+1 WHERE cd_id = 2"
                        sql=cursor.execute(query)
                        if sql :
                            query="UPDATE `user_registration` SET `flag`='1' WHERE `email`=%s"
                            cursor.execute(query,user1)
                            conn.commit()
                        conn.commit()
                    if cd3=="3":
                        query="UPDATE `candidates` SET `cd_votes`=`cd_votes`+1 WHERE cd_id = 3"
                        sql=cursor.execute(query)
                        if sql :
                            query="UPDATE `user_registration` SET `flag`='1' WHERE `email`=%s"
                            cursor.execute(query,user1)
                            conn.commit()
                        conn.commit()
            return render(request, 'voting.html')
        else:
            return redirect('/')
    except Exception as e:
        print("error",e)
        
# view for logout page 
def logout(request):
    del request.session['user']
    return redirect('/')
        
# view for face recognition page 
def authorization(request):
    path = 'C:/Users/DELL/3D Objects/vaibhav_project/vaibhav_project/onlineapp/static/images/images'
    images = []
    classNames = []
    myList = os.listdir(path) 
    print(myList)  
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode =face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
            return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        name=""
        success,img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            if len(myList):
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Webcam', img)
        cv2.waitKey(1) 
        if(len(name)):
            break
        else:
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                return redirect('signup')  
    return render(request, 'authorization.html')
# view for result  page 
def result(request):
    conn = mq.connect(host='127.0.0.1',user='root',password='',database="onlinevotingapp")
    cursor = conn.cursor()
    if cursor:
        print("Connection Establish")
    else:
        print("Connection Failed")
    query="SELECT cd_votes FROM `candidates`"
    cursor.execute(query)
    fv = cursor.fetchall()
    context = {
        'fav' : fv
    }
    print(fv)
    return render(request, 'result.html',context)

# view for profile page 
def profile(request):
    conn = mq.connect(host='127.0.0.1',user='root',password='',database="onlinevotingapp")
    cursor = conn.cursor()
    if cursor:
        print("Connection Establish")
    else:
        print("Connection Failed")
    if request.session['user']:
        user1=request.session['user']
        query="SELECT * FROM `user_registration` WHERE `email`=%s"
        cursor.execute(query,user1)
        fv = cursor.fetchone()
        
        context = {
        'fav' : fv
        }
    return render(request,"main.html",context)

