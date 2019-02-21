#include <SoftwareSerial.h>
#define HM11_RST 7

SoftwareSerial ble(0, 1);

void setup() {
  // rst HM-11 at power up
  pinMode(HM11_RST, OUTPUT);
  digitalWrite(HM11_RST, LOW);
  delay(100);
  digitalWrite(HM11_RST, HIGH);
  
  // initialize both serial ports:
  Serial.begin(9600);
  ble.begin(9600);
}

void loop() {
  // read from port 1, send to port 0:
  if (ble.available()) {
    int inByte = ble.read();
    Serial.write(inByte);
  }

  // read from port 0, send to port 1:
  if (Serial.available()) {
    int inByte = Serial.read();
    ble.write(inByte);
  }
}
