const int buttonPin = 10;

const int dirPin = 2;
const int stepPin1 = 4;
const int stepPin2 = 5;
const int stepPin3 = 6;
const int stepPin4 = 7;
const int stepPin5 = 8;
const int stepPin6 = 3;
const int stepPin7 = 9;

const int stepsPerCycle = 1000;
const int stepDelayMicros = 800;

// Переменные для антидребезга кнопки
bool dirState = LOW;
bool lastButtonState = HIGH;  // кнопка не нажата (INPUT_PULLUP)
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);

  pinMode(dirPin, OUTPUT);

  pinMode(stepPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(stepPin4, OUTPUT);
  pinMode(stepPin5, OUTPUT);
  pinMode(stepPin6, OUTPUT);
  pinMode(stepPin7, OUTPUT);
  pinMode(12, OUTPUT);
  digitalWrite(dirPin, dirState);

  digitalWrite(stepPin1, LOW);
  digitalWrite(stepPin2, LOW);
  digitalWrite(stepPin3, LOW);
  digitalWrite(stepPin4, LOW);
  digitalWrite(stepPin5, LOW);
  digitalWrite(stepPin6, LOW);
  digitalWrite(stepPin7, LOW);
  Serial.begin(9600);
}

void stepAll() {
   for (int i = 0; i < 200; i++) {
     digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin4, HIGH);
    digitalWrite(stepPin5, HIGH);
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }

  for (int i = 0; i < 200; i++) {
 
    digitalWrite(stepPin2, HIGH);
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin4, HIGH);
    digitalWrite(stepPin5, HIGH);
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }
  for (int i = 0; i < 200; i++) {
    
    digitalWrite(stepPin3, HIGH);
    digitalWrite(stepPin4, HIGH);
    digitalWrite(stepPin5, HIGH);
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }
  for (int i = 0; i < 200; i++) {
  
    digitalWrite(stepPin4, HIGH);
    digitalWrite(stepPin5, HIGH);
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }

  for (int i = 0; i < 200; i++) {
  
    digitalWrite(stepPin5, HIGH);
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }
 for (int i = 0; i < 200; i++) {
    
   
    digitalWrite(stepPin6, HIGH);
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7,LOW);
    delayMicroseconds(stepDelayMicros);
  }
  for (int i = 0; i < 200; i++) {
  
    digitalWrite(stepPin7, HIGH);
    delayMicroseconds(stepDelayMicros);
  
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    digitalWrite(stepPin3, LOW);
    digitalWrite(stepPin4, LOW);
    digitalWrite(stepPin5, LOW);
    digitalWrite(stepPin6, LOW);
    digitalWrite(stepPin7, LOW);
    delayMicroseconds(stepDelayMicros);
  }
}

void loop() {
  int reading = digitalRead(buttonPin);
  //Serial.println(digitalRead(buttonPin));
  if(digitalRead(buttonPin) == 0){
    
    while(reading==0){}
    digitalWrite(12,HIGH);
    Serial.println(123);
   // delay(12300);
    dirState =  !dirState;
  digitalWrite(dirPin, dirState);

  // Запускаем шаги
 
    
    stepAll();
  
  
    
    }
    digitalWrite(12,LOW);
  
  
 
    


  lastButtonState = reading;
}