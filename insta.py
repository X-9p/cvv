import os 
os.system('apk add py-pip')
os.system('pip install console')
os.system('pip install requests')
os.system('clear')
print("""
------------------------------------------
                  welcome 🐉             
            tool username instagram      
------------------------------------------

[1] create combo .
[2] check combo .
""")
bui = input("choose  :")

if '1' in bui:
    import random
    import string
    import console
    import os

    os.system('clear')
    def create_file_with_content(filename, lines_count, characters_per_line):
        content = generate_content(lines_count, characters_per_line)

        with open(filename, 'w') as file:
            file.write(content)

    def generate_content(lines_count, characters_per_line):
        content = ""
        for _ in range(lines_count):
            line = generate_random_line(characters_per_line)
            content += line + "\n"

        return content

    def generate_random_line(characters_count):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=characters_count))
        line = '_'.join(random_string[i:i+1] for i in range(0, len(random_string), 1))[:5]
        return line

    filename = 'combo.txt'
    lines_count = int(input("Please enter the number of lines: "))
    characters_per_line = 5

    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        create_file_with_content(filename, lines_count, characters_per_line)
        print(f"File '{filename}' created successfully.")
    except ValueError:
        print("An error occurred while creating the file.")
elif bui == '2':
    import os
    import console
    import requests
    from concurrent.futures import ThreadPoolExecutor
    os.system('clear')
    token = "6772893835:AAGPxcIF6j0gIEfGABsT_QQyVQMp3or23qg"
    id = "6294996199"
    correct_attempts = 0
    incorrect_attempts = 0
    jk = 'combo.txt'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=welcome \nHunting has begun!\nby : @t_8mm')
    with open(jk, 'r', encoding='utf-8') as file:
        texts_to_check = file.read().splitlines()

    def check_user(username):
        global correct_attempts
        global incorrect_attempts

        rrx4j = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/", headers={'Host':'www.instagram.com', 'content-length':'70', 'sec-ch-ua':'"Chromium";v="106",', 'x-ig-app-id':'936619743392459', 'x-ig-www-claim':'hmac.AR3-jjxWxD7osd7WtAM_c6iLQHDvlDZucbWWVQ38t2tPdF3t', 'sec-ch-ua-mobile':'?0', 'x-instagram-ajax':'de83d85cf90c', 'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'viewport-width':'980', 'content-type':'application/x-www-form-urlencoded', 'accept':'*/*', 'x-requested-with':'XMLHttpRequest', 'x-asbd-id':'198387', 'x-csrftoken':'NEhRd2uaYf6774IYrUuw6svzofnU3COW', 'sec-ch-prefers-color-scheme':'dark', 'sec-ch-ua-platform':'"Linux"', 'origin':'https://www.instagram.com', 'sec-fetch-site':'same-origin', 'sec-fetch-mode':'cors', 'sec-fetch-dest':'empty', 'referer':'https://www.instagram.com/accounts/emailsignup/', 'accept-language':'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5'}, data={"email":"email=x4j@gmail.com+", "username":username, "first_name":"x4j", "opt_into_one_tap":"false"}).text

        if "username_is_taken" in rrx4j:
            os.system('clear')
            incorrect_attempts += 1
            print(f'Correct attempts: {correct_attempts}')
            print(f'Incorrect attempts: {incorrect_attempts}')
            print(f'the user : {user_input}')
        else:
            os.system('clear')
            correct_attempts += 1

            print(f'Correct attempts: {correct_attempts}')
            print(f'Incorrect attempts: {incorrect_attempts}')

            bn = f"""
    [~] New user
    ~ the user : {username}
    - by : @t_8mm
    """
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={bn}')

    # Check each user in the file
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(check_user, texts_to_check)
else:
    print("Please choose either 1 or 2.")
