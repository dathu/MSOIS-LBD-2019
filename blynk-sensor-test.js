var blynkLib = require('blynk-library');  //blynklib is a instance of blunk lib
var sensorLib = require('node-dht-sensor'); // instance of 

var AUTH = 'e14b98c7913943e0aead115b1ba70e2c';

// Setup Blynk
var blynk = new blynkLib.Blynk(AUTH);  // blynk is an object of class Blynk which is there in blynkLib instance
// new- dynamic memory allocation.. Blynk() constructor

// Setup sensor, exit if failed
var sensorType = 11; // 11 for DHT11, 22 for DHT22 and AM2302
var sensorPin  = 4;  // The GPIO pin number for sensor signal
if (!sensorLib.initialize(sensorType, sensorPin)) {   // initialize is a method/function .. two inputs
    console.warn('Failed to initialize sensor');
    process.exit(1);
}

// Automatically update sensor value every 2 seconds . setInterval event called every 5 seconds
setInterval(function() {
    var readout = sensorLib.read();
    blynk.virtualWrite(3, readout.temperature.toFixed(1));
    blynk.virtualWrite(4, readout.humidity.toFixed(1));
    
    console.log('Temperature:', readout.temperature.toFixed(1) + 'C');
    console.log('Humidity:   ', readout.humidity.toFixed(1)    + '%');
}, 5000);