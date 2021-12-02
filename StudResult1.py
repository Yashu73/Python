str=input("Enter Student Name:")
clas=input("Enter the Class:")
RNo=input("Enter Rollno")
class Grade:
    #constructor will pass the parameters to the CalGrade function
    def __init__(self, Python, AdvanceInternetTechnology, ADBMS,
                 OptimizationTechnique, SPM):
        
        self.Python = Python
        self.AdvanceInternetTechnology = AdvanceInternetTechnology
        self.ADBMS = ADBMS
        self.OptimizationTechnique = OptimizationTechnique
        self.SPM = SPM
    
    def CalGrade(self):
        
       #Average is calculated
        average = (self.Python + self.AdvanceInternetTechnology + self.ADBMS                                                                                                                     
                            + self.OptimizationTechnique + self.SPM)/ 2.5
        
        print(" Your average is ", average)
        
        #average is checked for evaluating the Grade of the student                         
        if (90 <= average <= 100) :

            print(" You have obtained Grade A ")

        elif  (80 <= average < 90) :

            print(" You have obtained Grade B ")

        elif (70 <= average < 80) :

            print(" You have obtained Grade C ")

        elif  (60 <= average < 70) :

            print(" You have obtained Grade D ")

        else:

            print(" You have obtained Grade F ")


if __name__ == "__main__":
    
    Python= int(input(" Enter the marks obtained in Python subject: "))
    AdvanceInternetTechnology = int(input(" Enter the marks obtained in Advance Internet Technology subject: "))
    ADBMS = int(input(" Enter the marks obtained in ADBMS subject: "))
    OptimizationTechnique = int(input(" Enter the marks obtained in Optimization Technique subject:"))
    SPM= int(input(" Enter the marks obtained in SPM subject: "))
    #Object is created for class Grade
    Grade_obj = Grade(Python,  AdvanceInternetTechnology, ADBMS,  OptimizationTechnique, SPM)
    #CalGrade function is called
    Grade_obj.CalGrade()










    av=n*50
per=float((total)*(100/av))
