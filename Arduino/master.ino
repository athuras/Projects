//Master Test Implementation
//Master will tell the slave to turn a certain light on
//Master uses a relative reference to the light, the slave maps to correct I/O pins

#include <Wire.h>
 
int cnt = 0;

void setup(){
 Wire.begin(); 
}

void loop(){
   Wire.beginTransmission(4);
   Wire.write(cnt++);
   Wire.endTransmission();
   
   delay(1000);
}
