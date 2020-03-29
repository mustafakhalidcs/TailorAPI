import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import jsonify


APP = Flask(__name__)
CORS(APP)
API = Api(APP)

class Customer(Resource):
    
    def get(self):
        return 'Welcome to Tailor App'

    def post(self):
        args = request.get_json(force=True)

        cust_name = args.get('Name','')
        phone = args.get('phone','')
        address = args.get('Address','')
        lambai = args.get('lambai','')
        chatti = args.get('chatti','')
        teera = args.get('teera','')
        bazu = args.get('bazu','')
        neck = args.get('neck','')
        kameezdaman = args.get('kameezdaman','')
        shalwarlambai = args.get('shalwarlambai','')

        query = """
        INSERT INTO customer_measurements values ('{}','{}','{}','{}')
        """.format(cust_name,phone,address,lambai)

        return cust_name


API.add_resource(Customer, '/measure-data')

if __name__ == '__main__':
    APP.run(debug=True, threaded=True, host='0.0.0.0', port=8080)
