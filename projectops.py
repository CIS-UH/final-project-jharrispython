import mysql.connector
from flask import jsonify, request
from config import cred

def create_conn():

    return mysql.connector.connect(**cred)

def investor_list():

     with create_conn() as conn:

            with conn.cursor(dictionary = True) as cursor:

                cursor.execute("SELECT * FROM investor")
                investor = cursor.fetchall()

                if not investor:

                    return jsonify({'message': 'No items were found'})

                return jsonify(investor)

def investor_search(investor_id):
    with create_conn() as conn:

            with conn.cursor(dictionary = True) as cursor:
                
                cursor.execute("SELECT * FROM investor WHERE id = %s", (investor_id,))
                investor = cursor.fetchone()
                
                if not investor:

                    return jsonify({'message': 'Investor not found'}), 404


                return jsonify(investor)
    

def add_investor():
    data = request.json

    invest_id = data.get('id')
    first_name = data.get('firstname', 'None')
    last_name = data.get('lastname', 'None')

    if not invest_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    INSERT INTO investor (id, firstname, lastname)
                    VALUES (%s, %s, %s)
                """

                cursor.execute(query, (invest_id, first_name, last_name))
                conn.commit()

            return jsonify({'message': 'Investor created successfully.', 'id': invest_id})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})


def update_investor():

    data = request.json

    invest_id = data.get('id')
    first_name = data.get('firstname', 'None')
    last_name = data.get('lastname', 'None')


    if not invest_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    UPDATE investor SET firstname = %s, lastname = %s
                    WHERE id = %s 
                """

                cursor.execute(query, (first_name, last_name, invest_id))
                conn.commit()

                if cursor.rowcount > 0:
                    return jsonify({'message': 'Investor updated successfully.'})
                
                else:
                    return jsonify({'message': 'No investor found.'})
                


    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})


def delete_investor():
     
    data = request.json

    invest_id = data.get('id')

    if not invest_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = "DELETE FROM investor WHERE id = %s"

                cursor.execute(query, (invest_id, ))
                conn.commit()      

            if cursor.rowcount == 0:

                return jsonify({'message': 'No investor found'})

            return jsonify({'message': 'Investor removed successfully'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})
    




def add_stock():

    data = request.json

    stock_id = data.get('id')
    stock_name = data.get('stockname', 'None')
    stock_abb = data.get('abbreviation', 'None')
    stock_price = data.get('currentprice', 'None')

    if not stock_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    INSERT INTO stock (id, stockname, abbreviation, currentprice)
                    VALUES (%s, %s, %s, %s)
                """

                cursor.execute(query, (stock_id, stock_name, stock_abb, stock_price))
                conn.commit()

            return jsonify({'message': 'Stock created successfully.', 'id': stock_id})
    
    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})

def update_stock():

    data = request.json

    stock_id = data.get('id')
    stock_name = data.get('stockname', 'None')
    stock_abb = data.get('abbreviation', 'None')
    stock_price = data.get('currentprice', 'None')


    if not stock_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    UPDATE stock SET stockname = %s, abbreviation = %s, currentprice = %s
                    WHERE id = %s 
                """

                cursor.execute(query, (stock_name, stock_abb, stock_price, stock_id))
                conn.commit()

                if cursor.rowcount > 0:
                    return jsonify({'message': 'Stock updated successfully.'})
                
                else:
                    return jsonify({'message': 'No stock found.'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})

def delete_stock():
     
    data = request.json

    stock_id = data.get('id')

    if not stock_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = "DELETE FROM stock WHERE id = %s"

                cursor.execute(query, (stock_id, ))
                conn.commit()      

            if cursor.rowcount == 0:

                return jsonify({'message': 'No stock found'})

            return jsonify({'message': 'Stock removed successfully'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})
    




