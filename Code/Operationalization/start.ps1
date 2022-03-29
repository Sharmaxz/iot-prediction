#!/usr/bin/env bash
# requires: Python, PowerShell, Permission to run PS scripts
# permissions for this PS session only:   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# exit if cmdlet gives error
$ErrorActionPreference = "Stop"

# Check to see if root CA file exists, download if not
If (!(Test-Path ".\root-CA.crt")) {
    "`nDownloading AWS IoT Root CA certificate from AWS..."
    Invoke-WebRequest -Uri https://www.amazontrust.com/repository/AmazonRootCA1.pem -OutFile root-CA.crt
}

# Check to see if AWS Device SDK for Python exists, download if not
If (!(Test-Path ".\aws-iot-device-sdk-python")) {
    "`nCloning the AWS SDK...\n"
    git clone https://github.com/aws/aws-iot-device-sdk-python
}

# Check to see if AWS Device SDK for Python is already installed, install if not
python -c "import AWSIoTPythonSDK"
if (!($?)) {
    "`nInstalling AWS SDK..."
    cd aws-iot-device-sdk-python
    pip install AWSIoTPythonSDK
    $result=$?
    cd ..
    if (!$result) {
        "`nERROR: Failed to install SDK."
        exit
    }
}

"`nRunning pub/sub sample application..."
python aws-iot-device-sdk-python\samples\basicPubSub\basicPubSub.py -e a1apbqincnemcr-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c room.cert.pem -k room.private.key
