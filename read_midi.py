import time
from rtmidi import API_LINUX_ALSA, MidiIn


def read_midi():
    alsa_midi = MidiIn(API_LINUX_ALSA)
    print(alsa_midi.get_ports())
    selected_port = int(input("Select port: "))
    with alsa_midi.open_port(selected_port) as open_port:
        timer = time.time()
        try:
            while True:
                message = open_port.get_message()
                if message:
                    message, deltatime = message
                    timer += deltatime
                    print(" @%0.6f %r" % (timer, message))
                    print(message)
        except KeyboardInterrupt:
            print('')
        finally:
            print("Exit.")

if __name__ == '__main__':
    read_midi()