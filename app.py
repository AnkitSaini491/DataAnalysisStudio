# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

def page(title, body):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI;
}}

body{{
background:#1e1e1e;
color:white;
min-height:100vh;
}}

header{{
background:#252526;
padding:20px;
text-align:center;
box-shadow:0 0 15px rgba(0,0,0,.5);
}}

header h1{{
color:#00bfff;
font-size:40px;
}}

nav{{
background:#2d2d30;
padding:15px;
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:15px;
}}

nav a{{
text-decoration:none;
color:white;
background:#0078d7;
padding:12px 20px;
border-radius:10px;
transition:.3s;
}}

nav a:hover{{
background:#00bfff;
}}

.container{{
padding:40px;
}}

.card{{
background:#2d2d30;
padding:25px;
border-radius:15px;
margin-bottom:20px;
box-shadow:0 0 15px rgba(0,191,255,.2);
}}

footer{{
background:#252526;
padding:20px;
text-align:center;
margin-top:50px;
color:#bbb;
}}

textarea{{
width:100%;
height:300px;
background:#111;
color:#00ff00;
padding:15px;
border:none;
border-radius:10px;
}}

table{{
width:100%;
border-collapse:collapse;
}}

td,th{{
border:1px solid #555;
padding:10px;
}}

</style>
</head>

<body>

<header>
<h1>🐍 Data Analysis Studio</h1>
<p>Python • SQL • Excel • Visualization</p>
</header>

<nav>
<a href="/">Dashboard</a>
<a href="/editor">Python Editor</a>
<a href="/excel">Excel Analysis</a>
<a href="/sql">SQL Console</a>
<a href="/charts">Charts</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
</nav>

<div class="container">

{body}

</div>

<footer>
<h3>Designed & Developed by ANKIT SAINI</h3>
<p>Email: as3126061@gmail.com</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return page(
        "Dashboard",
        """
<div class="card">
<h2>🏠 Dashboard</h2>
<p>Welcome to Data Analysis Studio.</p>
</div>

<div class="card">
<h2>Features</h2>
<ul>
<li>🐍 Python Editor</li>
<li>📊 Excel Analysis</li>
<li>🗄 SQL Console</li>
<li>📈 Charts</li>
<li>🌙 Dark Theme</li>
</ul>
</div>
"""
)
  @app.route("/editor")
def editor():
    return page(
        "Python Editor",
        """
<div class="card">
<h2>🐍 Python Editor</h2>

<textarea>
# Write Python code here

print("Hello World")
</textarea>

</div>
"""
)

@app.route("/excel")
def excel():
    return page(
        "Excel Analysis",
        """
<div class="card">
<h2>📊 Excel / CSV Analysis</h2>

<table>
<tr>
<th>Name</th>
<th>Age</th>
<th>Department</th>
</tr>

<tr>
<td>Rahul</td>
<td>21</td>
<td>IT</td>
</tr>

<tr>
<td>Ankit</td>
<td>22</td>
<td>Data Science</td>
</tr>

<tr>
<td>Priya</td>
<td>20</td>
<td>CSE</td>
</tr>

</table>

</div>
"""
)

@app.route("/sql")
def sql():
    return page(
        "SQL Console",
        """
<div class="card">
<h2>🗄 SQL Console</h2>

<textarea>
SELECT * FROM students;

SELECT * FROM employees
WHERE salary > 50000;
</textarea>

</div>
"""
)

@app.route("/charts")
def charts():
    return page(
        "Charts",
        """
<div class="card">

<h2>📈 Visualization</h2>

<h3>Bar Chart</h3>

<pre>

Sales
|
|          ████
|     ████ ████
| ███ ████ ████
+----------------
 Jan Feb Mar Apr

</pre>

</div>
"""
)

@app.route("/about")
def about():
    return page(
        "About",
        """
<div class="card">

<h2>ℹ About Data Analysis Studio</h2>

<p>
Data Analysis Studio is a professional platform
for Python programming, SQL queries,
Excel analysis and data visualization.
</p>

<br>

<h3>Developer</h3>

<p><b>ANKIT SAINI</b></p>

<p>
B.Tech IT Student
</p>

<p>
Python | SQL | Data Analytics | Cybersecurity
</p>

</div>
"""
)

@app.route("/contact")
def contact():
    return page(
        "Contact",
        """
<div class="card">

<h2>📧 Contact Us</h2>

<p>
Email:
<b>as3126061@gmail.com</b>
</p>

</div>
"""
)  
