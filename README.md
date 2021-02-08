# IOT CLOUD PLATFORM

- This project is designed in order to ease the process of setting up multiple sensors with an IOT device and sending the data from local to cloud servers using MQTT protocol.

### IOT Device: Raspberry Pi

### Cloud Services: Google Cloud Platform (GCP)

### Sensors:

- IR Sensor
- MQ135 Gas Sensor

## Prerequisites

- Python

## Setup

1. Fork the respository

2. Clone the repositorty

   ```sh
   git clone https://github.com/your_username_/iot-cloud-platform
   ```

3. Install Google Cloud SDK
   ```sh
   curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-326.0.0-linux-x86.tar.gz
   ```
   ```sh
   tar –xvzf google-cloud-sdk-326.0.0-linux-x86.tar.gz
   ```
   ```sh
   ./google-cloud-sdk/install.sh
   ```
   ```sh
   ./google-cloud-sdk/bin/gcloud init
   ```

## Usage

### Reading Sensor Data

1. Add a python script that reads data from sensor in **_sensors_data_** folder.

- Examples can be found for MQ135 gas sensor and IR sensor in the same folder.

2. Import the functions in **_gcp_json_** file and update the **_get_payload_** function in this file such that it returns a Python Dictionary of the Data to be sent on Cloud and the data should be JSON serializable.

### Cloud Environment Setup

1. Make an account on [Google Cloud Platform](https://cloud.google.com/)

2. Create a Pub/Sub topic for your streaming data.

3. Create a Storage bucket and folder to store the data streaming from the IoT device.

4. Start a Dataflow job to save the data to your bucket.

5. Create registry under IOT core and add your sensor as a device alongside setting up authentication.

### Sending Data To Cloud

1. Make sure all python packages are installed for your sensor scripts.

2. Install required software packages.
   ```sh
   sudo apt-get install python3-pip openssl git -y
   ```
   ```sh
   sudo pip3 install pyjwt paho-mqtt cryptography
   ```
3. Set up environment variables

   ```sh
   export PROJECT_ID=<your-project-id>
   ```

   ```sh
   export MY_REGION=<nearest-region>
   ```

   ```sh
   export REGISTRY_ID=<your-registry-id>
   ```

   ```sh
   export DEVICE_ID=<your-device-id>
   ```

4. Run the **_gcp_json.py_** script.
   ```sh
   python gcp_json.py \
   --project_id=$PROJECT_ID \
   --cloud_region=$MY_REGION \
   --registry_id=$REGISTRY_ID \
   --device_id=$DEVICE_ID \
   --private_key_file=rsa_private.pem \
   --message_type=event \
   --algorithm=RS256 --num_messages=200
   ```

- private_key_file argument is supplied for authentication
- num_messages indicates the number of payloads or packages sent to cloud bucket.

## Sample Output

- IR Sensor
  <img src="./sample_cloud_output/ir_sensor.png" alt="IR data"/>

- MQ135 Sensor
  <img src="./sample_cloud_output/mq135_sensor.png" alt="MQ135 data"/>

## References

- [Streaming IoT Data to Cloud Storage](https://www.qwiklabs.com/focuses/2765?parent=catalog)

- [MCP3008 ADC Setup](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)

- [Reading IR Sensor Data](https://www.youtube.com/watch?v=qQTQcN44UWg)

- [Reading MQ Sensor Data](https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/)

- [MQ135 Data Sheet](https://www.olimex.com/Products/Components/Sensors/Gas/SNS-MQ135/resources/SNS-MQ135.pdf)
