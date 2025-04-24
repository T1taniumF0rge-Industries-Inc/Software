# KS3021 kit

## Introduction

The KS3021 kit from Keyestudio is a fun kit including IR sensors, LED's and more in all one packet. The main piece, a Raspberry Pi RP2040 controls everything, and uses MicroPython 2.2 as the base. All code for this kit will be located in this folder

Note that these programs require a Raspberry Pi 3+ with an internet connection, and Minicom's serial port.

## Requirements

1 -> Raspberry Pi with internet connection

2 -> Minicom Serial port

3 -> Thonny's programmer editor with interpreter configured

## Configuring interpreter

In Thonny, the default editor does not support the GPIO pins which are required for this project. You will need to go through one of the 5 menus on the top of the screen until you see an option that says configure interpreter. Choose the interpreter as MicroPython(Raspberry Pi Pico) or MicroPython(RP2040 device)

## My module doesn't work!

This is because MicroPython is stupid, and if you put a Python file in the same directory as another Python file, and you just do import filename, it should detect it. To use the modules, you must implant the lines of code from the modules directly into whatever file needs that module, then remove the module name, so if it was rotary.switch(), replace it with switch() and remove the import to that module.

### © Keyestudio: [`Keyestudio Inc`](https://www.keyestudio.com/)


