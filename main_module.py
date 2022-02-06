from server import create_app
app = create_app()
if __name__ == '__main__':
    print('11111')
    app.run(debug=True) #,use_reloader = False