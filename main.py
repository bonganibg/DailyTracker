from src.models.user_model import User

user = User(hourly_rate=53, role='Coding Mentor', division='Learning Experience')

print(user.model_dump())
