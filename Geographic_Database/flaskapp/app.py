from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('main-menu.html')

@app.route('/continents')
def continents():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Continent")
    if resultValue > 0:
        dataDetails = cur.fetchall()
        return render_template('continents.html', dataDetails = dataDetails)

@app.route('/add-continent', methods = ['GET', 'POST'])
def addContinent():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        population = dataDetails['population']
        area = dataDetails['area']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Continent(name, population, area) VALUES(%s, %s, %s)", (name, population, area))
        mysql.connection.commit()
        cur.close()
        return redirect('/continents')
    return render_template('add-continent.html')

@app.route('/edit-continent', methods = ['GET', 'POST'])
def editContinent():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        field = dataDetails['field']
        value = dataDetails['value']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Continent SET " + field + " = %s WHERE Name = %s;", (value, name))
        mysql.connection.commit()
        cur.close()
        return redirect('/continents')
    return render_template('edit-continent.html')

@app.route('/delete-continent', methods = ['GET', 'POST'])
def deleteContinent():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Continent WHERE Name = %s", [name])
        mysql.connection.commit()
        cur.close()
        return redirect('/continents')
    return render_template('delete-continent.html')
    
@app.route('/countries')
def countries():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Country")
    if resultValue > 0:
        dataDetails = cur.fetchall()
        return render_template('countries.html', dataDetails = dataDetails)

@app.route('/add-country', methods = ['GET', 'POST'])
def addCountry():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        population = dataDetails['population']
        area = dataDetails['area']
        yearOfEstablishment = dataDetails['yearOfEstablishment']
        continent = dataDetails['continent']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Country(name, population, area, yearOfEstablishment, continent) VALUES(%s, %s, %s %s %s)", (name, population, area, yearOfEstablishment, continent))
        mysql.connection.commit()
        cur.close()
        return redirect('/countries')
    return render_template('add-country.html')

@app.route('/edit-country', methods = ['GET', 'POST'])
def editCountry():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        field = dataDetails['field']
        value = dataDetails['value']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Country SET " + field + " = %s WHERE Name = %s;", (value, name))
        mysql.connection.commit()
        cur.close()
        return redirect('/countries')
    return render_template('edit-country.html')

@app.route('/delete-country', methods = ['GET', 'POST'])
def deleteCountry():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Country WHERE Name = %s", [name])
        mysql.connection.commit()
        cur.close()
        return redirect('/countries')
    return render_template('delete-country.html')

@app.route('/cities')
def cities():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM City")
    if resultValue > 0:
        dataDetails = cur.fetchall()
        return render_template('cities.html', dataDetails = dataDetails)

@app.route('/add-city', methods = ['GET', 'POST'])
def addCity():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        population = dataDetails['population']
        area = dataDetails['area']
        capitalCity = dataDetails['capitalCity']
        mostPopulousCity = dataDetails['mostPopulousCity']
        country = dataDetails['country']
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO City(name, population, area, capitalCity, mostPopulousCity, country) VALUES(%s, %s, %s, %s, %s, %s)", (name, population, area, capitalCity, mostPopulousCity, country))
        except: pass
        mysql.connection.commit()
        cur.close()
        return redirect('/cities')
    return render_template('add-city.html')

@app.route('/edit-city', methods = ['GET', 'POST'])
def editCity():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        field = dataDetails['field']
        value = dataDetails['value']
        cur = mysql.connection.cursor()
        try:    
            cur.execute("UPDATE City SET " + field + " = %s WHERE Name = %s;", (value, name))
        except: pass
        mysql.connection.commit()
        cur.close()
        return redirect('/cities')
    return render_template('edit-city.html')

@app.route('/delete-city', methods = ['GET', 'POST'])
def deleteCity():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM City WHERE Name = %s", [name])
        mysql.connection.commit()
        cur.close()
        return redirect('/cities')
    return render_template('delete-city.html')

@app.route('/currencies')
def currencies():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Currency")
    if resultValue > 0:
        dataDetails = cur.fetchall()
        return render_template('currencies.html', dataDetails = dataDetails)

@app.route('/add-currency', methods = ['GET', 'POST'])
def addCurrency():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        code = dataDetails['code']
        name = dataDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Currency(code, name) VALUES(%s, %s)", (code, name))
        mysql.connection.commit()
        cur.close()
        return redirect('/currencies')
    return render_template('add-currency.html')

@app.route('/edit-currency', methods = ['GET', 'POST'])
def editCurrency():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        code = dataDetails['code']
        field = dataDetails['field']
        value = dataDetails['value']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Currency SET " + field + " = %s WHERE Code = %s;", (value, code))
        mysql.connection.commit()
        cur.close()
        return redirect('/currencies')
    return render_template('edit-currency.html')

@app.route('/delete-currency', methods = ['GET', 'POST'])
def deleteCurrency():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        code = dataDetails['code']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Currency WHERE Code = %s", [code])
        mysql.connection.commit()
        cur.close()
        return redirect('/currencies')
    return render_template('delete-currency.html')

@app.route('/languages')
def languages():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Language")
    if resultValue > 0:
        dataDetails = cur.fetchall()
        return render_template('languages.html', dataDetails = dataDetails)

@app.route('/add-language', methods = ['GET', 'POST'])
def addLanguage():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        code = dataDetails['code']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Language(name, code) VALUES(%s, %s)", (name, code))
        mysql.connection.commit()
        cur.close()
        return redirect('/languages')
    return render_template('add-language.html')

@app.route('/edit-language', methods = ['GET', 'POST'])
def editLanguage():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        field = dataDetails['field']
        value = dataDetails['value']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Language SET " + field + " = %s WHERE Name = %s;", (value, name))
        mysql.connection.commit()
        cur.close()
        return redirect('/languages')
    return render_template('edit-language.html')

@app.route('/delete-language', methods = ['GET', 'POST'])
def deleteLanguage():
    if request.method == 'POST':
    # Fetch form data
        dataDetails = request.form
        name = dataDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Language WHERE Name = %s", [name])
        mysql.connection.commit()
        cur.close()
        return redirect('/languages')
    return render_template('delete-language.html')

if __name__ == '__main__':
    app.run(debug=True)