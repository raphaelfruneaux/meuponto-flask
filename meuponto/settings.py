import os

DEBUG = os.environ.get('DEBUG', True)
TEST = False

SECRET_KEY = "carambolasvoadorasmutantesninja"


# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://meuponto:meuponto@localhost:55432/meuponto')
SQLALCHEMY_TRACK_MODIFICATIONS = True



# project settings
PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha256'
PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds