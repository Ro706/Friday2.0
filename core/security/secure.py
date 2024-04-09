from cryptography.fernet import Fernet

# Random hash Generator: This code will generate a random hash key
# pip install cryptography: This library is used to generate a random hash key
# def genrate_key():
#     key = Fernet.generate_key()
#     print(key)


def getdata():
    # Generate or retrieve a random hash key
    key =  "ask admin for key"
    return key

def realpassword():
    # Return a predefined password
    real_password = b'gAAAAABmFXTTm3Bz3wKIRxBNZeVpTwEIHGYK1_R25J2Ya8oLftJeUP58-MvWSDEXQsjlykBC4tckYILhIkkcboIrlFGeQeguVA=='
    return real_password

def bardapi():
    # Generate or retrieve a random hash key
    key = getdata()
    password = b'gAAAAABmFXb2i8-TN92iM_NX14razCiR189qwP4ciuHNqkUmyFPCLFJ9lH7cv-P7D1kP5PDCDBiAH-fAo46ptZNHxFhDkCtXtXR4L5J0og2gyrAdtvPIqu34ZfKEjicfg2d_j-KSl6pv'
    f_obj = Fernet(key)
    dec_key = f_obj.decrypt(password).decode()
    return dec_key
def getdatamail():
    # Generate or retrieve a random hash key
    key = getdata()
    password = b'gAAAAABmFXUJUjhr2V8KxeOebDaTlKs3jf8b0s0EykT7K5lFJLqBlQPaxInSsirkCoCr_k8uFqase5YTBWp88yjmR54FHJ381mxg8UF0Y1uaX6wL5QWaIb8='
    f_obj = Fernet(key)
    dec_key = f_obj.decrypt(password).decode()
    print(dec_key)
    
def decrypt_password(enc_message, key):
    # Decrypt an encrypted password using the Fernet encryption scheme
    f_obj = Fernet(key)
    dec_message = f_obj.decrypt(enc_message).decode()
    return dec_message

def check_password(enc_message, real_password, key):
    # Check if the decrypted password matches the real password
    decrypted_password = decrypt_password(enc_message, key)
    return decrypted_password == real_password

def password_is_correct(password):
    # Check if the provided password is correct
    key = getdata()
    real_password = realpassword()
    return check_password(real_password, password, key)
