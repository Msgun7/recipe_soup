from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, SubRecipe, Review, Comment
from .serializers import RecipeSerializer, ReviewSerializer, CommentSerializer


# 레시피 전체 조회 및 등록
class RecipeView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 레시피 상세 조회
class RecipeDetailView(APIView):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 리뷰 조회 및 작성
class ReviewView(APIView):
    def get(self, request, recipe_id):
        review = Review.objects.filter(recipe_id=recipe_id)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, recipe_id):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(recipe=recipe_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 리뷰 상세
class ReviewDetailView(APIView):
    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    # pk = review_id
    def get(self, request, pk):
        comment = Review.objects.filter(review_id=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk = review_id
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # 유저도 같이 저장 추가 예정
            serializer.save(review=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk = comment_id
    def patch(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        serializer = ReviewSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk = comment_id
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


