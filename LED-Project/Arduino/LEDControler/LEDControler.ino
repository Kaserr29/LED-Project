#include <ArduinoJson.h>

int colors[10][3];
int n = 0;
int d = 0;
int h = 0;

int rPin = 9;
int gPin = 10;
int bPin = 11;

boolean newColor = false;

const char* json = "{\"d\":10000,\"h\":10000,\"n\":4,\"c\":[[255,0,0],[0,255,0],[0,0,255],[255,255,255]]}";
//{"d":1000,"h":1000,"n":4,"c":[[255,0,0],[0,255,0],[0,0,255],[255,255,255]]}
void setup() {
  Serial.begin(9600);
  pinMode(rPin, OUTPUT);
  pinMode(gPin, OUTPUT);
  pinMode(bPin, OUTPUT);

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 3; j++) {
      colors[i][j] = 0;
    }
  }

  while (!Serial.available()) {
  }
  convertSerial();
}

void loop() {
  newColor = false;
  colorLoop(colors, n, d, h);
}

void colorFade(int pColor[], int nColor[], int d) {
  unsigned long start = millis();
  unsigned long p = millis() - start;
  int r = pColor[0];
  int g = pColor[1];
  int b = pColor[2];
  while (start + p <= start + d) {
    p = millis() - start;
    r = (p * nColor[0] - (p - d) * pColor[0]) / d;
    g = (p * nColor[1] - (p - d) * pColor[1]) / d;
    b = (p * nColor[2] - (p - d) * pColor[2]) / d;
    analogWrite(rPin, r);
    analogWrite(gPin, g);
    analogWrite(bPin, b);
    convertSerial();
    if (newColor) {
      break;
    }
  }
}

void colorHold(int color[], int h) {
  unsigned long start = millis();
  unsigned long p = millis() - start;
  while (start + p <= start + h) {
    p = millis() - start;
    analogWrite(rPin, color[0]);
    analogWrite(gPin, color[1]);
    analogWrite(bPin, color[2]);
    convertSerial();
    if (newColor) {
      break;
    }
  }
}

void colorLoop(int c[][3], int l, int d, int h) {
  for (int i = 0; i < l; i++) {
    if (i < l - 1) {
      colorFade(c[i], c[i + 1], d);
      colorHold(c[i + 1], h);
    }
    else {
      colorFade(c[i], c[0], d);
      colorHold(c[0], h);
    }
    convertSerial();
    if (newColor) {
      break;
    }
  }
}

void convertJson(String json) {
  const size_t bufferSize = 9*JSON_ARRAY_SIZE(3) + JSON_ARRAY_SIZE(9) + JSON_OBJECT_SIZE(4) + 120;
  DynamicJsonBuffer jsonBuffer(bufferSize);

  JsonObject& root = jsonBuffer.parseObject(json);

  d = root["d"];
  Serial.println(d);
  h = root["h"];
  Serial.println(h);
  n = root["n"];
  Serial.println(n);

  JsonArray& c = root["c"];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 3; j++) {
      colors[i][j] = c[i][j];
      Serial.println(colors[i][j]);
    }
  }
}

void convertSerial() {
  if (Serial.available()) {
    convertJson(Serial.readString());
    newColor = true;
  }
}


