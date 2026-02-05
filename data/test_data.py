from faker import Faker

fake = Faker()


class FakeData:
    @property
    def LOGIN(self):
        return fake.user_name()

    @property
    def PASSWORD(self):
        return fake.password(length=12, special_chars=True, digits=True, upper_case=True)

    @property
    def LONG_STR(self):
        return fake.pystr(min_chars=100, max_chars=200)

    SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\",./<>?"


FakeData = FakeData()


class Users:
    STANDARD_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    GLITCH_USER = "performance_glitch_user"
    PASSWORD = "secret_sauce"
    WRONG_PASSWORD = "wrong_password"


class ErrorMessages:
    WRONG_CREDENTIALS = "Username and password do not match"
    LOCKED_OUT = "Sorry, this user has been locked out"
    USER_REQUIRED = "Username is required"
