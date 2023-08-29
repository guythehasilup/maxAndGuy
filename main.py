# Import Firebase REST API library
import firebase

# Firebase configuration
config = {
  "apiKey": "AIzaSyCWs9GVtgZsBwMYv5c6ij334SLcnSBaV3o",
  "authDomain": "communityconnect1234.firebaseapp.com",
  "databaseURL": "https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "communityconnect1234",
  "storageBucket": "communityconnect1234.appspot.com",
  "messagingSenderId": "991104782337",
  "appId": "1:991104782337:web:a6b1aa1adf3a91b6cbf000"
}

# Instantiates a Firebase app
app = firebase.initialize_app(config)

#
# # Firebase Authentication
auth = app.auth()
#
# # Create new user and sign in
# auth.create_user_with_email_and_password("1@gmail.com", "123456")
user = auth.sign_in_with_email_and_password("1@gmail.com", "123456")
#
#
# # Firebase Realtime Database
db = app.database()
#
# # Data to save in database
data = {
   "name": "Robert Downey Jr.",
   "email": user.get('email')
}

# Store data to Firebase Database
db.child("users").push(data, '0')

