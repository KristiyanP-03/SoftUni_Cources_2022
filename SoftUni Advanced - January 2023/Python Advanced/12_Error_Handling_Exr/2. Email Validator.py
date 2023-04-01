import re
email_username_pattern = r"[\w+\_\.]+@"
is_username_good = False
email_domain_patern = r"\.[a-z]+"
is_domain_good = False

class NameTooShortError(Exception):
    """"Name must be more than 4 characters"""
class MustContainAtSymbolError(Exception):
    """"Email must contain @"""
class InvalidDomainError(Exception):
    """"Domain must be one of the following: .com, .bg, .org, .net"""
list_with_domains = ["com", "bg", "org", "net"]

# Custom errors
class ContainsAtSymbolTwiceOrMoreError(Exception):
    """"Email must contain @ one time"""
class InvalidEmailTaitleError(Exception):
    """"Email title must be one of the following: mail, gmail, abv"""
list_with_email_titles = ["mail", "gmail", "abv"]

input_email = input()
while input_email != "End":

    # Errors raleted to symbol '@'
    if input_email.count('@') > 1:
        raise ContainsAtSymbolTwiceOrMoreError
    elif '@' in input_email:
    # All good   =>   username |@| email title |.| domain
        # email = username |@| email title and domain
        username, email_title_and_domain = input_email.split('@')
        #  email title and domain =  email title |.| domain
        email_title, domain = email_title_and_domain.split('.')
    else:
        raise MustContainAtSymbolError

    # Errors related to len(username)
    if len(username) <= 4:
        raise NameTooShortError
    else:
        # username   =>   username@
        username += '@'
    if re.findall(email_username_pattern, username):
        is_username_good = True

    #Error related to email title
    if email_title not in list_with_email_titles:
        raise InvalidEmailTaitleError

    # Errors related to invalid domain
    if domain not in list_with_domains:
        raise InvalidDomainError
    else:
        # domain   =>   .domain
        domain = ''.join(('.' ,domain))
    if re.findall(email_domain_patern, domain):
        is_domain_good = True

    #print the finished email
    if is_username_good and is_domain_good:
        print("Email is valid")
        is_username_good = False
        is_domain_good = False
    input_email = input()
