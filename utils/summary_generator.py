def generate_summary(scores):

    report = {}

    for topic, vals in scores.items():

        report[topic] = round(
            sum(vals)/len(vals),2
        )

    return report