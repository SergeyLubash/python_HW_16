from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)