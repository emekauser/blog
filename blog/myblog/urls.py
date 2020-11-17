from rest_framework import routers
from  .api import BlogViewSet,ArticleViewSet

router=routers.DefaultRouter()
router.register("api/v1/blogs", BlogViewSet, 'blogs')
router.register("api/v1/articles", ArticleViewSet, 'articles')
urlpatterns=router.urls