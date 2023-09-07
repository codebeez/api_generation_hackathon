from django.contrib import admin

from api.models import (
    Department,
    Employee,
    Employeedepartmenthistory,
    Employeepayhistory,
    Jobcandidate,
    Shift,
)


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)


class EmployeedepartmenthistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employeedepartmenthistory, EmployeedepartmenthistoryAdmin)


class EmployeepayhistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employeepayhistory, EmployeepayhistoryAdmin)


class JobcandidateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Jobcandidate, JobcandidateAdmin)


class ShiftAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shift, ShiftAdmin)
