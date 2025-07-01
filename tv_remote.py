#     Vzdálené ovládání počítače přes HTML stránku
#     Linux verze     (testováno na X11 ale protože to používá xdotool tak to asi nebude fungovat na Waylandu)
#     vytvořil: @opecko na yt


#     ZÁVISLOSTI: balíčky python3-flask, xdotool

from flask import Flask, request, jsonify
import os

app = Flask(__name__)


#HTML kód stránky
HTML_PAGE = """
<!doctype html>
<html>
<head>
  <title>Remote</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<style>
  body {
    background-color: #121212;
    color: #ffffff;
    text-align: center;
    font-family: sans-serif;
    margin: 0;
    padding: 20px;
    box-sizing: border-box;
  }

  h1 {
    margin-bottom: 30px;
  }

  .button-row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 10px;
  }

  button {
    background-color: #1e1e1e;
    color: #ffffff;
    border: 2px solid #333;
    border-radius: 8px;
    font-size: 24px;
    padding: 20px;
    flex: 1 1 30%;
    min-width: 100px;
    height: 80px;
    box-sizing: border-box;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #333;
  }

  #inputBox {
    margin-top: 10px;
    width: 95%;
    padding: 15px;
    font-size: 20px;
    background-color: #1e1e1e;
    color: #fff;
    border: 2px solid #444;
    border-radius: 8px;
    display: none;
  }
</style>
</head>
<body>
  <h1>TV Ovladač</h1>

  <div class="button-row">
    <button onclick="send('up')">⬆️</button>
  </div>
  <div class="button-row">
    <button onclick="send('left')">⬅️</button>
    <button onclick="send('enter')">⏎</button>
    <button onclick="send('right')">➡️</button>
  </div>
  <div class="button-row">
    <button onclick="send('space')">⏯</button>
    <button onclick="send('down')">⬇️</button>
    <button onclick="send('esc')">⏹</button>
    <button onclick="send('back')">🔙 Zpět</button>
  </div>
  <div class="button-row">
    <button onclick="send('volup')">🔊</button>
    <button onclick="toggleInput()">⌨️ Text</button>
    <button onclick="send('voldown')">🔉</button>
  </div>

  <input type="text" id="inputBox" onkeydown="handleInput(event)" placeholder="Zadej text a stiskni Enter">

  <script>
    function send(cmd) {
      fetch('/' + cmd).then(r => r.json()).then(j => console.log(j));
    }

    function toggleInput() {
      const box = document.getElementById('inputBox');
      box.style.display = box.style.display === 'block' ? 'none' : 'block';
      if (box.style.display === 'block') box.focus();
    }

    function handleInput(event) {
      if (event.key === 'Enter') {
        fetch('/text', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({text: event.target.value})
        }).then(r => r.json()).then(j => console.log(j));
        event.target.value = '';
        event.target.style.display = 'none';
      }
    }
  </script>
</body>
</html>
"""

keys = {
    "up": "key Up",
    "down": "key Down",
    "left": "key Left",
    "right": "key Right",
    "enter": "key Return",
    "space": "key space",
    "esc": "key Escape",
    "volup": "key XF86AudioRaiseVolume",
    "voldown": "key XF86AudioLowerVolume",
    "back": "key BackSpace"
}

@app.route("/")
def index():
    return HTML_PAGE

@app.route("/<key>") #mačkání kláves podle tlačítek na stránce
def press_key(key):
    if key in keys:
        os.system(f"xdotool {keys[key]}")
        return jsonify({"status": "ok", "action": key})
    return jsonify({"status": "error", "message": "Unknown key"}), 400

@app.route("/text", methods=["POST"]) #vstup textu
def type_text():
    data = request.get_json()
    text = data.get("text", "")
    safe_text = text.replace('"', r'\"')
    os.system(f'xdotool type "{safe_text}"')
    return jsonify({"status": "ok", "typed": text})

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) #hostování stránky a loop 
    #                       tady si mužete vybrat na jakem portu se bude hostovat stránka

