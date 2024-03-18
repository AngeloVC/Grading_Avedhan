import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lanthanum",
  database="grading"
)
mycursor = mydb.cursor()

#Program to modify table

def modTable():
    tr=input('''What you want to modify:
A:Name,
B.Subject,
C.Marks,
D.Grade:''')
    if tr in 'Aa':
        modName()
    elif tr in 'Bb':
        modSub()
    elif tr in 'Cc':
        modMark()
    elif tr in 'Dd':
        modGrade()
    else:
        print('INVALID INPUT')

def modName():
    nm=input('Enter the old name:')
    nnm=input('Enter the new name:')
    sql='UPDATE results SET name=%s WHERE name=%s'
    val=(nnm,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) name changed")

def modSub():
    sn=input('Enter the old subject:')
    nsn=input('Enter the new subject:')
    nm=input('Enter the name:')
    sql='UPDATE results SET subject=%s WHERE subject=%s AND name=%s'
    val=(nsn,sn,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) subject changed")

def modMark():
    nm=input('Enter the name:')
    sn=input('Enter the subject name:')
    mk=int(input('Enter the marks:'))
    sql='UPDATE results SET marks=%s WHERE name=%s AND subject=%s'
    val=(mk,nm,sn)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) marks changed")

def modGrade():
    nm=input('Enter the name:')
    sn=input('Enter the subject name:')
    gr=input('Enter the grade:')
    sql='UPDATE results SET grade=%s WHERE name=%s AND subject=%s'
    val=(gr,nm,sn)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) grade changed")

#Program to show tables

def showTable():
    mycursor.execute("SELECT * FROM results")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)

#Program to Delete Certain Rows of the DataBase

def delete():
    q=int(input('How many records you want to delete:'))
    for j in range(q):
        w=input('Enter The Name Of Student:').upper()
        sub=input('Enter The Name Of The Subject:').upper()
        sql = "DELETE FROM results WHERE name = %s AND subject = %s"
        adr = (w,sub)
        mycursor.execute(sql, adr)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

#Program for finding the grade in each subject of a student and insert the data into the database.

def insert():
    while True:
        name=input("ENTER STUDENTS NAME:").upper()
        try:
            a=int(input('ENTER THE NUMBER OF SUBJECTS:'))

            s=[]
            for i in range(a):
                f=input("ENTER NAME OF THE {} SUBJECT:".format(str(i+1)+inp(i))).upper()
                s.append(f)

            z=[]
            for k in range(a):
                l=int(input("ENTER {}'S MARKS FOR {}:".format(str(name),s[k])))
                z.append(l)

            print('DEAR {},'.format(name))

            g={}
            for k in range(a):
                t='YOUR GRADE FOR'
                if 90<z[k]<=100:
                    print(t,s[k],"IS A1")
                    g.update({s[k]:'A1'})
                elif 80<z[k]<=90:
                    print(t,s[k],"IS A2")
                    g.update({s[k]:'A2'})
                elif 70<z[k]<=80:
                    print(t,s[k],"IS B1")
                    g.update({s[k]:'B1'})
                elif 60<z[k]<=70:
                    print(t,s[k],"IS B2")
                    g.update({s[k]:'B2'})
                elif 50<z[k]<=60:
                    print(t,s[k],"IS C1")
                    g.update({s[k]:'C1'})
                elif 40<z[k]<=50:
                    print(t,s[k],"IS C2")
                    g.update({s[k]:'C2'})
                elif 30<z[k]<=40:
                    print(t,s[k],"IS D1")
                    g.update({s[k]:'D1'})
                elif 20<z[k]<=30:
                    print(t,s[k],"IS D2")
                    g.update({s[k]:'D2'})
                elif 10<z[k]<=20:
                    print(t,s[k],"IS E1")
                    g.update({s[k]:'E1'})
                elif 0<z[k]<=10:
                    print(t,s[k],"IS E2")
                    g.update({s[k]:'E2'})
                elif 0==z[k]:
                    print('NO GRADE')
                    g.update({s[k]:'NO GRADE'})
                else:
                    print('SORRY THE INPUT CANNOT BE ACCEPTED')

                sql = "INSERT INTO results VALUES (%s, %s, %s, %s)"
                val = (name,s[k],z[k],g[s[k]])
                mycursor.execute(sql, val)
                mydb.commit()
            print('DATA ENTERED TO DATABASE')
            print('THE TOTAL MARKS IS',sum(z[:a]),'AND THE TOTAL PERCENTAGE IS',(sum(z[:a])/a))
            print(g)

        except:
            print('ERROR OCCURED, PLEASE RETRY')
            continue



        #Programme Whether To Repeat.
        a=input("DO YOU WANT TO REPEAT?(Y/N):").lower()
        if a == 'n':
            print("GRADING APPLICATION CLOSED, THANKS FOR USING OUR SERVICE")
            break
        elif a == 'y':
            continue

#Program for Numbers in the Functions

def inp(i):
    'Accepts a natural number and Outputs st, nd, rd, and th of a number accordingly'
    if (i+1)%100 == 11:
        a="th"
    elif (i+1)%100 == 12:
        a="th"
    elif (i+1)%100 == 13:
        a="th"
    elif (i+1)%10 == 1:
        a="st"
    elif (i+1)%10 == 2:
        a="nd"
    elif (i+1)%10 == 3:
        a="rd"
    else:
        a="th"
    return a

#Main Program

while True:
    if input('ENTER PASSWORD:').lower() == 'user1':
        print('WELCOME TO GRADING APPLICATION!')
        print('''THIS IS HOW THE GRADING IS DONE:
                *THE MARKS HAVE TO BE GIVEN OUT OF HUNDRED
                *IF MARKS ARE ABOVE 91, A1 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 81, A2 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 71, B1 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 61, B2 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 51, C1 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 41, C2 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 31, D1 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 21, D2 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 11, E1 GRADE IS AWARDED
                *IF MARKS ARE ABOVE 1, E2 GRADE IS AWARDED
                *IF MARK IS 0, NO GRADE IS AWARDED''')
    else:
        print('SORRY, PASSSWORD IS WRONG.TRY AGAIN!')
        continue
    ask=input('''WHAT DO YOU WANT TO DO?
A.INSERT DATA,
B.SHOW TABLE FROM DATABASE,
C.DELETE DATA FROM DATABASE,
D.MODIFY DATA:''')
    if ask in 'Aa':
        insert()
    elif ask in 'Bb':
        showTable()
    elif ask in 'Cc':
        delete()
    elif ask in 'Dd':
        modTable()
    else:
        print('INVALID INPUT')

    b=input('CLOSE THE WINDOW?[Y/N]:').lower()
    if b == 'y':
        mydb.close()
        break
    elif b == 'n':
        continue
