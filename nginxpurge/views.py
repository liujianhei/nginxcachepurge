from django.http import HttpResponse
from django.shortcuts import render, redirect
from nginxpurge.text2html import text2html
import os,subprocess
bashpath = "/home/liujianhei/codes/python/django/nginxpurge/bin"

def index(request):
    return render(request, 'clean.html', {})

def clean(request):
    url = request.GET['url']+'\n'
    fd = open("bin/url.txt", 'wb')
    fd.write(url)
    fd.close()
    cmdline0 = "dos2unix %s/url.txt" % bashpath
    subprocess.call(cmdline0, shell=True)    
    cmdline = "cd %s && ./nginx-purge.sh url.txt" % bashpath
    print cmdline
    subprocess.call(cmdline, shell=True, stdout=open('out.txt', 'w'),stderr=subprocess.STDOUT)
    return redirect('/results')

def results(request):
    fout = open('out.txt', 'r')
    consoleout = fout.read()
    fout.close()
    return HttpResponse(text2html(consoleout))
