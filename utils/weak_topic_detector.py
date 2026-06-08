def find_weak_topics(scores):

    weak = []

    for topic, values in scores.items():

        avg = sum(values)/len(values)

        if avg < 6:
            weak.append(topic)

    return weak