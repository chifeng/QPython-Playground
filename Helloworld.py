import androidhelper
droid = androidhelper.Android()
respond = droid.dialogGetInput("Hello", "What is your name?")
print respond
name = respond.result
if name:
    message = 'Hello, %s!' % name
else:
    message = "Hey! And you're not very polite, %Username%!"
droid.makeToast(message)
