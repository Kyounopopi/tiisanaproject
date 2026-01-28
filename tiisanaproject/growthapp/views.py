from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import GrowthRecord


class GrowthView(View):

    def get(self, request):
        """成長データ一覧を表示"""
        growth = GrowthRecord.objects.all().order_by("-date")
        return render(request, "growth.html", {
            "growth": growth
        })

    def post(self, request):
        """成長データを登録"""
        date = request.POST.get("date")
        baby_log = request.POST.get("baby_log")
        comment = request.POST.get("comment")

        # DB保存
        GrowthRecord.objects.create(
            date=date,
            baby_log=baby_log,
            comment=comment
        )

        # ✅ 登録完了画面へリダイレクト
        return redirect("growthapp:growth_complete")


class GrowthUpdateView(View):

    def get(self, request, pk):
        # 編集画面を表示
        record = GrowthRecord.objects.get(pk=pk)
        return render(request, "growth_update.html", {
            "record": record
        })

    def post(self, request, pk):
        # 更新処理
        record = GrowthRecord.objects.get(pk=pk)

        record.date = request.POST.get("date")
        record.baby_log = request.POST.get("baby_log")
        record.comment = request.POST.get("comment")

        record.save()
        return redirect("growthapp:growth_update_complete")


class GrowthDeleteView(View):

    def post(self, request, pk):
        record = get_object_or_404(GrowthRecord, pk=pk)
        record.delete()
        return redirect("growthapp:growth_delete_complete")

class GrowthCompleteView(View):
    def get(self, request):
        return render(request, "growth_complete.html")

class GrowthUpdateCompleteView(View):
    def get(self, request):
        return render(request, "growth_update_complete.html")

class GrowthDeleteCompleteView(View):
    def get(self, request):
        return render(request, "growth_delete_complete.html")