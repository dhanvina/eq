from django.contrib import admin
from .models import Department, Lab, LabInCharge, Equipment, EquipmentIssue, EquipmentReview, PurchaseOrder,LabInchargeRegister,LabInchargeLogin

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_number', 'department_name', 'hod_name')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('lab_number', 'department', 'location')

@admin.register(LabInCharge)
class LabInChargeAdmin(admin.ModelAdmin):
    list_display = ('lab_incharge_name', 'lab')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_serial_number', 'lab', 'purchase_date', 'status')

@admin.register(EquipmentIssue)
class EquipmentIssueAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'lab_incharge', 'number_of_equipments')

@admin.register(EquipmentReview)
class EquipmentReviewAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'quantity', 'date', 'lab_incharge')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('purchase_order_number', 'purchase_date', 'supplier', 'total_value')

@admin.register(LabInchargeRegister)
class LabInchargeRegisterAdmin(admin.ModelAdmin):
    list_display = ('lab_incharge', 'password', 'confirm_password', 'email','department','lab')

@admin.register(LabInchargeLogin)
class LabInchargeLoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')