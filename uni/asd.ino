#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#include <Adafruit_NeoPixel.h>

uint32_t timer1;

const int relPin = 8; //реле + лампа
const int thermo = A0;//датчик температуры
const int dpt1 = 5;//дпт
const int pwm1 = 6;
const int dpt3 = 7;

const int led = 4; //свет лента
const int photo = A3; //фоторезистор
const int numpixels = 10;
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(numpixels, led, NEO_GRB + NEO_KHZ800);
Servo myservo;
Servo myservo2;

int gas_level_1_1;
int gas_level_1_2;
int gas_level_2_1;
int gas_level_2_2;
const int alarm_led = 11;

int izgib;

const int piezo = 9;
const int vibro = 10;

int hum;
int hum_high = 615;

const int button_alarm = 12;

LiquidCrystal_I2C lcd(32,16,2);

byte customChar[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};

byte arrowUp[] = {
  B00100,
  B01110,
  B10101,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100
};

byte arrowDown[] = {
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
  B10101,
  B01110,
  B00100
};
  
void setup() {
    Serial.begin(9600);
  
    lcd.begin(16,2);
    lcd.init();
    lcd.backlight();
    lcd.clear();
    //lcd.setCursor(0, 0);
    /*
    lcd.print("Lab. rabota 1");
    lcd.setCursor(0, 1);
    lcd.print("Kuznetsov D.");
    delay(3000);
    lcd.clear();
  
  // Делаем калибровку датчиков в течение 5 секунд
  int calibrationTime = 5000; 
  unsigned long startTime = millis(); // Запомнить время начала
  
  while (millis() - startTime < calibrationTime) {*/
        //lcd.setCursor(0, 0);
        //lcd.print("Calibration...");
  	    pinMode(relPin, OUTPUT);
  	    pinMode(thermo, INPUT);
  	    pinMode(dpt1, OUTPUT);
  	    pinMode(dpt3, OUTPUT);
  	    analogWrite(pwm1, 255);  
  	    analogReference(INTERNAL); //для датчика т-ры
  
  	    pinMode(photo, INPUT);
  	    pinMode(led, OUTPUT);
  	    myservo.attach(2);
  	    myservo2.attach(3);
  
  	    pixels.begin();
  
  	    pinMode(alarm_led, OUTPUT);
  	    pinMode(button_alarm, INPUT);
  	    pinMode(vibro, OUTPUT);
 // }
  //lcd.clear();
    lcd.setCursor (0, 0);
    lcd.print("1 2 3 4 5 6");
    lcd.createChar(0, customChar);
    lcd.createChar(1, arrowUp);
    lcd.createChar(2, arrowDown);
}


