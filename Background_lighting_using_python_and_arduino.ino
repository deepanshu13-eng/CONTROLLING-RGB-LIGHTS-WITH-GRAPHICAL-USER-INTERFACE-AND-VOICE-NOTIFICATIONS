String background;
int red = 7;
int blue = 9;
int green = 8;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(red, OUTPUT);
pinMode(blue, OUTPUT);
pinMode(green, OUTPUT);
digitalWrite(red, HIGH);
digitalWrite(blue, HIGH);
digitalWrite(green, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available() >0)
{
  background = Serial.readStringUntil('\n');
  if(background == "red on" || background == "RED ON")
  {
    digitalWrite(red,LOW);
    Serial.write("Red led is on"); //Communication of arduino with python
  }
  if(background == "blue on" || background == "BLUE ON")
  {
    digitalWrite(blue,LOW);
    Serial.write("Blue led is on"); //Communication of arduino with python
  }
  if(background == "green on" || background == "GREEN ON")
  {
    digitalWrite(green,LOW);
    Serial.write("Green led is on"); //Communication of arduino with python
  }
  if(background == "red off" || background == "RED OFF")
  {
    digitalWrite(red,HIGH);
    Serial.write("Red led is off"); //Communication of arduino with python
  }
  if(background == "blue off" || background == "BLUE OFF")
  {
    digitalWrite(blue,HIGH);
    Serial.write("Blue led is off"); //Communication of arduino with python
  }
  if(background == "green off" || background == "GREEN OFF")
  {
    digitalWrite(green,HIGH);
    Serial.write("Green led is off"); //Communication of arduino with python
  }
  if(background == "white off" || background == "WHITE OFF")
  {
    digitalWrite(green,HIGH);
    digitalWrite(red,HIGH);
    digitalWrite(blue,HIGH);
    Serial.write("White led is off"); //Communication of arduino with python
  }
  if(background == "white on" || background == "WHITE ON")
  {
    digitalWrite(green,LOW);
    digitalWrite(red,LOW);
    digitalWrite(blue,LOW);
    Serial.write("White led is on"); //Communication of arduino with python
  }
 if(background == "mergenta off" || background == "MERGENTA OFF")
  {
    digitalWrite(red,HIGH);
    digitalWrite(blue,HIGH);
    Serial.write("Mergenta colour is off"); //Communication of arduino with python
  } 
  if(background == "mergenta on" || background == "MERGENTA ON")
  {
    digitalWrite(red,LOW);
    digitalWrite(blue,LOW);
    Serial.write("Mergenta colour is on"); //Communication of arduino with python
  } 
  if(background == "cyan on" || background == "CYAN ON")
  {
    digitalWrite(green,LOW);
    digitalWrite(blue,LOW);
    Serial.write("Cyan colour is on"); //Communication of arduino with python
  } 
   if(background == "cyan off" || background == "CYAN OFF")
  {
    digitalWrite(green,HIGH);
    digitalWrite(blue,HIGH);
    Serial.write("Cyan colour is off"); //Communication of arduino with python
  } 
  if(background == "lemon green on" || background == "LEMON GREEN ON")
  {
    digitalWrite(green,LOW);
    digitalWrite(red,LOW);
    Serial.write("Lemon green colour is on"); //Communication of arduino with python
  } 
  if(background == "lemon green off" || background == "LEMON GREEN OFF")
  {
    digitalWrite(green,HIGH);
    digitalWrite(red,HIGH);
    Serial.write("Lemon green colour is off"); //Communication of arduino with python
  } 
   if(background == "all colours" || background == "ALL COLOURS")
  {
    for( int x = 0; x<2; x++){
      Serial.write("All colours will glow");
      digitalWrite(red,LOW);
      delay(4000);
      digitalWrite(red,HIGH);
      digitalWrite(blue,LOW);
      delay(4000);
      digitalWrite(blue,HIGH);
      digitalWrite(green,LOW);
      delay(4000);
      digitalWrite(green,HIGH);
      delay(10);
      digitalWrite(red,LOW);
      digitalWrite(blue,LOW);
      delay(4000);
      digitalWrite(red,HIGH);
      digitalWrite(blue,HIGH);
      delay(10);
      digitalWrite(green,LOW);
      digitalWrite(blue,LOW);
      delay(4000);
      digitalWrite(green,HIGH);
      digitalWrite(blue,HIGH);
      delay(10);
      digitalWrite(green,LOW);
      digitalWrite(red,LOW);
      delay(4000);
      digitalWrite(green,HIGH);
      digitalWrite(red,HIGH);
      
    }
    
  } 
}
}
