from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from RoutineHub.models.schedule import Schedule
from RoutineHub.models.workout import Workout

def get_workouts(request, current_user):
    filters = set(('start_date', 'end_date'))
    args = set(request.args.keys())
    args_intersection = args.intersection(filters)

    if 'start_date' in args_intersection and 'end_date' in args_intersection:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        start_day = datetime.strptime(start_date, '%d-%m-%Y')
        end_day = datetime.strptime(end_date, '%d-%m-%Y')
    else:
        workouts = Schedule.query\
            .join(Workout, Schedule.workout_id==Workout.id)
        return workouts

    workouts = Schedule.query\
            .filter(Schedule.start_date>=start_day, Schedule.start_date<=end_day, Schedule.user_id==current_user.id)\
            .join(Workout, Schedule.workout_id==Workout.id)

    return workouts



