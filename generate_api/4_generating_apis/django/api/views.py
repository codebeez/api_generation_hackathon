from rest_framework.viewsets import ModelViewSet

from api.models import (
    Department,
    Employee,
    Employeedepartmenthistory,
    Employeepayhistory,
    Jobcandidate,
    Shift,
)
from api.serializers import (
    DepartmentSerializer,
    EmployeedepartmenthistorySerializer,
    EmployeepayhistorySerializer,
    EmployeeSerializer,
    JobcandidateSerializer,
    ShiftSerializer,
)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeedepartmenthistoryViewSet(ModelViewSet):
    queryset = Employeedepartmenthistory.objects.all()
    serializer_class = EmployeedepartmenthistorySerializer


class EmployeepayhistoryViewSet(ModelViewSet):
    queryset = Employeepayhistory.objects.all()
    serializer_class = EmployeepayhistorySerializer


class JobcandidateViewSet(ModelViewSet):
    queryset = Jobcandidate.objects.all()
    serializer_class = JobcandidateSerializer


class ShiftViewSet(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
