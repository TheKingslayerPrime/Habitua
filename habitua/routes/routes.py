from . import bp

@bp.route('/')
def index():
    return "Hello, world!"

