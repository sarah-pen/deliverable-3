import os
import csv
import re
import random

# Directory where CSV files are stored
csv_directory = 'Deliverable-3/meets'

# try:
with open("Deliverable-3/meets/SEC-HS_Jamboree_#2_(Red)_Mens_5000_Meters_Reserve_Boys_24.csv", mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

    # Extract values from the first five rows
    title = rows[0][0]
    date = rows[1][0]
    link_url = rows[2][0]
    summary_text = rows[3][0]

    # Step 1: Extract the meet ID from the URL
    def extract_meet_id(url):
        # Regex to extract the meet ID, which is the number right after '/meet/'
        match = re.search(r"/meet/(\d+)", url)
        print(f"The meet id is {match}")
        if match:
            print(f"Returning {match.group(1)}")
            return match.group(1)
        else:
            raise ValueError("Meet ID not found in URL.")


    def select_random_photo():
        print(os.getcwd())
        all_files = os.listdir(f"Deliverable-3/images/meets/{extract_meet_id(link_url)}")

        # Filter out non-image files if necessary (assuming .jpg, .png, etc.)
        image_files = [f for f in all_files if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Select 1 random image
        return random.choice(image_files)

    # HTML template for the table (without CSS)
    html_template = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>37th Early Bird Open Mens 5000 Meters HS Open 5K</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/00d792a174.js" crossorigin="anonymous"></script>

    </head>
    <body>

    <a href="#main" id="skip">Skip to Main Content</a>
    
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="meets.html">Meet Results</a></li>
            <li><a href="#athletes">Athletes</a></li>
            <li><a href="#schedule">Schedule</a></li>
        </ul>
    </nav>

    <main id="main">
        <h1>Welcome to the Ann Arbor Skyline Cross Country Team!</h1>
        <br>

        <p>We are a high school cross country team located in Ann Arbor, Michigan, and we compete in races all over the Midwest! This site provides past race data, athlete profiles, and a photo gallery for each meet.</p>

        <h2>Race Highlight</h2>
        <h3>{title}</h3>
        <p>{date}</p>
        <br>
        <p>{summary_text}</p>
        <img src="{select_random_photo()}">


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

    </body>
    </html>
    '''



# Define the path where you want to save the HTML file
html_file_path = os.path.join("Deliverable-3", 'index.html')

# Save the final HTML to a file
with open(html_file_path, 'w') as f:
    f.write(html_template)

print("HTML file 'index.html' has been created!")


