try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)


from .main import main
from .consulclient import ConsulClient 


if __name__ == '__main__':
    main()
