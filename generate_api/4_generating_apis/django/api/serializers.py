from rest_framework.serializers import ModelSerializer

from api.models import (
    Department,
    Employee,
    Employeedepartmenthistory,
    Employeepayhistory,
    Jobcandidate,
    Shift,
)


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeedepartmenthistorySerializer(ModelSerializer):
    class Meta:
        model = Employeedepartmenthistory
        fields = "__all__"


class EmployeepayhistorySerializer(ModelSerializer):
    class Meta:
        model = Employeepayhistory
        fields = "__all__"


class JobcandidateSerializer(ModelSerializer):
    class Meta:
        model = Jobcandidate
        fields = "__all__"


class ShiftSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"
