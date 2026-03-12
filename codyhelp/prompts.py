#Prompts that are used to run each feature giving accurate responses to the user

def explain_prompt(code):
    return f"Explain what this code does in simple terms:\n\n{code}"

def interview_prompt(code):
    return f"Explain this code as if I need to defend it in a job interview. Include: how to explain it verbally, time/space complexity, likely follow-up questions, and key concepts to know.\n\n{code}"

def review_prompt(code):
    return f"Review this code and detect possible bugs. For each bug found, label it with a severity level: [HIGH], [MEDIUM], or [LOW]. Then suggest improvements.\n\n{code}"

def stacktrace_prompt(error):
    return f"You are a helpful coding assistant, explain errors in my code in simple words in the format:\n Error:\n What went wrong:\n Suggested fix:\n Concept to review:\n\n{error}"