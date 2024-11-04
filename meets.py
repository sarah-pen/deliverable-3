import os
import csv
import re

# Directory where CSV files are stored
csv_directory = 'meets'

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
    <script src="../animations.js"></script>
</head>
<body>

<a href="#main" id="skip">Skip to Main Content</a>

<header>
    <img src="images/banner.jpg" alt="running track close up">
    <div><h1>Skyline Cross Country Team</h1></div>
</header>
<nav>
    <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="meets.html">Meet Results</a></li>
    <li><a>Athletes</a></li>
    <li><a>Schedule</a></li>
    </ul>
</nav>

<main id="main">
<h1>Meet Results</h1><br>
<div id="meets-container">
<table id="all-meets">
    <thead>
        <tr>            
            <th>Meet Title</th>
            <th>Date</th>
            <th>Gender</th>
            <th>Place</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>
</div>


</main>

<footer>
    <p>
    Skyline High School<br>
    <address>
    2552 North Maple Road<br>
    Ann Arbor, MI 48103<br><br>
    </address>
    <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
    Follow us on Instagram <a href = "https://www.instagram.com/a2skylinexc/" aria-label="Instagram"><i class="fa-brands fa-instagram"></i>  </a> 


    </footer>
    <script src="js/imagePlaceholder.js"></script>
</body>
</html>
'''

# To hold table rows
table_rows = ''

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        csv_path = os.path.join(csv_directory, filename)
        
        # Determine the gender based on the filename
        if 'boys' in filename.lower() or 'Mens' in filename:
            gender = 'Boys'
        elif 'girls' in filename.lower() or 'womens' in filename.lower():
            gender = 'Girls'
        else:
            gender = 'Unknown'  # Default if filename doesn't indicate gender

        # Open and read the CSV file
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) < 5:
                continue

            # Extract relevant fields from the CSV
            meet_title = rows[0][0]
            
            date = rows[1][0]
            
            for row in rows:
                if "Ann Arbor Skyline" in row:
                    place = row[0].strip(".")
                    break

            # Generate a file name for the link (assuming meet page exists for each CSV)
            link = ("meets/" + filename.replace('.csv', '.html')).replace("#", "")

            # Create a row for the table, with the meet title as a hyperlink and gender column
            table_rows += f'''
            <tr>
                <td><a href="{link}">{meet_title}</a></td>
                <td>{date}</td>
                <td>{gender}</td>
                <td>{place}</td>
            </tr>
            '''

# Insert the table rows into the HTML template
final_html = html_template.format(table_rows=table_rows)

# Define the path where you want to save the HTML file
# html_file_path = os.path.join("Deliverable-3", 'meets.html')

# Save the final HTML to a file
with open("meets.html", 'w') as f:
    f.write(final_html)

print("HTML file 'meets.html' has been created!")


