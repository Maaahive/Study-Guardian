class ProgressAgent:
    def __init__(self, memory):
        self.progress = memory

    def update_progress(self, topic_score):
        for topic, result in topic_score.items():
            score = result["score"]
            total = result["total"]
            final_score = (score / total)
            self.progress.update_topic(topic, final_score)