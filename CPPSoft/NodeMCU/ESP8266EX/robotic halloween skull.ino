#include <Wire.h> // prerequisites
#include "paj7620.h"
#define GES_REACTION_TIME 200
#define GES_ENTRY_TIME 400
#define GES_QUIT_TIME 500
#include <FastLED.h>
const int LED_PIN_NUMBER = D3;
const int NUMBER_LEDS = 20;
CRGB leds[NUMBER_LEDS];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  FastLED.addLeds<NEOPIXEL, LED_PIN_NUMBER>(leds, NUMBER_LEDS);
  FastLED.clear();
  uint8_t error = 0;
  Serial.begin(9600);
  Serial.println("\nPAJ7620U2 TEST DEMO: Recognize 9 gestures.");
  error = paj7620Init();
  if (error) 
  {
    Serial.print("INIT ERROR, CODE:");
    Serial.println(error);
  }
  else
  {
    Serial.println("INIT OK!");
  }
  Serial.println("Please input your gestures:\n");
}
 
void loop() {
  // put your main code here, to run repeatedly:
  uint8_t data = 0, data1 = 0, error;
  error = paj7620ReadReg(0x43, 1, &data);   
  Serial.println(error);
  Serial.println(data);
  if (!error) {
    switch (data) {
      case GES_FORWARD_FLAG:
        Graduate_Normal_RGB();
        break;
      case GES_BACKWARD_FLAG:
        Graduate_Middle_RGB();
        break;
      case GES_RIGHT_FLAG:
        LedsOn_Normal();
        break;
      case GES_LEFT_FLAG:
        LedsOn_Red();
        break;
      case GES_UP_FLAG:
        LedsOn_Green();
        break;
      case GES_DOWN_FLAG:
        LedsOn_Blue();
        break;
      default:
        LedsOn_RGB();
    }
  }
}

