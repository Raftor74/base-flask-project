from flask import Blueprint
from utils.response import json_response
from utils.db_examples import get_all_users, get_single_user, insert_new_user
from models import UserModel

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    # Работа с БД через функции
    users = get_all_users()
    single_user = get_single_user()
    #new_user_id = insert_new_user()

    # Работа с БД через модели
    #user_model = UserModel()
    #users = user_model.get_list()
    #single_user = user_model.get_by_id(1)
    """new_user_id = user_model.create({
        'first_name': 'Тест модели',
        'last_name': 'Тест модели 2',
        'email': 'model@test.ru',
        'password': '123456'
    })"""

    response = {
        'users': users,
        'single_user': single_user,
        #'new_user_id': new_user_id,
    }

    return json_response.success(response)
