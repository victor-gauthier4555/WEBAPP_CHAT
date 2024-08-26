from app import Message, User

# Récupérer tous les messages
messages = Message.query.all()
users = User.query.all()

print("Messages : ")

# Afficher les messages
for message in messages:
    print(f"User ID: {message.user_id}, Channel: {message.channel}, Text: {message.text}, Image: {message.image_file}")


print("Utilisateurs : ")

# Afficher les utilisateurs
for user in users:
    print(f"User ID: {user.id}, Username: {user.username}, Password: {user.password}")
