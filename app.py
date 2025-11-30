from flask import Flask, render_template, request, redirect
import urllib.parse
from datetime import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

# Data for the template (easy to edit)
PROFILE = {
    "name": "Mayank Teli",
    "title": "Machine Learning Engineer — Samsung R&D, Bangalore",
    "email": "mayankteli7@gmail.com",
    "phone": "+91 80000 73439",
    "location": "Bangalore, India",
    "intro": "Machine Learning Engineer at Samsung R&D, Bangalore. Currently building multimodal RAG systems with Gemini live. I design, train, and deploy ML systems end-to-end.",
    "experience_years": "2+ years",
    "specialty": "Multimodal ML",
}

SKILLS = ["PyTorch", "NumPy", "TensorFlow", "Python", "Java", "Docker", "Git", "SQL","Linux","GenAI","Flask","FastAPI","Hugging Face","LangChain","Vector Databases","MLOps"]

PROJECTS = [
    {
        "title": "CLIP from Scratch",
        "desc": "Implemented Contrastive Language–Image Pretraining (CLIP) from scratch: dataset pipeline, dual-encoder models, contrastive loss, and evaluation. Explored image-text embeddings and retrieval experiments.",
        "stack": "PyTorch, Hugging Face datasets, FAISS",
    },
    {
        "title": "YouTube RAG",
        "desc": "Built a Retrieval-Augmented Generation system that ingests YouTube transcripts & captions, indexes vector embeddings, and answers questions grounded on video content.",
        "stack": "Vector DB, LLMs, embedding services",
    },
]

EDUCATION = {"degree": "B.Tech — NIT Trichy", "detail": "Completed undergraduate studies in engineering."}

CERTIFICATIONS = [
{"title": " Supervised Machine Learning: Regression and Classification", "image": "Coursera 5SDAUUX7EPTA.png"},
{"title": "Linear Algebra for Machine Learning and Data Science", "image": "Coursera CX6Q2TCJQ6ZB.png"},

{"title":"Transformer Models and BERT Models", "image": "Coursera FQYQVE8KDS9J.png"},
{"title": "Introduction to Applied Machine Learning", "image": "Coursera GLRUNX14YEFP.png"},
{"title": "Advanced Learning Algorithms", "image": "Coursera LGLO1W4GA0OW.png"},
]


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        education=EDUCATION,
        certifications=CERTIFICATIONS,
        year=datetime.now().year
    )



@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    message = request.form.get("message", "")
    subject = f"Portfolio contact from {name or 'Visitor'}"
    # URL-encode simple fields
    body = urllib.parse.quote(message)
    mailto = f"mailto:{PROFILE['email']}?subject={urllib.parse.quote(subject)}&body={body}"
    return redirect(mailto)


if __name__ == "__main__":
    # For development only. In production use gunicorn or other WSGI server.
    app.run(debug=True)
