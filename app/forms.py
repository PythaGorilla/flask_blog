from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from app.models import User



class oid_LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class LoginForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    password=TextField('password', validators = [Required()])
    
    remember_me = BooleanField('remember_me', default = False)
    def validate(self):
        if not Form.validate(self):
            return False
        user=User.query.filter_by(nickname = self.nickname.data).first()
        if user is None:
            self.nickname.errors.append('Wrong nickname ') 
            return False
        elif user.verify_password(self.password.data) ==True:
            return True
        self.password.errors.append('Wrong password')    
        return False

class Sign_up_form(Form):
    nickname = TextField('nickname', validators = [Required()])
    password=TextField('password', validators = [Required()])
    email=TextField('email', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(nickname = self.nickname.data).first()
        user2= User.query.filter_by(email = self.email.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        if user2 != None:
            self.email.errors.append('This Email is already in use.')
            return False
        return True


class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    signature=TextField('signature', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    email=TextField('email', validators = [Required()])





    def __init__(self, original_nickname, original_email,*args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        self.original_email=original_email

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None and self.nickname.data != self.original_nickname:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False

        user2= User.query.filter_by(email = self.email.data).first()
        if user2 != None and self.email.data != self.original_email:
            self.email
            self.email.errors.append("This E-mail is already in use. Please choose another one.")
            return False
        return True

class PostForm(Form):
    post = TextField('post', validators = [Required()])

class SearchForm(Form):
    search = TextField('search', validators = [Required()])
    

