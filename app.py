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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Data Analysis Studio</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
background:#1e1e1e;
color:white;
min-height:100vh;
}

.header{
width:100%;
padding:25px;
background:#252526;
text-align:center;
font-size:40px;
font-weight:bold;
color:#00bfff;
box-shadow:0 2px 15px rgba(0,0,0,.4);
}

.subtitle{
text-align:center;
padding:15px;
color:#bbb;
font-size:18px;
}

.container{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
gap:25px;
padding:30px;
}

.card{
background:#2d2d30;
border-radius:20px;
padding:30px;
box-shadow:0 0 20px rgba(0,191,255,.15);
transition:.4s;
}

.card:hover{
transform:translateY(-10px);
box-shadow:0 0 25px rgba(0,191,255,.4);
}

.card h2{
color:#00bfff;
margin-bottom:15px;
font-size:28px;
}

.card p{
color:#d0d0d0;
line-height:1.8;
font-size:17px;
}

button{
margin-top:20px;
padding:14px 25px;
background:#0078d7;
color:white;
border:none;
border-radius:10px;
font-size:16px;
cursor:pointer;
transition:.3s;
}

button:hover{
background:#00bfff;
}

.footer{
margin-top:50px;
background:#252526;
padding:30px;
text-align:center;
color:#aaa;
font-size:16px;
}

.footer h3{
color:white;
margin-bottom:10px;
}

@media(max-width:768px){

.header{
font-size:30px;
}

.card h2{
font-size:24px;
}

.card{
padding:25px;
}

}

</style>
</head>
<body>

<div class="header">
🐍 Data Analysis Studio
</div>

<div class="subtitle">
Professional Python • SQL • Excel • Visualization Workspace
</div>

<div class="container">

<div class="card">
<h2>🏠 Dashboard</h2>
<p>Central workspace for managing projects, datasets and analytics tasks.</p>
<button>Open Dashboard</button>
</div>

<div class="card">
<h2>🐍 Python Editor</h2>
<p>Write and execute Python programs in a VS Code style environment.</p>
<button>Open Editor</button>
</div>

<div class="card">
<h2>📊 Excel / CSV Analysis</h2>
<p>Import Excel and CSV datasets and perform powerful analysis.</p>
<button>Analyze Data</button>
</div>

<div class="card">
<h2>🗄 SQL Console</h2>
<p>Execute SQL queries and manage databases efficiently.</p>
<button>Open SQL Console</button>
</div>

<div class="card">
<h2>📈 Visualization</h2>
<p>Create interactive charts and graphical insights from data.</p>
<button>Create Charts</button>
</div>

<div class="card">
<h2>🌙 Dark Workspace</h2>
<p>Professional VS Code inspired dark interface for developers and analysts.</p>
<button>Explore</button>
</div>

</div>

<div class="footer">
<h3>Designed & Developed by ANKIT SAINI</h3>
<p>B.Tech IT Student | Python | SQL | Data Analytics | Cybersecurity</p>
<p>Email: as3126061@gmail.com</p>
<p>© 2026 Data Analysis Studio. All Rights Reserved.</p>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
