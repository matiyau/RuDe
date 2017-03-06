//moves=["x", "x2", "x'", "y", "y2", "y'", "U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]
#define SEQ_SRT '*'
#define SEQ_STP '#'
#define SEQ_SEP '<'

char dcsn_char;

int rots(int rot_code)
{
  return 1;
  return 0;
} 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
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
    if (!rots(Serial.parseInt()))
    {
      Serial.print("Q");
      return;
    }
    dcsn_char=Serial.read();
  }
  Serial.print("N");  
}
