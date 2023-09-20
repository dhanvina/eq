from rest_framework import serializers
from .models import Department, Lab, PurchaseOrder, Equipment, EquipmentIssue, EquipmentReview, LabInCharge
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentIssue
        fields = '__all__'

class EquipmentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentReview
        fields = '__all__'

class LabInChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabInCharge
        fields = '__all__'
        

