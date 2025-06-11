def count_words(text: str) ->int:
    words = text.split(" ")
    return len(words)

def count_char(text: str) ->dict:
    lower_text = text.lower()
    counter = {}
    for char in lower_text:
        if char.isalpha():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

def sort_on(dic: dict) ->list[dict]:
    result = []
    for key, value in dic.items():
        result.append({"char": key, "num": value})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result