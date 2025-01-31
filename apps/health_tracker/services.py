from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from apps.health_tracker.models import ActivityData, SleepData

class HealthScoreService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def calculate_health_score(self, user_id: str) -> int:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        activity_data = self.db_session.query(ActivityData)\
            .filter(ActivityData.user_id == user_id,
                    ActivityData.date >= start_date,
                    ActivityData.date <= end_date)\
            .all()

        sleep_data = self.db_session.query(SleepData)\
            .filter(SleepData.user_id == user_id,
                    SleepData.date >= start_date,
                    SleepData.date <= end_date)\
            .all()

        activity_score = sum(
            day.steps for day in activity_data if day.steps) / (10000 * 7)
        sleep_score = sum(day.duration_hours for day in sleep_data) / (8 * 7)

        health_score = (activity_score + sleep_score) / 2 * 100
        return int(health_score)
