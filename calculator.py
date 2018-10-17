from flask import Flask
from flask_restful import Resource, Api
import sys
import math

app = Flask(__name__)
api = Api(app)

class Add(Resource):

    def post(self, operand1, operand2):
        return {'sum': int(operand1+operand2)}

    def get(self, operand1, operand2):
        return {'sum': int(operand1+operand2)}

class Multiply(Resource):

    def post(self, operand1, operand2):
        return {'product': int(operand1*operand2)}

    def get(self, operand1, operand2):
        return {'product': int(operand1*operand2)}

class SquareRoot(Resource):

    def post(self, operand1):
        return {'sqrt': int(math.sqrt(operand1))}

    def get(self, operand1):
        return {'sqrt': int(math.sqrt(operand1))}


class Floor(Resource):

    def post(self, operand1):
        return {'floor': int(math.floor(operand1))}
    
    def get(self, operand1):
        return {'floor': int(math.floor(operand1))}


class Divide(Resource):

    def post(self, operand1, operand2):
        try:
            return {'quotient': int(operand1/operand2)}
        except ZeroDivisionError:
            return {'quotien': sys.maxint }

    def get(self, operand1, operand2):
        try:
            return {'quotient': int(operand1/operand2)}
        except ZeroDivisionError:
            return {'quotien': sys.maxint }


api.add_resource(Add, '/add/<int:operand1>/<int:operand2>')
api.add_resource(Multiply, '/multi/<int:operand1>/<int:operand2>')
api.add_resource(SquareRoot, '/sqrt/<int:operand1>')
api.add_resource(Floor, '/floor/<float:operand1>')
api.add_resource(Divide, '/divide/<int:operand1>/<int:operand2>')

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('--port')
    parser.add_option('--host')
    parser.add_option('--debug', dest='debug', action='store_true', default=False)
    opt, args = parser.parse_args()
    app.run(debug=opt.debug, host=opt.host, port=opt.port)
