# supremeBot

Working Supreme Bot as of June 1st, 2019.

My goal for writing this script was to make a Supreme bot that anyone could use as a lot of the bots on the market are unsafe (collect your credit card information) or are expensive. 

Problems encountered:

I wanted to make this bot as easy to use for anyone, regardless of coding experience. I envisioned a user filling out a simple dictionary with their information, and the bot would handle the rest of the work. One of the problems with this is how Selenium locates elements on a webpage. Selenium uses the Xpath of an element (consumed as a string) to find that element on the page and interact with it. So, the program couldn't be as simple to use unless I made a dictionary with every single Xpath element corresponding to the information the user put in (which would take a very long time). 

How to use the bot?

Download this project folder and move it a preferred location. 

Go to terminal and run the command: pip install selenium

Go to the three dots in the top right of chrome, press Help -> About Google Chrome. Find the version of chrome that you're using and download the corresponding Chrome Driver at: http://chromedriver.chromium.org/downloads. Move the unzipped file into this project folder.

Open the project folder in any IDE. Edit the config.py with the product url that you want, name, email, telephone number (no hyphens or brackets), address, zip, city, card number, cvv, and apt/unit number if you have one. 

Look at the variables in the bot.py file. There are web_countries, web_provinces, web_states, web_credit_card_month, and web_credit_card_year. They are all dictionaries and each key in the dictionary corresponds to a specific value. I have set the bot to my location so on line 134, it says option[2] which corresponds to Canada from the web_countries dictionary. Change the 2 to a 1 if you live in USA. Do this for the rest of the dropdown menus (indicated with option[some_number]). Save all of the files after properly updating them. 

Open up terminal/powershell and navigate to where the project folder is located. You will need some basic knowledge of git commands for the following steps. Enter "cd {preferred_destination}" to enter that directory, "ls" to see what's in that directory, and "cd.." to go back one level in the directory. All git commands should be entered without the quotes. When you navigate to the right directory, you should see something like: Josiahs-MacBook-Pro-2:Supremebot josiahparappally$. Now run the command: python bot.py and you should see a chrome instance pop up on your screen. The webdriver is non-headless so you can see exactly what is happening. The autofill will be complete but you will need to hand-solve the captcha at the end to confirm your purchase (I will fix this in a later version). 

To do:

Break captcha at the end

Speed up entire process in a different language (possibly C)

Will increase the ease of use of program for people new to coding through using variables, not dictionaries. 

If you have any questions/concersn with the program, please email me at: josiahparappally@gmaill.com
