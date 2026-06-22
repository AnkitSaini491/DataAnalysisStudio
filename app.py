if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Data Analysis Studio</title>

<style>
body{
background:#1e1e1e;
color:white;
font-family:Segoe UI;
margin:0;
}

.header{
background:#252526;
padding:20px;
text-align:center;
font-size:35px;
font-weight:bold;
color:#00bfff;
}

.container{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
gap:20px;
padding:30px;
}

.card{
background:#2d2d30;
padding:25px;
border-radius:15px;
box-shadow:0 0 15px rgba(0,191,255,.2);
transition:.3s;
}

.card:hover{
transform:translateY(-8px);
}

h2{
color:#00bfff;
}

button{
background:#0078d7;
color:white;
border:none;
padding:12px 20px;
border-radius:8px;
cursor:pointer;
font-size:16px;
}

button:hover{
background:#0099ff;
}

.footer{
background:#252526;
text-align:center;
padding:20px;
margin-top:30px;
color:#bbb;
}
</style>
</head>

<body>

<div class="header">
🐍 Data Analysis Studio
</div>

<div class="container">

<div class="card">
<h2>🏠 Dashboard</h2>
<p>Overview of projects and analytics workspace.</p>
<button>Open Dashboard</button>
</div>

<div class="card">
<h2>🐍 Python Editor</h2>
<p>Write and execute Python scripts.</p>
<button>Open Editor</button>
</div>

<div class="card">
<h2>📊 Excel / CSV Analysis</h2>
<p>Analyze Excel and CSV datasets.</p>
<button>Open Analysis</button>
</div>

<div class="card">
<h2>🗄 SQL Console</h2>
<p>Run SQL queries and manage databases.</p>
<button>Open SQL Console</button>
</div>

<div class="card">
<h2>📈 Visualization</h2>
<p>Create charts and data visualizations.</p>
<button>Open Charts</button>
</div>

<div class="card">
<h2>🌙 VS Code Dark Theme</h2>
<p>Professional dark interface for data scientists.</p>
<button>Explore</button>
</div>

</div>

<div class="footer">
<h3>Designed & Developed by ANKIT SAINI</h3>
<p>B.Tech IT Student | Python | SQL | Data Analytics | Cybersecurity</p>
<p>Email: as3126061@gmail.com</p>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
