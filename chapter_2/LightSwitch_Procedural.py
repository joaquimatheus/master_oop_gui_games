def turnOn():
    global switchIsOn

    switchIsOn = True

def turnOff():
    global switchIsOn

    switchIsOn = False

switchIsOn = False
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
