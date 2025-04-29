import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #connects us to a Database, or makes a new one if not already made
cur = conn.cursor()  # CURSOR is what lets python enact SQL commands, so this line is allowing commands to the connected DB

cur.execute('DROP TABLE IF EXISTS Counts') #drops a table if it already exists, in this case table Counts
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)') # creates our SQL table Counts with the columns 'email' and 'count'

#region quick file open + read

filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
fileread = open(filename)

#endregion

for line in fileread: # loops through each line in the opened file
    if not line.startswith('From: '): #if it does not start with From: 
        continue #next line
    
    split = line.split() # splits line that stars with from into a list
    email = split[1] # index for email inside the list
    
    cur.execute('SELECT count FROM Counts WHERE email=?', (email,)) # this is like the executes above, except we cant pull the email directly from the text, so we use the '?, (email,)) to use our stored email in py
    row = cur.fetchone() # Grabs only the first row/response
    if row is None: # if no record exists
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,)) # create record and add count to 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email=?', (email,)) #if it goes here, then it means its already shown up once, so count gets a + 1
        
    conn.commit() # updates the SQL DB
    
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()