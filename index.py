import os
import csv
import re
import random

# try:
with open("meets/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv", mode='r', newline='', encoding='utf-8') as csvfile:
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
        meet_id = extract_meet_id(link_url)
        path = f"images/meets/{meet_id}"
        if not os.path.exists(path):
            return ""
        all_files = os.listdir(path)

        # Filter out non-image files if necessary (assuming .jpg, .png, etc.)
        image_files = [f for f in all_files if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Select 1 random image
        image_path = f"images/meets/{meet_id}/" + random.choice(image_files)
        return image_path

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

    <header>
        <img src="images/banner.jpg" alt="running track close up">
        <div><h1>Skyline Cross Country Team</h1></div>
    </header>

    <a href="#main" id="skip">Skip to Main Content</a>
    
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="meets.html">Meet Results</a></li>
            <li><a>Athletes</a></li>
            <li><a>Schedule</a></li>
        </ul>
    </nav>

    <main id="main">
        <h1>Welcome to the Ann Arbor Skyline Cross Country Team!</h1>
        <br>

        <p>We are a high school cross country team located in Ann Arbor, Michigan, and we compete in races all over the Midwest! This site provides past race data, athlete profiles, and a photo gallery for each meet.</p>
        <hr>
        <div id="highlight">
            <h2>Race Highlight</h2>
            <h3><a href="{link_url}">{title}</a></h3>
            <p>{date}</p>
            <br>
            <p>{summary_text}</p>
        <br>
        <img src="{select_random_photo()}" width="200" alt="Athlete running in {title}">
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

    </body>
    </html>
    '''



# Define the path where you want to save the HTML file
# html_file_path = os.path.join("Deliverable-3", 'index.html')

# Save the final HTML to a file
with open("index.html", 'w') as f:
    f.write(html_template)

print("HTML file 'index.html' has been created!")


