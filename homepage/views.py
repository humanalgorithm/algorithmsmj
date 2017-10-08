from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect


def aboutus(request):
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))


def learnmore(request):
    return render_to_response("learnmore.html",
                              locals(),
                              context_instance=RequestContext(request))


def pythonabout(request):
    return render_to_response("pythonabout.html",
                              locals(),
                              context_instance=RequestContext(request))


def fourzerofour(request):
    return render_to_response("404.html",
                              locals(),
                              context_instance=RequestContext(request))

def home(request):
    return render_to_response("learnmore.html",
                              locals(),
                              context_instance=RequestContext(request))