#include<Servo.h>
Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo
int x;
int y;
int prevX;
int prevY;


void setup() {
  Serial.begin(9600);
  servoVer.attach(5); //Attach Vertical Servo to Pin 5
  servoHor.attach(10); //Attach Horizontal Servo to Pin 10
  servoVer.write(90);
  servoHor.write(90);

}

void pos() {
  if(prevX != x || prevY != y)
  {
    int servoX = map(x, 300, 0,170, 600);
    int servoY = map(y,0, 300,170, 45);
    /*
    servoX = min(servoX, 179);
    servoX = max(servoX, 1);
    servoY = min(servoY, 179);
    servoY = max(servoY, 1);
    */
    servoHor.write(servoX);
    servoVer.write(servoY);
  }
  delay(500);
}

void loop() {
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
       pos();
      }
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }

}
