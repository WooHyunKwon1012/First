#include <SoftwareSerial.h>
#include <MsTimer2.h>
#define TX 12
#define RX 13
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>




int speed = 255;
int motor_Ab=6;
int motor_Aa=5;
int motor_Bb=10;
int motor_Ba=9;
int buzzor=11;
int Echo =A0;
int Tri=A1;
int Encoder_0=2;
int Encoder_1=3;

char ble=0;
SoftwareSerial myBlue(TX,RX);

void setup() {
  Serial.begin(9600);
  myBlue.begin(9600);
  pinMode(motor_Ab,OUTPUT);
  pinMode(motor_Aa,OUTPUT);
  pinMode(motor_Bb,OUTPUT);
  pinMode(motor_Ba,OUTPUT);
  pinMode(buzzor,OUTPUT);
  pinMode(Echo,INPUT);
  pinMode(Tri,OUTPUT);
  
}

void loop() {
  
  

  analogWrite(Tri,0);
  delayMicroseconds(2);
  analogWrite(Tri,255);
  delayMicroseconds(10);
  analogWrite(Tri,0);
  delayMicroseconds(2);
  long duration=pulseIn(Echo,HIGH);
  long distance=(duration/2)/29.1;

  if(distance<10){
    analogWrite(motor_Aa,HIGH);
    analogWrite(motor_Ba,HIGH);
    analogWrite(motor_Ab,HIGH);
    analogWrite(motor_Bb,HIGH);
    Serial.println(distance);
    analogWrite(buzzor,30);
    delay(300);
    analogWrite(buzzor,0);
  }
  
  
  if(myBlue.available()>0){   //입력 데이터가 있나?
    char ble=myBlue.read();        //아두이노로 바이트 이지 ㄴ데이터 전달 . Serial.print(): ASC2코드 텍스트 전달
    Serial.write(ble);
    
    if(ble=='U'){
      analogWrite(motor_Aa,100);
      analogWrite(motor_Ba,100);
      analogWrite(motor_Ab,LOW);
      analogWrite(motor_Bb,LOW);
      
    }
    if(ble=='D'){
      analogWrite(motor_Aa,LOW);
      analogWrite(motor_Ba,LOW);
      analogWrite(motor_Ab,100);
      analogWrite(motor_Bb,100);
      
    }
    if(ble=='R'){
      analogWrite(motor_Aa,100);
      analogWrite(motor_Ba,LOW);
      analogWrite(motor_Ab,LOW);
      analogWrite(motor_Bb,LOW);
      
    }
    if(ble=='L'){
      analogWrite(motor_Aa,LOW);
      analogWrite(motor_Ba,100);
      analogWrite(motor_Ab,LOW);
      analogWrite(motor_Bb,LOW);
      
    }
    if(ble=='S'){
      analogWrite(motor_Aa,HIGH);
      analogWrite(motor_Ba,HIGH);
      analogWrite(motor_Ab,HIGH);
      analogWrite(motor_Bb,HIGH);
      
    }
    if(ble=='T'){
      analogWrite(motor_Aa,speed);
      analogWrite(motor_Ba,speed);
      analogWrite(motor_Ab,LOW);
      analogWrite(motor_Bb,LOW);
      delay(300);
    }
    if(ble=='B'){
      analogWrite(buzzor,30);
      delay(300);
      analogWrite(buzzor,0);
      delay(1000);
    }
  }
  
 
}
