def capitalize():
    s: str
    s = "tom and jerry"
    assert s.capitalize() == "Tom and jerry"
    s = "12wddd"
    assert s.capitalize() == s
    s = " tom and jerry"
    assert s.capitalize() == s
    assert "empty string" .capitalize() == "Empty string"
    assert "".capitalize() == ""
    assert "lPyThOn".capitalize() == "Lpython"
    x: str
    x = "lPyThOn"
    assert x.capitalize() == "Lpython"


def lower():
    s: str
    s = "AaaaAABBbbbbBB!@12223BN"
    assert s.lower() == "aaaaaabbbbbbbb!@12223bn"
    assert "DDd12Vv" .lower() == "ddd12vv"
    assert "".lower() == ""

def upper():
    s: str
    s = "AaaaAABBbbbbBB!@12223BN"
    assert s.upper() == "AAAAAABBBBBBBB!@12223BN"
    assert "DDd12Vv".upper() == "DDD12VV"
    assert "".upper() == ""

def strip():
    s: str
    s = "     AASAsaSas    "
    assert s.rstrip() == "     AASAsaSas"
    assert s.lstrip() == "AASAsaSas    "
    assert s.strip() == "AASAsaSas"
    assert "     AASAsaSas    " .rstrip() == "     AASAsaSas"
    assert "     AASAsaSas    " .lstrip() == "AASAsaSas    "
    assert "     AASAsaSas    " .strip() == "AASAsaSas"
    assert "".strip() == ""


def swapcase():
    s: str
    s = "aaaaaabbbbbbbb!@12223bn"
    assert s.swapcase() == "AAAAAABBBBBBBB!@12223BN"
    assert "AASAsaSas" .swapcase() == "aasaSAsAS"
    assert "".swapcase() == ""


def find():
    s: str
    sub: str
    s = "AaaaAABBbbbbBB!@12223BN"
    sub = "@"
    assert s.find(sub) == 15
    assert s.find('B') == 6
    assert "empty strings" .find("string") == 6
    s2: str
    s2 = "Well copying a string from a website makes us prone to copyright claims. Can you just write something of your own? Like just take this review comment and put it as a string?"
    assert s2.find("of") == 102
    assert s2.find("own") == 110
    assert s2.find("this") == 130
    assert s2.find("") == 0
    assert "".find("dd") == -1
    assert "".find("") == 0
    s2 = ""
    assert s2.find("") == 0
    assert s2.find("we") == -1
    assert "".find("") == 0


def startswith():
    s: str
    s = "   empty"
    assert s.startswith("  ") == True
    assert "  @" .startswith(" ") == True
    assert "   emptyAaaaAABBbbbbBB" .startswith(s) == True
    assert "   emptyAaaaAABBbbbbBB" .startswith("AABB") == False
    assert "   emptyAaaaAABBbbbbBB" .startswith("emptyAaxX") == False

    assert "". startswith("sd") == False
    assert "empty" .startswith("") == True
    assert "".startswith("") == True
    assert s.startswith("") == True
    s = ""
    assert s.startswith("") == True
    assert s.startswith("sdd") == False
    assert "".startswith("ok") == False

def endswith():

    # The following test suite fulfils the control flow graph coverage
    # in terms of Statement Coverage and Branch Coverage associated with endwith() functionality.

    # Case 1: When string is constant and suffix is also constant 
    assert "".endswith("") == True
    assert "".endswith(" ") ==  False
    assert "".endswith("%") == False
    assert "".endswith("a1234PT#$") == False
    assert "".endswith("blah blah") == False
    assert " rendezvous 5:30 ".endswith("") == True
    assert " rendezvous 5:30 ".endswith(" ") == True
    assert " rendezvous 5:30 ".endswith(" 5:30 ") == True
    assert " rendezvous 5:30 ".endswith("apple") == False
    assert "two plus".endswith("longer than string") == False


    # Case 2: When string is constant and suffix is variable
    suffix: str
    suffix = ""
    assert "".endswith(suffix) == True
    suffix = " "
    assert "".endswith(suffix) ==  False
    suffix = "5:30 "
    assert " rendezvous 5:30 ".endswith(suffix) == True
    suffix = ""
    assert " rendezvous 5:30 ".endswith(suffix) == True
    suffix = "apple"
    assert " rendezvous 5:30 ".endswith(suffix) == False
    suffix = "longer than string"
    assert "two plus".endswith(suffix) == False

    # Case 3: When string is variable and suffix is either constant or variable
    s: str
    s = ""
    assert s.endswith("") == True
    assert s.endswith("apple") == False
    assert s.endswith(" ") == False
    assert s.endswith(suffix) == False

    s = " rendezvous 5 "
    assert s.endswith(" $3324") == False
    assert s.endswith("5 ") == True
    assert s.endswith(s) == True
    suffix = "vous 5 "
    assert s.endswith(suffix) == True
    suffix = "apple"
    assert s.endswith(suffix) == False

