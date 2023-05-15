from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User




class RegistrationForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo Electronico',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('El usuario ya existe.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('El email ya existe.')

    

class LoginForm(FlaskForm):
    email = StringField('Correo Electronico',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Constraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Acceder')

class UpdateAccountForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo Electronico',
                        validators=[DataRequired(), Email()])
    picture = FileField('Actualizar imagen de perfil', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Actualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Este usuario ya existe, por favor elija otro.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Este usuario ya existe, por favor elija otro.')
            

class RequestResetForm(FlaskForm):
    email = StringField('Correo Electronico',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Solicitar restablecimiento de contraseña')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No cuenta con Email, por favor registrarse')

    
    
                 
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('restablecer la contraseña')