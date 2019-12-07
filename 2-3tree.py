import time
class Student:
    def __init__(self,first,last,ssn,email,age):
        self.mFirst = first
        self.mLast = last
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age
        
    def __eq__(self,rhs):
        return self.mSSN == rhs.mSSN
    
    def __ne__(self,rhs):
        return self.mSSN != rhs.mSSN
    
    def __gt__(self,rhs):
        return self.mSSN > rhs.mSSN
    
    def __lt__(self,rhs):
        return self.mSSN < rhs.mSSN
    
    def __ge__(self,rhs):
        return self.mSSN >= rhs.mSSN
    
    def __le__(self,rhs):
        return self.mSSN <= rhs.mSSN

    def getAge(self):
        return self.mAge

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mLeft = None
        self.mRight = None


class Tree:
    def __init__(self):
        self.mRoot = None

    def Exists(self,item):
        return self.ExistsR(item, self.mRoot)

    def ExistsR(self,item,current):
        if current is None:
            return False
        elif current.mItem == item:
            return True
        elif item < current.mItem:
            return self.ExistsR(item, current.mLeft)
        else:
            return self.ExistsR(item, current.mRight)

    def Insert(self, item):
        if self.Exists(item):
            return False
        self.mRoot=self.InsertR(item, self.mRoot)
        return True

    def InsertR(self, item, current):
        if current is None:
            current = Node(item)
        elif item < current.mItem:
            current.mLeft = self.InsertR(item, current.mLeft)
        else:
            current.mRight = self.InsertR(item, current.mRight)
        return current
        

    def Retrieve(self, item):
        return self.RetrieveR(item, self.mRoot)

    def RetrieveR(self, item, current):
        if current is None:
            return None
        elif current.mItem == item:
            return current.mItem
        elif item < current.mItem:
            return self.RetrieveR(item, current.mLeft)
        else:
            return self.RetrieveR(item, current.mRight)

    def Size(self):
        return self.SizeR(self.mRoot)

    def SizeR(self, current):
        if current is None:
            return 0
        return 1 + self.SizeR(current.mLeft) + self.SizeR(current.mRight)

    def Traverse(self, callback):
        self.TraverseR(callback, self.mRoot)

    def TraverseR(self, callback, current):
        if current:
            callback(current.mItem)
            self.TraverseR(callback, current.mRight)
            self.TraverseR(callback, current.mLeft)

    def Delete(self, item):
        if not self.Exists(item):
            return False

        self.mRoot  = self.DeleteR(item, self.mRoot)
        return True

    def DeleteR(self, item, current):
        if item < current.mItem:
            current.mLeft = self.DeleteR(item, current.mLeft)
        elif item > current.mItem:
            current.mRight = self.DeleteR(item, current.mRight)
        else:
            if current.mLeft is None and current.mRight is None:
                current = None
            elif current.mRight is None:
                current = current.mLeft
            elif current.mLeft is None:
                current = current.mRight
            else:
                z = current.mRight
                while z.mLeft:
                    z = z.mLeft
                current.mItem = z.mItem
                current.mRight = self.DeleteR(z.mItem, current.mRight)
                
        return current


gTotalAge = 0
def AddAges(student):
    global gTotalAge
    
    gTotalAge += int(student.getAge())





def main():
    #print what size methods returns 

    global gTotalAge
    TravTime = time.time()
    AllStudents = Tree()
    failed1 = 0
    success = 0
    fin = open("InsertNamesMedium.txt", "r")
    for line in fin:
        words = line.split()
        newStudent = Student(words[0],words[1],words[2],words[3],words[4])
        #Exists
        #Insert
        OK = AllStudents.Insert(newStudent)
        if not OK:
            print("error can't insert ", words)
            failed1 += 1
        if OK:
            success +=1
            
    fin.close()

    print("successes " + str(success))
    print("fails " + str(failed1))
    #avg age of student Traverse
    AllStudents.Traverse(AddAges)
    print (gTotalAge / AllStudents.Size())
    TravFin = time.time()
    time1 = TravFin - TravTime
    print("it took " + str(time1) + " seconds")



    #Delete given a ssn in afile maek a dummy student only has it ssn, call allstudents.delete(dumystudnet), first call exists. 
    deleteSuccess = 0
    deleted = 0
    failed = 0
    fin2 = open("DeleteNamesMedium.txt", "r")
    delTime = time.time()
    for line in fin2:
        deleted += 1
        ssn = line.split()
        dummy = Student("","",ssn[0],"","")
        ok = AllStudents.Delete(dummy)
        if not ok:
            #print("found matching ssn", ssn)
            deleted -= 1
            failed += 1
        if ok:
            deleteSuccess += 1

    fin2.close()




    DelFin = time.time()
    t2 = DelFin - delTime
    print("failed number of students " + str(failed))
    print("ssn deleted " + str(deleted))
    print("Successess " + str(deleteSuccess))
    print("it took " + str(t2) + " seconds")

    
    #Retrieve
    count = 0
    gTotalAge = 0
    retrieveF = 0
    fin3 = open("RetrieveNamesMedium.txt", "r")
    for line in fin3:
        ssn1 = line.split()
        s2 = Student("","",ssn1[0],"","")
        okay = AllStudents.Retrieve(s2)
        if not okay:
            #print("failed to retrieve ", ssn1)
            retrieveF +=1

        if okay:
            gTotalAge += int(okay.mAge)
            count +=1

    fin3.close()

    print(gTotalAge/count)
    print ("failed to retrieve: " + str(retrieveF) +" ssn's")
    print("successful retrieved count of ssn's: " + str(count))

main()
