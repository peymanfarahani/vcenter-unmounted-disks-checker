import ssl
from pyVim.connect import SmartConnect, Disconnect
import atexit
from pyVmomi import vim
from tabulate import tabulate
import os

# Retrieve vCenter credentials from environment variables or use defaults
vcenter_ip = os.getenv("VCENTER_IP", "vcenter_ip_or_hostname")
vcenter_user = os.getenv("VCENTER_USER", "your_vcenter_user")
vcenter_password = os.getenv("VCENTER_PASSWORD", "your_vcenter_password")

# Disable SSL warnings for testing environments
context = ssl._create_unverified_context()

def get_unmounted_disks(si):
    """
    Fetch a list of unmounted disks from virtual machines in vCenter.
    :param si: SmartConnect object for vCenter connection
    :return: List of unmounted disks with their details
    """
    content = si.RetrieveContent()
    vm_list = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    unmounted_disks = []

    # Iterate through all virtual machines
    for vm in vm_list.view:
        try:
            # Iterate through VM devices to find disks
            for device in vm.config.hardware.device:
                if isinstance(device, vim.vm.device.VirtualDisk):
                    # Check if the disk is unmounted
                    if hasattr(device.backing, 'deviceName') and device.backing.deviceName == "[Empty]":
                        disk_size_gb = device.capacityInKB / 1024 / 1024 if hasattr(device, 'capacityInKB') else "Unknown"
                        unmounted_disks.append({
                            'VM Name': vm.name,
                            'Disk Name': device.deviceInfo.label,
                            'Disk Size (GB)': disk_size_gb,
                            'Disk File': device.backing.fileName
                        })
        except Exception as e:
            print(f"Error processing VM {vm.name}: {e}")

    return unmounted_disks

def main():
    """
    Main function to connect to vCenter, retrieve unmounted disks, and display them.
    """
    try:
        # Connect to vCenter
        si = SmartConnect(host=vcenter_ip, user=vcenter_user, pwd=vcenter_password, sslContext=context)
        atexit.register(Disconnect, si)  # Ensure disconnect on script termination
    except Exception as e:
        print(f"Failed to connect to vCenter: {e}")
        return

    # Retrieve unmounted disks
    unmounted_disks = get_unmounted_disks(si)

    # Display results in a readable format
    if unmounted_disks:
        print("\nList of Unmounted Disks:")
        print(tabulate(unmounted_disks, headers="keys"))
    else:
        print("No unmounted disks found.")

if __name__ == "__main__":
    main()
