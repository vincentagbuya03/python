


class Student:
    class_email = "Vincent"
    class_password = "123"
    loggedIn = True
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def logIn(self):
        if self.email == self.class_email and self.password == self.class_password:
            return self.loggedIn
        else:
            return self.loggedIn == False



class Enrolled(Student):
    def __init__(self, name , password, is_enrolled):
        super().__init__(name, password)