'''Proba de Evaliacion Tecnoloxia Nicolás Gutiérrez Ávila 24/3/26'''
# Pregunta 3
#include "ABlocks_DHT.h"
#include <ESP32Servo.h>

double Temperatura;
double Humedad;
DHT dht23(23,DHT11);
Servo servo_18;

void setup()
{
  	pinMode(23, INPUT);
	servo_18.attach(18);

	Serial.begin(115200);
	Serial.flush();
	while(Serial.available()>0)Serial.read();

	dht23.begin();

}


void loop()
{
	yield();

  	Temperatura = dht23.readTemperature();
  	Humedad = dht23.readHumidity();
  	Serial.println(String("Temperatura")+String(Temperatura));
  	Serial.println(String("Humedad")+String(Humedad));
  	servo_18.write(3);
  	if (((Temperatura >= 22) || (Humedad >= 60))) {
  		servo_18.write(90);
  	}
  	else {
  		servo_18.write(3);
  	}

  	delay(2000);

}


























