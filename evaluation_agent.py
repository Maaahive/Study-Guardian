import logging
from llm_client import generate_text

class EvaluationAgent:
    def __init__(self, memory):
        self.memory = memory

    def evaluate_ans(self, quiz, user_ans):
        """
        quiz: list of {topic, question}
        user_answers: list of strings, same length as quiz

        Returns:
            results_per_question: list of dicts
            stats: dict with overall and per-topic performance
        """
         
        if len(quiz) != len(user_ans):
            raise ValueError("Number of Quiz and user answers mismatch.")
        
        logging.info("EvaluationAgent: Evaluating %d answers.", len(quiz))

        qna_blocks = []
        for i, (q, ans) in enumerate(zip(quiz, user_ans), start = 1):
            qna_blocks.append(f"Q{i} (Topic : {q['topic']}) : {q['question']}\nStudent answer: {ans}")
        qa_text = "\n\n".join(qna_blocks)

        prompt = f"""
        You are a strict but fair exam evaluator.

        Given the following questions and student answers, evaluate each answer.

        For EACH question:
        - Give a score between 0 and 1 (0 = completely wrong, 1 = perfect, allow decimals)
        - Give 1 short line of feedback

        Return output in this EXACT format, one line per question:

        Q<index> | <topic> | <score> | <feedback>

        Questions and answers:
        {qa_text}
        """
        text = generate_text(prompt, system_instruction="Evaluate exam answers and score them numerically.")

        results = []
        topic_stats = {}

        for line in text.splitlines():
            line = line.strip()
            if not line or not line.startswith("Q"):
                continue
            try:
                parts = [p.strip() for p in line.split("|")]
                q_index = int(parts[0][1:])
                topic = parts[1]
                score = float(parts[2])
                feedback = parts[3]
                results.append({"index": q_index, "topic": topic, "score": score, "feedback": feedback})
                
                if topic not in topic_stats:
                    topic_stats[topic] = []
                topic_stats[topic].append(score)

            except Exception as e:
                logging.error("EvaluationAgent: Error parsing evaluation line: %s (%s)", line, e)
                continue

        stats = {
            'overall_score': 0.0,
            "total_questions": len(results),
            "per_topic": {}
        }

        if results:
            stats['overall_score'] = sum(r['score'] for r in results) / len(results)

        for topic, scores in topic_stats.items():
            avg = sum(scores) / len(scores)
            stats['per_topic'][topic] = avg

            self.memory.update_topic(topic, avg)

            self.memory.quiz_history_append({
                "topic": topic,
                "score": sum(scores),
                "total": len(scores),
                "feedback": f"Average performance in {topic}: {avg:.2f}"
            })

        logging.info("EvaluationAgent: Evaluation complete. Overall score: %.2f", stats['overall_score'])
        return results, stats