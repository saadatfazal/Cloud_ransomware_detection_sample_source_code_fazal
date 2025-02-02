Ransomware Vault – Cloud-Based Ransomware Detection System
Overview
Ransomware Vault is a ransomware detection mechanism designed to monitor file access in a cloud-based secure vault. The algorithm continuously analyzes file accessibility and entropy levels to detect early signs of ransomware attacks.

How It Works
The detection mechanism operates on two key principles:

File Accessibility Monitoring – If a file becomes inaccessible due to unauthorized encryption, the system generates an alert.
Entropy Analysis – The algorithm calculates the entropy of files at regular intervals. If the entropy exceeds a predefined threshold (indicating possible encryption), an alarm is triggered.
This preemptive approach allows organizations to detect and respond to ransomware attacks before significant damage occurs.

Installation & Setup
1. Install pip3 (if not already installed)
Ensure that pip3 is installed on your system:

bash
Copy
sudo apt install python3-pip
2. Install Required Dependencies
All necessary Python libraries are listed in the requirements.txt file. Run the following command to install them:

bash
Copy
pip3 install -r requirements.txt
3. Install Pytest for Testing
To run automated tests, install pytest using the command:

bash
Copy
sudo apt install python-pytest
4. Run Automated Tests
Use the following command to execute test cases and validate the detection mechanism:

bash
Copy
python3 -m pytest src/test_code.py -vv -s
5. Set Up Environment Variable
Before running the main detection algorithm, set up the Python path as follows:

bash
Copy
export PYTHONPATH=`pwd`
Usage
Running the Detection Algorithm
The main source code for the ransomware detection mechanism is available in:

bash
Copy
/src/main.py
This script must be executed within a cloud-based virtual environment, ensuring compatibility with cloud storage and security monitoring systems.
How the Detection Works
The ransomware detection mechanism follows a multi-layered approach:

File Access Monitoring
The system constantly checks whether files are accessible.
If a file becomes unreadable or encrypted without authorization, an alert is generated.
Entropy-Based Detection
The system calculates the entropy of files at regular intervals.
If a file’s entropy exceeds a predefined threshold, it is flagged as potentially compromised.
High entropy suggests the presence of encrypted data, which is a key indicator of a ransomware attack.
