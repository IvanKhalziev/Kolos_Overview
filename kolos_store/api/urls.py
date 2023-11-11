from .views import AllItemsView, ClassicItemView, CasualItemView, FemaleClassicItemView, MaleClassicItemView, FemaleCasualItemView, MaleCasualItemView
from .views import PatchItemView, CollectionView, CategoryView

from rest_framework import routers
from django.urls import include, path
from .views import CategoryCollectionView

app_name = 'api'

all_items_router = routers.DefaultRouter()
all_items_router.register(r'', AllItemsView)

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

collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionView)

category_router = routers.DefaultRouter()
category_router.register(r'', CategoryView)

urlpatterns = [
    path('items/', include(all_items_router.urls)),
    path('products/', include(classic_router.urls)),
    path('products/', include(casual_router.urls)),
    path('products/', include(male_classic_router.urls)),
    path('products/', include(female_classic_router.urls)),
    path('products/', include(male_casual_router.urls)),
    path('products/', include(female_casual_router.urls)),
    path('products/', include(patch_router.urls)),

    path('collection/', include(collection_router.urls)),
    path('category/', include(category_router.urls)),
    path('category-collection/',
         CategoryCollectionView.as_view(), name='category-collection'),
]
