#define RPIN 11
#define BPIN 10
#define GPIN 9

int in = 0;
String r = "";
String g = "";
String b = "";

void setup() {
  Serial.begin(9600);
  pinMode(RPIN, OUTPUT);
  pinMode(GPIN, OUTPUT);
  pinMode(BPIN, OUTPUT);

}

void loop() {
  Serial.flush();
  if (Serial.available() > 0) {
    r = g = b = "";
    for (int i = 0; i < 3; i++) {
      /*for(int k = 0; k<2; k++){
        Serial.read();
      }*/
      for (int j = 0; j < 8; j++) {
        in = char(Serial.read() - 48);
        if (i == 0) {
          r += in;
        }
        if (i == 1) {
          g += in;
        }
        if (i == 2) {
          b += in;
        }
      }
    }
    while (Serial.available () > 0) {
      Serial.read();
    }
  }
  /*Serial.println(r + " " + g + " " + b);
  Serial.println(bin2int(r));
  Serial.println(bin2int(g));
  Serial.println(bin2int(b));*/

  analogWrite(RPIN,bin2int(r));
  analogWrite(GPIN,bin2int(g));
  analogWrite(BPIN,bin2int(b));

  delay(500);
}

int bin2int(String bin) {
  int decimal = 0;
  for (int i = 0; i < bin.length(); i++) {
    decimal *= 2;
    if (bin.charAt(i) == '1') {
      decimal++;
    }
  }
  return decimal;
}

