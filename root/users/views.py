from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash
from root.crawler import grade_stock, stock_info
from root.users.models import User

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """Registers the user with username and password hash in database"""
    logout_user()
    if request.method == "GET":
        return render_template("users/register.html")

    username = request.form.get("username")
    password = request.form.get("password")

    result = User.objects(username=username).first()
    print(result, username, password)
    # check the username is available and put the data in MongoDB
    if result != None:
        flash("The username has been registered!")
        return render_template("users/register.html")
        # return redirect("/error?msg=Sorry, this username has been registered.")
    password_hash = generate_password_hash(password)
    user = User(
        username=username,
        password_hash=password_hash,
    )
    user.save()
    flash("Thanks for registering!")
    login_user(user)
    flash(f"Welcome {user.username}!")
    return redirect(url_for("users.stock"))


@users.route("/login", methods=["GET", "POST"])
def login():
    """Logs the user in through username/password"""
    logout_user()
    if request.method == 'GET':
        return render_template("users/login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    result = User.objects(username=username).first()

    print(result, username, password)
    # check the username is available and put the data in MongoDB
    if result != None and result.check_password(password):
        user = result
        login_user(user)
        flash(f"Welcome {user.username}!")
        return redirect(url_for("users.stock"))
    flash("Invalid Username and/or Password. Please try again.")
    return render_template("users/login.html")


@users.route("/stock", methods=["GET", "POST"])
@login_required
def stock():
    '''Change the URL and render users/stock.html'''
    return render_template("users/stock.html")


@users.route("/crawler", methods=["POST"])
@login_required
def crawler():
    '''Call crawler to search the stock'''
    stock_no = request.form.get("stock_number")
    year = request.form.get("year")
    quarter = request.form.get("quarter")
    date = year+quarter
    # current_user表 現在login的user object

    stock_data = grade_stock.stock_grade(stock_no, date)
    if stock_data["grade"] != None:
        current_user.add_stock(stock_data)
        current_user.save()
    else:
        flash(f'Sorry,the data center refuted your request because you may crawl too frequently or the data you search is not available. Try another one or use the "Input Test Cases" below.')
    return redirect(url_for("users.stock"))


@users.route("/delete", methods=["POST"])
@login_required
def delete():
    '''Delete stock in user's stock list'''
    stock_no = request.args.get("stock_no", None)
    stock_quarter = request.args.get("stock_quarter", None)

    for index, stock in enumerate(current_user.stocks):
        no = stock.get("no")
        date = stock.get("date")
        if no == stock_no and date == stock_quarter:
            current_user.delete_stock(index)
            break
    current_user.save()
    return redirect(url_for("users.stock"))


@users.route("/test_case", methods=["POST"])
@login_required
def test_case():
    '''Input the test cases'''
    stock_cases = stock_info.test_case()
    for case in stock_cases:
        current_user.add_stock(case)
    current_user.save()
    return redirect(url_for("users.stock"))


@users.route("/sort", methods=["POST"])
@login_required
def sort_stock():
    '''Sort stocks by grade'''

    new = sorted(current_user.stocks, key=lambda stock: stock['grade'])
    print(new)
    current_user.stocks = new
    current_user.save()
    return redirect(url_for("users.stock"))


@users.route("/logout")
@login_required
def logout():
    """Log out the current user"""
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("users.login"))


# ----------------------------------------------------------------------------
# HELPER METHODS
# ----------------------------------------------------------------------------
