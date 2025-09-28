import logging
import json
from datetime import datetime

class TradingLogger:
    def __init__(self):
        self.logger = logging.getLogger('trading_bot')
        self.setup_special_loggers()
    
    def setup_special_loggers(self):
        """Loggers específicos para diferentes módulos"""
        self.order_logger = logging.getLogger('trading.orders')
        self.account_logger = logging.getLogger('trading.account')
        self.market_logger = logging.getLogger('trading.market')
        self.error_logger = logging.getLogger('trading.errors')
    
    def log_order(self, symbol, side, quantity, price, status):
        """Log específico para ordens"""
        self.order_logger.info(
            "ORDER %s - %s %s %s @ %s - %s", 
            status, side, quantity, symbol, price, status
        )
    
    def log_trade_signal(self, symbol, signal, price, reason):
        """Log para sinais de trading"""
        self.market_logger.info(
            "SIGNAL - %s %s at %s - Reason: %s", 
            symbol, signal, price, reason
        )
    
    def log_account_update(self, balance, available, locked):
        """Log para atualizações de conta"""
        self.account_logger.info(
            "ACCOUNT - Balance: %s, Available: %s, Locked: %s", 
            balance, available, locked
        )
    
    def log_error(self, error_type, message, details=None):
        """Log estruturado para erros"""
        error_data = {
            'type': error_type,
            'message': message,
            'details': details,
            'timestamp': datetime.now().isoformat()
        }
        self.error_logger.error(json.dumps(error_data))
        