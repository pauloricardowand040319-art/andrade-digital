from flask import Flask, render_template

app = Flask(_name_)

WHATSAPP_NUMBER = "5577981263624"

PROJECTS = [
    {
        "title": "Seu Chico Tandy",
        "category": "Cavalos 3D",
        "description": "Arte digital em 3D.",
        "image": "imagem/SEU CHICO TANDY 1.jpg"
    },
    {
        "title": "Seu Chico Tandy - Detalhes",
        "category": "Cavalos 3D",
        "description": "Uma segunda perspectiva do projeto 3D.",
        "image": "imagem/SEU CHICO TANDY 2.jpg"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=PROJECTS,
        whatsapp_number=WHATSAPP_NUMBER
    )

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)