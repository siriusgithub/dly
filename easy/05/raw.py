import hashlib
import getpass

def passcheck(user, password):
    passfile = file("./passwd", 'r')
    passhash = hashlib.sha512(password).digest()
    for line in passfile:
        try:
            fileuser, algo, filehash = line.split("$", 2)
        except ValueError:
            continue
        if user != fileuser:
            continue
        if (algo != 'sha512'): # add other hashlib algorithms, update hashes as necessary
            continue
        if passhash == filehash:
            passfile.close()
            return True
    passfile.close()
    return False

if __name__ == '__main__':
    user = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    if passcheck(user, password):
        print("Executing Global Thermonuclear War program.")
    else:
        print("No can do, bub.")
