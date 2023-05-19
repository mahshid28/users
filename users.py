from uuid import uuid4
import hashlib
import pickle
import json

class User:

    USER_DICT = {}

    def __init__(self, user_name: str, password: str, phone_number=None):
        self.user_name = user_name
        self.__password = password
        self.phone_number = phone_number
        self.id = uuid4()

    def update_profile(self, new_user_name: str, new_phone: str) -> dict:
        """
        update username and phone number.
        """
        User.load()
        self.USER_DICT[new_user_name] = self.USER_DICT.pop(self.user_name)
        self.USER_DICT[new_user_name]['user_name'] = new_user_name
        self.USER_DICT[new_user_name]['phone_number'] = new_phone
        self.save()
        return self.USER_DICT
    
    def profile_validator(self, user_name: str, password: str) -> str | bool:
        """
        check username and password are matching
        """
        User.load()
        if user_name in self.USER_DICT:
            #hash_pass = User.set_pass(password)
            if self.USER_DICT[self.user_name]['user_pass'] != password:
                raise ValueError("Incorrect password!")
            return True
        raise ValueError("Check username or submit")


    @staticmethod
    def set_pass(password: str) -> str:
        """
        generate hashed password
        """
        hashed_pass = hashlib.sha256(password.encode())
        return hashed_pass.hexdigest()

    @staticmethod
    def pass_validator(password: str) -> bool:
        """
        check length ot password
        """
        if len(password) < 4: 
            return False
        return True

    def change_pass(self, password: str, new_pass: str, rep_new_pass) -> str | None:
        """
        replace old password with new one
        """
        User.load()
        #hash_pass = User.set_pass(password)
        if self.USER_DICT[self.user_name]['user_pass'] == password:
            if new_pass == rep_new_pass:
                valid_pass = User.pass_validator(new_pass)
                if valid_pass:
                    #hash_pass = User.set_pass(self.new_pass)
                    self.USER_DICT[self.user_name]['user_pass'] = password
                    self.save()
                else:
                    raise ValueError("Invalid new password")
            else:
                raise ValueError("repeat password not match!")    
        else:
            raise ValueError("Incorrect password!")

    def __str__(self) -> str:
        return f"{self.user_name}: {self.phone_number}"
    
    def save(self):
        """
        save users dictionary in a file
        """
        with open("users_dict.pickle", "wb") as file:
            #hash_pass = User.set_pass(self.__password)
            user_dict = {
                'user_name': self.user_name,
                 'user_pass': self.__password,
                  'ID': self.id,
                  'phone_number': self.phone_number
                  }
            User.USER_DICT[self.user_name] = user_dict
            pickle.dump(User.USER_DICT, file)

    @classmethod
    def load(cls) -> dict:
        """
        load users dictionay from a file
        """
        try:
            with open("users_dict.pickle", "rb") as file:
                cls.USER_DICT = pickle.load(file)
        except FileNotFoundError:
            cls.USER_DICT = {}
        except EOFError:
            cls.USER_DICT = {}

    
    @classmethod
    def submit(cls, user_name: str, password: str, phone_number=None) -> str | __main__.User:
        """
        submit new user
        """
        cls.load()
        if not user_name in cls.USER_DICT:
            valid_pass = cls.pass_validator(password)
            if valid_pass:
                #hash_pass = cls.set_pass(password)
                user = cls(user_name, password, phone_number)
                cls.save(user)
                return user
            else:
                raise ValueError("Ivalid password!")
        else:
            raise ValueError("The username already exists!")
