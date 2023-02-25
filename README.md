# lcm-implementation
A simple implementation of the Lightweight Communications and Marshalling (LCM) library for obstacle detection.

In the master.py, the master performs background subtraction to see if any new obstacles are detected in the image frames of the incoming video stream. The master has a heartbeat message which it sends to the slaves, which includes two parameters: timestamp and a danger flag.
This heartbeat message is sent out every second. If any obstacle is detected, then the flag is updated. 

To run this code:

Run master.py and slave in two separate command line prompts.

## License
This code is licensed under LGPL-2.1 license
