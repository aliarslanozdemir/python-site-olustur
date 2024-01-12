# simple_site_generator.py

def generate_html():
    html_content = """
    <html>
        <head>
            <title>My Simple Site</title>
        </head>
        <body>
            <h1>Welcome to My Simple Site</h1>
            <p>This is a static site generated using Python.</p>
        </body>
    </html>
    """
    with open('index.html', 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_html()
