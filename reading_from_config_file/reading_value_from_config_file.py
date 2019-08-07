import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("modelSelection.ini")
Name=Config.get('General','Name')

print(Name)
# vishal_kr_yadav

# type
# <type 'str'>
