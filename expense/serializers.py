from rest_framework import serializers
from .models import ExpenseIncome


class ExpenseIncomeBaseSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        if obj.tax_type == "percentage":
            return round(obj.amount + (obj.amount * obj.tax / 100), 2)
        return round(obj.amount + obj.tax, 2)