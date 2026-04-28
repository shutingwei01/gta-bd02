
> **Document Version**: V1.0

# Product Overview

This voice board is specifically designed to provide edge-side voice functionalities and can be flexibly adapted to various pre-installed or aftermarket devices. The product features a compact form factor, rich interfaces, and requires no secondary development.

## Core Features

* **Basic Voice Capabilities**: Supports offline speech recognition, Text-to-Speech (TTS) broadcasting, and voice control commands.
* **Advanced Conversational Interaction**: Supports full-duplex continuous voice conversation.
  ```{note} 
  The voice broadcasting function requires an external amplifier and speaker. The speaker model and power rating can be selected and configured by the customer based on end product requirements.
  ```

## Core Hardware Components

1. **GTA Main Control Chip**: Built-in co-packaged LPDDR3 memory (512 MB), providing powerful edge-side computing capability.
2. **A2N Master Chip**: Used for daisy-chaining the microphone array board.
   ```{note}
   This voice board must be used in combination with the matching microphone board.
   ```
3. **Dedicated DAC Chip**: Provides high-quality audio output for connecting to external amplifiers/speakers.
4. **Storage Module**: Provides 512 MB of storage space (available in either plug-in SD card or surface-mount SD NAND form factors).
5. **Security Protection**: On-board dedicated encryption chip for hardware-level encryption protection of local models and firmware.

# Board Layout and Module Description

## Board Layout

```{figure} /_static/images/G10005_voiceboard-layout-v1.png
:align: center
:width: 70%
:alt: GTA1000 Series Voice Board Front Layout

GTA1000 Series Voice Board — Front Layout
```

```{figure} /_static/images/G10006_voiceboard-back-layout-v1.png
:align: center
:width: 80%
:alt: GTA1000 Series Voice Board Rear Layout

GTA1000 Series Voice Board — Rear Layout
```

## Module Description

| No. | Module Name | Interface / Component Description |
| :--- | :--- | :--- |
| **[1]** | 12V Power Terminal | Screw-type terminal block, 12V/3A DC input (silk-screen "ON" = powered on) |
| **[2]** | Main Power Switch | Main power toggle switch for the voice board |
| **[3]** | Type-C Power Port | Backup 12V/3A power interface (use either this or **[1]**, not both) |
| **[4]** | ASN Master Chip | Master chip responsible for audio data transmission |
| **[5]** | Encryption Chip | Handles local encryption of models and firmware |
| **[6]** | 3.5mm Audio Jack | DAC audio output interface for connecting an external amplifier/speaker |
| **[7]** | ASN Cable Connector | Dedicated connector for interfacing with the microphone board |
| **[8]** | NOR Flash | Stores basic firmware programs |
| **[9]** | Reset Button | System reset button |
| **[10]** | USB-A Communication Port | Built-in TTL-to-USB conversion chip; outputs USB to interface with the host device |
| **[11]** | SD Card Slot | Plug-in SD card socket (convenient for updating models and firmware) |
| **[12]** | TTL Serial Terminal | Screw-type terminal block for native TTL serial communication |
| **[13]** | Core Board | Contains the GTA main chip, crystal oscillator, core power supply circuits, etc. |
| **[14]** | Surface-Mount SD NAND | Surface-mount SD storage (compact, high stability; use either this or **[11]**, not both) |

# Functional Module Details

## Power Supply System

This voice board provides two independent 12V power supply methods (**select one only; do not use simultaneously**):

* **Option 1**: Connect a 12V/3A DC power source via the **[1]** screw terminal.
* **Option 2**: Connect a 12V/3A power adapter via the **[3]** Type-C port.
* **Power Scope Notice**: The above interfaces supply power only to the voice main board and the matching microphone board. If the device uses a high-power external speaker, the customer must provide a separate power supply and switching control for the speaker/amplifier. The **[2]** main power switch on this board controls only the voice board itself.

## Microphone and Audio Output

* **Audio Input**: Connect the microphone array board via the **[7]** ASN cable connector. The microphone board specifications (e.g., array configuration) and cable length can be customized to suit the specific product form factor.
* **Audio Output**: Connect an external amplifier or active speaker via the **[6]** 3.5mm audio jack. Device appearance, dimensions, and volume requirements are determined by product needs.

## Data Communication and Interfaces

This voice board communicates with the customer's host device via a USART serial interface (baud rate and other parameters are software-configurable). Two physical connection methods are available:

* **USB-A Port [10]**: Built-in TTL-to-USB chip; connects directly to the customer's device via a USB cable. Suitable for host controllers that only have USB interfaces.
* **TTL Terminal [12]**: Native screw terminal; supports direct TTL-level communication or connection to an external RS232/RS485 adapter module. Suitable for devices with traditional industrial serial ports.

## Storage Solution

To accommodate different application scenarios, this voice board offers two SD storage options:

1. **Plug-in SD Card [11]**: Easy to insert and remove, making it convenient for manually updating algorithm models and firmware in the field. Recommended for stationary devices not subject to severe vibration.
2. **Surface-Mount SD NAND [14]**: Soldered directly onto the core board. Advantages include compact size, vibration resistance, and high stability. The trade-off is that card content must be updated via a dedicated software interface.

# Installation and Usage Guide

## Typical Installation Steps

1. **Secure the Main Board**: Mount the voice board inside the target device enclosure using screws through the positioning holes around the perimeter of the board.
2. **Connect the Microphone**: Insert one end of the dedicated cable into the **[7]** ASN connector and route the cable according to the device's internal structure. Secure the matching microphone board at the pre-cut audio pickup opening on the device enclosure.
3. **Connect the Speaker**: Plug the speaker audio cable into the **[6]** 3.5mm audio jack and mount the speaker inside the device.

   ```{note}
   Acoustic isolation: Position the speaker as far as possible from the microphone pickup opening to minimize echo interference.
   ```

4. **Insert the Storage Card**: If using the plug-in SD card solution, ensure the SD card has been correctly pushed into the **[11]** SD card slot.
5. **Connect Communication Cable**: Based on the target device's interface type, use a USB cable to connect to the **[10]** USB-A port, or connect a RS232/RS485 or other serial communication module to the **[12]** terminal.
6. **Connect Power**: Confirm the **[2]** power switch is in the OFF position, then connect the 12V power supply (via Type-C or screw terminal). If the speaker requires independent power, connect it at the same time.
7. **Power On and Test**: Toggle the **[2]** power switch to ON and begin functional testing.

```{note}
For first-time integration customers, we can provide professional technical support and on-site installation and commissioning services.
```

# Packaging and Accessories List *(TBD)*

Accessory packages will be configured flexibly based on the customer's final requirements. The following lists the standard categories:

**Standard Package**
* GTA1000 Voice Main Board PCBA
* Microphone Array Board (specifications selectable)
* ASN Dedicated Connection Cable
* 12V Power Adapter

**Optional Accessories**
* Communication Adapter Module (RS232/RS485)
* Plug-in SD Card (with pre-loaded models)
* Active Amplified Speaker
* USB-A Communication Data Cable
