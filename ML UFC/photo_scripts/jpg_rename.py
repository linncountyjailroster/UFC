#code that changes all jpg files names.

import os
import glob

# file path here! the r is reading the file and associated with os.chdir().
os.chdir(r"C:/Users/nigel/Desktop/ground")
# for loop, index and oldfile place holders. enumerate finds all .jpg and starts at 1.
for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):

    #newfile is formating changes to name using index holder.
    newfile = '{}.jpg'.format(index)
    #Now add add string to newfile for final output
    newfile = 'ground_'+newfile
    
    #this print statement proves final output changes.
    print(newfile)

    #os.rename(src,dst)
    #src - This is the actual name of the file or directory.
    #dst − This is the new name of the file or directory.
#in this case are os.rename is rewritting to the same folder directory
    #os.rename (oldfile,newfile)

