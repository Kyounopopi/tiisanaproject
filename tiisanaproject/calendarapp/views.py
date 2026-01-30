#views.py
from datetime import date, timedelta
import calendar
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import DailyRecord
from .forms import CommentForm, DailyRecordForm

def calendar_view(request):
    today = date.today()

    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))
    day = request.GET.get("day")

    # dayが指定されていない場合は今日の日付を使用
    if day:
        selected_date = date(year, month, int(day))
    else:
        # 現在の月を表示している場合は今日、それ以外は1日
        if year == today.year and month == today.month:
            selected_date = today
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


def edit_comment(request, record_id):
    record = get_object_or_404(DailyRecord, id=record_id)

    if request.method == "POST":
        # request.FILESを追加することで画像がアップロードされる
        form = CommentForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            # 編集した記録の日付でカレンダーにリダイレクト
            url = reverse('calendarapp:currender') + f'?year={record.date.year}&month={record.date.month}&day={record.date.day}'
            return redirect(url)
    else:
        form = CommentForm(instance=record)

    return render(request, "calendar/edit_comment.html", {
        "form": form,
        "record": record,
    })

def add_record(request):
    year = int(request.GET.get('year'))
    month = int(request.GET.get('month'))
    day = int(request.GET.get('day'))
    selected_date = date(year, month, day)

    record, created = DailyRecord.objects.get_or_create(date=selected_date)

    if request.method == 'POST':
        form = DailyRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            url = reverse('calendarapp:currender') + f'?year={year}&month={month}&day={day}'
            return redirect(url)
    else:
        form = DailyRecordForm(instance=record)

    return render(request, 'calendar/add_record.html', {
        'form': form,
        'selected_date': selected_date
    })