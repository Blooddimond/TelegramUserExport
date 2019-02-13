#Requirements to run: Python, xlwt, telethon. to install these dependencies, run 
# pip install xlwt
# pip install telethon
import xlwt
from telethon import TelegramClient, sync
class userlist:

    client = None
    channel = None
    usersInBoth = []
    def login():
        #api_id and api_hash from https://my.telegram.org/apps, create a program to use. 
        #If the code is not modified to have one built in, it will instead prompt the user at runtime.
        
        api_id = 'YOUR_TOKEN_ID_HERE'
        if (api_id is 'YOUR_TOKEN_ID_HERE'):
            print("you did not set an api_id in the script.")
            api_id = input('Please input api_id: ')

        api_hash = 'YOUR_HASH_ID_HERE'
        if(api_hash is 'YOUR_HASH_ID_HERE'):
            print("you did not set an api_hash in the script.")
            api_hash = input('Please input api_hash: ') 

        #Authentication Token is saved to reuse in the future for less API prompts
        #saved in whatever directory the command prompt is running from
        #Enter your Phone number in format shown in telegram.
        return client = TelegramClient('authenticationToken', api_id, api_hash).start()
    
    def selectChat():
        #sets the program to connect to the chat channel listed.
        #for example, 't.me/joinchat/ChatInviteCode' or 't.me/ChatName'
        # If the code is not modified to have one built in, it will instead prompt the user at runtime.
        url = 'URL_TO_JOIN_HERE'
        if (url is 'URL_TO_JOIN_HERE'):
            print('you did not set a url in the script.')
            url = input("Please input a valid url: ")
        return channel = client.get_entity(url)
    
    def printUsers():
        # get all the users and saves them to xls file
        book = xlwt.Workbook()
        sheet = book.add_sheet('Sheet 1')
        i = 0
        #writes their id, firstname, lastname, and username to spreadsheet
        for u in client.get_participants(channel):
            sheet.write(i, 0, u.id)
            sheet.write(i, 1, u.first_name)
            sheet.write(i, 2, u.last_name)
            if u.username is not None:
                account = '@' + u.username
                sheet.write(i, 3, account)
            else:
                sheet.write(i, 3, u.username)
            i += 1

        print('saving to spreadsheet...')
        book.save('userlist.xls')
    
    def compareChats():
        chat1 = client.get_participants(channel)
        chat2 = client.get_participants(channel2)
        for u in chat1
            for u2 in chat2
                if u.id == u2.id
                    usersInBoth.append(u)
                    break


    def main():
        client = login()
        channel = selectChat()
        printUsers()