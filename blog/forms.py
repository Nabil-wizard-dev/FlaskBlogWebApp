from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Nom d'utilisateur", validators=[DataRequired("Champ Obligatoire!")]
    )
    password = PasswordField(
        "Mot de passe", validators=[DataRequired("Champ Obligatoire!")]
    )
    remember_me = BooleanField("Rester connecté")
    submit = SubmitField("Connexion")


class PostForm(FlaskForm):
    title = StringField(
        "Titre",
        validators=[
            DataRequired("Champ Obligatoire!"),
            Length(
                min=3,
                max=120,
                message="Assurez-vous que le titre a entre 3 et 120 caractères.",
            ),
        ],
    )
    description = TextAreaField(
        "Description",
        validators=[
            Length(
                max=240,
                message="Assurez-vous que le champ description ne dépasse pas 240 caractères.",
            )
        ],
    )
    body = TextAreaField("Contenu", validators=[DataRequired("Champ Obligatoire!")])
    image = FileField(
        "Couverture de l'article", validators=[FileAllowed(["jpg", "jpeg", "png"])]
    )
    submit = SubmitField("Publier l'article")


class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cet email est déjà utilisé. Veuillez en utiliser un autre.')
