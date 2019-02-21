import bluepy.btle as btle


class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print(data.decode("utf-8")) # printing the data received from HM-11

p = btle.Peripheral("AA:E1:92:BB:79:CC") # change to address can be found using AT+ADDR?

s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb") # mostly same for all modules
p.withDelegate(ReadDelegate())
c = s.getCharacteristics()[0]

# only 20 bytes can be sent, 21+ will be split into a second packet.
c.write(bytes("Hello world\n", "utf-8")) # send message once to HM-11

while True:
    # if running HM-11 serialProxy program, then just wait for Hello world to be printed on the Arduino Serial Monitor
    # and then type anything on the serial and press enter will be printed in this terminal
    while p.waitForNotifications(1): # wait for any incoming messages from HM-11
        pass

p.disconnect()
