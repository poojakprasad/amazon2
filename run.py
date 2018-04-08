from flask import Flask, send_from_directory, request, Response

app = Flask('mini-amazon', static_url_path='')

prod_list = []

@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET' :
        for products in prod_list :
            if products['name'] == request.args['name'] :
                return  Response(str(products), 200)
        return Response(str({}), 200)

    elif request.method == 'POST' :

        product = dict()
        product['name'] = request.form['name']
        product['description'] = request.form['description']
        product['price'] = request.form['price']


        print(product)

        prod_list.append(product)

        return Response('OK', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
