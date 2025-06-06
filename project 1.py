from flask import Flask, request, jsonify
import projectops

app = Flask(__name__)

@app.route('/investor', methods = ['GET'])
def investor_list_route():
    print("GET /investor called")  # Add this line
    return projectops.investor_list()

@app.route('/investor/<int:investor_id>', methods = ['GET'])
def investor_search_route(investor_id):
    return projectops.investor_search(investor_id)

@app.route('/investor', methods = ['POST'])
def add_investor_route():
    return projectops.add_investor()

@app.route('/investor', methods = ['PUT'])
def update_inestor_route():
    return projectops.update_investor()

@app.route('/investor', methods = ['DELETE'])
def delete_investor_route():
    return projectops.delete_investor()

@app.route('/investor', methods=['PUT'])
def update_investor():
    data = request.json  
    print('Received data:', data)
    
    return jsonify({'message': 'Investor updated successfully'})





@app.route('/stock', methods = ['POST'])
def add_stock_route():
    return projectops.add_stock()

@app.route('/stock', methods = ['PUT'])
def update_stock_route():
    return projectops.update_stock()

@app.route('/stock', methods = ['DELETE'])
def delete_stock_route():
    return projectops.delete_stock()




@app.route('/bond', methods = ['POST'])
def add_bond_route():
    return projectops.add_bond()

@app.route('/bond', methods = ['PUT'])
def update_bond_route():
    return projectops.update_bond()

@app.route('/bond', methods = ['DELETE'])
def delete_bond_route():
    return projectops.delete_bond()




@app.route('/investor/<int:investor_id>/portfolio', methods=['GET'])
def investor_portfolio_route(investor_id):
    return projectops.investor_portfolio(investor_id)

@app.route('/investor/transaction', methods=['POST'])
def make_transaction_route():
    return projectops.transaction()

@app.route('/transaction/cancel', methods=['DELETE'])
def cancel_transaction_route():
    return projectops.cancel_transaction()


if __name__ == '__main__':
    app.run(debug=True)