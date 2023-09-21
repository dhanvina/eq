from .serializers import DepartmentSerializer, LabSerializer, PurchaseOrderSerializer, EquipmentSerializer, EquipmentIssueSerializer, LabInChargeSerializer, EquipmentReviewSerializer, LabInchargeRegisterSerializer, LabInchargeLoginSerializer
from rest_framework import viewsets
from .models import Department, Lab, PurchaseOrder, Equipment, EquipmentIssue, EquipmentReview, LabInCharge, LabInchargeRegister, LabInchargeLogin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class LabViewSet(viewsets.ModelViewSet):
    serializer_class = LabSerializer
    queryset = Lab.objects.all()

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()

class EquipmentIssueViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentIssueSerializer
    queryset = EquipmentIssue.objects.all()

class EquipmentReviewViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentReviewSerializer
    queryset = EquipmentReview.objects.all()
    
class LabInChargeViewSet(viewsets.ModelViewSet):
    serializer_class = LabInChargeSerializer
    queryset = LabInCharge.objects.all()


class LabInchargeRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = LabInchargeRegisterSerializer
    queryset = LabInchargeRegister.objects.all()


class LabInchargeLoginViewSet(viewsets.ModelViewSet):
    serializer_class = LabInchargeLoginSerializer
    queryset = LabInchargeLogin.objects.all()

# @api_view(['POST'])
# def Login_api(request):
#     serializer = AuthTokenSerializer(data = request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     _, token = AuthToken.objects.create(user)
    
#     return Response({
#         'user_info': {
#             'id' : user.id,
#             'username' : user.username,
#             'email' : user.email,
#             },
#         'token' : token
#     })
    