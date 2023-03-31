from flask import Flask, request, send_from_directory, abort, render_template
import os

app = Flask(__name__)

# 生データを取得するエンドポイント
@app.route('/raw-data/<path:filename>')
def raw_data(filename):
    if filename == "data.txt":
        return send_from_directory(os.getcwd(), filename, as_attachment=True)
    else:
        abort(404)

# data.txtを更新するエンドポイント
@app.route('/update')
def update_data():
    username = request.args.get('username')
    number = request.args.get('number')

    if not username or not number or not number.isdigit() or int(number) not in range(10):
        return "Invalid input.", 400

    with open("data.txt", "r") as f:
        lines = f.readlines()

    users = {lines[i].strip(): lines[i+1].strip() for i in range(0, len(lines), 2)}

    users[username] = number

    with open("data.txt", "w") as f:
        for user, num in users.items():
            f.write(f"{user}\n{num}\n")

    return "Data updated successfully."

#aaaaaa
@app.route('/update-html')
def update_html():
    return render_template('update.html')


if __name__ == "__main__":
    app.run()
