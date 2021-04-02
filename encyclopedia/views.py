from django.shortcuts import render

from . import util
import markdown2,random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show(request,name):
    try:
        return render(request,"encyclopedia/entry_page.html",{
            "entries": markdown2.markdown(util.get_entry(name)),
            "entry_name":name
        })
    except:
        return render(request, "encyclopedia/no_match.html")

def search(request):
    entry_name=request.GET.get('q','')
    entry_list=[]
    res_list=[]
    entry_list=util.list_entries()
    try:
        return render(request, "encyclopedia/entry_page.html", {
            "entries": markdown2.markdown(util.get_entry(entry_name)),
            # "entry_name": util.list_entries()[util.list_entries().index(entry_name)]
            "entry_name": entry_name
        })
    except:
        try:
            for i in entry_list:
                j=i.lower()
                name=entry_name.lower()
                if name in j:
                    res_list.append(i)
            if len(res_list)==0:
                return render(request, "encyclopedia/no_match.html")
            else:
                return render(request,"encyclopedia/index.html",{
                    "entries":res_list
                })
        except:
            return render(request,"encyclopedia/no_match.html")

def no_match(request):
    return render(request, "encyclopedia/no_match.html")

def new_entry(request):
    return render(request,"encyclopedia/new_entry.html")

def create(request):
    title = request.GET.get('title','')
    content = request.GET.get('content','')
    list1=util.list_entries()
    for li in list1:
        if title.lower() not in li.lower():
            return render(request, "encyclopedia/no_match.html")
        else:
            util.save_entry(title,content)
            return render(request,"encyclopedia/success.html",{
                "entries": markdown2.markdown(util.get_entry(title))
            })

def random_page(request):
    entry_list=util.list_entries()
    list_num=len(entry_list)
    num=random.randint(0,list_num-1)
    return render(request, "encyclopedia/entry_page.html", {
        "entries": markdown2.markdown(util.get_entry(entry_list[num])),
        "entry_name":entry_list[num]
    })

def edit_entry(request, title):
    entry_title=title
    return render(request, "encyclopedia/edit_entry.html", {
        "entry":util.get_entry(entry_title),
        "name":entry_title
    })

def save_entry(request):
    title = request.GET.get('title', '')
    if title not in util.list_entries():
        return render(request, "encyclopedia/no_match.html")
    else:
        content = request.GET.get('content', '')
        util.save_entry(title, content)
        return render(request, "encyclopedia/success.html", {
            "entries": markdown2.markdown(util.get_entry(title))
        })