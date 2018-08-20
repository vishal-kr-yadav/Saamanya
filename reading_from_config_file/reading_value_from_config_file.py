import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
Name=Config.get('General','Name')

print(Name)
# vishal_kr_yadav

# type
# <type 'str'>
