#!/bin/bash
echo -ne "$1$2$3" | sudo tee /dev/spidev2.1 | xxd > /dev/null 2>&1
