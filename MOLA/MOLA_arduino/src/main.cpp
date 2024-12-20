#include <Arduino.h>
#include <SPI.h>
#include <Ethernet.h>

// Network settings
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; // Change to ethernet shields MAC address
IPAddress ip(192, 168, 1, 177); // IP address to assign to the Arduino
unsigned int localPort = 8888; // Local port to listen on

// Buffer to hold incoming packet
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

// Ethernet UDP instance
EthernetUDP Udp;

void setup() {
  // Initialize Ethernet
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);
  Serial.begin(9600);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    // Read the packet into packetBuffer
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.print("Received packet: ");
    Serial.println(packetBuffer);

    // Process the packet
    // Assuming the packet contains comma-separated values
    char* token = strtok(packetBuffer, ",");
    int values[6];
    int index = 0;
    while (token != NULL && index < 6) {
      values[index] = atoi(token);
      token = strtok(NULL, ",");
      index++;
    }

    // Assign each item to its own variable
    int t1_cmd = values[0];
    int t2_cmd = values[1];
    int t3_cmd = values[2];
    int t4_cmd = values[3];
    int tz1_cmd = values[4];
    int tz2_cmd = values[5];

    // Print out the values
    Serial.print("t1_cmd: ");
    Serial.println(t1_cmd);
    Serial.print("t2_cmd: ");
    Serial.println(t2_cmd);
    Serial.print("t3_cmd: ");
    Serial.println(t3_cmd);
    Serial.print("t4_cmd: ");
    Serial.println(t4_cmd);
    Serial.print("tz1_cmd: ");
    Serial.println(tz1_cmd);
    Serial.print("tz2_cmd: ");
    Serial.println(tz2_cmd);
  }
}