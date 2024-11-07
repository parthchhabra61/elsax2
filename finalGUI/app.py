import json
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
from threading import Thread

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

latest_json_data = None

class TelemetryServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data.json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open('data.json', 'r') as file:
                self.wfile.write(file.read().encode())
        else:
            super().do_GET()

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, TelemetryServer)
    print("Starting server at http://localhost:8000")
    httpd.serve_forever()

# Start the server in a separate thread
server_thread = Thread(target=run_server, daemon=True)
server_thread.start()

# Fetch data from JSON file
def fetch_data():
    global latest_json_data
    try:
        with open('data.json', 'r') as file:
            latest_json_data = json.load(file)
    except Exception as e:
        print(f"Error fetching data: {e}")

# Update telemetry data and display it
fig, ax = plt.subplots()
ax.set_title('Roll and Pitch')
ax.set_xlabel('Time')
ax.set_ylabel('Degrees')

roll_data, pitch_data, times = [], [], []

line1, = ax.plot(times, roll_data, label='Roll', color='r')
line2, = ax.plot(times, pitch_data, label='Pitch', color='b')
ax.legend()

# Update the chart with new data
def update_chart(frame):
    fetch_data()
    if latest_json_data is None:
        return

    current_time = time.strftime("%H:%M:%S", time.localtime())
    roll = latest_json_data.get('roll', 0)
    pitch = latest_json_data.get('pitch', 0)

    times.append(current_time)
    roll_data.append(roll)
    pitch_data.append(pitch)

    if len(times) > 10:
        times.pop(0)
        roll_data.pop(0)
        pitch_data.pop(0)

    line1.set_data(times, roll_data)
    line2.set_data(times, pitch_data)
    ax.relim()
    ax.autoscale_view()

# Set up 3D visualization for the rocket orientation
fig3d = plt.figure()
ax3d = fig3d.add_subplot(111, projection='3d')
ax3d.set_title("Rocket Orientation")

rocket_orientation = [0, 0, 0]

def update_3d_model():
    fetch_data()
    if latest_json_data is None:
        return

    global rocket_orientation
    roll = latest_json_data.get('roll', 0)
    pitch = latest_json_data.get('pitch', 0)

    rocket_orientation = [roll, pitch, 0]

    ax3d.clear()
    ax3d.quiver(0, 0, 0, rocket_orientation[0], rocket_orientation[1], rocket_orientation[2])
    ax3d.set_xlim([-360, 360])
    ax3d.set_ylim([-360, 360])
    ax3d.set_zlim([-360, 360])
    ax3d.set_xlabel('Roll')
    ax3d.set_ylabel('Pitch')
    ax3d.set_zlabel('Yaw')

# Run animations for telemetry charts and 3D models
ani_chart = animation.FuncAnimation(fig, update_chart, interval=500)
ani_3d = animation.FuncAnimation(fig3d, lambda frame: update_3d_model(), interval=500)

plt.show()
