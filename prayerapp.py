def fajr(time , sulah):
    print(f"{salah} Timings i.e {time} ! Offer prayers !")
def duhar(time , sulah):
    print(f"{salah} Timings i.e {time} ! Offer prayers !")
def asr(time , sulah):
    print(f"{salah} Timings i.e {time} ! Offer prayers !")
def maghrib(time , sulah):
    print(f"{salah} Timings i.e {time} ! Offer prayers !")
def isha(time , sulah):
    print(f"{salah} Timings i.e {time} ! Offer prayers !")
time = int(input("Whats your time Now ? (0-24hrs) :"))
if time <= 4 :
    salah = "Duhr"
    duhr(time , salah)
elif time <= 6 :
    salah = "Asr"
    asr(time , salah)
elif time <= 6 :
    salah = "Asr"
    (time , salah)
elif time <= 7 :
    salah = "Maghrib"
    duhr(time , salah)
