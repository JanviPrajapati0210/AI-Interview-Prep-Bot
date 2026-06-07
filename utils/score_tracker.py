def update_score(scores, topic, score):

    if topic not in scores:
        scores[topic] = []

    scores[topic].append(score)

    return scores