text = "HI there Vedesh here\nI am in Osmania!\n"
new_append = "Have a nice day! See ya\n"

with open('write.txt', 'a') as file:
    file.write(new_append)