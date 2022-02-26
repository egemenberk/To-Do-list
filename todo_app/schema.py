from flask_marshmallow import Marshmallow


ma = Marshmallow()

class TodoSchema(ma.Schema):
    class Meta:
        fields = (
                "id",
                "text",
                "completed",
                )

