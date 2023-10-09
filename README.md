
# Raspberry Pi LED Wizard

## Overview

This Python script is a simple tool to control LED strips connected to a Raspberry Pi. It allows you to toggle between different colors (Red, Green, and Blue).

## Prerequisites

- Python 3.x
- Raspberry Pi (any model with GPIO pins)
- LED Strips
- Required Python packages are listed in `requirements.txt`

## Installation

1. Clone this repository or download the ZIP file.
2. Navigate to the project directory and install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Wiring Guide

Connect the LED strips to the GPIO pins on your Raspberry Pi as follows:

- **LED Strip 1**: Connect to GPIO 17 for Red color
- **LED Strip 2**: Connect to GPIO 18 for Green color
- **LED Strip 3**: Connect to GPIO 27 for Blue color

## Usage

Run the script using:

```bash
python led_control.py
```

Follow the on-screen prompts to control your LEDs.

## License

MIT
