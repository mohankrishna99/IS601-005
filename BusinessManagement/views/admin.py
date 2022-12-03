import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import re
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        if file.filename.split('.')[-1] != 'csv':
            flash('Uploaded file is not CSV file', 'error')
            return redirect(request.url)
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
             INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            for row in stream:
                # print(row) #example
                pattern = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
                row = pattern.split(row)[1::2]
                print(row)
                if row[2] == 'company_name':
                    continue
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                companies.append({'name':row[2].strip('\"'), 'address':row[3], 'city':row[4], 'country':row[5], 'state':row[7], 'zip':row[8],'website':row[12]})
                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data
                employees.append({'first_name':row[0], 'last_name':row[1],'email':row[11], 'company_name':row[2].strip('\"')})
                pass
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    print(result)
                    flash(f'{len(companies)} companies have been inserted', 'message')
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                flash("No companies are loaded")
                pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    flash(f'{len(employees)} companies have been inserted', "information")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no companies were loaded
                flash("no employees are loaded")
                pass
    return render_template("upload.html")
