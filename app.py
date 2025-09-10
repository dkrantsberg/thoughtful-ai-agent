# app.py
import os, json, difflib, gradio as gr

def load_knowledge_base():
    """Load knowledge base from JSON file"""
    with open('knowledge_base.json', 'r', encoding='utf-8') as f:
        kb_data = json.load(f)
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
    try:
        import requests
        payload = {
            "model": "tinyllama",
            "prompt": query,
            "stream": False
        }
        r = requests.post("https://mlvoca.com/api/generate", json=payload, timeout=20)
        r.raise_for_status()
        data = r.json()
        text = data.get("response") or data.get("text") or data.get("output") or ""
        if text:
            return text.strip()
        return "I couldn’t generate a response right now. Could you rephrase your question?"
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
