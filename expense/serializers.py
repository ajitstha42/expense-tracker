from rest_framework import serializers
from .models import ExpenseIncome


class ExpenseIncomeBaseSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        if obj.tax_type == "percentage":
            return round(obj.amount + (obj.amount * obj.tax / 100), 2)
        return round(obj.amount + obj.tax, 2)


class ExpenseIncomeSerializer(ExpenseIncomeBaseSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = ["id", "title", "description", "amount", "transaction_type", "tax", "tax_type", "total", "created_at", "updated_at",]
        read_only_fields = ["id", "created_at", "updated_at", "total"]


class ExpenseIncomeListSerializer(ExpenseIncomeBaseSerializer):
    class Meta:
        model = ExpenseIncome
        fields = ["id", "title", "amount", "transaction_type", "total", "created_at"]