from flask_marshmallow import Marshmallow

ma = Marshmallow()


class TodoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "text",
            "completed",
        )


class TodoListSchema(ma.Schema):
    class Meta:
        fields = ("id",)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")
