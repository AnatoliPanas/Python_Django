from rest_framework import serializers

from books.models import Book, User, Author


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    rating = serializers.FloatField(
        default=0.0,
        min_value=0.0,
        max_value=10.00
    )
    pages = serializers.IntegerField()
    release_year = serializers.DateField()

    class Meta:
        model = None
        fields = ('title', 'rating', 'pages', 'release_year')


class AuthorShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "surname"
        ]


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorShortInfoSerializer()
    # author = AuthorShortInfoSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            'title',
            'genre',
            'author',
            'rating',
            'release_year',
            'price'
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    # publisher = serializers.StringRelatedField()
    publisher = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookCreateSerializer(serializers.ModelSerializer):
    discounted_price = serializers.DecimalField(
        max_digits=6,
        decimal_places=4,
        write_only=True,
        required=False,
        min_value=0
    )

    publisher_email = serializers.EmailField(
        max_length=75,
        required=False
    )

    class Meta:
        model = Book
        fields = [
            'title',
            'rating',
            'genre',
            'release_year',
            'author',
            'publisher_email',
            'price',
            'discounted_price',
            'pages',
            'language',
            'isbn'
        ]

    # def validate_field_name(self):
    #     pass

    def validate_pages(self, value: int):
        if value < 0:
            raise serializers.ValidationError(
                "The number of pages must be a valid integer and prater than 0"
            )

        return value

    def validate(self, attrs: dict[str, str | int | float]):
        disc_price = attrs.get('discounted_price')

        # if not disc_price:
        #     raise serializers.ValidationError(...)

        if disc_price and disc_price > attrs['price']:
            raise serializers.ValidationError(
                {
                    "discounted_price": "Цена со скидкой НЕ МОЖЕТ быть больше, чем оригинальна цена"
                }
            )
        return attrs

    def create(self, validated_data: dict[str, str | int | float]) -> Book:
        validated_data['discounted_price'] = float(validated_data['price']) * 0.7
        pub_email = validated_data.pop('publisher_email')
        publisher = User.objects.get(email=pub_email)

        book = Book.objects.create(publisher=publisher, **validated_data)

        return book
        # return super().create(validated_data)

    def update(self, instance: Book, validated_data: dict[str, str | int | float]) -> Book:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
