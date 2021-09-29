# Program A Day (Paddy 15)

# Placements team is maintaining list of all placed students as per the company in which they got placed. There is a chance for a particular student to be placed in multiple companies. Now a report needs to be generated indicating the placements team which student got placed in how many companies.
# Being a Python programmer, please assist the placements team. See the below input / output pattern to understand the requirement better.
# Input:
# Enter company name: Accenture
# Student details who selected for Accenture: S1 S8 S10 S20
# Is there any other company visited your campus? (Yes/No): Yes
# Enter company name: TCS
# Student details who selected for TCS: S1 S4 S7 S8 S12 S20
# Is there any other company visited your campus? (Yes/No): No
# Output:
# Final Report:
# S1 got placed in 2 companies
# S4 got placed in 1 company
# S7 got placed in 1 company
# S8 got placed in 2 companies
# S12 got placed in 1 company
# S10 got placed in 1 company
# S20 got placed in 2 companies

# PROGRAM:

class Company:
    def __init__(self):
        self.l1 = []
        self.dict = {}
        self.company_details()

    def other_company(self):
        n = input("Is there any other company visited your campus? (Yes/No):")
        n.lower()
        if n == "yes":
            return (self.company_details())
        elif n == "no":
            return (self.dictionary())
        else:
            print("invalid input")
            return (self.other_company())

    def company_details(self):
        n = input("Enter company name:")
        m = input("Student details who selected for" + " " + n + ":")
        self.l1.extend(m.split(" "))
        return (self.other_company())

    def dictionary(self):
        for i in self.l1:
            if i not in self.dict:
                self.dict[i] = self.l1.count(i)
        return (self.__str__())

    def __str__(self):
        for i in sorted(self.dict.keys()):
            if self.dict[i] > 1:
                print("{} got placed in {} companies".format(i, self.dict[i]))
            else:
                print("{} got placed in {} company".format(i, self.dict[i]))


Company()

# OUTPUT1:

# Enter company name:amazon
# Student details who selected for amazon:harsha
# Is there any other company visited your campus? (Yes/No):yes
# Enter company name:myntra
# Student details who selected for myntra:harsha
# Is there any other company visited your campus? (Yes/No):no
# harsha got placed in 2 companies

# OUTPUT2:

# Enter company name:exile
# Student details who selected for exile:harsha sindhu venkat
# Is there any other company visited your campus? (Yes/No):yes
# Enter company name:google
# Student details who selected for google:harsha sindhu 
# Is there any other company visited your campus? (Yes/No):no
# harsha got placed in 2 companies
# sindhu got placed in 2 companies
# venkat got placed in 1 company
