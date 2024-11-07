lsaX2 - Real-Time 3D Telemetry Visualization
Overview
elsaX2 is a cutting-edge real-time telemetry visualization project designed to transmit and display live telemetry data from an ESP32 microcontroller to a Raspberry Pi 4 over Wi-Fi. The project is specifically developed to display roll, pitch, cone_roll, and cone_pitch values on an interactive, locally-hosted website. This visualization includes dynamic 3D models and real-time data charts, making it a powerful tool for aerospace telemetry analysis and monitoring.

Features
Real-Time Telemetry Transmission: Data from ESP32 is transmitted to Raspberry Pi 4 with a latency of under 1 second.
3D Model Visualization:
Two custom 3D models (.obj format) display live roll and pitch movements.
First 3D model responds to roll and pitch values.
Second 3D model moves in response to cone_roll and cone_pitch.
Interactive Data GUI:
Charts displaying roll, pitch, cone_roll, and cone_pitch values.
Branding elements for elsaX2.
Data speedometer with color-coded indicators (turns red if speed exceeds 60).
Servo values column for actuator control insights.
Serial monitor for real-time serial data.
Locally Hosted Website: Displays telemetry values on a webpage hosted on the Raspberry Pi 4, enabling easy access to live monitoring and data visualization.

Usage
Power on the ESP32 and Raspberry Pi 4.
Connect to the Raspberry Pi’s locally hosted site to view live telemetry data.
Use the GUI to monitor:
Real-time 3D model: Watch the model’s orientation respond to roll/pitch and cone_roll/cone_pitch values.
Speedometer: View speed data with alerts if speed exceeds 60.
Charts: Track roll, pitch, cone_roll, and cone_pitch values over time.
Serial Monitor: Observe live serial data output.
Hardware Requirements
ESP32 with gyroscope (connected for roll/pitch and cone_roll/cone_pitch data).
Raspberry Pi 4 (running Flask server and locally hosting the webpage).
Wi-Fi connection for seamless data transmission.
Acknowledgments
This project was developed as part of Pacifest and CBSC Nationals. Special thanks to Aarav Singh for the project

