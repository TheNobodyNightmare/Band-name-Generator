class User:
    def __init__(self, username,roll_no):
        self.name = username
        self.identity_no = roll_no
        self.follows = 0
        self.following = 0

    def follow(self,user):
        user.follows += 1
        self.following += 1


user_1 = User("Gaurav",10)
user_2 = User("Dev",20)

user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.follows)
print(user_2.follows)
print(user_1.following)
print(user_2.following)