from .views import AllItemsView, ClassicItemView, CasualItemView, FemaleClassicItemView, MaleClassicItemView, FemaleCasualItemView, MaleCasualItemView, PatchItemView

from rest_framework import routers
from django.urls import include, path

app_name = 'api'

classic_router = routers.DefaultRouter()
classic_router.register(r'classic', ClassicItemView)

casual_router = routers.DefaultRouter()
casual_router.register(r'casual', CasualItemView)

male_classic_router = routers.DefaultRouter()
male_classic_router.register(r'male/classic', MaleClassicItemView)

female_classic_router = routers.DefaultRouter()
female_classic_router.register(r'female/classic', FemaleClassicItemView)

male_casual_router = routers.DefaultRouter()
male_casual_router.register(r'male/casual', MaleCasualItemView)

female_casual_router = routers.DefaultRouter()
female_casual_router.register(r'female/casual', FemaleCasualItemView)

patch_router = routers.DefaultRouter()
patch_router.register(r'item/quantity', PatchItemView)


urlpatterns = [
    path('items/', AllItemsView.as_view(), name='all_items'),
    path('products/', include(classic_router.urls)),
    path('products/', include(casual_router.urls)),
    path('products/', include(male_classic_router.urls)),
    path('products/', include(female_classic_router.urls)),
    path('products/', include(male_casual_router.urls)),
    path('products/', include(female_casual_router.urls)),
    path('products/', include(patch_router.urls)),
]
