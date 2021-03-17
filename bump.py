import re
import subprocess

try:
    version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"], stderr=subprocess.STDOUT).strip()
except subprocess.CalledProcessError:
    print("1.0.0")
    exit()

message = subprocess.check_output(["git", "log", "--pretty=format:%s", "--max-count=1"]).strip()

pattern_version = "^(\d+)\.(\d+)\.(\d+)$"
pattern_message = "^Merge pull request #\d+ from (.*feat.*)$"

if not re.match(pattern_version, version):
    print("1.0.0")
    exit()

result = re.search(pattern_version, version)

major = int(result.group(1))
minor = int(result.group(2))
patch = int(result.group(3))

if re.match(pattern_message, message):
    minor += 1
    patch = 0
else:
    patch += 1

print("{}.{}.{}".format(major, minor, patch))
