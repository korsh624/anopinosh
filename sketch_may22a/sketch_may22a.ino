#include "DHT.h"
#define DHTPIN 8
String data = "";
DHT dht(DHTPIN, DHT22);
///setPin13on - включает тестовый пин 13
///setPin13off - выключает тестовый пин
///intLight - внутренее освещение 2
///ExtLight - внешнее освещение 3
///OpenDoor - открывание двери(ворот)4
///OpenWindow - открывание окон 5
///backlight - режим автовключения подсветки
///autoLightMotion - режим автовключения света от движения
///TurnVent - включить вентеляцию  6
///AlarmSystem - сигнализация 7
String t = "nan";
void setup() {
  pinMode(13, OUTPUT);
  for (int i = 2; i < 8; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, 1);
  }
  dht.begin();
  Serial.begin(9600);
  digitalWrite(13, 0);
}
void readmessage(int pin, String message, int val) {

  if (data == message) {
    digitalWrite(pin, val);
    delay(1000);
    if (message == "GetTemp") {
      float temp = dht.readTemperature();
      t=String(temp);
      Serial.println(t);
      delay(500);
      digitalWrite(pin, 0);
    }
    else {
      Serial.println(data);
    }
  }

}
void loop() {
  if (Serial.available()) {
    data = Serial.readString();
  }
  readmessage(13, "setPin13on", 1);
  readmessage(13, "setPin13off", 0);
  readmessage(2, "intLighton", 0);
  readmessage(2, "intLightoff", 1);
  readmessage(3, "ExtLighton", 0);
  readmessage(3, "ExtLighton", 1);
  readmessage(4, "CloseDoor", 1);
  readmessage(4, "OpenDoor", 0);
  readmessage(5, "CloseWindow", 1);
  readmessage(5, "OpenWindow", 0);
  readmessage(6, "TurnVenton", 0);
  readmessage(6, "TurnVentoff", 1);
  readmessage(7, "AlarmSystemon", 0);
  readmessage(7, "AlarmSystemoff", 1);
  readmessage(13, "GetTemp", 1);

  data = "";
}
