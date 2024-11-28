#!/usr/bin/env python3
"""
This module contains Customers view
"""
from flask import (Blueprint, jsonify, request, abort, render_template,
                   flash, redirect, url_for)
from models.orders_model import OrderModel
from models.customers_model import CustomerModel
from models import storage
from api.v1.views import views

# from api.v1.jsonDB import jsondb
from os import path


# json_file = path.join(path.dirname(__file__), 'customers.json')


@views.route('/customers', methods=['GET'])
def get_all_customers():
    """
    Returns all Customers in database
    """
    customers_query = storage.all(CustomerModel).values()
    customers = []
    for customer in customers_query:
        customers.append(customer.to_dict())

    return jsonify(customers), 200


@views.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
    Get a single customer from database based on customer_id
    """
    customer = storage.get(CustomerModel, customer_id)
    if not customer:
        abort(404)

    return jsonify(customer.to_dict())
