from rest_framework import serializers

from products.models import Product, Category, Label, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'sub_category']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    label = LabelSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'subcategory', 'label', 'name', 'slug', 'image', 'description', 'price',
                  'available']
