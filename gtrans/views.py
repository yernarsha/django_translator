from django.shortcuts import render
from googletrans import Translator


def translator(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)

        translator = Translator()
        tr = translator.translate(txt, dest=lang)

        return render(request, 'gtrans/index.html', {"result": tr.text, "source": txt})
    else:
        return render(request, 'gtrans/index.html')

