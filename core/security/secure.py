from cryptography.fernet import Fernet
def getdata():
    # Generate or retrieve a random hash key
    key = "Ask for key from the system admin"
    return key

def realpassword():
    # Return a predefined password
    real_password = b'gAAAAABmVBjr-ZahRky8N2rUOzuW47J6d7SV-8x88YY73OaxspMpkhzOKvxT85OeEouSUi6ybRPse10nXMejdVOxhE2emPwhDw=='
    return real_password

def bardapi():
    # Generate or retrieve a random hash key
    key = getdata()
    password = b'gAAAAABmVBlQHL0QGgoM8kd44KxQFAUzZds547qaN_SCl4RsYA67jHuNhS9egHjPIKp3dfrf6zstir4cMrei-33WeKa-LC6GfkvxFJyViamaiEll1OPmNz3PV9f4ebYGMSGOe6hafqub'
    f_obj = Fernet(key)
    dec_key = f_obj.decrypt(password).decode()
    return dec_key
    
def getdatamail():
    # Generate or retrieve a random hash key
    key = getdata()
    password = b'gAAAAABmVBlKoalTqUxKzpE1COkfmrfgRy_kXIBH0dTS3QsLwoRM4aiSNNYEiCGRUdVokju2vk59PPBzJHjYfjJNgTPakUcmgIyPYpOgvZ7xv3UfhR-OX_o='
    f_obj = Fernet(key)
    dec_key = f_obj.decrypt(password).decode()
    return dec_key
    
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

