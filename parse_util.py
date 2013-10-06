# Given a string of the email content, an exact match of text
# Return the conbined paragraph text that contains this text

# when where what
# long paragraph

SHORT_SENTENCE_LIMIT = 60

def matchDateParagraph(email, date):
    paragraphs = email.split('\n')
    paragraphs = [line.strip() for line in paragraphs]

    i = 0
    result = ""
    while i < len(paragraphs) and paragraphs[i].find(date) == -1:
        i += 1

    # not found
    if i == len(paragraphs)
        return None

    if len(paragraphs[i] > SHORT_SENTENCE_LIMIT):
        return paragraphs[i]
    else:
        u = i
        d = i
        while u > 0 and len(paragraphs[u]) > 0 and len(paragraphs[u] <= SHORT_SENTENCE_LIMIT):
            u -= 1
        while d < len(paragraphs) and len(paragraphs[d]) > 0 and len(paragraphs[d] <= SHORT_SENTENCE_LIMIT):
            u -= 1


