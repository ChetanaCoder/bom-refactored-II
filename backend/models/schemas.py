"""
Pydantic models for the BOM comparison platform
"""

from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from datetime import datetime

class WorkflowState(BaseModel):
    workflow_id: str
    status: str
    current_stage: str
    progress: float
    created_at: str
    updated_at: str
    message: str

class BOMComparisonResult(BaseModel):
    workflow_id: str
    matches: List[Dict[str, Any]]
    summary: Dict[str, Any]

class QAClassificationSummary(BaseModel):
    classification_counts: Dict[int, int]
    confidence_distribution: Dict[str, int]
    total_items: int

class AutonomousWorkflowUpdate(BaseModel):
    workflow_id: str
    status: str
    progress: float
    current_stage: str
    message: str
    timestamp: datetime