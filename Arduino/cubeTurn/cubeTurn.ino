//moves=["x", "x2", "x'", "y", "y2", "y'", "U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'", "RESET"]

#include<Servo.h>

#define SEQ_SRT '*'
#define SEQ_STP '#'
#define SEQ_SEP '<'

#define L_HOLD 7
#define U_HOLD 8
#define R_HOLD 9 //: Disabled For Servo Maitenance
//#define R_HOLD 10 //Dummy Pin
#define D_HOLD 6

#define L_ROT 3
#define U_ROT 4
#define R_ROT 5

#define L_GRIP_ANG 150
#define U_GRIP_ANG 150
#define R_GRIP_ANG 150
#define D_GRIP_ANG 150

#define L_UGRIP_ANG 70
#define U_UGRIP_ANG 70
#define R_UGRIP_ANG 70
#define D_UGRIP_ANG 70

#define L_ROT_0 810
#define U_ROT_0 600
#define R_ROT_0 690

#define L_ROT_90 1550
#define U_ROT_90 1350
#define R_ROT_90 1400

#define L_ROT_180 2370
#define U_ROT_180 2050
#define R_ROT_180 2205


Servo servo[7];

char dcsn_char;
byte stepState=0;
byte stepDelay=10;
byte stepPins[4]={A0,A3,A1,A2};

int ROT_PTS[3][3]={{L_ROT_0, L_ROT_90, L_ROT_180}, {U_ROT_0, U_ROT_90, U_ROT_180}, {R_ROT_0, R_ROT_90, R_ROT_180}};
byte ROT_NOW[3]={1, 1, 1};

void servoWrite(byte servoNum, byte servoPos)
{
  servo[servoNum].writeMicroseconds(ROT_PTS[servoNum][servoPos]);
  ROT_NOW[servoNum]=servoPos;
}

uint8_t cubeRot(uint8_t moveCode)
{
  if (moveCode == 15)
  {
    servoWrite(0,1);
    servoWrite(1,1);
    servoWrite(2,1);
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

uint8_t fullXTurn(uint8_t stepCode)
{
  servoWrite(0,1);
  servoWrite(2,1);
  grip(2);
  if (stepCode==0)
  {
    servoWrite(0,0);
    servoWrite(2,0);
  }
  else if (stepCode==2)
  {
    servoWrite(0,2);
    servoWrite(2,2);
  }
  ugrip(2);
}

uint8_t fullYTurn(uint8_t stepCode)
{
  uint8_t stepDir;
  if (stepCode==1)
  {
    stepDir = 1;
    stepCode = 100;
  }
  else
  {
    stepDir = 1-stepCode;
    stepCode = 50;
  }
  digitalWrite(stepPins[stepState], HIGH);
  digitalWrite(stepPins[(stepState+2)%4], LOW);
  digitalWrite(stepPins[(stepState+1)%4], HIGH);
  digitalWrite(stepPins[(stepState+3)%4], LOW);
  delay(stepDelay);
  for (uint8_t stepCount = 0; stepCount<stepCode; stepCount++)
  {
    stepState = (stepState + stepDir + 4) % 4;
    digitalWrite(stepPins[stepState], HIGH);
    digitalWrite(stepPins[(stepState+2)%4], LOW);
    digitalWrite(stepPins[(stepState+1)%4], HIGH);
    digitalWrite(stepPins[(stepState+3)%4], LOW);
    delay(stepDelay);
  }
  digitalWrite(stepPins[0], LOW);
  digitalWrite(stepPins[1], LOW);
  digitalWrite(stepPins[2], LOW);
  digitalWrite(stepPins[3], LOW);
  return 0;
}

uint8_t faceTurn(uint8_t faceCode, uint8_t rotCode)
{
  uint8_t finPos = (ROT_NOW[faceCode]+rotCode)%4;
  if (finPos==3)
  {
    if (rotCode==3)
    {
      servoWrite(faceCode,ROT_NOW[faceCode]+1);
      delay(500);
      finPos = 0;
    }
    else
    {
      servoWrite(faceCode,ROT_NOW[faceCode]-1);
      delay(500);
      finPos = 2;
    }
  }
  grip(faceCode);
  servoWrite(faceCode,finPos);  
  delay(500);
  ugrip(faceCode);
}

uint8_t grip(uint8_t face)
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
    servoWrite(0,1);
    servoWrite(2,1);
    servo[4].write(U_GRIP_ANG);
    delay(500);
    digitalWrite(stepPins[stepState], HIGH);
    digitalWrite(stepPins[(stepState+2)%4], LOW);
    digitalWrite(stepPins[(stepState+1)%4], HIGH);
    digitalWrite(stepPins[(stepState+3)%4], LOW);
    delay(stepDelay);
  }
}

uint8_t ugrip(uint8_t face)
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
    digitalWrite(stepPins[0], LOW);
    digitalWrite(stepPins[1], LOW);
    digitalWrite(stepPins[2], LOW);
    digitalWrite(stepPins[3], LOW);
  }
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(stepPins[0],OUTPUT);
  pinMode(stepPins[1],OUTPUT);
  pinMode(stepPins[2],OUTPUT);
  pinMode(stepPins[3],OUTPUT);
  digitalWrite(stepPins[0], LOW);
  digitalWrite(stepPins[1], LOW);
  digitalWrite(stepPins[2], LOW);
  digitalWrite(stepPins[3], LOW);
  servo[0].attach(L_ROT, ROT_PTS[0][0], ROT_PTS[0][2]);
  servo[1].attach(U_ROT, ROT_PTS[1][0], ROT_PTS[1][2]);
  servo[2].attach(R_ROT, ROT_PTS[2][0], ROT_PTS[2][2]);
  servo[3].attach(L_HOLD, 600, 2150);
  servo[4].attach(U_HOLD, 650, 2200);
  servo[5].attach(R_HOLD, 535, 2185);
  servo[6].attach(D_HOLD, 630, 2340);
  servoWrite(0,1);
  servoWrite(1,1);
  servoWrite(2,1);
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
  dcsn_char = '/0';
  while (dcsn_char!=SEQ_STP)
  {
    uint8_t mov = Serial.parseInt();
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
