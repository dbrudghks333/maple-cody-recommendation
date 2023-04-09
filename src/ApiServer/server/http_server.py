import logging

from aiohttp import web
from aiohttp_middlewares import cors_middleware

from .config import Config
from .http_handler import HttpHandler
from aiohttp_prometheus_exporter.handler import metrics
from aiohttp_prometheus_exporter.middleware import prometheus_middleware_factory
class HttpServer:
    def __init__(
        self,
        logger: logging.Logger,
        config: Config,
    ) -> None:
        self.logger = logger
        self.app = web.Application(
            middlewares=[cors_middleware(allow_all=True)]
        )
        self.app.middlewares.append(prometheus_middleware_factory())
        self.config = config 
        self.HttpHandler = HttpHandler(
            logger=self.logger,
            config=config,
        )
        self.routes = self.HttpHandler.get_routes()
        self.app.add_routes(self.routes)


    def run(
        self,
    ) -> None:
        self.logger.info(f"server start! routing info: {self.routes}")
        web.run_app(self.app, port=8383)
