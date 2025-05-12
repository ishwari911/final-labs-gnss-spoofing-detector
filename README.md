
---

# GNSS Spoofing Detection Tool

## Problem Statement

Global Navigation Satellite System (GNSS) spoofing is a serious cybersecurity threat where attackers send fake GPS signals to deceive devices into believing they are in different locations. This can lead to significant risks, such as misguiding vehicles, drones, or other critical infrastructure. The goal of this project is to develop a tool that detects such spoofing attempts by analyzing GPS logs for unrealistic movement patterns or speed spikes.

This tool uses a **speed-based detection approach** to identify anomalies in GPS data that suggest possible spoofing. The analysis is based on the **Haversine formula**, which calculates the distance between two GPS coordinates, and compares the calculated speed to a predefined threshold.

## Project Goals

* Create a Python-based tool that processes GPS data logs (in NMEA format).
* Detect possible spoofing events based on speed anomalies.
* Provide alerts with timestamps and speed values when potential spoofing is detected.
* Offer a practical tool for experimenting with GNSS spoofing detection techniques.

## Project Structure

```
gnss-spoofing-detection/
├── detect_spoof.py          # Python script to detect spoofing using speed anomalies
├── sample_log.nmea         # Example GPS log in NMEA format
├── README.md               # Documentation and project setup instructions
└── LICENSE                 # License information (optional)
```

## Setup Instructions

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Clone the Repository**: Download or clone the project files.

   ```bash
   git clone https://github.com/ishwari911/final-labs-gnss-spoofing-detector.git

   ```
3. **Run the Script**:

   * The project uses basic Python libraries, so no additional dependencies are required.
   * You can run the script to check for spoofing in a GPS log file.

   ```bash
   python detect_spoof.py
   ```

   * The script will process the `sample_log.nmea` file, calculate the speeds, and flag potential spoofing attempts based on unusually high speeds.

## Example Attack Scenario

This tool detects when the calculated speed between two consecutive GPS positions exceeds a threshold (e.g., 300 km/h). This speed is usually unrealistic for regular GPS movement, indicating potential spoofing activity.

**Example Input**:

```
$GPRMC,123456.00,A,1234.56,N,09876.54,W,0.1,25.0,010522,000.0,E*6A
$GPRMC,123457.00,A,1235.56,N,09877.54,W,0.1,200.0,010522,000.0,E*6B
```

**Example Output**:

```
🚨 Possible spoofing at 12:34:57: Speed = 320.50 km/h
```

## Core Features

* **Speed-based spoofing detection**: Calculates the speed between GPS coordinates and flags high-speed anomalies.
* **Works offline**: Analyzes GPS log files locally.
* **Customizable**: Modify the speed threshold and adapt the code for real-time use.

## Real-World Use Cases

* **Autonomous vehicles**: Prevent GPS manipulation in self-driving cars.
* **Drones**: Detect spoofing attempts in drone navigation systems.
* **Critical infrastructure**: Secure GPS systems used in sectors like transportation, logistics, and aviation.

## Future Enhancements

* Integrate real-time GPS data analysis.
* Use machine learning for anomaly detection and better spoofing identification.
* Develop a web-based interface to visualize spoofing incidents on maps.

## Ethical & Educational Impact

* **Promotes cybersecurity awareness** by demonstrating the risks of GNSS spoofing.
* **Supports safe and ethical GPS usage** in critical industries, reducing the risk of malicious manipulation.

## Conclusion

GNSS spoofing is a growing threat, and this project aims to provide a practical tool to detect it. By identifying unrealistic speed and movement patterns, the tool helps raise awareness of this vulnerability and provides an educational demonstration of how to detect spoofing using GPS data logs.

---


