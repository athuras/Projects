#include <Wire.h>
#define default_address = 24

void setup(){
  Wire.begin();
  Serial.begin(9600);
}

void loop(){
  check_new( default_address );
  
}

void check_new(int address){
  
