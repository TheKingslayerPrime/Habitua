from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey

from datetime import datetime, timezone

from . import db, bcrypt, login


@login.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    coins: Mapped[int] = mapped_column(nullable=False, default=0)

    mood: Mapped[str] = mapped_column(nullable=False, default="very_happy")

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Habit(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    title: Mapped[str] = mapped_column(nullable=False, default="Title")

    is_positive: Mapped[bool] = mapped_column(nullable=False, default=True)
    is_countable: Mapped[bool] = mapped_column(nullable=False, default=False)

    value: Mapped[int] = mapped_column(nullable=False, default=0)
    highlight: Mapped[str] = mapped_column(nullable=True)


class Highlight(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    habit_id: Mapped[int] = mapped_column(ForeignKey("habit.id"))

    text: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime] = mapped_column(
            nullable=False,
            default=lambda: datetime.now(timezone.utc))
