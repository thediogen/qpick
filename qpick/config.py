import os

from dotenv import load_dotenv


load_dotenv(override=True)


APP_SECRET_KEY = os.getenv('app_secret_key')


# here's data that cannot be "None", because it can cause errors in the future
__REQUIRED_DATA = {
    'app_secret_key': APP_SECRET_KEY,
}

if None in __REQUIRED_DATA.values():
    raise ValueError('None value in ".env" file. it can cause errors in the future')
