from rest_framework import routers

from api.views import (
    DepartmentViewSet,
    EmployeedepartmenthistoryViewSet,
    EmployeepayhistoryViewSet,
    EmployeeViewSet,
    JobcandidateViewSet,
    ShiftViewSet,
)

router = routers.SimpleRouter()
router.register(r"department", DepartmentViewSet)
router.register(r"employee", EmployeeViewSet)
router.register(r"employeedepartmenthistory", EmployeedepartmenthistoryViewSet)
router.register(r"employeepayhistory", EmployeepayhistoryViewSet)
router.register(r"jobcandidate", JobcandidateViewSet)
router.register(r"shift", ShiftViewSet)

urlpatterns = router.urls
