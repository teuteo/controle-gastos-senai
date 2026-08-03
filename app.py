from flask import Flask, render_template, request, redirect
from dados import dados

app = Flask(__name__)


# ===========================
# HOME
# ===========================

@app.route("/")
def home():
    return render_template("index.html")


# ===========================
# MINHA RENDA
# ===========================

@app.route("/renda", methods=["GET", "POST"])
def renda():

    if request.method == "POST":

        valor = request.form["renda"]

        if valor != "":
            dados["renda"] = float(valor)

        return redirect("/resumo")

    return render_template("renda.html")


# ===========================
# ADICIONAR GASTO
# ===========================

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():

    if request.method == "POST":

        descricao = request.form["descricao"]
        categoria = request.form["categoria"]
        valor = float(request.form["valor"])

        dados["gastos"].append({
            "descricao": descricao,
            "categoria": categoria,
            "valor": valor
        })

        return redirect("/resumo")

    return render_template("adicionar.html")


# ===========================
# RESUMO
# ===========================

@app.route("/resumo")
def resumo():

    renda = dados["renda"]

    total_gastos = sum(
        gasto["valor"]
        for gasto in dados["gastos"]
    )

    saldo = renda - total_gastos

    return render_template(
        "resumo.html",
        renda=renda,
        total=total_gastos,
        saldo=saldo,
        gastos=dados["gastos"]
    )


# ===========================

if __name__ == "__main__":
    app.run(debug=True)