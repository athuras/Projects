//Slave Test Implementation
//Slave receives command from master to turn on a certain LED
//slave translates command into proper pin references 

#include <Wire.h>

int enable = 7;
int select1 = 6;
int select2 = 5;

void setup(){
  pinMode(enable, OUTPUT);
  pinMode(select1, OUTPUT);
  pinMode(select2, OUTPUT);
  digitalWrite(enable, LOW);
  Wire.begin(4); 
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}

void loop(){
  delay(100);
}

void receiveEvent(int howMany){
   int x = Wire.read();
   triggerOutput(x);
   Serial.println(x);
  
}

void triggerOutput(int cnt){
    if (cnt % 4 == 0){
      digitalWrite(select1, HIGH);
      digitalWrite(select2, HIGH);
   } if (cnt % 4 ==  1){
       digitalWrite(select1, HIGH);
       digitalWrite(select2, LOW);
   } if (cnt % 4 == 2){
       digitalWrite(select1, LOW);
       digitalWrite(select2, HIGH);
   } if (cnt % 4 == 3){ 
       digitalWrite(select1, LOW);
       digitalWrite(select2, LOW);
   } 
}
