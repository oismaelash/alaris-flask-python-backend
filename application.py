from flask import Flask, request
from flask_cors import cross_origin
from order import OrderController
from plan import PlanController

application = Flask(__name__)

@application.route('/', methods=['GET'])
@cross_origin()
def index():
    return 'API Works! v1.0.0'

@application.route('/order', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def order_controller_api():
    method = request.method
    order_controller = OrderController()
    print(method)

    if method == "GET":
        return order_controller.readAll()
    if method == "POST":
        payload = request.json
        return order_controller.create(payload)
    if method == "PUT":
        id = request.args.get('id')
        payload = request.json
        return order_controller.update(id, payload)
    if method == "DELETE":
        id = request.args.get('id')
        return order_controller.delete(id)


@application.route('/plan', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def plan_controller_api():
    method = request.method
    plan_controller = PlanController()
    print(method)

    if method == "GET":
        return plan_controller.readAll()
    if method == "POST":
        payload = request.json
        return plan_controller.create(payload)
    if method == "PUT":
        id = request.args.get('id')
        payload = request.json
        return plan_controller.update(id, payload)
    if method == "DELETE":
        id = request.args.get('id')
        return plan_controller.delete(id)


application.run()
