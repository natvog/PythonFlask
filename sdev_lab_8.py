'''
@author: Natalie Vogel
         SDEV 300
         10/2/2023

         References:
                    - https://www.geeksforgeeks.org/how-to-run-a-flask-application/
                    - https://code.visualstudio.com/docs/python/tutorial-flask
                    - https://www.geeksforgeeks.org/flask-login-without-database-python/
                    - https://www.educba.com/registration-form-in-html/
                    
         
'''
from flask import Flask, request, render_template
from passlib.hash import sha256_crypt

# member database ...
mdb = {'nat@aol.com': 'password',
        'test@gmail.com': 'pwd'}

# failed attempt logger ...
failed_logger = {'test': 'test'}

app = Flask(__name__)

# start page ...
@app.route('/')
def index():
    ''' start page for app '''
    return render_template('index.html')
#---------------------------------------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    ''' register for app '''
    if request.method == 'POST':
        # get inputs ...
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm')
        # hash the password ...
        hash_pass = sha256_crypt.hash(pwd)
        # call verify to compare the two entries ...
        pwd_verified = sha256_crypt.verify(pwd, hash_pass)
        pwd_match = pwd==confirm_pwd
        pwd_meets_req = password_check(pwd)
        pwd_not_common = common_pwd_check(pwd)
        if pwd_verified is True and pwd_match is True and pwd_meets_req is True and pwd_not_common is True:
            # add to memeber database ...
            mdb[email] = pwd
            # redirect once verified ...
            return render_template('home.html', name=email)
        failed_logger[email] = pwd
        return render_template('register.html',
                                info='Password does not meet requirements or too common!')
    return render_template('register.html')
#---------------------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' login for app '''
    if request.method == 'POST':
        # get inputs ...
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        # check inputs match member database ...
        if email in mdb and mdb[email] != pwd:
            failed_logger[email] = pwd
            return render_template('login.html',
                                info='Invalid Email or Password')
        return render_template('home.html', name=email)
    return render_template('login.html')
#---------------------------------------------------------------------------------------------------
@app.route('/password_update', methods=['GET', 'POST'])
def password_update():
    ''' password update for app '''
    if request.method == 'POST':
        # get inputs ...
        email = request.form.get('email')
        old_pwd = request.form.get('old_pwd')
        new_pwd = request.form.get('new_pwd')
        confirm = request.form.get('confirm')
        # check inputs match member database ...
        if email in mdb and mdb[email] != old_pwd:
            failed_logger[email] = old_pwd
            return render_template('password_update.html',
                                info='Invalid Email or Password')
        # hash the password ...
        hash_pass = sha256_crypt.hash(new_pwd)
        pwd_verified = sha256_crypt.verify(new_pwd, hash_pass)
        pwd_match = new_pwd == confirm
        pwd_meets_req = password_check(new_pwd)
        pwd_not_common = common_pwd_check(new_pwd)
        if pwd_verified is True and pwd_match is True and pwd_meets_req is True and pwd_not_common is True:
            # add to memeber database ...
            mdb[email] = new_pwd
            # redirect once verified ...
            return render_template('home.html', name=email)
        return render_template('password_update.html',
                            info='Password does not meet requirements or too common!')
    return render_template('password_update.html')
#---------------------------------------------------------------------------------------------------
def password_check(pwd):
    ''' checks password input on registration page '''
    upper_result = False
    lower_result = False
    digit_result = False
    for ele in pwd:
        # checking for uppercase character and flagging
        if ele.isupper():
            upper_result = True
        if ele.islower():
            lower_result = True
        if ele.isdigit():
            digit_result = True
    return bool(upper_result and lower_result and digit_result)
#---------------------------------------------------------------------------------------------------
def common_pwd_check(pwd):
    ''' checks password input on registration page and update password page'''
    common_result = False
    # reads file ...
    file = open("CommonPassword.txt", "r")
    data = file.read()
    # replacing end of line('/n') with ' ' and
    common_pwd_list = data.replace('\n', '')
    print(common_pwd_list)
    if pwd in common_pwd_list:
        common_result = True
    return bool(common_result)
#---------------------------------------------------------------------------------------------------
@app.route('/home')
def home():
    ''' home page for app '''
    return render_template('home.html')

# runs app ...
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
#---------------------------------------------------------------------------------------------------
# end
