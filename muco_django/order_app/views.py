from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderSerializer
from .models import Order
from django.db.models import Q



# class StripeCheckoutView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def post(self, request):
#         amount = int(float(request.data['amount']) * 100)
#         bid = request.data['bid_name']
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             mode='payment',
#             line_items=[{
#                 'price_data': {
#                     'currency': 'usd',
#                     'product_data': {'name': bid},
#                     'unit_amount': amount
#                 },
#                 'quantity': 1
#             }],
#             success_url='http://localhost:5173/success',
#             cancel_url='http://localhost:5173/cancel'
#         )
#         return Response({'url': session.url})
    
class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        queryset = Order.objects.filter(Q(brief__company=user) | Q(bid__user=user))
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def patch(self, request):
        data = request.data
        order_id=request.query_params['order_id']
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order,data=data, partial=True)
        if serializer.is_valid():
            serializer.save(completed=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SelectedOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        order_id = request.query_params['order_id']
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)        