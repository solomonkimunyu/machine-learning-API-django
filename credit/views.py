from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
import pickle

# Create your views here.
class predictViewset(viewsets.ViewSet):

    def predict_get(self, request):
        if request.method =='POST':
            data = request.data

            model = pickle.load(open('gradient.pkl','rb'))

            amount_x = float(data['amount_x'])
            repayment_amount = float(data['repayment_amount'])
            total_balance = float(data['total_balance'])
            amount_y = float(data['amount_y'])
            grace_period = float(data['grace_period'])
            interest_percentage = float(data['interest_percentage'])
            interest = float(data['interest'])
            total = float(data['total'])

            x = [amount_x, repayment_amount, total_balance, amount_y, grace_period,
                 interest_percentage, interest, total]

            prediction = model.predict([x])
            if prediction == 0:
                status = 'Paid'
            else:
                status = 'Default'

            predict_info = {
                            'Prediction': int(prediction),
                            'Status': status,
                            'message': "successfully predicted"
                            }

            return Response(predict_info)