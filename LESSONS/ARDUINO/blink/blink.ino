void setup() {
	
	pinMode(LED_BUILTIN, OUTPUT);
	}

void loop() {
	int  i=11;
	if(  i % 2 == 0  )
	{
		digitalWrite(LED_BUILTIN, HIGH);
		delay(1000);
		digitalWrite(LED_BUILTIN, LOW);
		delay(1000);
	}else{
		digitalWrite(LED_BUILTIN, HIGH);
		delay(100);
		digitalWrite(LED_BUILTIN, LOW);
		delay(100);
		}
	}

//  Export  Date: 05:45:00 PM - 17:Jul:2025;

