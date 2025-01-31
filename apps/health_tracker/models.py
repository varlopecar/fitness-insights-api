from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from common.models import Base

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

