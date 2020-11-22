from rest_framework import routers
from pegLoanerApi.viewsets import AgentViewset, CustomerViewset

router = routers.DefaultRouter()
router.register('agent', AgentViewset)
router.register('customer', CustomerViewset)