def partition():
    
    # Note: Both string or seperator cannot be empty 
    # Case 1: When string is constant and seperator is also constant 
    assert "   ".partition(" ") == (""," ","  ")
    assert "apple mango".partition(" ") == ("apple"," ","mango")
    assert "applemango".partition("afdnjkfsn") ==  ("applemango","","")
    assert "applemango".partition("an") == ("applem", "an", "go")
    assert "applemango".partition("mango") == ("apple", "mango", "")
    assert "applemango".partition("applemango") == ("", "applemango", "")
    assert "applemango".partition("ppleman") == ("a", "ppleman", "go")
    assert "applemango".partition("pplt") == ("applemango", "", "")

    # Case 2: When string is constant and seperator is variable
    seperator: str
    seperator = " "
    assert "   ".partition(seperator) == (""," ","  ")
    seperator = " "
    assert "apple mango".partition(seperator) ==  ("apple"," ","mango")
    seperator = "5:30 "
    assert " rendezvous 5:30 ".partition(seperator) == (" rendezvous ", "5:30 ", "")
    seperator = "^&"
    assert "@#$%^&*()#!".partition(seperator) == ("@#$%", "^&", "*()#!")
    seperator = "daddada "
    assert " rendezvous 5:30 ".partition(seperator) == (" rendezvous 5:30 ", "", "")
    seperator = "longer than string"
    assert "two plus".partition(seperator) == ("two plus", "", "")

    # Case 3: When string is variable and seperator is either constant or variable
    s: str
    s = "tomorrow"
    assert s.partition("apple") == ("tomorrow", "", "")
    assert s.partition("rr") == ("tomo", "rr", "ow")
    assert s.partition(seperator) == ("tomorrow", "", "")

    s = "rendezvous 5"
    assert s.partition(" ") == ("rendezvous", " ", "5")
    assert s.partition("5") == ("rendezvous ", "5", "")
    assert s.partition(s) == ("", "rendezvous 5", "")
    seperator = "vous "
    assert s.partition(seperator) == ("rendez", "vous ", "5")
    seperator = "apple"
    assert s.partition(seperator) == ("rendezvous 5", "", "")

def is_lower():
    # Case 1: When constant string is present
    assert "".islower() == False
    assert "APPLE".islower() == False
    assert "4432632479".islower() == False
    assert "%#$#$#32a".islower() == True
    assert "apple".islower() == True
    assert "apple is a fruit".islower() == True

    # Case 2: When variable string is present
    s: str
    s = "APPLE"
    assert s.islower() == False
    s = "238734587"
    assert s.islower() == False
    s = "%#$#$#32a"
    assert s.islower() == True
    s = "apple"
    assert s.islower() == True
    s = "apple is a fruit"
    assert s.islower() == True

def is_upper():
        # Case 1: When constant string is present
    assert "".isupper() == False
    assert "apple".isupper() == False
    assert "4432632479".isupper() == False
    assert "%#$#$#32A".isupper() == True
    assert "APPLE".isupper() == True
    assert "APPLE IS A FRUIT".isupper() == True

    # Case 2: When variable string is present
    s: str
    s = "apple"
    assert s.isupper() == False
    s = "238734587"
    assert s.isupper() == False
    s = "%#$#$#32A"
    assert s.isupper() == True
    s = "APPLE"
    assert s.isupper() == True
    s = "APPLE IS A FRUIT"
    assert s.isupper() == True

def is_decimal():
    # Case 1: When constant string is present
    assert "".isdecimal() == False
    assert "apple".isdecimal() == False
    assert "4432632479".isdecimal() == True
    assert "%#$#$#32A".isdecimal() == False
    assert "1.25".isdecimal() == False
    assert "-325".isdecimal() == False
    assert "12 35".isdecimal() == False

    # Case 2: When variable string is present
    s: str
    s = "apple"
    assert s.isdecimal() == False
    s = "238734587"
    assert s.isdecimal() == True
    s = "%#$#$#32A"
    assert s.isdecimal() == False
    s = "1.35"
    assert s.isdecimal() == False
    s = "-42556"
    assert s.isdecimal() == False
    s = "12 34"
    assert s.isdecimal() == False

def is_ascii():
    # Case 1: When constant string is present
    assert "".isascii() == True
    assert "    ".isascii() == True
    assert "Hello, World123!".isascii() == True
    assert "Hëllö, Wörld!".isascii() == False
    assert "This is a test string with some non-ASCII characters: 🚀".isascii() == False
    assert "\t\n\r".isascii() == True
    assert "12 35".isascii() == True

    # # Case 2: When variable string is present
    s: str
    s = "  "
    assert s.isascii() == True
    s = "Hello, World!"
    assert s.isascii() == True
    s = "Hëllö, Wörld!"
    assert s.isascii() == False
    s = "This is a test string with some non-ASCII characters: 🚀"
    assert s.isascii() == False
    s = "\t\n\r"
    assert s.isascii() == True
    s = "123 45 6"
    assert s.isascii() == True


def is_space():
    assert "\n".isspace() == True
    assert "    ".isspace() == True
    assert "\r".isspace() == True 

    s:str = " "
    assert s.isspace() == True   
    s = "a"
    assert s.isspace() == False

def check():
    capitalize()
    lower()
    upper()
    strip()
    swapcase()
    find()
    startswith()
    endswith()
    partition()
    is_lower()
    is_upper()
    is_decimal()
    is_ascii()
    is_space()

check()
