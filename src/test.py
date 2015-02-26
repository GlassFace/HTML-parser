import re
text = """Hello my friends.
        How are you doing?"""
        
output = re.sub(r"\s+", " ", text)
print(output)        