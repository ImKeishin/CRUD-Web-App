from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Filme")
    filme = cursor.fetchall()

    cursor.execute("SELECT * FROM Locatii")
    locatii = cursor.fetchall()

    cursor.execute("SELECT r.idrezervare, f.Nume, l.Nume, r.Pret, r.DataRezervare FROM Rezervari r "
                   "JOIN Filme f ON r.idfilm = f.idfilm "
                   "JOIN Locatii l ON r.idlocatie = l.idlocatie")
    rezervari = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('home.html', filme=filme, locatii=locatii, rezervari=rezervari)

@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    if request.method == 'POST':
        nume_film = request.form['nume_film']
        an_lansare = request.form['an_lansare']

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Filme (Nume, AnLansare) VALUES (%s, %s)", (nume_film, an_lansare))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('add_film.html')

@app.route('/edit_film', methods=['GET', 'POST'])
def edit_film():
    if request.method == 'POST':
        # Cazul 1: Utilizatorul a trimis formularul de căutare
        if 'nume_film' in request.form and not ('nume_film_edit' in request.form or 'an_lansare_edit' in request.form):
            nume_film = request.form['nume_film']

            connection = get_connection()
            cursor = connection.cursor()

            # Cautam filmul dupa numele introdus
            cursor.execute("SELECT * FROM Filme WHERE Nume = %s", (nume_film,))
            film = cursor.fetchone()

            cursor.close()
            connection.close()

            if film:
                # Filmul a fost gasit, afisam formularul pentru editare
                return render_template('edit_film.html', film=film)
            else:
                # Filmul nu a fost gasit
                return render_template('edit_film.html', error_message=f"Filmul '{nume_film}' nu a fost găsit în baza de date.", film=None)

        # Cazul 2: Utilizatorul a trimis modificarile pentru un film
        elif 'nume_film_edit' in request.form and 'an_lansare_edit' in request.form:
            nume_film_edit = request.form['nume_film_edit']
            an_lansare_edit = request.form['an_lansare_edit']
            nume_film_original = request.form.get('nume_film_original')

            connection = get_connection()
            cursor = connection.cursor()

            # Actualizam filmul in baza de date
            cursor.execute("UPDATE Filme SET Nume = %s, AnLansare = %s WHERE Nume = %s",
                           (nume_film_edit, an_lansare_edit, nume_film_original))
            connection.commit()

            cursor.close()
            connection.close()

            # Redirectionam la pagina principala dupa editare
            return redirect(url_for('home'))

        else:
            # Daca niciunul dintre cazuri nu este indeplinit, afisam o eroare generala
            return render_template('edit_film.html', error_message="Numele filmului este necesar.", film=None)

    # Daca metoda este GET, afisam formularul pentru cautarea unui film
    return render_template('edit_film.html', film=None)

@app.route('/delete_film', methods=['GET', 'POST'])
def delete_film():
    if request.method == 'POST':
        nume_film = request.form['nume_film']

        connection = get_connection()
        cursor = connection.cursor()

        # Cautam filmul in baza de date
        cursor.execute("SELECT * FROM Filme WHERE Nume = %s", (nume_film,))
        film = cursor.fetchone()

        if film:
            # Filmul a fost gasit, il stergem
            cursor.execute("DELETE FROM Filme WHERE Nume = %s", (nume_film,))
            connection.commit()
            cursor.close()
            connection.close()

            # Redirectionam catre pagina de succes
            return render_template('delete_success.html')
        
        else:
            # Filmul nu a fost gasit, returnam la pagina de stergere cu mesaj de eroare
            cursor.close()
            connection.close()
            return render_template('delete_film.html', error_message=f"Filmul '{nume_film}' nu a fost găsit în baza de date.")

    # Daca este GET, doar afisam formularul de stergere
    return render_template('delete_film.html')

