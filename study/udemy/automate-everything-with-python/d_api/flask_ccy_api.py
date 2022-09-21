from flask import Flask, jsonify

from a_browser_automation.scraper_bs4 import main as scraper_bs4

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return "<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>"


@app.route("/api/v1/<in_ccy>-<out_ccy>")
def ccy_conversion(in_ccy: str, out_ccy: str) -> str:
    if rate := scraper_bs4(in_ccy, out_ccy):
        return jsonify(
            {
                "input_currency": in_ccy,
                "output_currency": out_ccy,
                "rate": rate,
            }
        )


if __name__ == "__main__":
    app.run()
