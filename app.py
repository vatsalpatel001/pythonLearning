import os
from datetime import datetime
from bs4 import BeautifulSoup

# Get a list of all .html files in the current directory
html_files = [file for file in os.listdir() if file.endswith('.html')]

# Sort the list of HTML files for consistency
# html_files.sort()

# Create the index.html content
index_content = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    font-family: Arial, sans-serif;
  }
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: left;
  }
</style>
</head>
<body>
  <h1>Index of HTML Files</h1>
  <table>
    <tr>
      <th>Sr No</th>
      <th>File Name</th>
      <th>Description</th>
      <th>Last Modified</th>
    </tr>
"""

# Add rows to the table for each HTML file
num=0
for idx, html_file in enumerate(html_files, start=1):
    if html_file=="index.html":
        continue
    num+=1
    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract description from the first 100 characters of the <body> tag
    description = soup.body.text[:100]

    # Get last modified time
    modified_time = datetime.fromtimestamp(os.path.getmtime(html_file)).strftime('%Y-%m-%d %H:%M:%S')

    index_content += f"""
    <tr>
      <td>{num}</td>
      <td><a href="{html_file}">{html_file}</a></td>
      <td>{description}</td>
      <td>{modified_time}</td>
    </tr>
    """

# Close the index.html content
index_content += """
  </table>
</body>
</html>
"""

# Write the index.html content to a file
with open('index.html', 'w', encoding='utf-8') as index_file:
    index_file.write(index_content)

print("index.html created successfully!")
