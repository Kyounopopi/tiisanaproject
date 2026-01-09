# views.py
from datetime import date, timedelta
import calendar
from django.shortcuts import render
from .models import DailyRecord

def calendar_view(request):
    today = date.today()

    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))
    day = request.GET.get("day")

    if day:
        selected_date = date(year, month, int(day))
    else:
        selected_date = date(year, month, 1)

    # 月の日数
    _, last_day = calendar.monthrange(year, month)

    # 日付一覧（横スクロール）
    days = [
        date(year, month, d)
        for d in range(1, last_day + 1)
    ]

    # ⇔ 前月・次月
    prev_month = (date(year, month, 1) - timedelta(days=1)).replace(day=1)
    next_month = (date(year, month, last_day) + timedelta(days=1)).replace(day=1)

    records = DailyRecord.objects.filter(date=selected_date)

    context = {
        "year": year,
        "month": month,
        "selected_date": selected_date,
        "days": days,
        "records": records,
        "prev_month": prev_month,
        "next_month": next_month,
    }
    return render(request, "calendar/calendar.html", context)
