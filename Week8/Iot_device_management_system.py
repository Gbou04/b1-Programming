from datetime import datetime

class Device:
    def __init__(self, device_id, device_type, owner_username, firmware_version="1.0.0"):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__owner = owner_username
        self.__firmware_version = firmware_version
        self.__compliance_status = "unknown"
        self.__last_security_scan = None
        self.__is_active = True
        self.__access_log = []

    #User-Device Interaction with authorise_access method
    def authorize_user(self, user):
        if not self.__is_active:
            self.__log_access(user.get_username(), "Access Denied - Device Inactive.")
            return False

        if self.__compliance_status != "compliant" and not user.check_privileges("admin"):
            self.__log_access(user.get_username(), "Access Denied - Non-Compliant Device.")
            return False

        self.__log_access(user.get_username(), "Access granted.")
        return True

    # Step 3: Security Validation use update_firmware, run_security_scan, check_compluiiance
    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.__compliance_status = "compliant"
        self.__log_access("SYSTEM", "Security Scan Completed.")

    #Devices automatically become non-compliant if not scanned within 30 days
    def is_compliant(self):
        if not self.__last_security_scan:
            self.__compliance_status = "unknown"
            return False
        days_since_last_scan = (datetime.now() - self.__last_security_scan).days
        if days_since_last_scan > 30:
            self.__compliance_status = "non-compliant"
            return False
        self.__compliance_status = "compliant"
        return True


    #UPDATE FIRMWARE. ONLY ADMINS
    def update_firmware(self, version, user):
        if not user.check_privileges("admin"):
            return False
        self.__firmware_version = version
        self.__log_access(user.get_username(),f"Firmware Updated to {version}")
        return True

    #QUARANTINE DEVICE
    def quarantine(self, user):
        if not user.check_privileges("admin"):
            return False
        self.__is_active = False
        self.__log_access(user.get_username(), "Device Quarantined.")
        return True

    #LOG ACCESS
    def __log_access(self, username, action):
        timestamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        self.__access_log.append(f"{timestamp} - {username}: {action}")

    #Device info
    def get_device_info(self):
        return {
            "device_id" : self.__device_id,
            "device_type" : self.__device_type,
            "compliance_status" : self.__compliance_status,
            "owner": self.__owner,
            "firmware_version" : self.__firmware_version,
            "is_active" : self.__is_active,
        }

    #STEP 4 DEVICE MANAGER add, remove, generate security report
class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        info = device.get_device_info()
        self.__devices[info["device_id"]] = device

    def remove_device(self, device_id, user):
        if not user.check_privileges("admin"):
            return False
        return self.__devices.pop(device_id, None) is not None

    def generate_security_report(self, user):
        if not user.check_privileges("admin"):
            return None
        report = []
        for device in self.__devices.values():
            device.is_compliant()
            report.append(device.get_device_info())
        return report


