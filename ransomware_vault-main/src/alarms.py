from playsound import playsound


def generate_alarm(filename):
    print ("----------------------")
    print ("----------------------")
    print ("----------------------")
    print ("Issue in file: {}".format(filename))
    playsound("src/alarm.wav")
