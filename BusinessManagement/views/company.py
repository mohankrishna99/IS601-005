from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    ## UCID: mk994 Date: Dec 03
    ## Select query to get company data for search
    query = "SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website FROM IS601_MP2_Companies c WHERE 1=1"
    print(query)
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    ## UCID: mk994 Date: Dec 03
    ## retieving the arguments
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    ##UCID: mk994 Date: Dec 03
    ## appending the respective arguments and flash message for limit
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND c.name like %s"
        args.append(f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND c.country like %s"
        args.append(f"%{country}%")
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND c.state like %s"
        args.append(f"%{state}%")
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        #print(result)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        ## UCID: mk994 Date: Dec 03
        print(e)
        flash("Error occured, please check the data and try again", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        ## UCID: mk994 Date: Dec 03 retrieving the form data
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        zip = request.form.get("zip")
        website = request.form.get("website")
        country = request.form.get("country")
        state = request.form.get("state")
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-6 country is required (flash proper error message)
        # TODO add-7 website is not required
        ## UCID; mk994 Date: Dec 03 flash error messages for required fields
        if name == "":
            flash("Enter company name", 'warning')
            return redirect(request.url)
        if address == "":
            flash("Enter Address", 'warning')
            return redirect(request.url)
        if city == "":
            flash("Enter city", 'warning')
            return redirect(request.url)
        if state == "":
            flash("Enter state", 'warning')
            return redirect(request.url)
        if country == "":
            flash("Enter country", 'warning')
            return redirect(request.url)
        
        has_error = False # use this to control whether or not an insert occurs
        

        if not has_error:
            try:
                ## UCID: mk994 Date: Dedc 03
                ## Insert query to add a company
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
                """, {'name':name, 'address':address, 'city':city, 'country':country, 'state':state, 'zip':zip, 'website':website}) 
                # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                ## UCID: mk994 Date: Dedc 03
                ## flash message
                print(e)
                flash("Error adding the data, check again" + str(e), "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    if True: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = request.args.get('name')
            address = request.args.get('address')
            city = request.args.get('city')
            state = request.args.get('state')
            country = request.args.get('country')
            zipcode = request.args.get('zip')
            website = request.args.get('website')
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-8 website is not required
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            try:
                # TODO edit-9 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s
                WHERE id = %s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash(str(e), "danger")
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    ## UCID: mk994 Date: Dec 04
    ## code for deleting company
    id = request.args.get('id')
    args = {**request.args}
    # TODO delete-1 delete company by id (unallocate any employees)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    if id:
        DB.update("""UPDATE IS601_MP2_Employees SET company_id = %s where company_id = %s""", None, id)
        result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
        del args['id']
        if result:
            flash("Deleted successfully")
    return redirect(url_for("company.search", **args))
    pass