# fmt: off
logging_settings = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s][%(name)s][%(levelname)s] %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S"
        },
        "simple": {
            "format": "[%(levelname)s] %(message)s"
        },
        "message_only": {
            "format": " %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "./logs/all.log",
            "formatter": "verbose"
            },
        "db_handler": {
            "()": "logs.handler.DatabaseHandler",
            "formatter": "message_only"
        },
    },
    "root": {
        "handlers": ["console", "file", "db_handler"],
        "level": "INFO",
    },
    "loggers": {
        "general": {
            "handlers": ["console", "file", "db_handler"],
            "level": "INFO",
        }
    },
}
