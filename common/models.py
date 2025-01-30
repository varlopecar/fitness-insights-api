from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class UserProfile(Base):
    __tablename__ = 'user_profiles'
    user_id = Column(String, primary_key=True)
    name = Column(String(100))
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    # beginner, intermediate, advanced
    fitness_level = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class ActivityData(Base):
    __tablename__ = 'activity_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user_profiles.user_id'))
    date = Column(Date, nullable=False)
    steps = Column(Integer, nullable=True)
    calories_burned = Column(Float, nullable=True)
    workout_minutes = Column(Integer, nullable=True)
    heart_rate_avg = Column(Float, nullable=True)
    user = relationship("UserProfile", back_populates="activities")


class SleepData(Base):
    __tablename__ = 'sleep_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user_profiles.user_id'))
    date = Column(Date, nullable=False)
    duration_hours = Column(Float, nullable=False)
    # poor, average, good, excellent
    sleep_quality = Column(String(50), nullable=False)
    user = relationship("UserProfile", back_populates="sleep_records")


class HealthScore(Base):
    __tablename__ = 'health_scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user_profiles.user_id'))
    date = Column(Date, nullable=False)
    score = Column(Integer, nullable=False)  # 0-100 scale
    user = relationship("UserProfile", back_populates="health_scores")


class ReadinessScore(Base):
    __tablename__ = 'readiness_scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user_profiles.user_id'))
    date = Column(Date, nullable=False)
    score = Column(Integer, nullable=False)  # 0-100 scale, AI-driven
    user = relationship("UserProfile", back_populates="readiness_scores")


class AIRecommendation(Base):
    __tablename__ = 'ai_recommendations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user_profiles.user_id'))
    date = Column(Date, nullable=False)
    category = Column(String(50), nullable=False)  # workout, diet, sleep
    recommendation = Column(Text, nullable=False)
    user = relationship("UserProfile", back_populates="recommendations")


UserProfile.activities = relationship("ActivityData", back_populates="user")
UserProfile.sleep_records = relationship("SleepData", back_populates="user")
UserProfile.health_scores = relationship("HealthScore", back_populates="user")
UserProfile.readiness_scores = relationship(
    "ReadinessScore", back_populates="user")
UserProfile.recommendations = relationship(
    "AIRecommendation", back_populates="user")
