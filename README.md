# PyPerspective

A Simple Perspective API Library.

## Why PyPerspective
- Simple Requests
- Auto Rate Limiter
- Class Orianted
- Handles Errors

### Example Usages
```py
from PyPerspective.Perspective import Perspective
perspective = Perspective("API KEY",ratelimit=True,default_not_store=True) # Default Do Not Store Option Is True.
# Default Not Store Option Is For Not Providing Do_Not_Store Kwarg In Get Score Function
# You Can Overwrite Default If You Gave Kwarg In Get Score Func

scores = perspective.get_score("Hello What Are You Doing?",tests=["TOXICITY"],langs=["en"]) # Tests Default Setted To TOXICITY, Langs Default Setted To English
# Scores Variable Is A Comment Class

# Usage Of Comment Class:
print(scores.text) # Sended Text
print(scores.raw_data) # Result That Sended By API
print(scores.detected_langs) # Detected Langs By API
print(scores.requests_langs) # Requested Langs
print(str(scores)) # Equals To scores.tedt
print(scores["TOXICITY"]) # Returns Test Attribute Class

# Usage Of Attribute Class:
My_Attribute = scores["TOXICITY"] # Gets Class Of Provided Test
print(My_Attribute.name)  # Name Of Test
print(My_Attribute.score) # Score Of Test
print(My_Attribute.score_type) # Score Type Of Test
print(My_Attribute.spans) # Returns List Of Span Class

# Usage Of Span Class:
My_Span = scores["TOXICITY"].spans[0] # Gets First Span
print(My_Span.start) # Span Start Index
print(My_Span.end) # Span End Index
print(My_Span.score) # Span Score
print(My_Span.score_type) # Span Score Type
print(str(My_Span)) # Returns Text Between Start Index And End Index (Both Is Included)
```

###  This Package Still On Development
PyPerspective Package Still On Development. Bugs And Errors Can Be Found In Usage. Report This Bugs And Errors On Github Or [Discord](https://discord.gg/MeaWMrVX)
