class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
         raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not len(value) >= 8 or not any(char.isdigit() for char in value) or \
                not any(char.isupper() for char in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password()

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"

profile_with_invalid_password = Profile('My_username', 'My-password')

profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")

print(correct_profile)