#!/usr/bin/env python3
"""
This module contains orders view
"""
from flask import (Blueprint, jsonify, request, abort, render_template,
                   flash, redirect, url_for)
from api.v1 import views
from models.orders_model import OrderModel
from models import storage

# from api.v1.jsonDB import jsondb
from os import path
from uuid import uuid4


# json_file = path.join(path.dirname(__file__), 'orders.json')
# customer_json_file = path.join(path.dirname(__file__), 'customers.json')


# @views.route('/orders', methods=['GET'])
# def get_all_orders():
#     """
#     Gets all orders from the database
#     """
    # orders = jsondb.read_json(json_file)

    # if orders:
    #     return jsonify(orders), 200
    # else:
    #     return jsonify({"error": "Orders not found!"}), 404


# @views.route('/orders/customers/<customer_id>', methods=['GET'])
# def get_order(customer_id):
#     """
#     Gets an order based on the order_id
#     """
    # orders = jsondb.read_json(json_file)
   
    # for order in orders:
    #     if order['customer_id'] == customer_id:
    #         return jsonify(order), 200

    # return jsonify({"error": "No order found for this ID!"}), 404


# @views.route('/orders/customers/<customer_id>', methods=['POST'])
# def create_order(customer_id):
#     """
#     Creates an order with the customer_id
#     """
    # order = request.get_json()
    # customers = jsondb.read_json(customer_json_file)
    # id_exists = any(entry.get("id") == customer_id for entry in customers)

    # if not id_exists:
    #     return jsonify({"error": "Customer with that ID does not exist!"}), 404

    # order['customer_id'] = customer_id
    # jsondb.write_json(order, json_file)

    # return jsonify(order), 201


# @views.route('/orders/customers/<customer_id>', methods=['PUT'])
# def update_order(customer_id):
#     """
#     Update an order
#     """
    # inp_order = request.get_json()
    # db_order = jsondb.read_json(json_file)

    # for order in db_order:
    #     if order['customer_id'] == customer_id:
    #         order['order_name'] = inp_order.get('order_name', order['order_name'])
    #         order['order_description'] = inp_order.get('order_description', order['order_description'])
    #         order['order_purchase_time'] = inp_order.get('order_name', order['order_name'])
    
    # # jsondb.write_json()
    # return jsonify(order)
