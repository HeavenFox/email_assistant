import alchemyapi

def generate_topics(title, body, weight=5):
    text = "\n".join([title] * weight + [body])

    api = alchemyapi.AlchemyAPI()

    keywords = api.keywords('text', text)['keywords']

    last_relevance = 1
    topics = []
    for kw in keywords:
        if last_relevance - float(kw['relevance']) > 0.3:
            break
        last_relevance = float(kw['relevance'])
        topics.append(kw['text'])

    return topics


