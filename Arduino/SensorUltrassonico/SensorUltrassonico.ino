#include <Ultrasonic.h> //Inclui a biblioteca do ultrassônico
Ultrasonic ultrassom(2, 4);

float distancia;
float dura;

void setup() {
  Serial.begin(115200);
}

void loop() {

  distancia = ultrassom.read();

  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");
  delay(1000);
}
