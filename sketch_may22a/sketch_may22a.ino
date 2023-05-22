String data = "";
void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  digitalWrite(2, 0);
}

void loop() {
  if (Serial.available()) {
    data = Serial.readString();
    if (data == "starting") {
      digitalWrite(13, 1);
      delay(1000);
      digitalWrite(13, 0);
      Serial.println(data);
    }
  }
  data="";
}
