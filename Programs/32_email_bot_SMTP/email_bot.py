import smtplib, datetime as dt, random as rd, pandas as pd

# Email authentication 
my_email = "Add your email"
password = "Add the app password"
smtp = "Your smtp"

# Getting the current day and month
today_date = dt.datetime.now()
mon = today_date.month
day = today_date.day

# Opening the wishes file, getting the list of wishes and choosing a random wish
with open("wishes.txt") as file:
    wish = file.read()
    wish = wish.split(sep='\n\n')
    random_wish = rd.choice(wish)

# Reading the birthday dataset and making a new dataset with today's birthdays
birthdays_data = pd.read_csv("birthdays.csv")
todays_birthdays = birthdays_data[(birthdays_data["month"] == mon) & (birthdays_data["day"] == day)]

# Sending the email to everyone in the today's birthdays dataset
for index, row in todays_birthdays.iterrows():
    todays_wish = f"Subject: Birthday Greetings\n\nHi {row['name']}, \n\n{random_wish} \nLove, Your Name."
    todays_wish = todays_wish.encode('utf-8')
    with smtplib.SMTP(smtp, port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs= row['email'], 
            msg= todays_wish)
