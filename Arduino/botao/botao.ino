#define x 13
#define y 12
#define botao 14
#define led 23

bool ledState = false;
bool lastButtonState = HIGH;

void setup() {
  Serial.begin(115200);
  pinMode(botao, INPUT_PULLUP);
  pinMode(led, OUTPUT);

  
}

void loop() {

int valorx = analogRead(x);
  int valory = analogRead(y);
  int estadobotao = digitalRead(botao);

  if (estadobotao == LOW && lastButtonState == HIGH) {
    // Alterne o estado do LED
    ledState = !ledState;
    digitalWrite(led, ledState ? HIGH : LOW);
  }

  
  lastButtonState = estadobotao;

  delay(100);
  

  

}
