### `unmounted_disks_checker.py`:
```python
import ssl
from pyVim.connect import SmartConnect, Disconnect
import atexit
from pyVmomi import vim

# vCenter settings
vcenter_ip = "vcenter_ip_or_hostname"
vcenter_user = "your_vcenter_user"
vcenter_password = "your_vcenter_password"

# Disable SSL warnings (for testing and to avoid SSL errors)
context = ssl._create_unverified_context()

def get_unmounted_disks(si):
    # Retrieve all virtual machines
    content = si.RetrieveContent()
    vm_list = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    
    unmounted_disks = []
    
    # Check each virtual machine
    for vm in vm_list.view:
        print(f"Checking VM: {vm.name}")
        
        # Check the disks
        for device in vm.config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualDisk):
                # If the disk is unmounted
                if device.backing.deviceName == "[Empty]" or not device.unitNumber:
                    unmounted_disks.append({
                        'VM Name': vm.name,
                        'Disk Name': device.deviceInfo.label,
                        'Disk Size (GB)': device.capacityInKB / 1024 / 1024,
                        'Disk File': device.backing.fileName
                    })
    
    return unmounted_disks

def main():
    # Connect to vCenter
    si = SmartConnect(host=vcenter_ip, user=vcenter_user, pwd=vcenter_password, sslContext=context)
    
    # Ensure disconnect after the script finishes
    atexit.register(Disconnect, si)
    
    # Get unmounted disks
    unmounted_disks = get_unmounted_disks(si)
    
    if unmounted_disks:
        print("\nList of Unmounted Disks:")
        for disk in unmounted_disks:
            print(f"VM: {disk['VM Name']}, Disk: {disk['Disk Name']}, Size: {disk['Disk Size (GB)']} GB, File: {disk['Disk File']}")
    else:
        print("No unmounted disks found.")
    
if __name__ == "__main__":
    main()
