#include <Stepper.h> // Include the header file
#include <Servo.h>

Servo myservo_1;  
Servo myservo_2;
Servo myservo_3;

// change this to the number of steps on your motor
#define STEPS 200
// create an instance of the stepper class using the steps and pins
Stepper stepper(STEPS, 8, 10, 9, 11);

int potpin_1 = 1;  
int potpin_2 = 2;
int potpin_3 = 3;
int val_1 = 0;    
int val_2 = 0;
int val_3 = 0;

int val = 0;
int potpin = 0;

void setup() {
  Serial.begin(9600);
  stepper.setSpeed(200);

  myservo_1.attach(7);  
  myservo_2.attach(6);
  myservo_3.attach(5);
}

void loop() {

potpin = map(analogRead(A0),0,1024,0,500);
if (potpin>val)
  stepper.step(5);
if (potpin<val)
  stepper.step(-5);

val = potpin;

Serial.println(val); //for debugging

val_2 = analogRead(potpin_2);
val_2 = map(val_2, 0, 1023, 0, 180);
myservo_2.write(val_2);
delay(15);
val_1 = analogRead(potpin_1);            // reads the value of the potentiometer (value between 0 and 1023)
val_1 = map(val_1, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
myservo_1.write(val_1);                  // sets the servo position according to the scaled value
delay(15);                               // waits for the servo to get there
val_3 = analogRead(potpin_3);
val_3 = map(val_3, 0, 1023, 0, 180);
myservo_3.write(val_3);
delay(15);
}
