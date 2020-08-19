import os
from flask import Blueprint,render_template, send_from_directory, redirect
from ..functions import products, financial, plates

bp = Blueprint("bp", __name__, static_folder="static", template_folder="templates")

def init_app(app):
    app.register_blueprint(bp)

@bp.route('/favicon.ico')
def favicon(): 
    return send_from_directory(os.path.join(bp.root_path, 'static'), 'favicon.ico', mimetype='static/favicon.ico')

@bp.route("/", methods=["GET"])
@bp.route("/home", methods=["GET"])
def index():
    return "<h1>FUTURA PAGINA DE DOKA LOGADO</h1>"

@bp.route("/login", methods=["GET"])
def login():
    return render_template("index.html")

@bp.route("/product/new")
def productView():
    return render_template("formProducts.html")

@bp.route("/product/add", methods=["POST"])
def product():
    return products.new_product()

@bp.route("/product/<name_product>", methods=["GET", "PUT", "DELETE"])
def find_product(name_product):
    return products.specify_product(name_product.lower())

@bp.route("/product/add_qntd/<name_product>", methods=["PUT"])
def add_qnt_produtcs(name_product):
    return products.add_product(name_product.lower())

@bp.route("/product/withdraw_qntd/<name_product>", methods=["PUT"])
def withdraw_qnt_produtcs(name_product):
    return products.withdraw_product(name_product.lower())

@bp.route("/pdf")
def pdf():
    return products.generate_pdf_products()

@bp.route("/financial/new", methods=["POST"])
def new_financial():
    return financial.new()

@bp.route("/plate", methods=["POST", 'GET'])
def plate():
    return plates.managePlate()

@bp.route("/plate/<name_plate>", methods=["GET", "PUT", "DELETE"])
def find_plate(name_plate):
    return plates.specify_plate(name_plate.lower())
