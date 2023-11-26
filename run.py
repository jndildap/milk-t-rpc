# flake8: noqa
import logging

import vnpy.trader.ui # noqa

from vnpy_ctp import CtpGateway
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy_ctp import CtpGateway

from vnpy_webtrader import WebEngine
from vnpy_algotrading import AlgoTradingApp

import sys

logger = logging.getLogger('Milk-T-RPC')
logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)



setting = {
    "req_address": 'tcp://127.0.0.1:2014',
    "sub_address": 'tcp://127.0.0.1:4102'
}


def main():
    """Start VN Trader"""
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(AlgoTradingApp)

    web_engine = WebEngine(main_engine, event_engine)

    logger.info("Start server:%s", setting['req_address'])
    web_engine.start_server(setting['req_address'], setting['sub_address'])


if __name__ == "__main__":
    main()
