# Pull in the CSV file and store it to file
file = open("UserList.csv")

# Read the file to convert it into text to store in contents
contents = file.read()

# Split the contents into a list of rows based on the newline
rows = contents.split("\n")

# Loop through the rows in order to find which ones contain "229.62.232.190"
for row in rows:

    # If the index of "229.62.232.190" is found then print "COMPANY SERVER FOUND" and user info
    if(row.find("229.62.232.190") > -1):
        print("COMPANY PRIVATE SERVER FOUND")

        # Split the current row on commas
        user_info = row.split(",")

        # Print out the user's name, password, and hours online
        print("USER: " + user_info[0])
        print("PASSWORD: " + user_info[1])
        print("HOURS ONLINE: " + user_info[2])

        # Split the IP column into a list on semicolons
        ip_list = user_info[3].split(";")

        # Loop through the ip_list and print them to the screen
        print("IPs:")
        for IP in ip_list:
            print(IP)

        print("----------")


