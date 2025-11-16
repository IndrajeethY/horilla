from django.urls import include, path

urlpatterns = [
    path("auth/", include("kite_api.api_urls.auth.urls")),
    path("asset/", include("kite_api.api_urls.asset.urls")),
    path("base/", include("kite_api.api_urls.base.urls")),
    path("employee/", include("kite_api.api_urls.employee.urls")),
    path("notifications/", include("kite_api.api_urls.notifications.urls")),
    path("payroll/", include("kite_api.api_urls.payroll.urls")),
    path("attendance/", include("kite_api.api_urls.attendance.urls")),
    path("leave/", include("kite_api.api_urls.leave.urls")),
]
