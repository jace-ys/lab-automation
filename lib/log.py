import logging
import sys

import structlog


class Logger:
    def new(stream=sys.stdout, level=logging.INFO):
        logging.basicConfig(format="%(message)s", stream=stream, level=level)

        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
                structlog.processors.format_exc_info,
                structlog.processors.StackInfoRenderer(),
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.UnicodeDecoder(),
                structlog.processors.JSONRenderer(sort_keys=True),
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
        )

        return structlog.get_logger()
