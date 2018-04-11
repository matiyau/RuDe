//moves=["x", "x2", "x'", "y", "y2", "y'", "U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'", "RESET"]

#include<Servo.h>

#define SEQ_SRT '*'
#define SEQ_STP '#'
#define SEQ_SEP '<'

#define L_HOLD 11
#define U_HOLD 12
#define R_HOLD 13
#define D_HOLD 7

#define L_ROT 8
#define U_ROT 9
#define R_ROT 10

#define L_GRIP_ANG 150
#define U_GRIP_ANG 150
#define R_GRIP_ANG 150
#define D_GRIP_ANG 150

#define L_UGRIP_ANG 60
#define U_UGRIP_ANG 60
#define R_UGRIP_ANG 60
#define D_UGRIP_ANG 60

#define L_ROT_0 810
#define U_ROT_0 725
#define R_ROT_0 690

#define L_ROT_90
#define U_ROT_90
#define R_ROT_90

#define L_ROT_180 2370
#define U_ROT_180 2445
#define R_ROT_180 2205


Servo servo[7];

char dcsn_char;
byte stepState=0;
byte stepDelay=10;
byte stepPins[4]={2,4,3,5};

byte ROT_PTS[3][3]={{L_ROT_0, L_ROT_90, L_ROT_180}, {U_ROT_0, U_ROT_90, U_ROT_180}, {R_ROT_0, R_ROT_90, R_ROT_180}};
byte ROT_NOW[3]=={1, 1, 1};

void servoWrite(byte servoNum, byte servoPos)
{
  servo[servoNum].writeMicroseconds(ROT_PTS[servoNum][servoPos]);
  ROT_NOW[servoNum]=servoPos;
}

byte cubeRot(byte moveCode)
{
  if (moveCode == 15)
  {
    servo[0].write(90);
    servo[1].write(90);
    servo[2].write(90);
    servo[3].write(L_UGRIP_ANG);
    servo[4].write(U_UGRIP_ANG);
    servo[5].write(R_UGRIP_ANG);
    servo[6].write(D_GRIP_ANG);    
  }
  else if (moveCode/3 == 0)
  {
    fullXTurn(moveCode%3);
  }
  else if (moveCode/3 == 1)
  {
    fullYTurn(moveCode%3);
  }
  else if (moveCode/3 == 4)
  {
    fullYTurn(2);
    faceTurn(2, (moveCode%3)+1);
    fullYTurn(0);
  }
  else
  {
    faceTurn((moveCode/3)-1, (moveCode%3)+1);
  }
  return 1;
} 

void fullXTurn(byte stepCode)
{
  grip(2);
  if (stepCode==0)
  {
    servo[0].write(0);
    servo[2].write(0);
  }
  else if (stepCode==2)
  {
    servo[0].write(180);
    servo[2].write(180);
  }
  ugrip(2);
}

void fullYTurn(byte stepCode)
{
  byte stepDir;
  if (stepCode==1)
  {
    stepDir = 1;
    stepCode = 100;
  }
  else
  {
    stepDir = -(stepCode-1);
    stepCode = 50;
  }
  for (int stepCount = 0; stepCount<stepCode; stepCount++)
  {
    digitalWrite(stepPins[stepState], LOW);
    stepState = (stepState + stepDir + 4) % 4;
    digitalWrite(stepPins[stepState], HIGH);
    delay(stepDelay);
  }
}

void faceTurn(byte faceCode, byte rotCode)
{
  byte finPos = (servo[faceCode].read()+90*rotCode)%360;
  if (finPos==270)
  {
    if (rotCode==3)
    {
      servo[faceCode].write(servo[faceCode].read()+90);
      finPos = 0;
    }
    else
    {
      servo[faceCode].write(servo[faceCode].read()-90);
      finPos = 180;
    }
  }
  grip(faceCode);
  servo[faceCode].write(finPos);
  delay(500);
  ugrip(faceCode);
}

void grip(byte face)
{
  if (face==0 || face==2)
  {
    servo[3].write(L_GRIP_ANG);
    servo[5].write(R_GRIP_ANG);
    delay(500);
    servo[6].write(D_UGRIP_ANG);
    delay(500);
  }
  else
  {
    servo[4].write(U_GRIP_ANG);
    delay(500);
  }
}

void ugrip(byte face)
{
  if (face==0 || face==2)
  {
    servo[6].write(D_GRIP_ANG);
    delay(500);
    servo[3].write(L_UGRIP_ANG);
    servo[5].write(R_UGRIP_ANG);
    delay(500);
  }
  else
  {
    servo[4].write(U_UGRIP_ANG);
    delay(500);
  }
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(5,OUTPUT);
  servo[0].attach(L_ROT, L_ROT_PTS[0], L_ROT_PTS[2]);
  servo[1].attach(U_ROT, U_ROT_PTS[0], U_ROT_PTS[2]);
  servo[2].attach(R_ROT, R_ROT_PTS[0], R_ROT_PTS[2]);
  servo[3].attach(L_HOLD, 600, 2150);
  servo[4].attach(U_HOLD, 650, 2200);
  servo[5].attach(R_HOLD, 535, 2185);
  servo[6].attach(D_HOLD, 630, 2340);
  servo[0].write(90);
  servo[1].write(90);
  servo[2].write(90);
  servo[3].write(L_UGRIP_ANG);
  servo[4].write(U_UGRIP_ANG);
  servo[5].write(R_UGRIP_ANG);
  servo[6].write(D_GRIP_ANG);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()<1)
  {
    return;
  }
  if (Serial.read()!=SEQ_SRT)
  {
    return;
  }
  dcsn_char=Serial.read();
  while (dcsn_char!=SEQ_STP)
  {
    byte mov = Serial.parseInt();
    //Serial.println(mov);
    if (!cubeRot(mov))
    {
      Serial.print("Error");
      return;
    }
    
    dcsn_char=Serial.read();
  }
  Serial.write('N');  
}
