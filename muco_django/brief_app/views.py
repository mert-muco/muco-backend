from rest_framework.response import Response
from .serializers import BriefSerializer
from .models import Brief
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

class TopBriefsView(APIView):
    def get(self, request):
        queryset = Brief.objects.annotate(bid_count=Count('bid')).order_by('-bid_count')[:3]
        serializer = BriefSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BriefView(APIView):
    def get(self, request):
        query = request.query_params.get('brief')
        brief = Brief.objects.get(id=query)
        serializer = BriefSerializer(brief)
        return Response(serializer.data)

class BrowseView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        bid_query = request.query_params.get('bid_count', 0)
        due_query = request.query_params.get('date', None)
        budget_query = request.query_params.get('budget', None)
        budget_query = None if int(budget_query) >= 1000 else budget_query
        budget_sort = request.query_params.get('budget_sort', False)
        queryset = Brief.objects.annotate(bid_count=Count('bid')).filter(bid_count__lte=bid_query)
        if query:
            queryset = Brief.objects.filter(title__icontains=query)
        if due_query and due_query != 'undefined':
            queryset = queryset.filter(due_date__lte=due_query)
        if budget_query:
            queryset = queryset.filter(budget__lte=budget_query)
        if budget_sort:
            if budget_sort == '1':
                queryset = queryset.order_by('-budget')
            elif budget_sort == '2':
                queryset = queryset.order_by('budget')
        serializer = BriefSerializer(queryset, many=True)
        return Response(serializer.data)
    

class CompanyBriefs(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        company = request.user
        if company.account_type == 'br':
            queryset = Brief.objects.filter(company=company)
        elif company.account_type == 'usr':
            queryset = Brief.objects.filter(bid__user=company)
        serializer = BriefSerializer(queryset, many=True)
        return Response(serializer.data)
    
class CreateBreifView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        data = request.data
        serializer = BriefSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)