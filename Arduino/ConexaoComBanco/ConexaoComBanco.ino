#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "Casa";
const char *password = "nildapereira";
const char *supabaseUrl = "https://vkrlyyyvattgjcwimumr.supabase.co";
const char *supabaseApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrcmx5eXl2YXR0Z2pjd2ltdW1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE4NDU5MTEsImV4cCI6MjAzNzQyMTkxMX0.RQYD0a8Z3jBXCsuglOSgGMbhisZEgtOVSdHDeTabCIk";

const int trigger = 2;
const int echo = 4;
float dist;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    float distancia = getDistancia();

    String jsonPayload = "{";
    jsonPayload += "\"distancia\":" + String(distancia);
    jsonPayload += "}";

    String url = String(supabaseUrl) + "/rest/v1/sensor_data";
    http.begin(url);
    http.addHeader("Content-Type", "application/json");
    http.addHeader("apikey", supabaseApiKey);
    http.addHeader("Authorization", "Bearer " + String(supabaseApiKey));

    int httpCode = http.POST(jsonPayload);
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(payload);
    } else {
      Serial.print("Erro na requisição: ");
      Serial.println(httpCode);
    }
    http.end();
  }
  delay(15000);
}

float getDistancia() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(5);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  dist = pulseIn(echo, HIGH);
  dist = dist / 58;
  return dist;
}
