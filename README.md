# **Twitch Song Request Filter**

This little app helps you automatically find song requests from a spreadsheet and add them to a Spotify playlist for you to review.

## **Part 1: One-Time Setup**

You only need to do this part **once**.

### **Step 1: Get Your Spotify API Keys**

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.  
2. Click **"Create App"**.  
3. Give it a name like My Twitch Songs and a description. Check the boxes to agree to the terms.  
4. You will now see a **Client ID** and a **Client Secret**. Keep this page open\!  
5. Click the green **"Edit Settings"** button.  
6. In the box that says **"Redirect URIs"**, type exactly this: http://127.0.0.1:8888/callback  
7. Click **"Add"**, then scroll down and click **"Save"**.

### **Step 2: Download and Unzip the Project**

Download the streamer-song-requests folder and unzip it to a memorable location, like your Desktop.

### **Step 3: Fill in Your Details**

You need to tell the app about your secret keys and your playlist.

1. **Fill in your API Keys:**  
   * In the project folder, find the file named .env-example, rename to.env.  
   * Open it with a simple text editor (like Notepad or TextEdit).  
   * Copy your **Client ID** and **Client Secret** from the Spotify page into this file.  
   * Save and close the file. It should look like this:  
     SPOTIPY\_CLIENT\_ID='YOUR\_CLIENT\_ID\_HERE'  
     SPOTIPY\_CLIENT\_SECRET='YOUR\_CLIENT\_SECRET\_HERE'  
     SPOTIPY\_REDIRECT\_URI='http://127.0.0.1:8888/callback'

2. **Fill in your Playlist Info:**  
   * Find the file named config.py and open it.  
   * **PLAYLIST\_ID**: Go to the Spotify playlist you want the songs added to. Click the ... button \-\> Share \-\> "Copy Spotify URI". Paste it in, and then **delete everything except the long code at the end**.  
     * *Example:* If you copy spotify:playlist:5AbBao6L4A3o5U9262z4wM, you only want 5AbBao6L4A3o5U9262z4wM.  
   * **SPOTIFY\_USERNAME**: Go to your [Spotify Account Page](https://www.spotify.com/account/overview/). Your username is shown there (it might be a random string of letters and numbers). Copy it.  
   * Save and close the file.

### **Step 4: Install the Required Tools**

1. **Windows:** Open the Start Menu, type cmd, and press Enter.  
2. **Mac:** Open the Spotlight search (Cmd+Space), type Terminal, and press Enter.  
3. In the black window that appears, you need to navigate to the project folder. Type cd (with a space), then drag the spotify-song-requests folder from your Desktop directly into the window and press Enter.  
4. Now, copy and paste the following command into the window and press Enter. This will install the tools the app needs.  
   pip install \-r requirements.txt

**Setup is complete\! You won't have to do these steps again.**

## **Part 2: How to Use (Your Regular Routine)**

Do this every time you want to process new song requests.

### **Step 1: Get Your Song Requests**

1. Open your Google Form responses in Google Sheets.  
2. Go to File \-\> Download \-\> Comma Separated Values (.csv).  
3. Find the downloaded file. Rename it to song\_requests.csv.  
4. Move this song\_requests.csv file into the data folder inside your main spotify-song-requests project folder. **Replace the old file if it asks.**

**Important:** Your spreadsheet **must** have columns named exactly Song Name, Artist, and Album.

### **Step 2: Run the App**

1. Open the Terminal or Command Prompt window again, just like in the setup.  
2. Make sure you are in the project folder (use the cd command from setup if you closed the window).  
3. Copy and paste the following command and press Enter:  
   python \-m src.main

**The very first time you run this**, a web browser will pop up asking you to log in to Spotify and agree. This is normal. After you agree, you can close the browser tab. The app will then run in the terminal.

You will see the app searching for the songs and telling you which ones it added to your playlist. That's it\!