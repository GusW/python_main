from flask import Flask, render_template, request

from i_web_and_desktop_apps.constants import INDEX_HTML_NAME


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(INDEX_HTML_NAME)


@app.route("/", methods=["POST"])
def home_post():
    form_input = request.form
    dim_1 = float(form_input.get("first_dim") or 0)
    dim_2 = float(form_input.get("second_dim") or 0)
    dim_3 = float(form_input.get("third_dim") or 0)
    return render_template(
        INDEX_HTML_NAME,
        dim_1=dim_1,
        dim_2=dim_2,
        dim_3=dim_3,
        volume=(dim_1 * dim_2 * dim_3),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
