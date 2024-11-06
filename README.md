# vcenter-unmounted-disks-checker

This is a Python script to check and list **unmounted disks** in virtual machines (VMs) on a vCenter Server.

### Features
- Connects to vCenter using **vSphere API**.
- Lists virtual machines and their disks.
- Identifies unmounted disks.
- Displays unmounted disk details (VM name, disk name, size, file).

### Prerequisites
To run this script, you'll need:
1. **Python 3.x** installed.
2. **pyvmomi** library installed (for interacting with the vSphere API).
3. vCenter access credentials (IP, username, password).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vcenter-unmounted-disks-checker.git
   cd vcenter-unmounted-disks-checker
