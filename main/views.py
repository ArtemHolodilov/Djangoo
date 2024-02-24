from django.shortcuts import render
from django.http import HttpResponse


def australia(reqest):
    return render(reqest, 'main/australia.html')


def eurasia(reqest):
    return render(reqest, 'main/eurasia.html')


def africa(reqest):
    return render(reqest, 'main/africa.html')


def southamerica(reqest):
    return render(reqest, 'main/southamerica.html')


def northamerica(reqest):
    return render(reqest, 'main/northamerica.html')


def main(reqest):
    return render(reqest, 'main/main.html')


def antarctica(reqest):
    return render(reqest, 'main/antarctica.html')


