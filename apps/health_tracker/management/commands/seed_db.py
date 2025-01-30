from django.core.management.base import BaseCommand
from faker import Faker
from sqlalchemy.orm import sessionmaker
from common.models import Base, UserProfile, ActivityData, SleepData, HealthScore, ReadinessScore, AIRecommendation
from apps.core.database import engine
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create sample users
        users = []
        for _ in range(10):
            user = UserProfile(
                user_id=fake.uuid4(),
                name=fake.name(),
                age=random.randint(18, 70),
                weight=round(random.uniform(50, 100), 1),
                height=round(random.uniform(150, 200), 1),
                fitness_level=random.choice(
                    ['beginner', 'intermediate', 'advanced']),
                created_at=fake.date_time_this_year(tzinfo=None)
            )
            users.append(user)

        session.add_all(users)
        session.commit()

        # Create sample data for each user
        for user in users:
            # Activity Data
            for _ in range(30):  # Last 30 days of activity
                activity = ActivityData(
                    user_id=user.user_id,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    steps=random.randint(1000, 20000),
                    calories_burned=round(random.uniform(100, 1000), 1),
                    workout_minutes=random.randint(0, 120),
                    heart_rate_avg=random.randint(60, 100)
                )
                session.add(activity)

            # Sleep Data
            for _ in range(30):  # Last 30 days of sleep data
                sleep = SleepData(
                    user_id=user.user_id,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    duration_hours=round(random.uniform(4, 10), 1),
                    sleep_quality=random.choice(
                        ['poor', 'average', 'good', 'excellent'])
                )
                session.add(sleep)

            # Health Scores
            for _ in range(30):  # Last 30 days of health scores
                health_score = HealthScore(
                    user_id=user.user_id,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    score=random.randint(0, 100)
                )
                session.add(health_score)

            # Readiness Scores
            for _ in range(30):  # Last 30 days of readiness scores
                readiness_score = ReadinessScore(
                    user_id=user.user_id,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    score=random.randint(0, 100)
                )
                session.add(readiness_score)

            # AI Recommendations
            for _ in range(10):  # 10 random recommendations
                recommendation = AIRecommendation(
                    user_id=user.user_id,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    category=random.choice(['workout', 'diet', 'sleep']),
                    recommendation=fake.paragraph()
                )
                session.add(recommendation)

        session.commit()
        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database'))
