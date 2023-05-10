from django.shortcuts import render

# Create your views here.
def wtp_open(request):
    return render(
        request,
        'wtp_open/wtp_open.html'
    )