void LedsOn_Normal() {
  // put your code to turn all the LEDs with white on at the same time:
  for (int i = 0; i < NUMBER_LEDS; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
  FastLED.show();
  delay(100);
}

void LedsOn_Red() {
  // put your code to turn all the LEDs with red on at the same time:
  for (int i = 0; i < NUMBER_LEDS; i++) {
    leds[i] = CRGB(255, 0, 0);
  }
  FastLED.show();
  delay(100);
}

void LedsOn_Green() {
  // put your code to turn all the LEDs with green on at the same time:
  for (int i = 0; i < NUMBER_LEDS; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
  FastLED.show();
  delay(100);
}

void LedsOn_Blue() {
  // put your code to turn all the LEDs with blue on at the same time:
  for (int i = 0; i < NUMBER_LEDS; i++) {
    leds[i] = CRGB(0, 0, 255);
  }
  FastLED.show();
  delay(100);
}

void LedsOn_RGB() {
  // put your code to turn all the LEDs with RGB on at the same time:
  RGB_Color_Codes_LEDs();
}

void LedsOff() {
  // put your code to turn all the LEDs off at the same time:
  for (int i = 0; i < NUMBER_LEDS; i++) {
    leds[i] = CRGB(0, 0, 0);
  }
  FastLED.show();
  delay(100);
}

void LedsFlash() {
  // put your code to make all the LEDs flash at the same time:
  LedsOn_Normal();
  LedsOff();
}

void Graduate_Normal_RGB() {
  // put your Graduate_Normal_RGB code here:
  FastLED.clear();
  delay(50);
  leds[0] = CRGB(255, 0, 0);
  delay(80);
  FastLED.show();
  leds[1] = CRGB(255, 128, 0);
  delay(80);
  FastLED.show();
  leds[2] = CRGB(255, 255, 0);
  delay(80);
  FastLED.show();
  leds[3] = CRGB(0, 255, 0);
  delay(80);
  FastLED.show();
  leds[4] = CRGB(0, 204, 0);
  delay(80);
  FastLED.show();
  leds[5] = CRGB(0, 0, 153);
  delay(80);
  FastLED.show();
  leds[6] = CRGB(76, 0, 153);
  delay(80);
  FastLED.show();
  leds[7] = CRGB(153, 0, 153);
  delay(80);
  FastLED.show();
  leds[8] = CRGB(153, 0, 76);
  delay(80);
  FastLED.show();
  leds[9] = CRGB(255, 255, 255);
  delay(80);
  FastLED.show();
  leds[10] = CRGB(153, 0, 76);
  delay(80);
  FastLED.show();
  leds[11] = CRGB(153, 0, 153);
  delay(80);
  FastLED.show();
  leds[12] = CRGB(76, 0, 153);
  delay(80);
  FastLED.show();
  leds[13] = CRGB(0, 0, 153);
  delay(80);
  FastLED.show();
  leds[14] = CRGB(0, 204, 0);
  delay(80);
  FastLED.show();
  leds[15] = CRGB(0, 255, 0);
  delay(80);
  FastLED.show();
  leds[16] = CRGB(255, 255, 0);
  delay(80);
  FastLED.show();
  leds[17] = CRGB(255, 128, 0);
  delay(80);
  FastLED.show();
  leds[18] = CRGB(255, 0, 0);
  delay(80);
  FastLED.show();
  leds[19] = CRGB(255, 255, 255);
  delay(50);
  FastLED.show();
}

void Graduate_Middle_RGB() {
  // put your Graduate_Middle_RGB code here:
  FastLED.clear();
  delay(50);
  leds[9] = CRGB(255, 0, 0);
  FastLED.show();
  leds[10] = CRGB(255, 0, 0);
  delay(80);
  FastLED.show();
  leds[8] = CRGB(255, 128, 0);
  FastLED.show();
  leds[11] = CRGB(255, 128, 0);
  delay(80);
  FastLED.show();
  leds[7] = CRGB(255, 255, 0);
  FastLED.show();
  leds[12] = CRGB(255, 255, 0);
  delay(80);
  FastLED.show();
  leds[6] = CRGB(0, 255, 0);
  FastLED.show();
  leds[13] = CRGB(0, 255, 0);
  delay(80);
  FastLED.show();
  leds[5] = CRGB(0, 204, 0);
  FastLED.show();
  leds[14] = CRGB(0, 204, 0);
  delay(80);
  FastLED.show();
  leds[4] = CRGB(0, 0, 153);
  FastLED.show();
  leds[15] = CRGB(0, 0, 153);
  delay(80);
  FastLED.show();
  leds[3] = CRGB(76, 0, 153);
  FastLED.show();
  leds[16] = CRGB(76, 0, 153);
  delay(80);
  FastLED.show();
  leds[2] = CRGB(153, 0, 153);
  FastLED.show();
  leds[17] = CRGB(153, 0, 153);
  delay(80);
  FastLED.show();
  leds[1] = CRGB(153, 0, 76);
  FastLED.show();
  leds[18] = CRGB(153, 0, 76);
  delay(80);
  FastLED.show();
  leds[0] = CRGB(255, 255, 255);
  FastLED.show();
  leds[19] = CRGB(255, 255, 255);
  delay(50);
  FastLED.show();
}

void Snake_RGB() {
  // put your Snake_RGB code here:
  FastLED.clear();
  delay(50);
  leds[0] = CRGB(255, 0, 0);
  delay(80);
  FastLED.show();
  leds[1] = CRGB(255, 128, 0);
  delay(80);
  FastLED.show();
  leds[2] = CRGB(255, 255, 0);
  delay(80);
  FastLED.show();
  leds[3] = CRGB(0, 255, 0);
  delay(80);
  FastLED.show();
  leds[4] = CRGB(0, 204, 0);
  delay(80);
  FastLED.show();
  leds[5] = CRGB(0, 0, 153);
  delay(80);
  FastLED.show();
  leds[6] = CRGB(76, 0, 153);
  delay(80);
  FastLED.show();
  leds[7] = CRGB(153, 0, 153);
  delay(80);
  FastLED.show();
  leds[8] = CRGB(153, 0, 76);
  delay(80);
  FastLED.show();
  leds[9] = CRGB(255, 255, 255);
  delay(80);
  FastLED.show();
  leds[0] = CRGB(0, 0, 0);
  FastLED.show();
  leds[10] = CRGB(153, 0, 76);
  delay(80);
  FastLED.show();
  leds[1] = CRGB(0, 0, 0);
  FastLED.show();
  leds[11] = CRGB(153, 0, 153);
  delay(80);
  FastLED.show();
  leds[2] = CRGB(0, 0, 0);
  FastLED.show();
  leds[12] = CRGB(76, 0, 153);
  delay(80);
  FastLED.show();
  leds[3] = CRGB(0, 0, 0);
  FastLED.show();
  leds[13] = CRGB(0, 0, 153);
  delay(80);
  FastLED.show();
  leds[4] = CRGB(0, 0, 0);
  FastLED.show();
  leds[14] = CRGB(0, 204, 0);
  delay(80);
  FastLED.show();
  leds[5] = CRGB(0, 0, 0);
  FastLED.show();
  leds[15] = CRGB(0, 255, 0);
  delay(80);
  FastLED.show();
  leds[6] = CRGB(0, 0, 0);
  FastLED.show();
  leds[16] = CRGB(255, 255, 0);
  delay(80);
  FastLED.show();
  leds[7] = CRGB(0, 0, 0);
  FastLED.show();
  leds[17] = CRGB(255, 128, 0);
  delay(80);
  FastLED.show();
  leds[8] = CRGB(0, 0, 0);
  FastLED.show();
  leds[18] = CRGB(255, 0, 0);
  delay(80);
  FastLED.show();
  leds[9] = CRGB(0, 0, 0);
  FastLED.show();
  leds[19] = CRGB(255, 255, 255);
  delay(80);
  FastLED.show();
  leds[10] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[11] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[12] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[13] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[14] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[15] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[16] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[17] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[18] = CRGB(0, 0, 0);
  delay(80);
  FastLED.show();
  leds[19] = CRGB(0, 0, 0);
  delay(50);
  FastLED.show();
}

void Messy_Combination() {
  RGB_Color_Codes_LEDs();
  Snake_RGB();
  
}

void RGB_Color_Codes_LEDs() {
  // put your RGB_Color_Codes_LEDs setting here:
  leds[0] = CRGB(255, 0, 0);
  leds[1] = CRGB(255, 128, 0);
  leds[2] = CRGB(255, 255, 0);
  leds[3] = CRGB(0, 255, 0);
  leds[4] = CRGB(0, 204, 0);
  leds[5] = CRGB(0, 0, 153);
  leds[6] = CRGB(76, 0, 153);
  leds[7] = CRGB(153, 0, 153);
  leds[8] = CRGB(153, 0, 76);
  leds[9] = CRGB(255, 255, 255);
  leds[10] = CRGB(153, 0, 76);
  leds[11] = CRGB(153, 0, 153);
  leds[12] = CRGB(76, 0, 153);
  leds[13] = CRGB(0, 0, 153);
  leds[14] = CRGB(0, 204, 0);
  leds[15] = CRGB(0, 255, 0);
  leds[16] = CRGB(255, 255, 0);
  leds[17] = CRGB(255, 128, 0);
  leds[18] = CRGB(255, 0, 0);
  leds[19] = CRGB(255, 255, 255);
}
