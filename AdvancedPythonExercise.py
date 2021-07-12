import shutil, re, os


def search(file_path, pattern = r'\d{3}-\d{3}-\d{4}'):

    file = open(file_path, 'r')
    text = file.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


'''
shutil.unpack_archive('C:\\Users\\imshi\\Downloads\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip', '', 'zip')

with open('extracted_content/Instructions.txt') as file:
    print(file.read())
'''

results = []

for folder, sub_folder, files in os.walk(os.getcwd() + '\\extracted_content'):

    for file in files:
        full_path = folder + '\\' + file

        results.append(search(full_path))

for result in results:
    if result != '':
        print(result.group())