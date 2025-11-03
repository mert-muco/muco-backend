from .models import Bid
from .serializers import BidSerializer, BidPreviewSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class BidsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        if user.account_type == 'br':
            brief = request.query_params.get('brief')
            queryset = Bid.objects.filter(brief=brief)
        elif user.account_type == 'usr':
            queryset = Bid.objects.filter(user=user)
        serializer = BidPreviewSerializer(queryset, many=True)
        return Response(serializer.data)

class BidView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        bid = request.query_params.get('bid')
        query = Bid.objects.get(id=bid)
        serializer = BidSerializer(query)
        return Response(serializer.data)
    
class CreateBidView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        data = request.data
        serializer = BidSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)