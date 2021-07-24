from django.views.generic import TemplateView  # django が用意している View

class IndexView(TemplateView):  # TemplateView を継承させる
    template_name = "index.html"  # ユーザに返す HTML を指定