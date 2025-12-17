int dataPin = 8;    // к выводу 14 регистра SD
int clockPin = 9;  // к выводу 11 регистра (SH_CP)
int latchPin = 10;  // к выводу 12 регистра (ST_CP)
int dir = 12;
int f5 = 2;
int but = 4;
void setup() {
 pinMode(latchPin, OUTPUT);
 pinMode(clockPin, OUTPUT);
 pinMode(dataPin, OUTPUT);
 pinMode(f5, OUTPUT);
 pinMode(dir, OUTPUT);
 pinMode(but, INPUT_PULLUP);
 digitalWrite(latchPin, LOW);
 digitalWrite(dir,LOW);
 
 Serial.begin(9600);
 
}

void zero(){
digitalWrite(dir, HIGH);
for(int i=0; i<600; i++){
// Устанавливаем все 16 бит в 1 (два байта)
setByte(0b11111111);
delayMicroseconds(1000);

// Устанавливаем все 16 бит в 0 (два байта)
setByte(0b00000000);
delayMicroseconds(1000);
}
}

void start_up(){
  digitalWrite(dir, LOW); // направление

for (int i = 0; i < 500; i++) {
  setByte(0b11111111);
  delayMicroseconds(1000); // время импульса
  setByte(0b00000000);
  delayMicroseconds(1000); // пауза между шагами
}

}
void usk(){
   for(int i=0; i<300; i=i+50){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b11111111);
  delayMicroseconds(i);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(i);
  }
}
void les(){
  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b11111111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }
  
  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b01111111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00111111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00011111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00001111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00000111);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00000011);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }

  for(int i=0; i<300; i++){
  // Устанавливаем все 16 бит в 1 (два байта)
  setByte(0b00000001);
  delayMicroseconds(2000);

  // Устанавливаем все 16 бит в 0 (два байта)
  setByte(0b00000000);
  delayMicroseconds(2000);
  }
  
  
}
bool e = 0;
boolean buttonWasUp = true;  // была ли кнопка отпущена?
boolean ledEnabled = false; 
void loop() {
  //
 boolean buttonIsUp = digitalRead(but);
 if (buttonWasUp && !buttonIsUp) {
  buttonIsUp = digitalRead(but);
  delay(10);
  int chek_b = 0;
  
 
    delay(30);
   if (e == 0){
    Serial.println(e);
    e = 1;
        digitalWrite(f5, HIGH);
     start_up();
      usk();
      les();
      digitalWrite(f5, LOW);
    }
    else{
      Serial.println(2);
      e = 0;
      digitalWrite(f5, HIGH);
      
      digitalWrite(dir, HIGH);
      les();
      zero();
      digitalWrite(f5, LOW);
    
  }
  delay(100);

 }

 // 
 

  

}

void setByte(byte value) {
 digitalWrite(latchPin, LOW); // начинаем передачу данных
 // устанавливаем нужный байт
 shiftOut(dataPin, clockPin, LSBFIRST, value);
 digitalWrite(latchPin, HIGH); // прекращаем передачу данных
}