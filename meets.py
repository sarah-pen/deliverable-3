import os
import csv

# Directory where CSV files are stored
csv_directory = 'Deliverable-3/meets'

# HTML template for the table (without CSS)
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meet Results</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">

</head>
<body>

<a href="#main" id="skip">Skip to Main Content</a>

<!-- <div class="logo-section">
    <a href="index.html">
        <img src="images/logo.png" alt="Event Logo" class="logo">
    </a>
    <h1>Ann Arbor Skyline High School Cross Country</h1>
</div> -->

<nav>
    <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="meets.html">Meet Results</a></li>
    <li><a href="#athletes">Athletes</a></li>
    <li><a href="#schedule">Schedule</a></li>
    <li><a href="#gallery">Gallery</a></li>
    </ul>
</nav>

<header>
<h1>Meet Results</h1>
</header>

<main>
<table id="all-meets">
    <thead>
        <tr>
            <th>Meet Title</th>
            <th>Date</th>
            <th>Summary</th>
            <th>Link</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>
</main>

</body>
</html>
'''

# To hold table rows
table_rows = ''

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        csv_path = os.path.join(csv_directory, filename)
        
        # Open and read the CSV file
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:

            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) < 5:
                continue
        
            # Extract relevant fields from the CSV

            meet_title = rows[0][0]
            date = rows[1][0]
            summary = rows[3][0]

            # Generate a file name for the link (assuming meet page exists for each CSV)
            link = ("meets/" + filename.replace('.csv', '.html')).replace("#", "")

            # Create a row for the table
            table_rows += f'''
            <tr>
                <td>{meet_title}</td>
                <td>{date}</td>
                <td>{summary}</td>
                <td><a href="{link}">View Full Results</a></td>
            </tr>
            '''

# Insert the table rows into the HTML template
final_html = html_template.format(table_rows=table_rows)

# Define the path where you want to save the HTML file
html_file_path = os.path.join("Deliverable-3", 'meets.html')

# Save the final HTML to a file
with open(html_file_path, 'w') as f:
    f.write(final_html)

print("HTML file 'meets.html' has been created!")
