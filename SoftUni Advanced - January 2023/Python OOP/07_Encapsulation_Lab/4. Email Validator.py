class EmailValidator:
    def __init__(self, min_lenght: int, mails: list(), domains: list()):
        self.min_length = min_lenght
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        name, rest = email.split('@')
        domain, mail = rest.split('.')

        if self.__is_name_valid(email) and self.__is_mail_valid(email) and self.__is_domain_valid(email):
            return True
        else:
            return False

