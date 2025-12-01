class MemoryStore:
    def __init__(self):
        self.data = {
            "topic_progress" : {},
            "metrics": {
                "quizzes_taken" : 0,
                "questions_asked" : 0
            },
            "quiz_history" : []
        }

    def update_topic(self, topic, result):
        self.data["topic_progress"][topic] = result

    def increment_quiz_metrics(self, num_questions):
        self.data["metrics"]["quizzes_taken"] += 1
        self.data["metrics"]["questions_asked"] += num_questions

    def quiz_history_append(self, quiz):
        """
        result = {
            "topic" : str,
            "score" : float,
            "total" : int
            "feedback" : str
        }
        """
        self.data["quiz_history"].append(quiz)
    def get_memory(self):
        return self.data