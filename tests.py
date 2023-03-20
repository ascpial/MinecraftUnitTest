import subprocess

process = subprocess.Popen(
    ["java", "-jar", "server.jar"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)

try:
    while process.poll() is None:
        realtime_output = process.stdout.readline()

        print(realtime_output)
except KeyboardInterrupt:
    process.kill()
