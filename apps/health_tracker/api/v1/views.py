from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from ...services import HealthScoreService
from .serializers import HealthScoreSerializer
from sqlalchemy.orm import Session
from ....core.database import get_db_session


class HealthScoreView(APIView):
    def get(self, request, user_id):
        try:
            with get_db_session() as db_session:
                health_service = HealthScoreService(db_session)
                health_score = health_service.calculate_health_score(user_id)

                serializer = HealthScoreSerializer(data={
                    'user_id': user_id,
                    'health_score': health_score
                })

                if serializer.is_valid():
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
