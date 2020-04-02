# textmebitcoin
Get an hourly text with the current value of bitcoin.
Get a text with the current value of bitcoin at any interval you wish.
Originally this was made to run hourly non stop, that has since changed with the latest commit.

this was a length of python code to help learn a new bitcoin code i learned recently.

if you plan on having this run in the background of, lets say, a raspberry pi, leave the output
commented out like i have it set. if you really do want output, uncomment.

this code requires a twilio account https://www.twilio.com/try-twilio . once you make a trial account you will get the variables from your settings to implement here, in my case i run my code from an ubuntu host and store my variables in the .bashrc folder, and use os.environ.get to retrieve them. it helps keep my info private, allows me to post here, and i think adding that to the code looks really nice.
