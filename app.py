# app.py
import os, json, difflib, gradio as gr
from dotenv import load_dotenv

load_dotenv()

def load_knowledge_base():
    """Load knowledge base from JSON file"""
    with open('knowledge_base.json', 'r', encoding='utf-8') as f:
        kb_data = json.load(f)
    # Convert to tuple format for compatibility with existing code
    return [(item['question'], item['answer']) for item in kb_data]

KB = load_knowledge_base()

THRESHOLD = 0.55

def kb_answer(query: str):
    questions = [q for q, _ in KB]
    match = difflib.get_close_matches(query, questions, n=1, cutoff=0.0)
    if not match:
        return None, 0.0, ""
    best_q = match[0]
    score = difflib.SequenceMatcher(None, query.lower(), best_q.lower()).ratio()
    ans = dict(KB)[best_q]
    return ans, score, best_q

def llm_fallback(query: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return ("I don’t have a direct match in the knowledge base. "
                "High level: Thoughtful AI builds automation agents for healthcare workflows "
                "like eligibility verification (EVA), claims (CAM), and payment posting (PHIL). "
                "What specifics do you need (pricing, integrations, security)?")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content":
                 "You are a concise support agent for Thoughtful AI. "
                 "Prefer factual, generic guidance if KB is missing."},
                {"role": "user", "content": query}
            ]
        )
        print(r.choices[0].message.content.strip())
        return r.choices[0].message.content.strip()
    except Exception:
        return "LLM fallback is temporarily unavailable. Can you share more details?"

def respond(user_msg, history):
    ans, score, matched_q = kb_answer(user_msg)
    if ans and score >= THRESHOLD:
        return f"{ans}\n\n_**Source:** KB · **Match:** `{score:.2f}` · **Q:** {matched_q}_"
    return f"{llm_fallback(user_msg)}\n\n_**Source:** LLM fallback_"

demo = gr.ChatInterface(
    fn=respond,
    title="Thoughtful AI — Support Agent",
    description="Answers from a small KB first (fuzzy matching), then LLM fallback if needed.",
    retry_btn="Retry", clear_btn="Clear"
)

if __name__ == "__main__":
    demo.launch()