@app.route('/add_location', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        nume_locatie = request.form['nume_locatie']
        adresa_locatie = request.form['adresa_locatie']

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Locatii (Nume, Adresa) VALUES (%s, %s)", (nume_locatie, adresa_locatie))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('add_location.html')

@app.route('/edit_location', methods=['GET', 'POST'])
def edit_location():
    if request.method == 'POST':
        if 'nume_locatie' in request.form and not ('nume_locatie_edit' in request.form or 'adresa_locatie_edit' in request.form):
            nume_locatie = request.form['nume_locatie']

            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Locatii WHERE Nume = %s", (nume_locatie,))
            locatie = cursor.fetchone()

            cursor.close()
            connection.close()

            if locatie:
                return render_template('edit_location.html', locatie=locatie)
            else:
                return render_template('edit_location.html', error_message=f"Locația '{nume_locatie}' nu a fost găsită în baza de date.", locatie=None)

        elif 'nume_locatie_edit' in request.form and 'adresa_locatie_edit' in request.form:
            nume_locatie_edit = request.form['nume_locatie_edit']
            adresa_locatie_edit = request.form['adresa_locatie_edit']
            nume_locatie_original = request.form.get('nume_locatie_original')

            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("UPDATE Locatii SET Nume = %s, Adresa = %s WHERE Nume = %s",
                           (nume_locatie_edit, adresa_locatie_edit, nume_locatie_original))
            connection.commit()

            cursor.close()
            connection.close()

            return redirect(url_for('home'))

    return render_template('edit_location.html', locatie=None)

@app.route('/delete_location', methods=['GET', 'POST'])
def delete_location():
    if request.method == 'POST':
        nume_locatie = request.form['nume_locatie']

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Locatii WHERE Nume = %s", (nume_locatie,))
        locatie = cursor.fetchone()

        if locatie:
            cursor.execute("DELETE FROM Locatii WHERE Nume = %s", (nume_locatie,))
            connection.commit()
            cursor.close()
            connection.close()

            return render_template('delete_success.html', message=f"Locația '{nume_locatie}' a fost ștearsă cu succes.")
        else:
            cursor.close()
            connection.close()
            return render_template('delete_location.html', error_message=f"Locația '{nume_locatie}' nu a fost găsită în baza de date.")

    return render_template('delete_location.html')

@app.route('/add_reservation', methods=['GET', 'POST'])
def add_reservation():
    if request.method == 'POST':
        idfilm = request.form['idfilm']
        idlocatie = request.form['idlocatie']
        pret = request.form['pret']
        data_rezervare = request.form['data_rezervare']

        connection = get_connection()
        cursor = connection.cursor()

        # Inseram rezervarea in baza de date
        cursor.execute("INSERT INTO Rezervari (idfilm, idlocatie, Pret, DataRezervare) VALUES (%s, %s, %s, %s)",
                       (idfilm, idlocatie, pret, data_rezervare))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    # Pentru metoda GET, populam listele derulante
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT idfilm, Nume FROM Filme")
    filme = cursor.fetchall()

    cursor.execute("SELECT idlocatie, Nume FROM Locatii")
    locatii = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('add_reservation.html', filme=filme, locatii=locatii)

@app.route('/edit_reservation', methods=['GET', 'POST'])
def edit_reservation():
    connection = get_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        nume_film = request.form['nume_film']

        # Cautam rezervarile dupa numele filmului
        cursor.execute("""
            SELECT r.idrezervare, f.Nume, l.Nume, r.Pret, r.DataRezervare
            FROM Rezervari r
            JOIN Filme f ON r.idfilm = f.idfilm
            JOIN Locatii l ON r.idlocatie = l.idlocatie
            WHERE f.Nume = %s
        """, (nume_film,))
        rezervare = cursor.fetchone()

        if rezervare:
            # Daca se doreste actualizarea rezervarii
            if 'pret_edit' in request.form and 'data_rezervare_edit' in request.form:
                pret_edit = request.form['pret_edit']
                data_rezervare_edit = request.form['data_rezervare_edit']

                # Actualizam rezervarea
                cursor.execute("""
                    UPDATE Rezervari
                    SET Pret = %s, DataRezervare = %s
                    WHERE idrezervare = %s
                """, (pret_edit, data_rezervare_edit, rezervare[0]))
                connection.commit()
                return redirect(url_for('home'))

            return render_template('edit_reservation.html', rezervare=rezervare)

        else:
            # Rezervare inexistenta
            return render_template('edit_reservation.html', error_message=f"Rezervare pentru filmul '{nume_film}' nu a fost găsită.")

    return render_template('edit_reservation.html', rezervare=None)

@app.route('/delete_reservation', methods=['GET', 'POST'])
def delete_reservation():
    connection = get_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        nume_film = request.form['nume_film']

        # Cautam rezervarile dupa numele filmului
        cursor.execute("""
            SELECT r.idrezervare, f.Nume, l.Nume, r.Pret, r.DataRezervare
            FROM Rezervari r
            JOIN Filme f ON r.idfilm = f.idfilm
            JOIN Locatii l ON r.idlocatie = l.idlocatie
            WHERE f.Nume = %s
        """, (nume_film,))
        rezervare = cursor.fetchone()

        if rezervare:
            # Stergem rezervarea
            cursor.execute("DELETE FROM Rezervari WHERE idrezervare = %s", (rezervare[0],))
            connection.commit()
            return render_template('delete_success.html')

        else:
            # Rezervare inexistenta
            return render_template('delete_reservation.html', error_message=f"Rezervare pentru filmul '{nume_film}' nu a fost găsită.")

    return render_template('delete_reservation.html')


if __name__ == '__main__':
    app.run(debug=True)