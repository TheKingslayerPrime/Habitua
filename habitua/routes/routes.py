from flask import render_template, request

from . import bp
from .. import htmx, db
from ..models import User, Habit
from ..kitten import mood, food, toys

@bp.route('/')
def index():
    user = User.query.first()
    habits = Habit.query.filter_by(user_id=user.id).all()
    return render_template("index.html",
                           user=user,
                           habits=habits,
                           kitten=mood,
                           food=food,
                           toys=toys)


@bp.route('/create_habit', methods=['POST'])
def create_habit():
    print(request.form)

    if not htmx:
        return "Forbidden", 403

    user = User.query.first()

    habit = Habit()
    habit.user_id = user.id
    habit.title = request.form.get('title', "Title")
    
    habit_type = request.form.get('type', '1')
    match habit_type:
        case '1':
            habit.is_positive = True
            habit.is_countable = False
        case '2':
            habit.is_positive = False
            habit.is_countable = False
        case '3':
            habit.is_positive = True
            habit.is_countable = True
        case '4':
            habit.is_positive = False
            habit.is_countable = True

    db.session.add(habit)
    db.session.commit()

    habits = Habit.query.all()

    return render_template('part/habits.html', habits=habits)

