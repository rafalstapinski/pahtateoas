from pathatoes.dom import *

z = div()[
    "thinger",
    div()[p()["paragraph",],],
]

print(z.to_html())
