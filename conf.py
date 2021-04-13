TORTOISE_ORM = {
    "connections": {"default": "postgres://user:example@localhost:5432/aerich_test"},
    "apps": {
        "app": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
