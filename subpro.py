import subprocess

# subprocess.call(["firefox"], shell=True)

out = subprocess.check_output(["whoami"])
print(out.decode())

