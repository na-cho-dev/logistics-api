#!/usr/bin/env python3
"""
This module contains authentication view for both users and admin
"""
from flask import (Blueprint, jsonify, request, abort, render_template,
                   flash, redirect, url_for)

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import storage
from models.customers_model import CustomerModel

from os import path
# from api.v1.jsonDB import jsondb


auth = Blueprint('auth', __name__, url_prefix='/auth')
# json_file = path.join(path.dirname(__file__), 'customers.json')


@auth.route('/register-admin', methods=['POST'])
def register_admin():
    pass


@auth.route('/login-admin', methods=['POST'])
def login_admin():
    pass


@auth.route('/register-customer', methods=['POST'])
def register_customer():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")

    user_obj = {
        "first_name": first_name, "last_name": last_name,
        "username": username, "email": email,
        "phone_number": phone_number}

    new_customer = CustomerModel(first_name=first_name, last_name=last_name,
                                 username=username, email=email,
                                 phone_number=phone_number)
    storage.create(new_customer)
    storage.save()

    return jsonify(new_customer.to_dict()), 201


@auth.route('/login-customer', methods=['POST'])
def login_customer():
    pass
