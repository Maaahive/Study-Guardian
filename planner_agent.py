from tools.scheduling_tool import allocate_schedule
from llm_client import generate_text
import logging

class PlannerAgent:
    def __init__(self, memory):
        self.memory = memory

    def generate_plan(self, syllabus, exam_date, daily_study_time):
        schedule = allocate_schedule(syllabus, exam_date, daily_study_time)
        logging.info("PlannerAgent: generated schedule with %d items", len(schedule))
        
        return schedule
    
    def summarize_plan(self, schedule, exam_date):
        """
        Uses Gemini to create a friendly summary of the study plan.
        """

        logging.info("PlannerAgent: Summarizing study plan.")
        topics = [item["topic"] for item in schedule]

        prompt = f"""
        The student has the exam on {exam_date}.
        They need to study the following topics: {', '.join(topics)}.
        Study Schedule:
        {schedule}

        Write a short and friendly summary explaining :
        - what topics to focus on
        - how to manage time effectively
        - any additional study tips

        Address them as "you"
        """
        summary = generate_text(prompt, system_instruction="You are a helpful study assistant.")
        return summary