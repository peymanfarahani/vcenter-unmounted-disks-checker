# Unmounted Disks Checker

This Python script connects to a vCenter server using the pyVmomi library to find and display unmounted virtual disks across virtual machines in a VMware environment.

## Features
- Lists unmounted disks in virtual machines.
- Displays disk size, VM name, and file details in a readable table format.
- Handles SSL warnings for testing environments.
- Supports connection to vCenter using environment variables for added security.

## Prerequisites
- Python 3.6 or higher.
- Access to a vCenter server with appropriate credentials.
- Required Python libraries listed in the `requirements.txt` file.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/unmounted-disks-checker.git
   cd unmounted-disks-checker

2. Install the required libraries:
 -  pip install -r requirements.txt

## Usage
1. Set your vCenter credentials as environment variables:
  export VCENTER_IP="your_vcenter_ip"
  export VCENTER_USER="your_username"
  export VCENTER_PASSWORD="your_password"

2. Run the script:
   python unmounted_disks_checker.py

## Output Example
The script will display a table like this:

List of Unmounted Disks:
VM Name    Disk Name    Disk Size (GB)    Disk File
vm1        Hard disk 1  50.0             [datastore1] vm1/vm1_1.vmdk
vm2        Hard disk 2  100.0            [datastore2] vm2/vm2_2.vmdk







