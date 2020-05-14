import hashlib
 
# Some variable declaration
userFound = False
ind = 0
logged_in = False
# Get user list from txt file
usertxt = open('users.txt', 'r')
userlist = usertxt.read().split('\n')
usertxt.close()
# Get username from user, check if valid
user = raw_input('Username: ')
for line in userlist:
    if user in line:
        userFound = True
        ind = userlist.index(line)
        break
# Get pass list from txt file
passtxt = open('pass.txt', 'r')
passlist = passtxt.read().split('\n')
passtxt.close()
pass_ = raw_input('Password: ')
pass_ = hashlib.sha256(pass_).hexdigest()
# Confirms if password is good or not, logs in if good
if pass_ == passlist[ind]:
    logged_in = True
 
if logged_in:
    print "Log in succesful. Welcome %s." % user
else:
    print "Log in failed. Username or password incorrect."
