from flask import Flask

app = Flask(__name__)

def page(title, content):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>

<style>
body {{
    margin:0;
    font-family:Arial;
    background:#1e1e1e;
    color:white;
}}

header {{
    background:#252526;
    padding:20px;
    text-align:center;
    font-size:35px;
    color:#00bfff;
}}

nav {{
    text-align:center;
    padding:20px;
}}

nav a {{
    text-decoration:none;
    color:white;
    background:#0078d7;
    padding:15px 25px;
    border-radius:10px;
    margin:10px;
    display:inline-block;
}

nav a:hover {{
    background:#00bfff;
}}

.content {{
    padding:40px;
    text-align:center;
}}

footer {{
    background:#252526;
    text-align:center;
    padding:20px;
    margin-top:50px;
}}
</style>
</head>
<body>

<header>
🐍 Data Analysis Studio
</header>

<nav>
<a href="/">Dashboard</a>
<a href="/editor">Python Editor</a>
<a href="/excel">Excel Analysis</a>
<a href="/sql">SQL Console</a>
<a href="/charts">Visualization</a>
<a href="/about">About</a>
</nav>

<div class="content">
{content}
</div>

<footer>
Designed & Developed by <b>ANKIT SAINI</b><br>
Email: as3126061@gmail.com
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return page(
        "Dashboard",
        """
        <h1>🏠 Dashboard</h1>
        <p>Welcome to Data Analysis Studio.</p>
        """
    )

@app.route("/editor")
def editor():
    return page(
        "Python Editor",
        """
        <h1>🐍 Python Editor</h1>
        <textarea rows="20" cols="80"
        style="background:black;color:#00ff00;padding:10px;">
print("Hello World")
        </textarea>
        """
    )

@app.route("/excel")
def excel():
    return page(
        "Excel Analysis",
        """
        <h1>📊 Excel / CSV Analysis</h1>
        <p>Upload and analyze datasets.</p>
        """
    )

@app.route("/sql")
def sql():
    return page(
        "SQL Console",
        """
        <h1>🗄 SQL Console</h1>
        <textarea rows="10" cols="80"
        style="background:black;color:white;padding:10px;">
SELECT * FROM table_name;
        </textarea>
        """
    )

@app.route("/charts")
def charts():
    return page(
        "Visualization",
        """
        <h1>📈 Visualization</h1>
        <p>Charts and graphs section.</p>
        """
    )

@app.route("/about")
def about():
    return page(
        "About",
        """
        <h1>ℹ About Data Analysis Studio</h1>
        <p>Professional platform for Python, SQL and Data Analysis.</p>

        <h3>Developer</h3>
        <p><b>ANKIT SAINI</b></p>
        <p>B.Tech IT Student</p>
        <p>Email: as3126061@gmail.com</p>
        """
    )

if __name__ == "__main__":
    app.run(debug=True)
