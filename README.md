# GMailCleaner
Python script to clear your mails from GMail

## How to use it
You should check the [Gmail API Overview Guide](https://developers.google.com/workspace/gmail/api/guides) to authenticate and manage authorization of the script.
Once you had completed the authentication flow, lunch the mail_deleter.py program by using:

```
python3 mail_deleter.py
```

And that's it !

## Filter

### From Filter
You can write the gmail adresses to delete the mails those send you.
You simply need to write the emails in the filterFrom.txt file. In this current file, there are some examples.

### Your own filters

You can write your own filter using the [documentation gave by Google](https://support.google.com/mail/answer/7190?hl=en&ref_topic=3394593&sjid=4645570934335304100-EU), place it at the line **96** and uncomment the whole line.
