# utils.py

import datetime, hashlib, random, string

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

def getRandomString (size=12, chars=chars):
    return ''.join(random.choice(chars) for x in range(size))

def genGuid(rand_length=4):
    """
    Creates a 12 char timestamp postfixed with a random string of length rand_length.
    Default would produce a 16 char string = <timestamp><random 4 chars>
    """
    d = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    r = getRandomString(size=rand_length)
    guid = d + r
    return guid

def hashEmailAddress(email, salt):
    return 'sha256$' + hashlib.sha256(email + salt).hexdigest()



