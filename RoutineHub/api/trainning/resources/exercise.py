from RoutineHub.extensions import ma

class ExerciseSchema(ma.Schema):

    id = ma.Int(dump_only=True)
    title = ma.String()
    description = ma.String()
    image_url = ma.String()
    sets = ma.Int()
    reps = ma.Int()
    cadence = ma.Int()
    set_seconds = ma.Int()
    rest_seconds = ma.Int()
    min_reps_interval = ma.Int()
    max_reps_interval = ma.Int()
    user_id = ma.Int()

