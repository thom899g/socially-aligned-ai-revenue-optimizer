"""
The base module for Socially-Aligned AI Revenue Optimizer (SAARO)
"""

from .market_analysis import MarketAnalysisModule
from .user_behavior_analytics import UserBehaviorAnalyticsModule
from .strategy_execution_engine import StrategyExecutionEngine
from .revenue_prediction_model import RevenuePredictionModel
from .monetization_tactics_database import MonetizationTacticsDatabase
from .performance_monitoring import PerformanceMonitoringModule
from .ethical_compliance_validator import EthicalComplianceValidator
from .reporting_dashboard import ReportingDashboard

__all__ = [
    'MarketAnalysisModule',
    'UserBehaviorAnalyticsModule',
    'StrategyExecutionEngine',
    'RevenuePredictionModel',
    'MonetizationTacticsDatabase',
    'PerformanceMonitoringModule',
    'EthicalComplianceValidator',
    'ReportingDashboard'
]

class SAARO:
    """
    The main class initializing all components of the Socially-Aligned AI Revenue Optimizer system.
    """

    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
        self.components = {
            'market_analysis': MarketAnalysisModule(),
            'user_behavior': UserBehaviorAnalyticsModule(),
            'strategy_execution': StrategyExecutionEngine(),
            'revenue_prediction': RevenuePredictionModel(),
            'monetization_tactics': MonetizationTacticsDatabase(),
            'performance_monitoring': PerformanceMonitoringModule(),
            'ethical_compliance': EthicalComplianceValidator(),
            'reporting_dashboard': ReportingDashboard()
        }
        
    def _load_config(self, config_path: str) -> dict:
        """
        Load configuration from a specified path.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            Dictionary containing the loaded configuration.
        """
        try:
            with open(config_path, 'r') as f:
                import json
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file at {config_path}")

    def get_component(self, component_name: str):
        """
        Retrieve a specific component by its name.
        
        Args:
            component_name: Name of the component to retrieve.
            
        Returns:
            The component object if found; otherwise, raises KeyError.
        """
        return self.components.get(component_name)