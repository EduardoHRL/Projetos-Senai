
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <BH1750.h>

//Define o display I2C no endereco 0x3F
LiquidCrystal_I2C lcd(0x27, 16,2);

//Define o sensor BH1750
BH1750 lightMeter;

void setup()
{
  Serial.begin(115200);
  //Inicializa o LCD
  lcd.init();
  //Inicializa o BH1750
  lightMeter.begin();
}

void loop()
{
  //Le os valores do sensor de lux
  uint16_t lux = lightMeter.readLightLevel();
  
  //Mostra as informacoes na serial
  Serial.print("Luminosidade: ");
  Serial.print(lux);
  Serial.println(" lux");

  //Mostra as informacoes no LCD
  lcd.setBacklight(HIGH);
  lcd.setCursor(0, 0);
  lcd.print(" Sensor  BH1750");
  lcd.setCursor(0, 1);
  lcd.print("Lumin.:      lux");
  lcd.setCursor(8, 1);
  lcd.print(lux);
  
  delay(1000);
}