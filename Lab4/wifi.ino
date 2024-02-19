#include <WiFi.h> /*WIFI library included*/

#include <WiFiMulti.h> /*Multi WIFI library included*/

WiFiMulti wifiMulti;
/*Per AP connect time. Increase when ESP32 take more time for connection*/
const uint32_t connectTimeoutMs = 10000;
void setup()
{
    Serial.begin(115200); /*Serial communication begins*/
    delay(10);
    WiFi.mode(WIFI_STA); /*ESP32 WIFI initialized as Station*/
    /*Type all known SSID and their passwords*/
    wifiMulti.addAP("SECRET", "SECRET2"); /*Network 1 we want to connect*/
    wifiMulti.addAP("SECRET", "SECRET2"); /*Network 2 we want to connect*/
    // WiFi.scanNetworks will give total networks
    int n = WiFi.scanNetworks(); /*Scan for available network*/
    Serial.println("scan done");
    if (n == 0)
    {
        Serial.println("No Available Networks"); /*Prints if no network found*/
    }
    else
    {
        Serial.print(n);
        Serial.println(" Networks found"); /*Prints if network found*/
        for (int i = 0; i < n; ++i)
        {
            Serial.print(i + 1); /*Print the SSID and RSSI of available network*/
            Serial.print(": ");
            Serial.print(WiFi.SSID(i));
            Serial.print(" (");
            Serial.print(WiFi.RSSI(i));
            Serial.print(")");
            Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? " " : "*");
            delay(10);
        }
    }
    /*Connects to strongest available defined network with SSID and Password available*/
    Serial.println("Connecting to Wifi...");
    if (wifiMulti.run() == WL_CONNECTED)
    {
        Serial.println("");
        Serial.println("Connected to WIFI Network");
        Serial.println("IP address of Connected Network: ");
        Serial.println(WiFi.localIP()); /*Prints IP address of connected network*/
    }
}
void loop()
{
    if (wifiMulti.run(connectTimeoutMs) == WL_CONNECTED)
    { /*if the connection lost it will connect to next network*/
        Serial.print("WiFi connected: ");
        Serial.print(WiFi.SSID());
        Serial.print(" ");
        Serial.println(WiFi.RSSI());
    }
    else
    {
        Serial.println("WiFi not connected!"); /*if all conditions fail print this*/
    }
    delay(1000);
}
