from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from datetime import date, timedelta
from .models import DailyRecord

def calendar_view(request):
    selected_date = request.GET.get("date")

    if selected_date:
        selected_date = date.fromisoformat(selected_date)
    else:
        selected_date = date.today()

    # 横スクロール用（日付 ±3日）
    days = [
        selected_date + timedelta(days=i)
        for i in range(-3, 4)
    ]

    records = DailyRecord.objects.filter(date=selected_date)

    context = {
        "selected_date": selected_date,
        "days": days,
        "records": records,
    }
    return render(request, "calendar/calendar.html", context)
