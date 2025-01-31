from sqlalchemy import Column, Integer, String, Float, DateTime
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
    fitness_level = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    # Relationships
    activities = relationship("ActivityData", back_populates="user")
    sleep_records = relationship("SleepData", back_populates="user")
    health_scores = relationship("HealthScore", back_populates="user")
    readiness_scores = relationship("ReadinessScore", back_populates="user")
    recommendations = relationship("AIRecommendation", back_populates="user")
