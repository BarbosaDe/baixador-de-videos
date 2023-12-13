from django.shortcuts import render
from django.http import HttpResponse
from .downloader import tools


def home(request):
    return render(request, 'index.html')




tl = tools.Tools()
def info(request):
    if request.method == "GET": return

    link = request.POST['video_id']
    tl.filter()
    return HttpResponse(link)
    

    
"""

https://www.youtube.com/watch?v=ij99kTigTh8&list=RDMMij99kTigTh8&start_radio=1

https://www.instagram.com/p/C0wcKwJtSWDvy0WgympQbTXHn_paJ7XoCWw5i00


"""