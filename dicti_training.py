book = {}

book.update({"blueberry": ["mustikka", "blåbär"]})
book.update({"apple": "omena"})
book.update({"banana": "banaani"})
book["orange"] = "appelsiini"
book["kiwi"] = "kiivi"

book.setdefault("strawberry", "mansikka")

print(book)