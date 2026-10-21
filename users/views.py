from rest_framework import filters
from rest_framework.generics import ListAPIView
from users.models import Payment
from users.serializers import PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('payment_method', 'paid_course', 'paid_lesson')
    ordering_fields = ['pay_date']

