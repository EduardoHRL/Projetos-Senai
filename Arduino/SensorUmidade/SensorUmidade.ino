const int sensorUmidade = 34;
int leitura;
void setup() {
  Serial.begin(115200);
  pinMode(sensorUmidade, INPUT);

}
void loop() {
  leitura = analogRead(sensorUmidade);

  Serial.print("Valor do sensor de umidade: ");
  Serial.println(leitura);

  delay(1000);

}

