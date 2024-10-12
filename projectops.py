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
    
