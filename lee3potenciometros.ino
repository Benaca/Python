const int pinRED = A0;
const int pinGREEN = A1;
const int pinBLUE = A2;


void setup(){
  Serial.begin(115200); 
}

void loop(){ 

  Serial.print("R:");
  Serial.println(analogRead(A0));
  Serial.print("G:");
  Serial.println(analogRead(A1));
  Serial.print("B:");
  Serial.println(analogRead(A2));
  delay(100);
  
}
