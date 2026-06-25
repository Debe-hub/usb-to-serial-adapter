# USB to Serial Adapter
CP2102N Based USB-UART Bridge

## Overview
A custom PCB design for a USB to Serial adapter built around the Silicon Labs CP2102N chip. 
This board converts USB signals to UART serial communication, commonly used for 
programming and debugging embedded systems.

## Features
- CP2102N USB to UART bridge IC
- USB Micro-B connector
- Standard 6-pin FTDI header output
- Power indicator LED
- Decoupling capacitors for signal integrity
- Two layer PCB design

## Hardware
- **IC:** Silicon Labs CP2102N (QFN-20 package)
- **Connector:** USB Micro-B
- **Output:** 6-pin FTDI header (3.3V)
- **PCB:** 2 layer, 60mm x 30mm

## Repository Structure
usb-to-serial-adapter/
├── hardware/
│   ├── gerbers/          # Manufacturing files
│   ├── schematic.pdf     # Full schematic
│   ├── pcb-layout.png    # PCB layout screenshot
│   └── pcb-3d.png        # 3D view screenshot
├── software/
│   └── serial_test.py    # Serial loopback test script
└── README.md

## Tools Used
- KiCad 10.0 — Schematic and PCB design
- Python 3 — Serial communication testing

## Author
Osadebe Osakwe
