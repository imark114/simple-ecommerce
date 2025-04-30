from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .dashboard import dashboard_callback
 
@staff_member_required
def admin_dashboard(request):
    context = {}
    context = dashboard_callback(request, context)
    return render(request, 'ecommerce/dashboard.html', context) 