class info:
    def __init__(self, name, gender, phone_number, mail, religion):
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.mail = mail
        self.religion = religion

    def get_info(self):
        self.name = input("Enter your name: ")
        self.gender = (input("Enter your gender: "))
        self.phone_number = int(input("Enter your phone number: "))
        self.mail = (input("Enter your mail: "))
        self.religion = input("Enter your religion: ")

    def display_info(self):
        print("BELOW ARE YOUR DETAILS")
        print()
        print("Name:", self.name)
        print("gender:", self.gender)
        print("phone_number:", self.phone_number)
        print("Email:", self.mail)

inst_1 = info("asre", "male", 9876555, "asre@gmail.com", "muslim")
next = inst_1.get_info()
final = inst_1.display_info()

print(final)
