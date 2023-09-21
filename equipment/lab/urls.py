from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, LabViewSet, PurchaseOrderViewSet, EquipmentViewSet, EquipmentIssueViewSet, EquipmentReviewViewSet, LabInChargeViewSet, LabInchargeRegisterViewSet, LabInchargeLoginViewSet
from . import views

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'lab', LabViewSet)
router.register(r'purchase_order', PurchaseOrderViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'equipment_issue', EquipmentIssueViewSet)
router.register(r'equipment_review', EquipmentReviewViewSet)
router.register(r'labincharge', LabInChargeViewSet)
# router.register(r'Login_api', Login_api)
router.register(r'LabInchargeRegister', LabInchargeRegisterViewSet)
router.register(r'LabInchargeLogin', LabInchargeLoginViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
