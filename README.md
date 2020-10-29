# mail-checker
tool to check whether the email address is valid or not

- $ git clone https://github.com/ExsoKamabay/mail-checker.git
- $ cd 'mail-checker'
- $ pip3 install -r requirements.txt
- $ python3 mail_checker.py

or

- $ git clone https://github.com/ExsoKamabay/mail-checker.git && cd 'mail-checker' && pip3 install -r requirements.txt && python3 mail_checker.py

Valid emails return green results, invalid results return orange results<br>
input = Mail, Mode, Arg 
- Mode : check,random,file
- M check : lexyong@gmail.com check -> just check whether it is valid or invalid.
- M random: *yong66@gmail.com random xle -> Check and repeat ten times using a random string.
- M file : *yong@gmail.com file word.txt -> checking using the list inside the file
<img src='https://raw.githubusercontent.com/ExsoKamabay/mail-checker/main/screenshoot.png'>
type 'help me': how to use
