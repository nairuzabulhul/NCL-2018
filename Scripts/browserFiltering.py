import sqlite3   
import time, datetime

def firefox_history(file_name):

       # Connect to the Database
        connect_db = sqlite3.connect(file_name)
        
        # access data using cursor
        access_db = connect_db.cursor()

        # select specific field from the the database
        db = access_db.execute('SELECT url,title, last_visit_date FROM moz_places')

        # loop through the db
        #save_browser_logs(("FireFox History\n\n"), browser_file)
        for row in db:
            row = list(row)
            urls = row[0]          # returns website urls
            website_title = row[1] # returns website titles

            # print results 
            print(("Website Title: " + unicode(website_title) + "\n"))
            print(("URL: " + urls + "\n"), browser_file)
                #print (("Visit Time: " + str(visit_time) + "\n"), browser_file)
                #print(("\n\n"), browser_file)


print firefox_history("browser.sqlite")
