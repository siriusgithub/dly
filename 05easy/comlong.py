import hashlib, getpass, os, inspect
 
def generate_hash(x, salt=b'$iS"A)u[Tq'):
    crypt = hashlib.md5();
    crypt.update(salt + x.encode('utf-8'));
   
    return crypt.hexdigest();
 
def query_root_path():
    return ''.join(os.path.split(os.path.join(inspect.getfile(inspect.currentframe())))[0]);
   
def query_users_path():
    return os.path.join(query_root_path(), 'users.txt');
 
def query_passwords_path():
    return os.path.join(query_root_path(), 'password.txt');
 
def save(x, password=False):
    with open(query_users_path() if not password else query_passwords_path(), mode="a+", encoding='utf-8') as file:
        file.write(x + "\n");
 
def user_exists(x):  
    with open(query_users_path()) as file:
        test = file.read().split();
        return test.index(x) if x in test else None;
       
def get_password(id):    
    with open(query_passwords_path()) as file:
        text = file.read().split();
        return text[id] if len(text) >= id else None;
       
def create_user(name=''):
    user, password, confirm = input("Please input your username: ") if not name else name, getpass.getpass("Please input your password: "), getpass.getpass("Please confirm your password: ");
   
    while password != confirm:
        print("\n");
        password, confirm = getpass.getpass("Your passwords do not match. Please input your password: "), getpass.getpass("Please confirm your password: ");
   
    save(user);
    save(generate_hash(password), True);
   
if __name__ == '__main__':
    if not os.path.exists(query_users_path()) or not os.path.exists(query_passwords_path()):
        print("Application cannot find user/password data. Creating new user and files.");
        create_user();
    else:
        user = input("User: ");
        id = user_exists(user);
       
        if id == None:
            print("That user doesn't exist. Creating it...");
            create_user(user);
        else:
            password , confirm = get_password(id), getpass.getpass();
           
            if id == None:
                print("An error prevented the system from retrieving your password.");
            else:
                while generate_hash(confirm) != password:
                    confirm = getpass.getpass("Wrong password. Try again: ");
           
            print("Welcome back!");
