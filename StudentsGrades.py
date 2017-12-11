#Get GPA
#The grade class stores the information
#for a grade
class grade:
    def __init__(self,course,gpoint,credit):
        self.course=course
        self.gpoint=gpoint
        self.credit=credit
    #allow another class to get the values
    def getCourse(self):
        return self.course
    def getGradePoint(self):
        return self.gpoint
    def getCredits(self):
        return self.credit
    def __str__(self):
        return self.course + " " + str(self.gpoint) + " " + str(self.credits)

#student class includes GPA generated from a list of grades
class student:
    def __init__(self,sid,name,email):
        self.sid=sid
        self.name=name
        self.email=email
        self.grades=[]#empty list for grades

    #this method adds grade objects to the grades list
    def addGrades(self, gradepoint):
        self.grades.append(gradepoint)

    def calculateGPA(self):
        #initialize variables
        self.gpa=0
        weight=0
        total=0
        #make sure the list is not empty
        if len(self.grades) != 0:
            #loop throug the objects in the grades list
            #get the weight by multiplying credits and grades
            for g in self.grades:
               weight += g.credit * g.gpoint
               total += g.credit #get total credits
            #caluclate GPA
            self.gpa=weight / total

    def __str__(self):
        self.calculateGPA() #call the calculate method
        #string to be output if you print the class
        return self.sid + " " + self.name + " " + self.email + " " + str(self.gpa)


def main():
    #initialize the student object
    s=student("122453","John Depp",'jd@gmail.com')
    stop="n"
    #loop to enter grades
    while stop=="n":
        course = input("Enter the course name: ")
        gp = float(input("Enter the final grade: "))
        cr=int(input("Enter the number credits: "))
        #create a grade object
        g=grade(course, gp, cr)
        #add it to the student's grade list
        s.addGrades(g)
        stop = input("Do you want to stop? 'n' to continue ")
    print(s)#print the __str__ from student
        
            
main() 














    
