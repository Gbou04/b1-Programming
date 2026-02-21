from datetime import datetime

class User:
    def __init__(self, username, password, privilege="standard"):
        # hashed password, privilege level, login attempts, status
        self.__username = username
        self.__password_hashed = self.__hashed_password(password)
        self.__privilege_level = privilege
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []

    #Add methods including authenticate(), check_privileges(), lock_account(), reset_login_attempts(), and log_activity().
    #SENSITIVE ATTRIBUTES MUST BE PRIVATE (just password)
    def __hashed_password(self, password):
        return "secured_" + password


    #ACCESS CONTROL LOGIC. 3 FAILED ATTEMPTS = LOCKED
    def authenticate(self, password):
        if self.__account_status == "locked":
            self.log_activity("Login Attempt on a Locked Account.")
            return False

        if self.__hashed_password(password) == self.__password_hashed:
            self.__login_attempts = 0
            self.log_activity("Login Successful.")
            return True
        else:
            self.__login_attempts += 1
            self.log_activity (f"Failed Login Attempt #{self.__login_attempts}")

            if self.__login_attempts >= 3:
                self.lock_account()

            return False

    def log_activity(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__activity_log.append(f"{timestamp} - {message}")

    def check_privileges(self, required_level):
        levels = {"guest": 0, "standard": 1, "admin": 2}
        return levels.get(self.__privilege_level, 0) >= levels.get(required_level, 0)

    def lock_account(self):
        self.__account_status = "locked"
        self.log_activity(" Account is Locked After 3 Failed Attempts.")

    def reset_login_attempts(self, admin_password):
        # Only admins can override compliance checks
        if self.__hashed_password(admin_password) == "secured_admin":
            self.__login_attempts = 0
            self.__account_status = "active"
            self.log_activity("Account Unlocked by Admin.")
            return True
        return False

    #Add a method to safely display user information without exposing sensitive data
    def display_safe_info(self):
        return {
            "username": self.__username,
            "account_status": self.__account_status,
            "privilege_level": self.__privilege_level,
        }

    #PROPER USE OF GETTERS AND SETTERS
    def get_username(self):
        return self.__username

    def get_privilege_level(self):
        return self.__privilege_level









