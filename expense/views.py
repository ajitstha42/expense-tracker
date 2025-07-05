from rest_framework import viewsets
from .models import ExpenseIncome
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseIncomeSerializer, ExpenseIncomeListSerializer
from .permissions import IsOwnerOrSuperuser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Expenses"])
class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ExpenseIncomeListSerializer
        return ExpenseIncomeSerializer
