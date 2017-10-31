import hashlib


def passwd_jiami(password):
    sha = hashlib.sha256()
    new_password = 'hellopython' + password
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()