import datetime
from datetime import timedelta


def zmiana_czasu(dif_time):
    total_seconds = 0
    parts = dif_time.split()
    for part in parts:
        if part[-1] == 'd':
            total_seconds += int(part[:-1]) * 24 * 3600
        if part[-1] == 'h':
            total_seconds += int(part[:-1]) * 3600
        if part[-1] == 'm':
            total_seconds += int(part[:-1]) * 60
        if part[-1] == 's':
            total_seconds += int(part[:-1])
    return timedelta(seconds=total_seconds)


def main():
    dif_time = input("Podaj różnicę czasu, którą masz na myśli w formacie 'Xd' 'Xh' 'Xm' 'Xs': ")
    czas_aktualny = datetime.datetime.now()
    gmt_time = datetime.datetime.utcnow()
    print("Bierzący czas to: ", czas_aktualny.strftime('%a, %d %b %Y, %H:%M:%S , %Z'))
    print("Lokalny czas GMT to: ", gmt_time.strftime('%a, %d %b %Y, %H:%M:%S , %Z'))

    time_difference = zmiana_czasu(dif_time)
    new_time = czas_aktualny + time_difference
    print("Data i czas po dodaniu różnicy czasu: ", new_time.strftime('%a, %d %b %Y, %H:%M:%S , %Z'))

    new_time2 = czas_aktualny - time_difference
    print("Data i czas po odjęciu różnicy czasu: ", new_time2.strftime('%a, %d %b %Y, %H:%M:%S , %Z'))


if __name__ == "__main__":
    main()
