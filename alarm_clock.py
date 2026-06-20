from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        #Esto hace enfasis a cque despues de cierto tiempo la alarma va a sonar las veces que el dispositivo lo permita
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"Tiempo restante: {minutes_left} minutos y {seconds_left} segundos")

alarm(10)