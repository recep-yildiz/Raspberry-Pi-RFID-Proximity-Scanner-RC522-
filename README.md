# Raspberry Pi RFID Proximity Scanner with RC522

## Overview
This project leverages the Raspberry Pi and the RC522 RFID reader module to create a proximity scanner that can read various RFID-enabled cards through a simple graphical user interface developed with Python Tk. This system is ideal for reading RFID tags such as student IDs, bus cards, and access tokens, providing a unique identifier for each scanned tag that can be used for database entries or other applications.

## Features
- **Simple Tkinter User Interface**: Provides a minimalistic and easy-to-use interface to interact with the RFID scanner.
- **RFID Tag Reading**: Capable of reading RFID tags when the 'RFID ON' button is clicked. The system waits for an RFID tag to be presented and retrieves a unique numerical identifier from each scanned tag.

## Warnings
- **Library Path**: You may need to specify the path to the `pirc522` library in your script depending on your setup. This library is included in the project directory for ease of use.

## Setup and Configuration
### Connecting the RC522 to Raspberry Pi
The connections between the RC522 module and the Raspberry Pi are critical for the operation of your scanner. You can find detailed instructions on how to establish these connections in the `pirc522/readme.md` file included in this project.

### Prerequisites
- Raspberry Pi (any model with GPIO pins)
- RC522 RFID Reader Module
- Jumper wires for connection
- Python with Tkinter installed

### Installation
1. Clone the repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/recep-yildiz/Raspberry-Pi-RFID-Proximity-Scanner-RC522-.git
   ```

2. Installation
  ```bash
   cd Raspberry-Pi-RFID-Proximity-Scanner-RC522
```

3. Navigate to the project directory
  ```bash
   cd Raspberry-Pi-RFID-Proximity-Scanner-RC522
```

4. Install required Python libraries
  ```bash
   pip install -r requirements.txt
```

### Usage
