# filechooser.py: simple file dialog for Android
#
# Copyright (c) dmych, 2014
#
# You may use, redistribute it and/or modify it
# under the terms of the GNU General Public License
# as published by the Free Software Foundation,
# either version 3 of the License, or any later version.

def _dialog(title, flist):
    '''display dialog with list of files/folders title
    allowing user to select any item or click Cancel 
    get user input and return selected index or None
    '''
    import androidhelper
    droid = androidhelper.Android()
    droid.dialogCreateAlert(title, '')
    droid.dialogSetItems(flist)
    droid.dialogSetNegativeButtonText('Cancel')
    droid.dialogShow()
    resp = droid.dialogGetResponse()
    droid.dialogDismiss()
    print resp
    if resp.result.has_key('item'):
        print 'RETURN:', resp.result['item']
        return resp.result['item']
    else:
        return None
    
def chooseFile(title='Choose File', folder='.'):
    '''Display choose file dialog with title and a list of
    files/folders in specified folder and allow user to
    browse file system and select file.
    Return full name of the file choosen or None
    '''
    import os.path
    from glob import glob
    d = folder
    while True:
        flist = [ os.path.split(fn)[1] for fn in glob(os.path.join(d, '*')) ]
        if d != '/':               # if it is not root
            flist.insert(0, '..')  # add parent 
        selected = _dialog(title, flist)
        if selected is None:       # user cancelled
            return None
        d = os.path.abspath(os.path.join(d, flist[selected]))
        if not os.path.isdir(d):
            return d

if __name__ == '__main__':
    print chooseFile()
