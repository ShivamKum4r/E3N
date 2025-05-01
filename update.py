import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ENTER_TEXT = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full textarea";
BUTTON_ICON = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full button";
REPLY_TEXT = "[id='__next'] [class='py-1 relative break-anywhere']  span";

def getReplyFromPi(question):
    mobile_emulation = {
        "deviceMetrics": {"width": 400, "height": 652, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options
                              )
    driver.get("https://pi.ai/talk")
    time.sleep(5)

    if driver.current_url == "https://pi.ai/onboarding":
        driver.get("https://pi.ai/talk")

    i = 2
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ENTER_TEXT))).click()

    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).click();
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).send_keys(question)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, BUTTON_ICON).click()
    time.sleep(5)
    ele = driver.find_elements(By.CSS_SELECTOR, REPLY_TEXT)
    return ele[i+1].text;

def me():
    video_folder = "C:\\E3N\\media\\else\\me"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def nolan():
    video_folder = "C:\\E3N\\media\\else\\nolan"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def pain():
    video_folder = "C:\\E3N\\media\\else\\pain"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def song():
    video_folder = "C:\\E3N\\media\\else\\song"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def world():
    video_folder = "C:\\E3N\\media\\else\\world"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def baldev():
    video_folder = "C:\\E3N\\media\\shivam"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")


    

    elif 'black hole' in query:
                       video_path = 'C:\\E3N\\media\\else\\black.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
    elif 'love' in query:
                       video_path = 'C:\\E3N\\media\\else\\love.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
    elif 'song' in query or 'songs' in query:
                       song()
                       stop()
    elif 'christopher Nolan' in query:
                       nolan()
                       stop()
    elif 'painful thoughts' in query:
                       pain()
                       stop()
    elif 'alpha' in query:
                       me()
                       stop()
    elif 'world' in query:
                       world()
                       stop()
    

    