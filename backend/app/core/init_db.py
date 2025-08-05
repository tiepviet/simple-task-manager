from sqlalchemy.orm import Session
from app.core.database import engine
from app.models import User, Task
from app.core.security import get_password_hash

def init_db(db: Session) -> None:
    # Create tables
    User.metadata.create_all(bind=engine)
    Task.metadata.create_all(bind=engine)
    
    # Create admin user if it doesn't exist
    admin_user = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin_user:
        admin_user = User(
            username="admin",
            email="admin@example.com",
            password=get_password_hash("admin123"),
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        print("Admin user created: admin@example.com / admin123")
    
    # Create sample user if it doesn't exist
    sample_user = db.query(User).filter(User.email == "user@example.com").first()
    if not sample_user:
        sample_user = User(
            username="user",
            email="user@example.com",
            password=get_password_hash("user123"),
            is_admin=False
        )
        db.add(sample_user)
        db.commit()
        print("Sample user created: user@example.com / user123") 