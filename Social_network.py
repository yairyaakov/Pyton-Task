from abc import ABC, abstractmethod


class SocialNetwork():
    __isUserExist = []
    __passwords = []

    def __init__(self, nameNetwork):
        self.nameNetwork = nameNetwork

    def sign_up (self, uzerName, password):
        flag = True
        for x in self.__isUserExist:
            if(x == uzerName):
                flag = False

        if(len(password)<4, len(password)>8):
                flag = False

        if (flag == True):
            self.__isUserExist.append(uzerName)
            User(uzerName, password)



class User(SocialNetwork):
    Followed = list() #userlist=[]

    def __init__(self, uzerName, password):
        self.uzerName = uzerName
        self.password = password


    def follow (self, User):
        flag = True

        for x in self.userlist:
           if(x == User.uzerName):
             flag = False

        if (flag == True):
          self.Followed.append(User.uzerName)
          print(self.uzerName, " started following ", User.uzerName)

    def unfollow (self, User):
        name_to_remove = User.uzerName

        if name_to_remove in self.Followed:
            self.Followed.remove(name_to_remove)


    def publish_post(self ,type, description, price, place, image):
        if(type == "Text"):
            TextPost(description)

        elif(type == "Image"):
            ImagePost(image)

        elif(type == "Sale"):
            TextPost(description, price, place)



class Post(ABC,User):
    likes = list()
    #def __init__(self):


    def like(self, User):
        flag = True

        for x in User.likes:
            if (x == self.uzerName):
                flag = False

        if (flag == True):
            User.likes.append(self.uzerName)







class TextPost(Post):
     def __init__(self, description):
        print(self.uzerName, " published a post:")
        print(description)




class ImagePost(Post):
     def __init__(self, image):
        print(self.uzerName," posted a picture")
        print(image)



class SalePost(Post):
    def __init__(self,description, price, place):
        print(self.uzerName, " posted a product for sale:")
        print("For sale! ",description," price: ", price," pickup from: ",place)

    def discount(Percentage_discount, password):


