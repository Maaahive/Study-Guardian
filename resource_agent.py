from llm_client import generate_text
import logging

class ResourceAgent:
    def __init__(self, memory):
        self.memory = memory

    def find_resources(self, plan):
        logging.info("ResourceAgent: Finding resources for study plan.")
        resources = {}

        topics = [item["topic"] for item in plan]
        topics_str = ",".join(topics)

        prompt = f"""
        You are an expert educational resource AI.
        Your task is to provide REAL study resources.

        Topics: {topics_str}

        For each topic:
        -provide EXACTLY 3 high-quality study resources.
        -all links must be real access URLS(no placeholders).
        -provide a 1 sentence summary for each resource.

        STRICT OUTPUT FORMAT (do not add extra text, no introductions, no markdown, no bullet points, no multiline summaries):
        Topic: <topic_name>
        1. Title: <title> | URL: <url> | Summary: <summary>
        2. Title: <title> | URL: <url> | Summary: <summary>
        3. Title: <title> | URL: <url> | Summary: <summary>

        REPEAT for each topic.

        remember: output must be in the STRICT FORMAT above.
        """
        text = generate_text(prompt, system_instruction="Find structured study resources")
        
        logging.info("ResourceAgent: Raw result received.")

        curr_topic = None
        resources = {}

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            
            if line.lower().startswith("topic:") :
                curr_topic = line.split(":", 1)[1].strip()
                resources[curr_topic] = []

            elif line[0].isdigit() and curr_topic:
                try:
                    parts = line.split("|")
                    title_part = parts[0].split(":", 1)[1].strip()
                    url_part = parts[1].split(":", 1)[1].strip()
                    summary_part = parts[2].split(":", 1)[1].strip()
                    resources[curr_topic].append({
                        "title": title_part,
                        "url": url_part,
                        "summary": summary_part
                    })
                except:
                    continue

        return resources