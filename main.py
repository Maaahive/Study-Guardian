from planner_agent import PlannerAgent
from resource_agent import ResourceAgent
from quiz_agent import QuizAgent
from progress_agent import ProgressAgent
from evaluation_agent import EvaluationAgent
from session_memory import MemoryStore
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def main():
    print("Welcome to Study Guardian!")

    memory = MemoryStore()
    planner = PlannerAgent(memory)
    resource_finder = ResourceAgent(memory)
    quiz_agent = QuizAgent(memory)
    progress_tracker = ProgressAgent(memory)
    evaluator = EvaluationAgent(memory)

    syllabus = [
        {"topic" : "Algebra", "difficulty": "medium"},
        {"topic" : "Geometry", "difficulty": "low"},
        {"topic" : "Calculus", "difficulty": "high"}
    ]
    exam_date = "2025-12-15"
    daily_study_time = 4  # hours

    plan = planner.generate_plan(syllabus, exam_date, daily_study_time)
    print("Generated Study Plan:", plan)

    plan_summary = planner.summarize_plan(plan, exam_date)
    print("\nGenerated Plan Summary(Gemini):")
    print(plan_summary)

    resources = resource_finder.find_resources(plan)
    print("\nRecommended Resources:")
    for topic, links in resources.items():
        print(f"\n{topic}:")
        for r in links:
            print(f"-{r['title']} | {r['url']}")
            print(f" {r['summary']}")

    quiz = quiz_agent.create_quiz(["Algebra"])
    print("Sample Quiz Questions:")
    for q in quiz:
        print(f"{q['topic']} -> {q['question']}")

    user_ans = []
    for i, q in enumerate(quiz):
        if i < 3:
            user_ans.append("This is my attempted answer.")

        else:
            user_ans.append("I don't know.")

    results, stats = evaluator.evaluate_ans(quiz, user_ans)
    print("\nQuiz Evaluation Results:")
    for r in results:
        print(f"Q{r['index']} ({r['topic']})-> Score={r['score']:.2f}, Feedback={r['feedback']}")

    print("\nQuiz Stats:")
    print(f"Overall Score: {stats['overall_score']:.2f}")
    print("Per Topic Scores:")
    for topic, score in stats['per_topic'].items():
        print(f"- {topic}: {score:.2f}")
    
    print("\nUpdating Progress...")
    print(memory.get_memory())

    progress_tracker.update_progress({"Algebra" : {"score" : 6, "total" : 10}})
    print("Updated Progress:", memory.get_memory())

if __name__ == "__main__":
    main()