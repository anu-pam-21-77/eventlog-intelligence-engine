import subprocess

def run_ps1(script_path, params=None):
    cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]
    if params:
        cmd.extend(params)

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Script failed:\n{result.stderr}")

    return result.stdout

# Usage
output = run_ps1(".\\scripts\\export_windows_events.ps1")
print(output)