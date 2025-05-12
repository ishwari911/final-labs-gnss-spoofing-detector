

# GNSS Spoofing Detection Tool

## Problem Statement

GNSS (Global Navigation Satellite System) spoofing is a malicious activity where attackers transmit fake GPS signals to mislead receivers. Spoofing can cause severe consequences in navigation, transportation, and military applications. Detecting such spoofing attempts is crucial to maintaining the integrity of GPS-based systems.

This project aims to develop a **GNSS Spoofing Detection Tool** that analyzes GPS log files, identifies anomalies, and alerts users to possible spoofing activities. The tool checks for irregularities like sudden jumps in location or abnormal speeds, which are common indicators of spoofing.

### Key Features:

* **GPS Log Parsing:** The tool processes GPS log files (in NMEA format) to extract location and speed data.
* **Speed Analysis:** It calculates the speed between consecutive GPS points and flags speeds that exceed a predefined threshold.
* **Distance Calculation:** The tool uses the Haversine formula to compute distances between GPS coordinates to check for large, suspicious jumps.
* **Spoofing Alerts:** If potential spoofing is detected, the tool raises alerts with the timestamp and details of the anomaly.

## Setup Instructions

### 1. Clone the repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/gnss-spoofing-detector.git
```

### 2. Install dependencies

Navigate to the project directory and install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

The dependencies include libraries like `haversine` for distance calculation, and other necessary packages for handling GPS data and logging.

### 3. Run the tool

Once the setup is complete, you can run the tool using:

```bash
python tool/source_code/detect_spoof.py
```

### 4. Input Format:

The tool expects GPS log files in **NMEA format**. Ensure your log files are in the same directory or provide the path to the file in the script. You can find sample NMEA log files from various online sources or generate your own using GPS logging apps.

### 5. Output

The tool will output logs indicating potential spoofing based on excessive speed or distance anomalies. For example:

```
 Possible spoofing detected at 12:34:56: Speed = 452.2 km/h (Threshold exceeded)
```

## 📸 Screenshots / Logs / Diagrams

### Sample Output:

When spoofing is detected, the following message will appear in the terminal or console:

```
 Possible spoofing detected at 12:34:56: Speed = 452.2 km/h (Threshold exceeded)
```

### Example Log:

The tool processes GPS data and produces logs like:

```
Processing GPS data...
Distance between points: 120 km
Speed: 452 km/h
Spoofing detected: Yes
```

### Diagrams:

* **Spoofing Detection Flow:**
  Below is a flowchart representing the spoofing detection process:

  ![Spoofing Detection Flow](images/spoofing-detection-flow.png)

  * **Step 1:** GPS data is read from the log file.
  * **Step 2:** Distances between consecutive GPS points are calculated.
  * **Step 3:** Speed is computed, and anomalies are checked against defined thresholds.
  * **Step 4:** If a threshold is exceeded, the system flags the point as a potential spoof.

---

This **README.md** is now more detailed and should meet the required structure. Feel free to adjust the content to fit your exact project details, and let me know if you need any further adjustments!
