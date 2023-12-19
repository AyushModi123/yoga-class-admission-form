import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from resources.users import router as UserRouter
from resources.payment import router as PaymentRouter