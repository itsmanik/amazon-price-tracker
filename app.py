import smtplib

my_mail = "manikstestmail@gmail.com"
password = "ohdy fcoe hstn hvdu"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=password)
message = "Subject:Hello..\n\n"
connection.sendmail(my_mail, "maniksh2004@gmail.com", message)
connection.close()

# import requests
# import smtplib
# from bs4 import BeautifulSoup

# r = requests.get("https://www.flipkart.com/motorola-edge-50-fusion-forest-green-256-gb/p/itm372843264e10a?pid=MOBHYVFV3RNAGXF6&lid=LSTMOBHYVFV3RNAGXF6A8TQA2&marketplace=FLIPKART&q=phone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=92275c1c-2c11-409d-a87a-9cb5746a3e9a.MOBHYVFV3RNAGXF6.SEARCH&ppt=hp&ppn=homepage&ssid=36bc8bq8n40000001727088886589&qH=f7a42fe7211f98ac")
# soup = BeautifulSoup(r.content, "html.parser")
# product_name = soup.find("span", class_="VU-ZEz").text
# price = soup.find("div", class_="Nx9bqj CxhGGd").text
# content = product_name + "\nPrice: " + price


# my_mail = "manikstestmail@gmail.com"
# password = "ohdy fcoe hstn hvdu"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_mail, password=password)
# message = "Subject:Price Today\n\n" + content
# print(message)
# message = ''.join([char if ord(char) < 128 else ' ' for char in message])
# print(message)
# connection.sendmail(my_mail, "maniksh2004@gmail.com", message)
# connection.close()