
from server4 import current_time
def routers():
    urlpatterns = (
        ('/current_time', current_time),
    )

    return urlpatterns