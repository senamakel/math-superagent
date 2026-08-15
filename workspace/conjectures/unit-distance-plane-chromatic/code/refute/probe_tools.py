import subprocess, shutil
print("which geng:", shutil.which("geng"))
print("which nauty-geng:", shutil.which("nauty-geng"))
for name in ["geng","nauty-geng","gentourng"]:
    try:
        r = subprocess.run([name,"--help"],capture_output=True,text=True,timeout=5)
        print(name, "OK", r.stdout[:80].replace("\n"," "))
    except Exception as e:
        print(name, "err", e)
