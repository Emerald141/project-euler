def listexclude(entrylist, *badnums):
        editedlist = entrylist[:]
        for badnum in badnums:
                try:
                        editedlist.remove(badnum)
                except ValueError:
                        pass
        return editedlist