def add_bond():

    data = request.json

    bond_id = data.get('id')
    bond_name = data.get('bondname', 'None')
    bond_abb = data.get('abbreviation', 'None')
    bond_price = data.get('currentprice', 'None')

    if not bond_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    INSERT INTO bond (id, bondname, abbreviation, currentprice)
                    VALUES (%s, %s, %s, %s)
                """

                cursor.execute(query, (bond_id, bond_name, bond_abb, bond_price))
                conn.commit()

            return jsonify({'message': 'Bond created successfully.', 'id': bond_id})
    
    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})

def update_bond():

    data = request.json

    bond_id = data.get('id')
    bond_name = data.get('bondname', 'None')
    bond_abb = data.get('abbreviation', 'None')
    bond_price = data.get('currentprice', 'None')


    if not bond_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = """
                    UPDATE bond SET bondname = %s, abbreviation = %s, currentprice = %s
                    WHERE id = %s 
                """

                cursor.execute(query, (bond_name, bond_abb, bond_price, bond_id))
                conn.commit()

                if cursor.rowcount > 0:
                    return jsonify({'message': 'Bond updated successfully.'})
                
                else:
                    return jsonify({'message': 'No bond found.'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})

def delete_bond():
     
    data = request.json

    bond_id = data.get('id')

    if not bond_id:
        return jsonify({'error': 'id is required.'}), 400

    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                query = "DELETE FROM bond WHERE id = %s"

                cursor.execute(query, (bond_id, ))
                conn.commit()      

            if cursor.rowcount == 0:

                return jsonify({'message': 'No bond found'})

            return jsonify({'message': 'Bond removed successfully'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})
    


def investor_portfolio(investor_id):

    with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                stock_query = """
                            SELECT s.id AS stock_id, s.stockname AS stock_name, s.abbreviation, s.currentprice, 
                            st.quantity, st.date
                            FROM stocktransaction st
                            JOIN stock s ON st.stockid = s.id
                            WHERE st.investorid = %s
                            """
                cursor.execute(stock_query, (investor_id,))
                stocks = cursor.fetchall()

                bond_query = """
                            SELECT b.id AS bond_id, b.bondname AS bond_name, 
                            b.abbreviation, b.currentprice,
                            bt.quantity, bt.date
                            FROM bondtransaction bt
                            JOIN bond b ON bt.bondid = b.id
                            WHERE bt.investorid = %s
                            """
                cursor.execute(bond_query, (investor_id,))
                bonds = cursor.fetchall()

                if not stocks and not bonds:
                    return jsonify({'message': 'No portfolio found for this investor.'}), 404
                
                portfolio = {
                'stocks': stocks,
                'bonds': bonds
                }

                return jsonify(portfolio)

def transaction():

    data = request.json

    investor_id = data.get('investor_id')
    asset_type = data.get('asset_type')
    asset_id = data.get('asset_id')
    quantity = data.get('quantity')
    transaction_type = data.get('transaction_type')

    if not all([investor_id, asset_type, asset_id, quantity, transaction_type]):
        return jsonify({'error': 'All fields are required.'}), 400
    
    if transaction_type == 'sell':
        quantity = -abs(quantity)
    elif transaction_type == 'buy':
        quantity = abs(quantity)
    else:
        return jsonify({'error': 'transaction type must be either "buy" or "sell".'}), 400
    
    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:
                if asset_type == 'stock':
                    
                    query = """
                            INSERT INTO stocktransaction (investorid, stockid, quantity, date)
                            VALUES (%s, %s, %s, NOW())
                        """
                    cursor.execute(query, (investor_id, asset_id, quantity))

                elif asset_type == 'bond':
                    
                    query = """
                            INSERT INTO bondtransaction (investorid, bondid, quantity, date)
                            VALUES (%s, %s, %s, NOW())
                            """
                    cursor.execute(query, (investor_id, asset_id, quantity))

                else:
                    return jsonify({'error': 'asset must be either "stock" or "bond".'}), 400

                conn.commit()
                return jsonify({'message': f'Transaction successful for {transaction_type} of {asset_type}.'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})

def cancel_transaction():

    data = request.json

    transaction_type = data.get('transaction_type')
    transaction_id = data.get('transaction_id')

    if not all([transaction_type, transaction_id]):
        return jsonify({'error': 'Both type and id are required.'}), 400
    
    try:
        with create_conn() as conn:

            with conn.cursor(dictionary=True) as cursor:

                if transaction_type == 'stock':

                    query = "DELETE FROM stocktransaction WHERE id = %s"
                elif transaction_type == 'bond':

                    query = "DELETE FROM bondtransaction WHERE id = %s"

                else:
                    return jsonify({'error': 'transaction must be either "stock" or "bond".'}), 400

                cursor.execute(query, (transaction_id,))
                conn.commit()

                if cursor.rowcount == 0:
                    return jsonify({'message': 'No transaction found.'}), 404

                return jsonify({'message': f'{transaction_type} transaction canceled successfully.'})

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error: {str(e)}'})