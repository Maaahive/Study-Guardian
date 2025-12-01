from llm_client import generate_text
import logging

class QuizAgent:
    def __init__(self, memory):
        self.memory = memory

    def create_quiz(self, topics, num_questions=3):
        logging.info("QuizAgent: Creating quiz for topics: %s", topics)

        topics_str = ",".join(topics)

        prompt = f"""
        You are a strict exam setter.

        Topics: {topics_str}

        For each topic, generate {num_questions} short answer questions.
        Make them exam-style, conceptual, 1-2 lines each and not multiple choice.
        Format your answer as plain text in this structure:

        Topic: <topic_name>
        1. <question_1>
        2. <question_2>
        3. <question_3>

        Repeat for each topic.
        """
        
        import time

        for attempt in range(3):
            try:
                text = generate_text(prompt, system_instruction="Create exam questions")
                break
            except Exception as e:
                logging.error("QuizAgent: Gemini request failed, retrying... (%s)", e)
                time.sleep(2)
        else:
            raise RuntimeError("QuizAgent failed after 3 retries.")

        quiz = []
        curr_topic = None

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue

            if line.lower().startswith("topic:") :
                curr_topic = line.split(":", 1)[1].strip()
            elif line[0].isdigit() and "." in line and curr_topic:
                question = line.split(".", 1)[1].strip()
                quiz.append({"topic": curr_topic, "question": question})

        if hasattr(self.memory, "increment_quiz_metrics"):
            self.memory.increment_quiz_metrics(len(quiz))

        logging.info("QuizAgent: Generated %d questions", len(quiz))
        return quiz