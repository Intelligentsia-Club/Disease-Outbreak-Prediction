from app import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = 'karthik@115'  # Set a secure secret key for session handling
    app.run(debug=True)
