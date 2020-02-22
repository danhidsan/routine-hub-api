from RoutineHub.extensions import ma

class EnumField(ma.Field):
    """Field that serializes to a name case enum and deserializes
    to a lower case string.
    """

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return value.name

    def _deserialize(self, value, attr, data, **kwargs):
        return value