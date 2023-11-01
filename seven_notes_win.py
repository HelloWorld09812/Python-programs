import winsound

notes = [262, 294, 330, 349, 392, 440, 494]
duration = 250
while True:
    for frequency in notes:
        winsound.Beep(frequency, duration)
