"""
# create zip file
import zipfile
with zipfile.ZipFile("new.zip","w")as zip:
    zip.write("a1.text")
    zip.write("a2.text")

"""
"""
# extract zip/ unzip

import zipfile
with zipfile.ZipFile("new.zip","r") as file:
    file.extractall()
    extracted_file = file.namelist()
    print(extracted_file)

 """

  # zip form folder/directory

import shutil
shutil.make_archive("new_file","zip","new")  