import androidhelper as android

droid = android.Android()
droid.makeToast('Hello, Android!')
droid.dialogCreateAlert('ASE', 'Hello, Android!')
droid.dialogSetPositiveButtonText('Continue')
droid.dialogShow()
