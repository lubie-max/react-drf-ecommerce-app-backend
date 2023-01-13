from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User





class CategorySerializer(serializers.ModelSerializer):
    parent= serializers.CharField(source='parent.name', read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','parent','slug' ]



class ColorVarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVarient
        fields = '__all__'


class SizeVarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVarient
        fields = '__all__'






class ProductSerializer(serializers.ModelSerializer):
    category =CategorySerializer()
    #  serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    color = ColorVarientSerializer(many=True)
    size = SizeVarientSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductImagesSerializer(serializers.ModelSerializer):
    product= ProductSerializer()
    class Meta:
        model = ProductImages
        fields = '__all__'




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CartItem
        fields= '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    
    # def create(self, user, *args , **kwargs):
    #     cart,_ = Cart.objects.get_or_create(user=user)
    #     return cart


    def get_items(self, obj):
        items = CartItem.objects.filter(cart=obj)
        serializer =CartItemSerializer(items, many=True)
        return serializer.data


    class Meta:
        model = Cart
        fields = '__all__'