void loop()
{
  
    if(millis() - timer1 >= 200) {
    
        timer1 = millis();
    
        if (Serial.available() > 0) {
    	    char marker = Serial.read(); // Чтение маркера начала передачи данных
    	    if (marker == 'A') {
      		    gas_level_1_1 = Serial.parseInt(); // Чтение первого значения
      		    char separator = Serial.read(); // Чтение разделителя
      		    gas_level_1_2 = Serial.parseInt(); // Чтение второго значения
        	    char separator2 = Serial.read();
        	    gas_level_2_1 = Serial.parseInt();
        	    char separator3 = Serial.read();
        	    gas_level_2_2 = Serial.parseInt();
        	    char separator4 = Serial.read();
        	    izgib = Serial.parseInt();
          	    char sep5 = Serial.read();
          	    hum = Serial.parseInt();
            }
        }
    
	    //1: ТЕМПЕРАТУРА
    
        int read = analogRead(thermo);
        float voltage = (read * 1.1) / 1024.0; 
        float temp = (voltage - 0.5) * 100;
        //Serial.println("Themperature: " + String(temp))
        //ПОНИЖЕНА: При температуре менее 20 градусов будет вкл лампа
        if(temp < 20) { 
            digitalWrite(relPin, LOW);
            digitalWrite(dpt1, LOW);
            digitalWrite(dpt3, LOW);
            lcd.setCursor(1, 0);
            lcd.write(2);
        }
    
        //ПОВЫШЕНА: При температуре выше 30 будет вкл ДПТ
        else if(temp > 30)  {
            digitalWrite(relPin, HIGH);
            digitalWrite(dpt1, HIGH);
            digitalWrite(dpt3, LOW);
            lcd.setCursor(1, 0);
            lcd.write(1);
        }
    
        //НОРМ
        else {
            digitalWrite(relPin, HIGH);
            digitalWrite(dpt1, LOW);
            digitalWrite(dpt3, LOW);
            lcd.setCursor(1, 0);
            lcd.print(" ");
        }
    
        //2: УРОВЕНЬ ОСВЕЩЕНИЯ

        int light_level = analogRead(photo);
        //Serial.println("Light level: " + String(light_level));
    
        //ПОНИЖЕН
        if(light_level < 300) {
            myservo.write(-360);
            myservo2.write(360);
            lcd.setCursor(3, 0);
            lcd.write(2);
    	    for(int i = 0; i < numpixels; i++) {
        	    pixels.setPixelColor(i, pixels.Color(255, 250, 245));
    	    }
        }
        //НОРМ
        else if(light_level > 300 && light_level < 600) {
            lcd.setCursor(3, 0);
            lcd.print(" ");
            for (int i = 0; i < numpixels; i++) {
      		    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
            }
        }   
        else {
            //ПОВЫШЕН
            myservo.write(360);
            myservo2.write(-360);
            lcd.setCursor(3, 0);
            lcd.write(1);
            for (int i = 0; i < numpixels; i++) {
      		    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
            }   
        }
   	    pixels.show();
    
        //5-6: ЗАДЫМЛЕНИЕ
    
        int gas_alarm = 266;
        if(gas_level_1_1 >= gas_alarm && gas_level_1_2 >= gas_alarm ||
        gas_level_2_1 >= gas_alarm && gas_level_2_2 >= gas_alarm) {
            fireAlarm();
            if(gas_level_1_1 >= gas_alarm && gas_level_1_2 >= gas_alarm) {
            //5
            lcd.setCursor(9, 0);
            lcd.write(0);
            }
            if(gas_level_2_1 >= gas_alarm && gas_level_2_2 >= gas_alarm) {
                //6
                lcd.setCursor(11, 0);
                lcd.write(0);
            }
        }   
        else {
            noTone(piezo);
            digitalWrite(alarm_led, LOW);
            lcd.setCursor(9, 0);
            lcd.print(" ");
            lcd.setCursor(11, 0);
            lcd.print(" ");
        }
    
	    //3: ВЛАЖНОСТЬ
    
        if (hum >= hum_high) {
      	    //ПОВЫШЕНА
   		    digitalWrite(relPin, HIGH);
      	    digitalWrite(dpt1, HIGH);
      	    digitalWrite(dpt3, LOW);
      	    lcd.setCursor(5, 0);
      	    lcd.write(1);
        }   
        else {
            //НОРМ
            lcd.setCursor(5, 0);
            lcd.print(" ");
            if(temp > 30){}
            else {
                digitalWrite(dpt1, LOW);
                digitalWrite(dpt3, LOW);
            }
        }

        //4: ИЗГИБ
        if(izgib == 1) {
            lcd.setCursor(7, 0);
            lcd.write(0);
        }
        else {
            lcd.setCursor(7, 0);
            lcd.print(" ");
        }
    
  	    int alarm_button_read = digitalRead(button_alarm);
        if(alarm_button_read == HIGH) {
            fireAlarm();
        }
    }
}

void fireAlarm() {
    for (int i = 0; i < 6; i++) {   // включаем и выключаем вибромотор 6 раз (3 секунды / 0.5 секунды = 6 раз)
        digitalWrite(vibro, HIGH);     // включаем вибромотор
        delay(500);                    // ждем 0,5 секунды
        digitalWrite(vibro, LOW);      // выключаем вибромотор
        delay(500);                    // ждем 0,5 секунды
    }
    tone(piezo, 100);
    digitalWrite(alarm_led, HIGH);
    delay(3000);
    noTone(piezo);
    digitalWrite(alarm_led, LOW);
}

void sensorsCalibration() {
  
}
  