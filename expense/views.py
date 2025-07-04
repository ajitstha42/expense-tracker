from rest_framework import viewsets
from .models import ExpenseIncome
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseIncomeSerializer, ExpenseIncomeListSerializer
from .permissions import IsOwnerOrSuperuser


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    queryset = ExpenseIncome
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ExpenseIncomeListSerializer
        return ExpenseIncomeSerializer
