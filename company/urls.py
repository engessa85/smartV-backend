from django.urls import path
from .views import CompanyListCreateAPIView, UserComaniesView, AppointmentView, UserDashBoardInfo


urlpatterns = [
   path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
   path('user-companies', UserComaniesView.as_view(), name='user-companies'),
   path('user-companies/<int:company_id>', UserComaniesView.as_view(), name='update-companies'),
   path('user-appointment', AppointmentView.as_view(), name='user-appointment'),
   path("user-appointment/<int:appointment_id>", AppointmentView.as_view(), name="update_appointment"),

   path("user-dashboard/", UserDashBoardInfo.as_view(), name="user-dashboard"),

]
