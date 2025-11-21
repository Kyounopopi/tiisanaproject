from django.shortcuts import render
from datetime import date
import calendar
# Create your views here.

def calendar_view(request, year=None, month=None):
    # 年と月を指定（URLパラメータが無ければ今日の年月）
    if year is None:  year = date.today().year
    if month is None: month = date.today().month

    year = int(year)
    month = int(month)

    # カレンダー生成（月の2次元配列）
    cal = calendar.Calendar(firstweekday=0)     # 0=月曜
    month_days = cal.monthdayscalendar(year, month)

    context = {
        "year": year,
        "month": month,
        "month_days": month_days,
        "month_name": calendar.month_name[month],
    }
    return render(request, "currender.html", context)
