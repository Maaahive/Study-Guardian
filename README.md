# Study-Guardian
AI Study & Exam Agent for Syllabus Overloaded Students

# Project Overview

Study Guardian is an intelligent multi-agent AI system designed to help students prepare effectively for exams by generating personalized study plans, fetching curated learning resources, generating topic-wise quiz questions, evaluating student answers automatically, and tracking progress over time.

This project demonstrates a complete multi-agent pipeline powered by Gemini models, real-time evaluation logic, memory-based personalization, and structured output generation.

# Problem​‍​‌‍​‍‌ Statement

Students fail most times in heavily unstructured preparation for their exams, they lack directions as to what to study and the manner in which they are evaluated is also not very effective. Inflexible schedules, impersonal materials, and the traditional way of doing self-assessment result in low memorization and a weak level of readiness for the ​‍​‌‍​‍‌exam.

# Solution​‍​‌‍​‍‌ Summary

Study Guardian operates its AI agent team to:

Develop personalized study schedules
- Create a natural language plan summary
- Suggest top-notch learning resources
- Design subject-related quizzes
- Automatically grade answers
- Record performance and mastery levels

Such a system is a very powerful and flexible learning assistant which, due to its continuous adaptation, can be considered as a real tutor rather than a static study ​‍​‌‍​‍‌plan.

# Why​‍​‌‍​‍‌ Use Agents?

Using the agents system helps to organize the workflow in a decentralized way, each agent is responsible for a specialized task and can pass the results to the next agent. Such a system design gives the possibilities:

- Modular system design
- Limitless functionality
- Parallel/Sequential processing
- Memory-based ​‍​‌‍​‍‌personalization

# System Architecture
User Input  → PlannerAgent → ResourceAgent → QuizAgent → EvaluationAgent → ProgressAgent → Memory

# Agents Used
- Agent: Role
- PlannerAgent: Creates schedule + task allocation
- ResourceAgent: Finds curated external study resources
- QuizAgent: Generates exam-style questions
- EvaluationAgent: Scores user answers and gives feedback
- ProgressAgent: Updates metrics and mastery progression
- MemoryStore: Persistent topic-level mastery history

# Key AI Concepts Demonstrated

- Multi-Agent System (sequential workflow)
- LLM-powered reasoning
- Long-term memory + progress tracking
- Logging & observability
- Context engineering
- Real-time evaluation agent

# Technology Stack
- Component: Technology
- LLM: Gemini 2.5-Flash
- Language: Python
- Memory: Custom in-memory store
- Logging: Python logging module
- Architecture: Multi-agent sequential
- Execution: Local CLI app
- Tools: dotenv, google-generativeai

# Installation & Setup
1. Clone Repository
git clone https://github.com/<your-repo>  
cd Study-Guardian  

2. Create Virtual Environment  
python -m venv .venv  
source .venv/Scripts/activate

4. Install Dependencies  
pip install -r requirements.txt

5. Add Environment Variables  
Create .env file:  
GOOGLE_API_KEY=YOUR_KEY_HERE

6. Run Application  
python main.py

# Value & Impact  
Metric:  Improvement  
Time Saved:	~70% reduction vs manual planning  
Accuracy & Focus:	Personalized topic-wise mastery tracking  
Efficiency:	Automated evaluation eliminates guesswork  
Learning Outcome:	Higher retention via spacing, resources, quizzes

# Future Enhancements

- Streamlit UI
- Voice-based assistant mode
- Daily learning reminders and notifications
- Adaptive difficulty quizzes
- Cloud deployment

# Conclusion

Study Guardian demonstrates how AI agents can build a complete autonomous learning companion capable of planning, teaching, assessing, and optimizing student preparation.
