login_attempts = [
("Naima", "success"),
("Isabelle", "failed"),
("Giovanni", "failed"),
("Cagla", "success"),
("Haley", "failed"),
("Nina", "failed")
    ]

print("Analyzing login attempts...")

# Track how many times each username fails
failed_counts = {}

# Check failed attempts with loop
for username, status in login_attempts:
    if status == "failed":
        failed_counts[username] = failed_counts.get(username, 0) + 1

    else:
        failed_counts[username] = 1

# if it failed 3 times or more
for username in failed_counts:
    if failed_counts[username] >=3:
        print("CAUTION: User'" + username + "'has" +str(failed_counts[username]) + " failed login attempts.")

print("Failed login detector is complete.")