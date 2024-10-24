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
</head>
<body>

<h2>Meet Results</h2>
<table>
    <thead>
        <tr>
            <th>Meet Title</th>
            <th>Date</th>
            <th>Location</th>
            <th>Summary</th>
            <th>Link</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>

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
            link = filename.replace('.csv', '.html')

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
