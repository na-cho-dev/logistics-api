from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/api/v1')


from api.v1.views import customers_view
# from api.v1.views.admins_view import *
# from api.v1.views.orders_view import *
