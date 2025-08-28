def book_words(book_str):
    words = book_str.split()
    return len(words)

def letter_count(book):
    count = {}
    for let in book.lower():
        count.setdefault(let, 0)
        count[let] += 1
    return count

def sort_on(d):
    return d["num"]

def chars_sorted_list(num_chars):
    sorted = []
    for ch in num_chars:
        sorted.append({"char": ch, "num": num_chars[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
