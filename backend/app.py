from flask import Flask, request, jsonify
import pdfplumber
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are a legal contract analysis AI.

Return ONLY valid JSON in this format:

{
  "parties": "",
  "contract_duration": "",
  "payment_terms": "",
  "termination_clauses": "",
  "renewal_terms": "",
  "confidentiality": "",
  "liability_clauses": "",
  "risk_flags": {
      "auto_renewal_trap": "",
      "liability_risk": "",
      "missing_exit_clause": ""
  },
  "plain_english_summary": ""
}
"""

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@app.route("/analyze", methods=["POST"])
def analyze():
    contract_text = None

    # If file uploaded
    if "file" in request.files:
        file = request.files["file"]
        contract_text = extract_text_from_pdf(file)

    # If JSON text provided
    elif request.is_json:
        data = request.get_json()
        contract_text = data.get("text")

    if not contract_text:
        return jsonify({"error": "No contract text provided"}), 400

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": contract_text}
            ],
            temperature=0
        )

        result = completion.choices[0].message.content.strip()

        # Clean markdown blocks
        result = result.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(result)

        return jsonify(parsed)

    except Exception as e:
        return jsonify({
            "error": "Backend processing failed",
            "details": str(e)
        }), 500
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)